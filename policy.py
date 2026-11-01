import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical


ACTION_DIMS = [9, 5, 9, 28, 28, 28]
LEGACY_ACTION_DIMS = [7, 5, 9, 28, 28, 28]


class TFTPolicy(nn.Module):
  
    def __init__(self, obs_dim, action_dims, hidden_size=512):
        super().__init__()

        # 🛡️ Valida o contrato das seis dimensões antes de criar as camadas.
        expected_dims = ACTION_DIMS

        if list(action_dims) != expected_dims:
            raise ValueError(
                f"Dimensões de ação inválidas: {action_dims}. "
                f"Esperado: {expected_dims}"
            )

        self.obs_dim = obs_dim
        self.action_dims = action_dims
        self.num_action_types = action_dims[0]
        
        # --- DIMENSÕES BLINDADAS (Lendo de frente para trás) ---
        self.num_cell_features = 5  # [cost/5, star/3, impact, comp_score, role]
        self.pre_board_dim = 22     # Tamanho fixo do início: 10 do Core + 12 de Strategy
        self.board_flat_dim = 4 * 7 * self.num_cell_features  # 140
        self.economic_context_dim = 5

        # Derive explicit phase/level/reserve features from native core fields.
        # They are inserted before the candidate tail for checkpoint migration.
        self.global_features_dim = (
            obs_dim - self.board_flat_dim + self.economic_context_dim
        )

        # Encoder Convolucional (Percepção Espacial Geométrica)
        self.board_cnn = nn.Sequential(
            nn.Conv2d(in_channels=self.num_cell_features, out_channels=32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Flatten()
        )
        cnn_output_dim = 4 * 7 * 64  # 1792 neurônios de mapas de características

        # Encoder MLP para Dados Globais e Contextuais combinados
        self.global_mlp = nn.Sequential(
            nn.Linear(self.global_features_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU()
        )

        # Camada de Fusão de Alta Performance
        self.fusion = nn.Sequential(
            nn.Linear(cnn_output_dim + 256, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU()
        )

        # --- Cabeças de Decisão Autorregressivas ---
        self.type_head = nn.Linear(hidden_size, action_dims[0])
        # The native observation ends with 9 bench + 5 shop candidate records,
        # each with 8 explicit strategic features. Shared per-slot scorers make
        # each action logit depend on that candidate, not only its slot index.
        self.candidate_feature_dim = 8
        self.candidate_observation_dim = (action_dims[2] + action_dims[1]) * self.candidate_feature_dim
        self.shop_head = nn.Sequential(
            nn.Linear(hidden_size + self.num_action_types + self.candidate_feature_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
        )
        self.sell_head = nn.Sequential(
            nn.Linear(hidden_size + self.num_action_types + self.candidate_feature_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
        )
        self.bench_head = nn.Linear(hidden_size + self.num_action_types, action_dims[2])
        self.bench_to_board_head = nn.Linear(
            hidden_size + self.num_action_types + action_dims[2] + self.candidate_feature_dim,
            action_dims[3],
        )
        self.board_source_head = nn.Linear(hidden_size + self.num_action_types, action_dims[4])
        self.board_move_target_head = nn.Linear(
            hidden_size + self.num_action_types + action_dims[4], action_dims[5]
        )
        # Item operations share the same action type distribution and six-value
        # action record, but use conditional argument heads so legacy shop/move
        # argument heads retain their original dimensions.
        self.item_inventory_head = nn.Linear(hidden_size + self.num_action_types, 9)
        self.item_component_first_head = nn.Linear(hidden_size + self.num_action_types, 10)
        self.item_component_second_head = nn.Linear(
            hidden_size + self.num_action_types + 10, 10
        )
        self.item_target_head = nn.Linear(
            hidden_size + self.num_action_types + 20, 37
        )
        # Slot-local semantic scorers let item actions compare the actual item,
        # component, recipe and target rather than learning arbitrary slot IDs.
        # Their final layers start at zero to preserve legacy checkpoint logits.
        self.item_component_feature_dim = 10
        self.item_semantic_feature_dim = 17
        self.item_target_feature_dim = 18
        self.item_anvil_observation_dim = 3 + 9 * 11
        self.item_state_observation_dim = (
            self.item_component_feature_dim
            + 9 * self.item_semantic_feature_dim
            + 100 * self.item_semantic_feature_dim
            + 37 * self.item_target_feature_dim
        )
        self.item_inventory_candidate_head = nn.Sequential(
            nn.Linear(hidden_size + self.num_action_types + self.item_semantic_feature_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
        )
        self.item_component_candidate_head = nn.Sequential(
            nn.Linear(hidden_size + self.num_action_types + 10 + 1, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
        )
        self.item_target_candidate_head = nn.Sequential(
            nn.Linear(
                hidden_size + self.num_action_types + 20
                + self.item_semantic_feature_dim + self.item_target_feature_dim,
                128,
            ),
            nn.ReLU(),
            nn.Linear(128, 1),
        )
        for candidate_head in (
            self.item_inventory_candidate_head,
            self.item_component_candidate_head,
            self.item_target_candidate_head,
        ):
            nn.init.zeros_(candidate_head[-1].weight)
            nn.init.zeros_(candidate_head[-1].bias)
        self.value_head = nn.Linear(hidden_size, 1)

    def load_compatible_state_dict(self, state_dict):
        """Load current weights or migrate supported input-shape changes.

        New global observation features must be inserted immediately before the
        fixed candidate tail. Existing global encoder columns are shifted around
        that insertion; new columns and new bench-target conditioning columns start
        at zero so inference initially preserves the old logits.
        """
        target = self.state_dict()
        item_head_keys = {key for key in target if key.startswith((
            "item_inventory_head.", "item_component_first_head.",
            "item_component_second_head.", "item_target_head.",
            "item_inventory_candidate_head.", "item_component_candidate_head.",
            "item_target_candidate_head."
        ))}
        missing = sorted((set(target) - set(state_dict)) - item_head_keys)
        unexpected = sorted(set(state_dict) - set(target))
        if missing or unexpected:
            raise RuntimeError(
                f"Checkpoint keys incompatible: missing={missing[:8]}, "
                f"unexpected={unexpected[:8]}"
            )

        migrated = False
        loaded = {}
        for key, target_value in target.items():
            if key not in state_dict:
                # New item-specific heads start from their deterministic module initialization.
                loaded[key] = target_value
                migrated = True
                continue
            source_value = state_dict[key]
            if source_value.shape == target_value.shape:
                loaded[key] = source_value
                continue

            if (
                key in {"type_head.weight", "type_head.bias"}
                and source_value.ndim == target_value.ndim
                and source_value.shape[0] == 7
                and target_value.shape[0] == 9
                and source_value.shape[1:] == target_value.shape[1:]
            ):
                expanded = torch.zeros_like(target_value)
                expanded[:7] = source_value
                loaded[key] = expanded
                migrated = True
                continue

            if (
                key == "global_mlp.0.weight"
                and source_value.ndim == 2
                and target_value.ndim == 2
                and source_value.shape[0] == target_value.shape[0]
                and target_value.shape[1] > source_value.shape[1]
            ):
                added = target_value.shape[1] - source_value.shape[1]
                insertion = source_value.shape[1] - self.candidate_observation_dim
                expanded = torch.zeros_like(target_value)
                if 0 <= insertion <= source_value.shape[1]:
                    expanded[:, :insertion] = source_value[:, :insertion]
                    expanded[:, insertion + added:] = source_value[:, insertion:]
                else:
                    # Older checkpoints without the explicit candidate tail:
                    # preserve their known columns and initialize the new tail.
                    expanded[:, :source_value.shape[1]] = source_value
                loaded[key] = expanded
                migrated = True
                continue

            if (
                key == "bench_to_board_head.weight"
                and source_value.ndim == 2
                and target_value.ndim == 2
                and source_value.shape[0] == target_value.shape[0]
                and source_value.shape[1] < target_value.shape[1]
            ):
                expanded = torch.zeros_like(target_value)
                expanded[:, :source_value.shape[1]] = source_value
                loaded[key] = expanded
                migrated = True
                continue

            raise RuntimeError(
                f"Checkpoint shape incompatível em {key}: "
                f"{tuple(source_value.shape)} != {tuple(target_value.shape)}"
            )

        self.load_state_dict(loaded, strict=True)
        return migrated

    def encode(self, obs):
        """ Fatia cirurgicamente o tabuleiro do meio do vetor de estado e processa em 2D """
        # FIX: se o env mudar de dimensão, o erro aparece aqui com mensagem clara
        # em vez do CNN processar features errados silenciosamente.
        assert obs.shape[-1] == self.obs_dim, (
            f"obs_dim mismatch: esperado {self.obs_dim}, recebido {obs.shape[-1]}. "
            f"Verifique se pre_board_dim={self.pre_board_dim} está alinhado com _get_state()."
        )
        # Extrai a seção geométrica do tabuleiro usando o deslocamento inicial fixo
        board_part = obs[:, self.pre_board_dim : self.pre_board_dim + self.board_flat_dim]

        # Keep candidate records at the tail; the compatible-checkpoint loader
        # inserts the five derived economic features immediately before them.
        pre_part = obs[:, :self.pre_board_dim]
        post_part = obs[:, self.pre_board_dim + self.board_flat_dim :]
        candidate_tail = post_part[:, -self.candidate_observation_dim:]
        middle_part = post_part[:, :-self.candidate_observation_dim]
        economic_context = self._economic_context_features(obs)
        global_part = torch.cat(
            [pre_part, middle_part, economic_context, candidate_tail], dim=-1
        )

        # Transforma o vetor plano em uma imagem estruturada (Batch, Features, Rows, Cols) -> (B, 5, 4, 7)
        board_2d = board_part.view(-1, self.num_cell_features, 4, 7)
        
        # Processamento paralelo nas sub-redes dedicadas
        cnn_features = self.board_cnn(board_2d)
        global_features = self.global_mlp(global_part)
        
        # Fusão latente
        combined = torch.cat([cnn_features, global_features], dim=-1)
        return self.fusion(combined)

    def _economic_context_features(self, obs):
        """Expose phase target/reserve context explicitly to the PPO encoder.

        The native observation already contains the source fields. Deriving these
        features here keeps the engine contract stable and ensures action sampling,
        value estimation and PPO replay all see exactly the same deterministic data.
        """
        gold = (obs[:, 1] * 50.0).clamp(min=0.0)
        hp = (obs[:, 0] * 100.0).clamp(0.0, 100.0)
        level = (obs[:, 2] * 9.0).clamp(1.0, 10.0)

        round_fraction = obs[:, 6].clamp(0.0, 0.999)
        round_number = (10.0 * round_fraction / (1.0 - round_fraction)).clamp(1.0, 42.0)
        stage = torch.where(
            round_number <= 4.0,
            torch.ones_like(round_number),
            2.0 + torch.floor((round_number - 5.0) / 7.0),
        ).clamp(1.0, 7.0)

        # Core strategy one-hot occupies [10:17], matching the C++ observation.
        strategy = obs[:, 10:17].argmax(dim=-1)
        target_level = torch.where(
            stage <= 1.0, 3.0,
            torch.where(stage <= 2.0, 5.0,
                torch.where(stage <= 3.0, 7.0,
                    torch.where(stage <= 4.0, 8.0, 9.0))),
        )
        target_level = torch.where(strategy == 2, 8.0, target_level)  # FAST8
        target_level = torch.where(strategy == 3, 6.0, target_level)  # SLOWROLL

        reserve = torch.where(
            stage <= 2.0, 30.0,
            torch.where(stage <= 3.0, 15.0,
                torch.where(stage <= 4.0, 10.0,
                    torch.where(stage <= 5.0, 5.0, 0.0))),
        )
        slowroll_reserve = torch.where(
            stage <= 3.0, 30.0,
            torch.where(stage <= 4.0, 25.0, 15.0),
        )
        reserve = torch.where(strategy == 3, slowroll_reserve, reserve)
        reserve = torch.where(hp <= 30.0, 5.0, reserve)
        reserve = torch.where((hp <= 20.0) | (strategy == 4), 0.0, reserve)
        reserve = torch.where(
            (hp <= 40.0) & (hp > 20.0) & (strategy != 4),
            (reserve - 5.0).clamp(min=0.0),
            reserve,
        )

        level_deficit = (target_level - level).clamp(0.0, 8.0)
        spendable_gold = (gold - reserve).clamp(0.0, 200.0)
        phase_pressure = (
            ((stage - 2.0) / 4.0).clamp(0.0, 1.0)
            * (level_deficit / 3.0).clamp(0.0, 1.0)
        )
        return torch.stack(
            [
                target_level / 10.0,
                level_deficit / 8.0,
                reserve / 50.0,
                spendable_gold / 200.0,
                phase_pressure,
            ],
            dim=-1,
        )

    def _candidate_features(self, obs):
        """Extract slot-aligned strategic features appended by the native C++ engine."""
        if obs.shape[-1] < self.candidate_observation_dim:
            raise ValueError(
                f"Observação curta para features de candidatos: {obs.shape[-1]} < "
                f"{self.candidate_observation_dim}. Recompile a engine C++ atualizada."
            )
        candidate_tail = obs[:, -self.candidate_observation_dim:]
        bench_size = self.action_dims[2] * self.candidate_feature_dim
        bench = candidate_tail[:, :bench_size].reshape(
            -1, self.action_dims[2], self.candidate_feature_dim
        )
        shop = candidate_tail[:, bench_size:].reshape(
            -1, self.action_dims[1], self.candidate_feature_dim
        )
        return bench, shop

    def _item_state_features(self, obs):
        """Decode the semantic item block appended immediately before the candidate tail."""
        start = obs.shape[-1] - self.candidate_observation_dim - self.item_state_observation_dim
        end = obs.shape[-1] - self.candidate_observation_dim
        if start < self.item_anvil_observation_dim:
            # Small synthetic/legacy policy fixtures do not include the native
            # item block. Treat them as an empty inventory rather than changing
            # their established observation contract.
            batch = obs.shape[0]
            zeros = torch.zeros(batch, device=obs.device, dtype=obs.dtype)
            return (
                zeros.unsqueeze(-1).expand(-1, 10),
                zeros.view(batch, 1, 1).expand(-1, 9, self.item_semantic_feature_dim),
                zeros.view(batch, 1, 1).expand(-1, 100, self.item_semantic_feature_dim),
                zeros.view(batch, 1, 1).expand(-1, 37, self.item_target_feature_dim),
                torch.zeros(batch, device=obs.device, dtype=torch.bool),
            )
        block = obs[:, start:end]
        offset = 0
        components = block[:, offset:offset + self.item_component_feature_dim]
        offset += self.item_component_feature_dim
        inventory_size = 9 * self.item_semantic_feature_dim
        inventory = block[:, offset:offset + inventory_size].reshape(
            -1, 9, self.item_semantic_feature_dim
        )
        offset += inventory_size
        recipe_size = 100 * self.item_semantic_feature_dim
        recipes = block[:, offset:offset + recipe_size].reshape(
            -1, 100, self.item_semantic_feature_dim
        )
        offset += recipe_size
        targets = block[:, offset:].reshape(-1, 37, self.item_target_feature_dim)
        anvil_index = start - self.item_anvil_observation_dim
        anvil_pending = (
            obs[:, anvil_index] > 0.5
            if anvil_index >= 0 else torch.zeros(obs.shape[0], device=obs.device, dtype=torch.bool)
        )
        return components, inventory, recipes, targets, anvil_pending

    def _item_inventory_logits(self, conditioned, inventory_features, anvil_pending):
        logits = self.item_inventory_head(conditioned)
        context = conditioned.unsqueeze(1).expand(-1, 9, -1)
        scores = self.item_inventory_candidate_head(torch.cat(
            [context, inventory_features.to(dtype=conditioned.dtype)], dim=-1
        )).squeeze(-1)
        return logits + scores * (~anvil_pending).to(dtype=logits.dtype).unsqueeze(-1)

    def _item_component_logits(self, conditioned, component_features, first_context=None):
        if first_context is None:
            first_context = torch.zeros(
                conditioned.shape[0], 10, device=conditioned.device, dtype=conditioned.dtype
            )
            logits = self.item_component_first_head(conditioned)
        else:
            logits = self.item_component_second_head(torch.cat([conditioned, first_context], dim=-1))
        candidate_context = torch.cat([
            conditioned.unsqueeze(1).expand(-1, 10, -1),
            first_context.unsqueeze(1).expand(-1, 10, -1),
            component_features.unsqueeze(-1).to(dtype=conditioned.dtype),
        ], dim=-1)
        return logits + self.item_component_candidate_head(candidate_context).squeeze(-1)

    def _item_target_logits(
        self, conditioned, target_context, item_features, target_features, anvil_pending
    ):
        logits = self.item_target_head(torch.cat([conditioned, target_context], dim=-1))
        batch = conditioned.shape[0]
        joined = torch.cat([
            conditioned.unsqueeze(1).expand(-1, 37, -1),
            target_context.unsqueeze(1).expand(-1, 37, -1),
            item_features.unsqueeze(1).expand(-1, 37, -1).to(dtype=conditioned.dtype),
            target_features.to(dtype=conditioned.dtype),
        ], dim=-1)
        scores = self.item_target_candidate_head(joined).squeeze(-1)
        return logits + scores * (~anvil_pending).to(dtype=logits.dtype).unsqueeze(-1)

    def _bench_to_board_logits(self, conditioned, selected_slots, bench_candidate_features):
        """Score board destinations conditioned on the selected bench unit."""
        slot_onehot = F.one_hot(
            selected_slots.long(),
            num_classes=self.action_dims[2],
        ).to(dtype=conditioned.dtype)
        selected_features = bench_candidate_features.gather(
            1,
            selected_slots.long().view(-1, 1, 1).expand(
                -1, 1, self.candidate_feature_dim
            ),
        ).squeeze(1).to(dtype=conditioned.dtype)
        target_input = torch.cat(
            [conditioned, slot_onehot, selected_features],
            dim=-1,
        )
        return self.bench_to_board_head(target_input)

    @staticmethod
    def _candidate_logits(head, conditioned, candidate_features):
        """Score each candidate with shared weights and its own slot-local features."""
        batch, slots, feature_dim = candidate_features.shape
        context = conditioned.unsqueeze(1).expand(-1, slots, -1)
        joined = torch.cat([context, candidate_features], dim=-1)
        return head(joined.reshape(batch * slots, -1)).reshape(batch, slots)

    def get_value(self, obs, masks=None):
        """ Retorna a estimativa de valor do estado (ignora as máscaras se enviadas) """
        return self.value_head(self.encode(obs)).squeeze(-1)

    def get_action(self, obs, masks=None, deterministic=False):
        """ Atalho para compatibilidade com o trainer.py """
        return self.get_action_and_value(obs, masks=masks, deterministic=deterministic)

    @staticmethod
    def _mask_logits(logits, mask):
        """🛡️ Valida máscaras antes de criar uma distribuição."""
        mask = torch.as_tensor(mask, device=logits.device)

        if mask.shape != logits.shape:
            raise ValueError(
                f"Shape de máscara inválido: {tuple(mask.shape)}; "
                f"esperado: {tuple(logits.shape)}"
            )

        if mask.dtype != torch.bool:
            if mask.is_floating_point() and not torch.isfinite(mask).all():
                raise ValueError("A máscara contém NaN ou infinito.")

            if not ((mask == 0) | (mask == 1)).all():
                raise ValueError("A máscara deve conter somente 0 e 1.")

            mask = mask.bool()

        # 🚫 Não permitir distribuições sem nenhuma opção válida.
        invalid_rows = ~mask.any(dim=-1)

        if invalid_rows.any():
            rows = invalid_rows.nonzero().flatten().tolist()
            raise ValueError(
                f"Máscara sem opções válidas nas linhas: {rows}"
            )

        if not torch.isfinite(logits).all():
            raise FloatingPointError(
                "Os logits contêm NaN ou infinito."
            )

        return logits.masked_fill(
            ~mask,
            torch.finfo(logits.dtype).min,
        )

    @staticmethod
    def _validate_selected_actions(actions, mask, name):
        """🔎 Rejeita ações registradas que a máscara proíbe."""
        actions = actions.long()

        if actions.ndim != 1 or mask.ndim != 2:
            raise ValueError(
                f"Formato inválido ao validar ação '{name}'."
            )

        if actions.shape[0] != mask.shape[0]:
            raise ValueError(
                f"Batch incompatível ao validar ação '{name}'."
            )

        if ((actions < 0) | (actions >= mask.shape[1])).any():
            raise ValueError(
                f"Índice fora dos limites para a ação '{name}'."
            )

        selected_valid = mask.to(
            device=actions.device,
            dtype=torch.bool,
        ).gather(1, actions.unsqueeze(1)).squeeze(1)

        if not selected_valid.all():
            rows = (~selected_valid).nonzero().flatten().tolist()
            raise ValueError(
                f"Ação '{name}' bloqueada pela máscara "
                f"nas linhas: {rows}"
            )

    @staticmethod
    def _sample_categorical(logits, deterministic):
        if deterministic:
            return torch.argmax(logits, dim=-1)
        else:
            dist = Categorical(logits=logits)
            return dist.sample()

    def get_action_and_value(self, obs, masks=None, deterministic=False):
        """API original usada pelo PPO; mantém as quatro saídas existentes."""
        actions, logprob, entropy, value, _ = self._get_action_and_value_impl(
            obs, masks=masks, deterministic=deterministic, collect_diagnostics=False
        )
        return actions, logprob, entropy, value

    def get_action_and_value_with_diagnostics(self, obs, masks=None, deterministic=False):
        """Inferência opt-in com as distribuições realmente usadas, sem segunda amostragem."""
        return self._get_action_and_value_impl(
            obs, masks=masks, deterministic=deterministic, collect_diagnostics=True
        )

    def get_action_and_value_with_entropy_diagnostics(self, obs, masks=None, deterministic=False):
        """Retorna entropia por cabeça sem materializar probabilidades/top-k completos."""
        return self._get_action_and_value_impl(
            obs, masks=masks, deterministic=deterministic, collect_entropy_diagnostics=True
        )

    def _get_action_and_value_impl(
        self, obs, masks=None, deterministic=False, collect_diagnostics=False,
        collect_entropy_diagnostics=False
    ):
        device = obs.device
        batch_size = obs.shape[0]
        player_diagnostics = [[] for _ in range(batch_size)]
        bench_candidate_features, shop_candidate_features = self._candidate_features(obs)
        (
            item_component_features, item_inventory_features, item_recipe_features,
            item_target_features, item_anvil_pending,
        ) = self._item_state_features(obs)

        def record_distribution(name, logits, chosen, row_indices, applied_mask=None):
            if not collect_diagnostics and not collect_entropy_diagnostics:
                return
            probabilities = torch.softmax(logits, dim=-1).detach()
            selected = chosen.detach().long()
            row_ids = row_indices.detach().long().tolist()
            if applied_mask is not None:
                valid_counts = applied_mask.to(
                    device=probabilities.device, dtype=torch.bool
                ).sum(dim=-1).clamp_min(1)
            else:
                valid_counts = torch.full(
                    (probabilities.shape[0],), probabilities.shape[-1],
                    device=probabilities.device, dtype=torch.long,
                )
            entropy_nats = -(
                probabilities * probabilities.clamp_min(
                    torch.finfo(probabilities.dtype).tiny
                ).log()
            ).sum(dim=-1)
            max_entropy = valid_counts.to(probabilities.dtype).log()
            normalized_entropy = torch.where(
                max_entropy > 0,
                entropy_nats / max_entropy.clamp_min(torch.finfo(probabilities.dtype).tiny),
                torch.zeros_like(entropy_nats),
            )
            entropy_values = entropy_nats.detach().tolist()
            normalized_entropy_values = normalized_entropy.detach().tolist()

            # Training only needs compact entropy scalars. The viewer's full
            # diagnostics retain masks, probabilities, selected action and top-k.
            if collect_diagnostics:
                selected_values = selected.tolist()
                mask_values = (
                    applied_mask.detach().bool().tolist()
                    if applied_mask is not None else None
                )
                top_count = min(3, probabilities.shape[-1])
                top_probs, top_indices = probabilities.topk(top_count, dim=-1)
                top_probs = top_probs.detach().tolist()
                top_indices = top_indices.detach().tolist()
                all_probs = probabilities.tolist()

            for row, player_id in enumerate(row_ids):
                item = {
                    "head": name,
                    "entropy_nats": float(entropy_values[row]),
                    "entropy_normalized": float(normalized_entropy_values[row]),
                }
                if collect_diagnostics:
                    item.update({
                        "mask": mask_values[row] if mask_values is not None else None,
                        "probabilities": all_probs[row],
                        "selected": int(selected_values[row]),
                        "selected_probability": float(all_probs[row][selected_values[row]]),
                        "top_choices": [
                            {"index": int(index), "probability": float(probability)}
                            for index, probability in zip(top_indices[row], top_probs[row])
                        ],
                    })
                player_diagnostics[player_id].append(item)

        features = self.encode(obs)

        # --- Action type ---
        type_logits = self.type_head(features)
        if masks is not None:
            type_logits = self._mask_logits(type_logits, masks["type_mask"])
        else:
            # Without the native legality snapshot, do not sample item commands
            # that cannot be resolved/validated by the runtime.
            type_logits = type_logits.clone()
            type_logits[:, 7:] = torch.finfo(type_logits.dtype).min
        action_type = self._sample_categorical(type_logits, deterministic)
        
        type_dist = Categorical(logits=type_logits)
        type_logprob = type_dist.log_prob(action_type)
        type_entropy = type_dist.entropy()
        record_distribution(
            "type", type_logits, action_type,
            torch.arange(batch_size, device=device),
            masks.get("type_mask") if masks is not None else None,
        )

        total_logprob = type_logprob.clone()
        total_entropy = type_entropy.clone()

        # --- Conditioning ---
        type_onehot = F.one_hot(action_type, num_classes=self.num_action_types).float()
        conditioned = torch.cat([features, type_onehot], dim=-1)

        # Default tensors
        shop_slot = torch.zeros(batch_size, dtype=torch.long, device=device)
        bench_slot = torch.zeros(batch_size, dtype=torch.long, device=device)
        board_target = torch.zeros(batch_size, dtype=torch.long, device=device)
        board_source = torch.zeros(batch_size, dtype=torch.long, device=device)
        board_move_target = torch.zeros(batch_size, dtype=torch.long, device=device)

        # --- BUY ---
        buy_mask = action_type == 0
        if buy_mask.any():
            logits = self._candidate_logits(
                self.shop_head, conditioned[buy_mask], shop_candidate_features[buy_mask]
            )
            if masks is not None:
                logits = self._mask_logits(logits, masks["shop_mask"][buy_mask])
            sampled = self._sample_categorical(logits, deterministic)
            shop_slot[buy_mask] = sampled
            dist = Categorical(logits=logits)
            total_logprob[buy_mask] += dist.log_prob(sampled)
            total_entropy[buy_mask] += dist.entropy()
            record_distribution(
                "shop_slot", logits, sampled, torch.where(buy_mask)[0],
                masks["shop_mask"][buy_mask] if masks is not None else None,
            )

        # --- MOVE BENCH ---
        move_bench_mask = action_type == 3
        if move_bench_mask.any():
            # Bench source
            logits = self.bench_head(conditioned[move_bench_mask])

            if masks is not None:
                # Máscara específica para mover unidades do banco.
                # bench_source_mask continua disponível para SELL.
                source_mask = masks.get(
                    "bench_move_source_mask",
                    masks["bench_source_mask"]
                )
                logits = self._mask_logits(
                    logits,
                    source_mask[move_bench_mask]
                )

            sampled = self._sample_categorical(logits, deterministic)
            bench_slot[move_bench_mask] = sampled
            dist = Categorical(logits=logits)
            total_logprob[move_bench_mask] += dist.log_prob(sampled)
            total_entropy[move_bench_mask] += dist.entropy()
            record_distribution(
                "bench_slot", logits, sampled, torch.where(move_bench_mask)[0],
                masks.get("bench_move_source_mask", masks["bench_source_mask"])[move_bench_mask]
                if masks is not None else None,
            )

            # Board target condicionado ao slot selecionado no banco
            logits = self._bench_to_board_logits(
                conditioned[move_bench_mask],
                sampled,
                bench_candidate_features[move_bench_mask],
            )

            if masks is not None:
                batch_indices = torch.where(move_bench_mask)[0]

                if "bench_to_board_target_masks" in masks:
                    target_mask = masks["bench_to_board_target_masks"][
                        batch_indices,
                        sampled,
                        :
                    ]
                else:
                    # Compatibilidade com máscaras antigas.
                    target_mask = masks["board_target_mask"][move_bench_mask]

                logits = self._mask_logits(logits, target_mask)

            sampled_target = self._sample_categorical(logits, deterministic)
            board_target[move_bench_mask] = sampled_target
            dist = Categorical(logits=logits)
            total_logprob[move_bench_mask] += dist.log_prob(sampled_target)
            total_entropy[move_bench_mask] += dist.entropy()
            record_distribution(
                "board_target", logits, sampled_target, torch.where(move_bench_mask)[0],
                target_mask if masks is not None else None,
            )

        # --- MOVE BOARD ---
        move_board_mask = action_type == 4
        if move_board_mask.any():
            # Source
            logits = self.board_source_head(conditioned[move_board_mask])
            if masks is not None:
                logits = self._mask_logits(
                    logits,
                    masks["board_source_mask"][move_board_mask]
                )

            sampled_source = self._sample_categorical(logits, deterministic)
            board_source[move_board_mask] = sampled_source
            src_dist = Categorical(logits=logits)
            total_logprob[move_board_mask] += src_dist.log_prob(sampled_source)
            total_entropy[move_board_mask] += src_dist.entropy()
            record_distribution(
                "board_source", logits, sampled_source, torch.where(move_board_mask)[0],
                masks["board_source_mask"][move_board_mask] if masks is not None else None,
            )

            # Target condicionado à origem selecionada
            source_onehot = F.one_hot(
                sampled_source,
                num_classes=self.action_dims[4]
            ).float()

            target_input = torch.cat(
                [conditioned[move_board_mask], source_onehot],
                dim=-1
            )
            target_logits = self.board_move_target_head(target_input)

            if masks is not None:
                full_move_masks = masks["board_move_target_masks"]
                batch_indices = torch.where(move_board_mask)[0]
                target_mask = full_move_masks[
                    batch_indices,
                    sampled_source,
                    :
                ]
                target_logits = self._mask_logits(target_logits, target_mask)

            target_sampled = self._sample_categorical(
                target_logits,
                deterministic
            )
            board_move_target[move_board_mask] = target_sampled
            target_dist = Categorical(logits=target_logits)
            total_logprob[move_board_mask] += target_dist.log_prob(target_sampled)
            total_entropy[move_board_mask] += target_dist.entropy()
            record_distribution(
                "board_move_target", target_logits, target_sampled,
                torch.where(move_board_mask)[0],
                target_mask if masks is not None else None,
            )

        # --- EQUIP FROM INVENTORY ---
        equip_item_mask = action_type == 7
        if equip_item_mask.any():
            conditioned_item = conditioned[equip_item_mask]
            logits = self._item_inventory_logits(
                conditioned_item, item_inventory_features[equip_item_mask],
                item_anvil_pending[equip_item_mask],
            )
            inventory_mask = masks["item_inventory_mask"][equip_item_mask] if masks is not None else None
            if inventory_mask is not None:
                logits = self._mask_logits(logits, inventory_mask)
            item_index = self._sample_categorical(logits, deterministic)
            shop_slot[equip_item_mask] = item_index
            dist = Categorical(logits=logits)
            total_logprob[equip_item_mask] += dist.log_prob(item_index)
            total_entropy[equip_item_mask] += dist.entropy()
            record_distribution("item_inventory", logits, item_index, torch.where(equip_item_mask)[0], inventory_mask)

            item_context = F.one_hot(item_index, num_classes=9).to(dtype=conditioned.dtype)
            item_context = F.pad(item_context, (0, 1))
            target_context = torch.cat([item_context, torch.zeros_like(item_context)], dim=-1)
            selected_item_features = item_inventory_features[equip_item_mask].gather(
                1, item_index.view(-1, 1, 1).expand(-1, 1, self.item_semantic_feature_dim)
            ).squeeze(1)
            target_logits = self._item_target_logits(
                conditioned_item, target_context, selected_item_features,
                item_target_features[equip_item_mask], item_anvil_pending[equip_item_mask],
            )
            target_mask = masks["item_target_mask"][equip_item_mask] if masks is not None else None
            if target_mask is not None:
                target_logits = self._mask_logits(target_logits, target_mask)
            target_index = self._sample_categorical(target_logits, deterministic)
            bench_slot[equip_item_mask] = target_index
            target_dist = Categorical(logits=target_logits)
            total_logprob[equip_item_mask] += target_dist.log_prob(target_index)
            total_entropy[equip_item_mask] += target_dist.entropy()
            record_distribution("item_target", target_logits, target_index, torch.where(equip_item_mask)[0], target_mask)

        # --- CRAFT AND EQUIP ---
        craft_item_mask = action_type == 8
        if craft_item_mask.any():
            conditioned_item = conditioned[craft_item_mask]
            first_logits = self._item_component_logits(
                conditioned_item, item_component_features[craft_item_mask], None
            )
            first_mask = masks["item_component_first_mask"][craft_item_mask] if masks is not None else None
            if first_mask is not None:
                first_logits = self._mask_logits(first_logits, first_mask)
            first_index = self._sample_categorical(first_logits, deterministic)
            shop_slot[craft_item_mask] = first_index
            first_dist = Categorical(logits=first_logits)
            total_logprob[craft_item_mask] += first_dist.log_prob(first_index)
            total_entropy[craft_item_mask] += first_dist.entropy()
            record_distribution("item_component_first", first_logits, first_index, torch.where(craft_item_mask)[0], first_mask)

            first_onehot = F.one_hot(first_index, num_classes=10).to(dtype=conditioned.dtype)
            second_logits = self._item_component_logits(
                conditioned_item, item_component_features[craft_item_mask], first_onehot
            )
            pair_masks = masks["item_component_pair_masks"][craft_item_mask] if masks is not None else None
            second_mask = pair_masks[torch.arange(first_index.shape[0], device=device), first_index] if pair_masks is not None else None
            if second_mask is not None:
                second_logits = self._mask_logits(second_logits, second_mask)
            second_index = self._sample_categorical(second_logits, deterministic)
            bench_slot[craft_item_mask] = second_index
            second_dist = Categorical(logits=second_logits)
            total_logprob[craft_item_mask] += second_dist.log_prob(second_index)
            total_entropy[craft_item_mask] += second_dist.entropy()
            record_distribution("item_component_second", second_logits, second_index, torch.where(craft_item_mask)[0], second_mask)

            second_onehot = F.one_hot(second_index, num_classes=10).to(dtype=conditioned.dtype)
            target_context = torch.cat([first_onehot, second_onehot], dim=-1)
            recipe_index = first_index * 10 + second_index
            selected_recipe_features = item_recipe_features[craft_item_mask].gather(
                1, recipe_index.view(-1, 1, 1).expand(-1, 1, self.item_semantic_feature_dim)
            ).squeeze(1)
            target_logits = self._item_target_logits(
                conditioned_item, target_context, selected_recipe_features,
                item_target_features[craft_item_mask], item_anvil_pending[craft_item_mask],
            )
            target_mask = masks["item_target_mask"][craft_item_mask] if masks is not None else None
            if target_mask is not None:
                target_logits = self._mask_logits(target_logits, target_mask)
            target_index = self._sample_categorical(target_logits, deterministic)
            board_target[craft_item_mask] = target_index
            target_dist = Categorical(logits=target_logits)
            total_logprob[craft_item_mask] += target_dist.log_prob(target_index)
            total_entropy[craft_item_mask] += target_dist.entropy()
            record_distribution("item_target", target_logits, target_index, torch.where(craft_item_mask)[0], target_mask)

        # --- SELL ---
        sell_mask = action_type == 5
        if sell_mask.any():
            logits = self._candidate_logits(
                self.sell_head, conditioned[sell_mask], bench_candidate_features[sell_mask]
            )
            if masks is not None:
                # Venda continua usando a máscara original do banco.
                logits = self._mask_logits(
                    logits,
                    masks["bench_source_mask"][sell_mask]
                )

            sampled = self._sample_categorical(logits, deterministic)
            bench_slot[sell_mask] = sampled
            dist = Categorical(logits=logits)
            total_logprob[sell_mask] += dist.log_prob(sampled)
            total_entropy[sell_mask] += dist.entropy()
            record_distribution(
                "bench_slot", logits, sampled, torch.where(sell_mask)[0],
                masks["bench_source_mask"][sell_mask] if masks is not None else None,
            )

        actions = torch.stack([
            action_type, shop_slot, bench_slot, board_target, board_source, board_move_target
        ], dim=-1)

        value = self.value_head(features).squeeze(-1)

        if collect_diagnostics or collect_entropy_diagnostics:
            return actions, total_logprob, total_entropy, value, player_diagnostics
        return actions, total_logprob, total_entropy, value, None

    def evaluate_actions(self, obs, actions, masks):
        hidden = self.encode(obs)
        bench_candidate_features, shop_candidate_features = self._candidate_features(obs)
        (
            item_component_features, item_inventory_features, item_recipe_features,
            item_target_features, item_anvil_pending,
        ) = self._item_state_features(obs)

        # Type
        type_logits = self.type_head(hidden)
        type_logits = self._mask_logits(type_logits, masks["type_mask"])
        type_dist = Categorical(logits=type_logits)
        action_type = actions[:, 0]

        # 🛡️ Validar se o tipo escolhido é permitido
        self._validate_selected_actions(
            action_type,
            masks["type_mask"],
            "type",
        )

        total_logprob = type_dist.log_prob(action_type)
        total_entropy = type_dist.entropy()

        # Conditioning
        type_onehot = F.one_hot(action_type, num_classes=self.num_action_types).float()
        conditioned = torch.cat([hidden, type_onehot], dim=-1)

        # BUY
        buy_mask = action_type == 0
        if buy_mask.any():
            logits = self._candidate_logits(
                self.shop_head, conditioned[buy_mask], shop_candidate_features[buy_mask]
            )
            shop_mask = masks["shop_mask"][buy_mask]
            logits = self._mask_logits(logits, shop_mask)

            # 🛡️ Validar o slot selecionado
            self._validate_selected_actions(
                actions[buy_mask, 1],
                shop_mask,
                "shop_slot",
            )

            dist = Categorical(logits=logits)
            total_logprob[buy_mask] += dist.log_prob(actions[buy_mask, 1])
            total_entropy[buy_mask] += dist.entropy()

        # MOVE BENCH
        move_bench_mask = action_type == 3
        if move_bench_mask.any():
            # Bench source
            logits = self.bench_head(conditioned[move_bench_mask])

            source_mask = masks.get(
                "bench_move_source_mask",
                masks["bench_source_mask"]
            )
            source_mask = source_mask[move_bench_mask]

            logits = self._mask_logits(logits, source_mask)

            # 🛡️ Validar a origem escolhida
            selected_bench_slots = actions[move_bench_mask, 2]
            self._validate_selected_actions(
                selected_bench_slots,
                source_mask,
                "bench_source",
            )

            dist = Categorical(logits=logits)
            total_logprob[move_bench_mask] += dist.log_prob(
                selected_bench_slots
            )
            total_entropy[move_bench_mask] += dist.entropy()

            # Target condicionado ao slot selecionado no banco
            logits = self._bench_to_board_logits(
                conditioned[move_bench_mask],
                selected_bench_slots,
                bench_candidate_features[move_bench_mask],
            )

            batch_indices = torch.where(move_bench_mask)[0]

            if "bench_to_board_target_masks" in masks:
                target_mask = masks["bench_to_board_target_masks"][
                    batch_indices,
                    selected_bench_slots,
                    :
                ]
            else:
                # Compatibilidade com máscaras antigas.
                target_mask = masks["board_target_mask"][move_bench_mask]

            logits = self._mask_logits(logits, target_mask)

            # 🛡️ Validar o destino escolhido
            self._validate_selected_actions(
                actions[move_bench_mask, 3],
                target_mask,
                "bench_target",
            )

            dist = Categorical(logits=logits)
            total_logprob[move_bench_mask] += dist.log_prob(
                actions[move_bench_mask, 3]
            )
            total_entropy[move_bench_mask] += dist.entropy()

        # MOVE BOARD
        move_board_mask = action_type == 4
        if move_board_mask.any():
            # Source
            logits = self.board_source_head(conditioned[move_board_mask])
            logits = self._mask_logits(
                logits,
                masks["board_source_mask"][move_board_mask]
            )
            dist = Categorical(logits=logits)
            total_logprob[move_board_mask] += dist.log_prob(
                actions[move_board_mask, 4]
            )
            total_entropy[move_board_mask] += dist.entropy()

            # Target condicionado à origem selecionada
            source_action = actions[move_board_mask, 4]

            # 🛡️ Validar a origem escolhida
            self._validate_selected_actions(
                source_action,
                masks["board_source_mask"][move_board_mask],
                "board_source",
            )

            source_onehot = F.one_hot(
                source_action,
                num_classes=self.action_dims[4]
            ).float()

            target_input = torch.cat(
                [conditioned[move_board_mask], source_onehot],
                dim=-1
            )
            target_logits = self.board_move_target_head(target_input)

            # Máscara condicional por origem
            full_move_masks = masks["board_move_target_masks"]
            batch_indices = torch.where(move_board_mask)[0]
            target_mask = full_move_masks[
                batch_indices,
                source_action,
                :
            ]
            target_logits = self._mask_logits(target_logits, target_mask)

            # 🛡️ Validar o destino escolhido
            self._validate_selected_actions(
                actions[move_board_mask, 5],
                target_mask,
                "board_move_target",
            )

            target_dist = Categorical(logits=target_logits)
            total_logprob[move_board_mask] += target_dist.log_prob(
                actions[move_board_mask, 5]
            )
            total_entropy[move_board_mask] += target_dist.entropy()

        # EQUIP FROM INVENTORY
        equip_item_mask = action_type == 7
        if equip_item_mask.any():
            conditioned_item = conditioned[equip_item_mask]
            item_index = actions[equip_item_mask, 1].long()
            inventory_mask = masks["item_inventory_mask"][equip_item_mask]
            logits = self._mask_logits(
                self._item_inventory_logits(
                    conditioned_item, item_inventory_features[equip_item_mask],
                    item_anvil_pending[equip_item_mask],
                ), inventory_mask
            )
            self._validate_selected_actions(item_index, inventory_mask, "item_inventory")
            dist = Categorical(logits=logits)
            total_logprob[equip_item_mask] += dist.log_prob(item_index)
            total_entropy[equip_item_mask] += dist.entropy()

            target_index = actions[equip_item_mask, 2].long()
            item_context = F.one_hot(item_index, num_classes=9).to(dtype=conditioned.dtype)
            item_context = F.pad(item_context, (0, 1))
            target_context = torch.cat([item_context, torch.zeros_like(item_context)], dim=-1)
            target_mask = masks["item_target_mask"][equip_item_mask]
            selected_item_features = item_inventory_features[equip_item_mask].gather(
                1, item_index.view(-1, 1, 1).expand(-1, 1, self.item_semantic_feature_dim)
            ).squeeze(1)
            target_logits = self._mask_logits(
                self._item_target_logits(
                    conditioned_item, target_context, selected_item_features,
                    item_target_features[equip_item_mask], item_anvil_pending[equip_item_mask],
                ), target_mask,
            )
            self._validate_selected_actions(target_index, target_mask, "item_target")
            target_dist = Categorical(logits=target_logits)
            total_logprob[equip_item_mask] += target_dist.log_prob(target_index)
            total_entropy[equip_item_mask] += target_dist.entropy()

        # CRAFT AND EQUIP
        craft_item_mask = action_type == 8
        if craft_item_mask.any():
            conditioned_item = conditioned[craft_item_mask]
            first_index = actions[craft_item_mask, 1].long()
            second_index = actions[craft_item_mask, 2].long()
            target_index = actions[craft_item_mask, 3].long()

            first_mask = masks["item_component_first_mask"][craft_item_mask]
            first_logits = self._mask_logits(
                self._item_component_logits(
                    conditioned_item, item_component_features[craft_item_mask], None
                ), first_mask
            )
            self._validate_selected_actions(first_index, first_mask, "item_component_first")
            first_dist = Categorical(logits=first_logits)
            total_logprob[craft_item_mask] += first_dist.log_prob(first_index)
            total_entropy[craft_item_mask] += first_dist.entropy()

            first_onehot = F.one_hot(first_index, num_classes=10).to(dtype=conditioned.dtype)
            second_logits = self._item_component_logits(
                conditioned_item, item_component_features[craft_item_mask], first_onehot
            )
            pair_masks = masks["item_component_pair_masks"][craft_item_mask]
            second_mask = pair_masks[
                torch.arange(first_index.shape[0], device=first_index.device), first_index
            ]
            second_logits = self._mask_logits(second_logits, second_mask)
            self._validate_selected_actions(second_index, second_mask, "item_component_second")
            second_dist = Categorical(logits=second_logits)
            total_logprob[craft_item_mask] += second_dist.log_prob(second_index)
            total_entropy[craft_item_mask] += second_dist.entropy()

            second_onehot = F.one_hot(second_index, num_classes=10).to(dtype=conditioned.dtype)
            target_context = torch.cat([first_onehot, second_onehot], dim=-1)
            target_mask = masks["item_target_mask"][craft_item_mask]
            recipe_index = first_index * 10 + second_index
            selected_recipe_features = item_recipe_features[craft_item_mask].gather(
                1, recipe_index.view(-1, 1, 1).expand(-1, 1, self.item_semantic_feature_dim)
            ).squeeze(1)
            target_logits = self._mask_logits(
                self._item_target_logits(
                    conditioned_item, target_context, selected_recipe_features,
                    item_target_features[craft_item_mask], item_anvil_pending[craft_item_mask],
                ), target_mask,
            )
            self._validate_selected_actions(target_index, target_mask, "item_target")
            target_dist = Categorical(logits=target_logits)
            total_logprob[craft_item_mask] += target_dist.log_prob(target_index)
            total_entropy[craft_item_mask] += target_dist.entropy()

        # SELL
        sell_mask = action_type == 5
        if sell_mask.any():
            logits = self._candidate_logits(
                self.sell_head, conditioned[sell_mask], bench_candidate_features[sell_mask]
            )
            sell_source_mask = masks["bench_source_mask"][sell_mask]
            logits = self._mask_logits(logits, sell_source_mask)

            # 🛡️ Validar o slot que será vendido
            self._validate_selected_actions(
                actions[sell_mask, 2],
                sell_source_mask,
                "sell_source",
            )

            dist = Categorical(logits=logits)
            total_logprob[sell_mask] += dist.log_prob(actions[sell_mask, 2])
            total_entropy[sell_mask] += dist.entropy()

        value = self.value_head(hidden).squeeze(-1)
        return total_logprob, total_entropy, value