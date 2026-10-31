import torch
import torch.optim as optim
import numpy as np
import os

from cpp_lobby_env import CppTFTLobbyWrapper

from torch.utils.tensorboard import SummaryWriter


from vector_lobby_env import LobbyVectorEnv

from policy import TFTPolicy
from rollout import RolloutBuffer
from ppo import PPOTrainer, exponential_schedule_value

from engine_contracts import Strategy
from engine_contracts import ActionType

def refresh_opgg_meta_catalog() -> None:
    """Refresh at the training entrypoint, never when Trainer is imported or constructed in tests."""
    from pathlib import Path
    project_root = Path(__file__).resolve().parent
    os.environ.setdefault("TFT_OPGG_META_CATALOG", str(project_root / "data" / "opgg_tft_meta.json"))
    if os.environ.get("TFT_OPGG_DISABLE_REFRESH", "").strip().lower() in {"1", "true", "yes"}:
        print("OP.GG refresh desabilitado por TFT_OPGG_DISABLE_REFRESH.")
        return
    import subprocess
    import sys
    collector = project_root / "scripts" / "update_opgg_meta_catalog.py"
    if not collector.is_file():
        print("⚠️ Coletor OP.GG não encontrado; usando o planejador nativo.")
        return
    try:
        command = [sys.executable, str(collector), "--if-stale"]
        configured_catalog = os.environ.get("TFT_OPGG_META_CATALOG")
        if configured_catalog:
            command.extend(["--output", configured_catalog])
        result = subprocess.run(
            command, cwd=str(project_root), capture_output=True, text=True, timeout=90,
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print(result.stderr.strip())
        if result.returncode != 0:
            print("⚠️ Catálogo OP.GG indisponível; a engine continuará com o planejador nativo.")
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(f"⚠️ Não foi possível atualizar OP.GG antes do treino: {exc}")


class Trainer:
    # ================================================================
    # 🏟️ CONFIGURAÇÃO DA LOBBY
    # ================================================================

    PLAYERS_PER_LOBBY = 8

    # ================================================================
    # 🎮 ACTION SPACE
    # ================================================================

    ACTION_DIMS = [
        9,   # type
        5,   # shop_slot
        9,   # bench_slot
        28,  # board_target
        28,  # board_source
        28   # board_move_target
    ]

    ACTION_DIM = 6

    # ================================================================
    # 🎭 MASK SHAPES
    # ================================================================

    MASK_SHAPES = {
        "type_mask": (9,),
        "shop_mask": (5,),
        "bench_source_mask": (9,),
        "board_target_mask": (28,),
        "board_source_mask": (28,),
        "board_move_target_masks": (28, 28),
        "bench_move_source_mask": (9,),
        "bench_to_board_target_masks": (9, 28),
        "item_inventory_mask": (9,),
        "item_component_first_mask": (10,),
        "item_component_pair_masks": (10, 10),
        "item_target_mask": (37,),
    }

    def __init__(
        self,
        num_envs=4,
        use_subprocess=True,
        item_catalog_path=None,
    ):

        # ============================================================
        # 🖥️ DEVICE
        # ============================================================

        print(
            f"GPU disponível: "
            f"{torch.cuda.is_available()}"
        )

        if torch.cuda.is_available():

            print(
                f"GPU nome: "
                f"{torch.cuda.get_device_name(0)}"
            )

            print(
                f"Memória total: "
                f"{torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB"
            )

        # ------------------------------------------------------------
        # Mantendo CPU por enquanto
        # ------------------------------------------------------------

        # self.device = torch.device(
        #     "cuda" if torch.cuda.is_available()
        #     else "cpu"
        # )

        self.device = torch.device("cpu")

        # ============================================================
        # 🏟️ ENV CONFIG
        # ============================================================

        # IMPORTANTE:
        #
        # Agora num_envs representa:
        #
        #     número de LOBBIES
        #
        # e não número de jogadores.
        #
        # Exemplo:
        #
        #     num_envs = 4
        #
        #     4 lobbies
        #     × 8 jogadores
        #     = 32 agentes
        #
        self.num_envs = num_envs

        self.use_subprocess = use_subprocess

        self.num_agents = (
            self.num_envs
            * self.PLAYERS_PER_LOBBY
        )

        print(
            f"🏟️ Lobbies: {self.num_envs}"
        )

        print(
            f"👥 Jogadores por lobby: "
            f"{self.PLAYERS_PER_LOBBY}"
        )

        print(
            f"🤖 Agentes totais: "
            f"{self.num_agents}"
        )

        # ============================================================
        # 📊 TENSORBOARD
        # ============================================================

        self.writer = SummaryWriter(
            "tft_logs/AkameIA_V8"
        )

        # ============================================================
        # 🏭 ENV FACTORY / ENGINE BACKEND
        # ============================================================

        print("🧩 Engine selecionada: C++ (única engine)")

        resolved_item_catalog = item_catalog_path or os.environ.get("TFT_ITEM_CATALOG_PATH")
        def make_env():
            return CppTFTLobbyWrapper(item_catalog_path=resolved_item_catalog)

# ============================================================
        # 🚀 VECTOR ENV
        # ============================================================

        # LobbyVectorEnv é serial: uma instância por lobby.
        # Inicializamos independentemente de use_subprocess.
        self.vec_env = LobbyVectorEnv(
            [make_env for _ in range(self.num_envs)]
        )

        dummy_obs = self.vec_env.reset()

        if dummy_obs.ndim != 3:
            raise ValueError(
                "Esperava observações no formato "
                "(num_lobbies, 8, obs_dim), "
                f"recebi {dummy_obs.shape}"
            )

        self.obs_dim = dummy_obs.shape[-1]

        print(f"📐 Observation dim: {self.obs_dim}")
        print(f"📐 Vec observation shape: {dummy_obs.shape}")

        # ============================================================
        # 🧠 POLICY
        # ============================================================

        self.policy = TFTPolicy(
            self.obs_dim,
            self.ACTION_DIMS
        ).to(self.device)

        # ============================================================
        # 💾 CHECKPOINT
        # ============================================================

        self.start_update = 1

        checkpoint_path = (
            "tft_checkpoint.pt"
        )

        if os.path.exists(
            checkpoint_path
        ):

            print(
                "📂 Carregando checkpoint completo..."
            )

            checkpoint = torch.load(
                checkpoint_path,
                map_location=self.device
            )

            migrated_checkpoint = self.policy.load_compatible_state_dict(
                checkpoint["policy"]
            )
            if migrated_checkpoint:
                print(
                    "⚠️ Checkpoint migrado para a observação temporal e a nova cabeça "
                    "MOVE_BENCH. O estado do optimizer/scheduler será reiniciado."
                )
            else:
                print("✅ Pesos da política carregados sem migração.")

            # --------------------------------------------------------
            # OPTIMIZER
            # --------------------------------------------------------

            self.optimizer = optim.Adam(
                self.policy.parameters(),
                lr=3e-4,
                eps=1e-5
            )

            if "optimizer" in checkpoint and not migrated_checkpoint:

                self.optimizer.load_state_dict(
                    checkpoint["optimizer"]
                )

                print("✅ Estado do optimizer restaurado.")
                restored_lr = [float(group["lr"]) for group in self.optimizer.param_groups]
                print(f"📉 LR efetiva após restaurar optimizer: {restored_lr}")
            elif migrated_checkpoint:
                print("ℹ️ Optimizer reiniciado porque as formas dos pesos mudaram.")

            # --------------------------------------------------------
            # SCHEDULER
            # --------------------------------------------------------

            self.scheduler = (
                optim.lr_scheduler.CosineAnnealingLR(
                    self.optimizer,
                    T_max=2000,
                    eta_min=5e-5
                )
            )

            if "scheduler" in checkpoint and not migrated_checkpoint:

                self.scheduler.load_state_dict(
                    checkpoint["scheduler"]
                )

                print("✅ Estado do scheduler restaurado.")
                print(
                    f"🗓️ Scheduler restaurado | last_epoch={self.scheduler.last_epoch} | "
                    f"LR atual={[float(group['lr']) for group in self.optimizer.param_groups]}"
                )
            elif migrated_checkpoint:
                print("ℹ️ Scheduler reiniciado para a arquitetura atual.")

            # --------------------------------------------------------
            # Controlled LR override (opt-in via TFT_PPO_LR)
            # --------------------------------------------------------
            requested_lr = os.getenv("TFT_PPO_LR")
            if requested_lr:
                controlled_lr = float(requested_lr)
                if not np.isfinite(controlled_lr) or controlled_lr <= 0:
                    raise ValueError("TFT_PPO_LR deve ser um número finito > 0.")
                for group in self.optimizer.param_groups:
                    group["lr"] = controlled_lr
                min_lr = float(os.getenv("TFT_PPO_MIN_LR", str(min(2e-5, controlled_lr))))
                if not np.isfinite(min_lr) or min_lr < 0 or min_lr > controlled_lr:
                    raise ValueError("TFT_PPO_MIN_LR deve estar entre 0 e TFT_PPO_LR.")
                # Reinicia a fase do scheduler para que a curva antiga do
                # checkpoint não altere silenciosamente o teste controlado.
                self.scheduler = optim.lr_scheduler.CosineAnnealingLR(
                    self.optimizer,
                    T_max=2000,
                    eta_min=min_lr,
                )
                print(
                    f"🧪 LR controlado via ambiente: lr={controlled_lr:.2e}, "
                    f"eta_min={min_lr:.2e}"
                )

            # --------------------------------------------------------
            # UPDATE
            # --------------------------------------------------------

            self.start_update = (
                checkpoint.get(
                    "update",
                    0
                )
                + 1
            )

            print(
                f"▶️ Retomando do update "
                f"{self.start_update}"
            )

            print(
                "⚠️ ATENÇÃO: o checkpoint anterior "
                "foi treinado antes do Self-Play."
            )

            print(
                "⚠️ Os pesos são compatíveis com a "
                "policy, mas o comportamento aprendido "
                "é de ambiente antigo."
            )

        else:

            print(
                "⚠️ Nenhum checkpoint encontrado, "
                "iniciando do zero."
            )

            self.optimizer = optim.Adam(
                self.policy.parameters(),
                lr=3e-4,
                eps=1e-5
            )

            self.scheduler = (
                optim.lr_scheduler.CosineAnnealingLR(
                    self.optimizer,
                    T_max=2000,
                    eta_min=5e-5
                )
            )

            requested_lr = os.getenv("TFT_PPO_LR")
            if requested_lr:
                controlled_lr = float(requested_lr)
                if not np.isfinite(controlled_lr) or controlled_lr <= 0:
                    raise ValueError("TFT_PPO_LR deve ser um número finito > 0.")
                for group in self.optimizer.param_groups:
                    group["lr"] = controlled_lr
                min_lr = float(os.getenv("TFT_PPO_MIN_LR", str(min(2e-5, controlled_lr))))
                if not np.isfinite(min_lr) or min_lr < 0 or min_lr > controlled_lr:
                    raise ValueError("TFT_PPO_MIN_LR deve estar entre 0 e TFT_PPO_LR.")
                # Reinicia a fase do scheduler para que a curva antiga do
                # checkpoint não altere silenciosamente o teste controlado.
                self.scheduler = optim.lr_scheduler.CosineAnnealingLR(
                    self.optimizer,
                    T_max=2000,
                    eta_min=min_lr,
                )
                print(
                    f"🧪 LR controlado via ambiente: lr={controlled_lr:.2e}, "
                    f"eta_min={min_lr:.2e}"
                )

        # ============================================================
        # 🧠 PPO TRAINER
        # ============================================================

        self.ppo = PPOTrainer(
            self.policy,
            self.optimizer,
            self.writer,
            clip_coef=0.2,
            ent_coef=0.02,
            vf_coef=0.5,
            max_grad_norm=0.5,
            target_kl=0.02
        )

    # ================================================================
    # 🔄 FLATTEN OBSERVATIONS
    # ================================================================

    def _flatten_observations(
        self,
        observations
    ):
        """
        Converte:

            (num_lobbies, 8, obs_dim)

        para:

            (num_lobbies * 8, obs_dim)

        Exemplo:

            (4, 8, 300)
                ↓
            (32, 300)
        """

        observations = np.asarray(
            observations,
            dtype=np.float32
        )

        expected_shape = (
            self.num_envs,
            self.PLAYERS_PER_LOBBY,
            self.obs_dim
        )

        if observations.shape != expected_shape:

            raise ValueError(
                "Shape de observation inválido: "
                f"{observations.shape} "
                f"!= {expected_shape}"
            )

        return observations.reshape(
            self.num_agents,
            self.obs_dim
        )

    # ================================================================
    # 🎭 FLATTEN MASKS
    # ================================================================

    # ================================================================
    # AUDITAR AÇÃO ESCOLHIDA CONTRA AS MÁSCARAS
    # ================================================================
    def _audit_selected_action_masks(self, actions, masks, action_array=None):
        """Conta ações incompatíveis com as máscaras usadas pela policy.

        action_array permite reutilizar a conversão CPU/NumPy já feita
        pelo loop de rollout, mantendo a chamada antiga compatível.
        """
        action_np = (
            action_array
            if action_array is not None
            else actions.detach().cpu().numpy()
        )
        mask_np = {
            key: value.detach().cpu().numpy().astype(np.bool_, copy=False)
            for key, value in masks.items()
        }
        counts = {"actions_checked": int(action_np.shape[0]), "type_invalid": 0,
                  "conditional_invalid": 0, "selected_invalid": 0}
        for agent_idx, action in enumerate(action_np):
            action_type = int(action[0])
            type_valid = (0 <= action_type < mask_np["type_mask"].shape[1]
                          and bool(mask_np["type_mask"][agent_idx, action_type]))
            if not type_valid:
                counts["type_invalid"] += 1
                counts["selected_invalid"] += 1
                continue
            conditional_valid = True
            if action_type == int(ActionType.BUY):
                slot = int(action[1])
                conditional_valid = (0 <= slot < mask_np["shop_mask"].shape[1]
                                     and bool(mask_np["shop_mask"][agent_idx, slot]))
            elif action_type == int(ActionType.SELL):
                slot = int(action[2])
                conditional_valid = (
                    0 <= slot < mask_np["bench_source_mask"].shape[1]
                    and bool(mask_np["bench_source_mask"][agent_idx, slot])
                )
            elif action_type == int(ActionType.MOVE_BENCH):
                source, target = int(action[2]), int(action[3])
                source_mask = mask_np["bench_move_source_mask"][agent_idx]
                target_masks = mask_np["bench_to_board_target_masks"][agent_idx]
                conditional_valid = (0 <= source < source_mask.shape[0]
                                     and bool(source_mask[source])
                                     and 0 <= target < target_masks.shape[1]
                                     and bool(target_masks[source, target]))
            elif action_type == int(ActionType.MOVE_BOARD):
                source, target = int(action[4]), int(action[5])
                source_mask = mask_np["board_source_mask"][agent_idx]
                target_masks = mask_np["board_move_target_masks"][agent_idx]
                conditional_valid = (0 <= source < source_mask.shape[0]
                                     and bool(source_mask[source])
                                     and 0 <= target < target_masks.shape[1]
                                     and bool(target_masks[source, target]))
            elif action_type == int(ActionType.EQUIP_FROM_INVENTORY):
                item_slot, target = int(action[1]), int(action[2])
                inventory_mask = mask_np["item_inventory_mask"][agent_idx]
                target_mask = mask_np["item_target_mask"][agent_idx]
                conditional_valid = (
                    0 <= item_slot < inventory_mask.shape[0]
                    and bool(inventory_mask[item_slot])
                    and 0 <= target < target_mask.shape[0]
                    and bool(target_mask[target])
                )
            elif action_type == int(ActionType.CRAFT_AND_EQUIP):
                first, second, target = int(action[1]), int(action[2]), int(action[3])
                first_mask = mask_np["item_component_first_mask"][agent_idx]
                pair_masks = mask_np["item_component_pair_masks"][agent_idx]
                target_mask = mask_np["item_target_mask"][agent_idx]
                conditional_valid = (
                    0 <= first < first_mask.shape[0]
                    and bool(first_mask[first])
                    and 0 <= second < pair_masks.shape[1]
                    and bool(pair_masks[first, second])
                    and 0 <= target < target_mask.shape[0]
                    and bool(target_mask[target])
                )
            if not conditional_valid:
                counts["conditional_invalid"] += 1
                counts["selected_invalid"] += 1
        return counts

    def _flatten_masks(
        self,
        gym_masks
    ):
        """
        Converte as máscaras:

            lobby 0
                player 0
                player 1
                ...
                player 7

            lobby 1
                player 0
                ...

        para:

            num_agents

        Retorna um dicionário:

            {
                "type_mask":        (agents, 9),
                "item_inventory_mask": (agents, 9),
                "item_component_first_mask": (agents, 10),
                "item_component_pair_masks": (agents, 10, 10),
                "item_target_mask": (agents, 37),
                "shop_mask":        (agents, 5),
                ...
            }

        ============================================================
        ⚠️ JOGADOR MORTO
        ============================================================

        Jogador morto recebe máscara de PASS.

        PASS = ActionType.PASS = 6

        Isso evita distribuição categórica inválida.
        """

        flat_masks = {}

        # ------------------------------------------------------------
        # Quantidade de lobbies
        # ------------------------------------------------------------

        if len(gym_masks) != self.num_envs:

            raise ValueError(
                f"Número de máscaras recebido "
                f"({len(gym_masks)}) != "
                f"num_envs ({self.num_envs})"
            )

        # ------------------------------------------------------------
        # Percorrer lobbies
        # ------------------------------------------------------------

        for lobby_idx in range(
            self.num_envs
        ):

            lobby_masks = gym_masks[
                lobby_idx
            ]

            if len(lobby_masks) != self.PLAYERS_PER_LOBBY:

                raise ValueError(
                    f"Lobby {lobby_idx} possui "
                    f"{len(lobby_masks)} jogadores "
                    f"nas máscaras."
                )

        # ------------------------------------------------------------
        # Cada máscara
        # ------------------------------------------------------------

        for key, shape in self.MASK_SHAPES.items():

            values = []

            for lobby_idx in range(
                self.num_envs
            ):

                lobby_masks = gym_masks[
                    lobby_idx
                ]

                for player_idx in range(
                    self.PLAYERS_PER_LOBBY
                ):

                    raw_mask = np.asarray(lobby_masks[player_idx][key])

                    expected_shape = shape

                    # 1. Validar o formato antes da conversão
                    if raw_mask.shape != expected_shape:
                        raise ValueError(
                            f"Máscara '{key}' inválida para "
                            f"lobby={lobby_idx}, player={player_idx}: "
                            f"shape recebido={raw_mask.shape}, "
                            f"esperado={expected_shape}"
                        )

                    # 2. Aceitar somente tipos booleanos ou numéricos
                    if not (
                        np.issubdtype(raw_mask.dtype, np.bool_)
                        or np.issubdtype(raw_mask.dtype, np.number)
                    ):
                        raise TypeError(
                            f"Máscara '{key}' possui tipo inválido: "
                            f"{raw_mask.dtype}"
                        )

                    # Boolean masks already satisfy both value checks:
                    # they cannot contain NaN/Inf and every value is 0 or 1.
                    # Keep the full validation path for numeric masks.
                    if not np.issubdtype(raw_mask.dtype, np.bool_):
                        if not np.all(np.isfinite(raw_mask)):
                            raise ValueError(
                                f"Máscara '{key}' contém NaN ou infinito."
                            )

                        if not np.all((raw_mask == 0) | (raw_mask == 1)):
                            raise ValueError(
                                f"Máscara '{key}' deve conter somente 0 e 1."
                            )

                    # astype(copy=False) reuses bool arrays without copying.
                    # Shape was checked before conversion; astype never changes it.
                    player_mask = raw_mask.astype(np.bool_, copy=False)

                    values.append(
                        player_mask
                    )

            flat_mask = np.asarray(
                values,
                dtype=np.bool_
            )

            flat_masks[key] = torch.as_tensor(
                flat_mask,
                dtype=torch.bool,
                device=self.device
            )

        # ============================================================
        # ☠️ CORREÇÃO DE JOGADORES MORTOS
        # ============================================================

        type_mask = flat_masks[
            "type_mask"
        ]

        invalid_agents = ~type_mask.any(dim=1)

        if bool(invalid_agents.any()):
            # Apply the same PASS fallback to all invalid agents in one
            # tensor operation instead of synchronizing/checking each row.
            type_mask[invalid_agents] = False
            type_mask[invalid_agents, int(ActionType.PASS)] = True

            flat_masks["shop_mask"][invalid_agents] = False
            flat_masks["shop_mask"][invalid_agents, 0] = True

            flat_masks["bench_source_mask"][invalid_agents] = False
            flat_masks["bench_source_mask"][invalid_agents, 0] = True

            flat_masks["board_target_mask"][invalid_agents] = False
            flat_masks["board_target_mask"][invalid_agents, 0] = True

            flat_masks["board_source_mask"][invalid_agents] = False
            flat_masks["board_source_mask"][invalid_agents, 0] = True

            flat_masks["board_move_target_masks"][invalid_agents] = False
            flat_masks["board_move_target_masks"][invalid_agents, 0, 0] = True

        return flat_masks

    # ================================================================
    # 🎮 ACTIONS → DICTS
    # ================================================================

    def _actions_to_lobby_format(
        self,
        actions,
        action_array=None,
    ):
        """
        Converte ações da policy:

            (num_agents, 6)

        para:

            [
                [
                    player0,
                    player1,
                    ...
                    player7
                ],
                [
                    player0,
                    ...
                ]
            ]

        Formato exigido pelo TFTGymEnv.
        """

        actions = (
            action_array
            if action_array is not None
            else actions.detach().cpu().numpy()
        )

        expected_shape = (
            self.num_agents,
            self.ACTION_DIM
        )

        if actions.shape != expected_shape:

            raise ValueError(
                f"Shape de actions inválido: "
                f"{actions.shape} "
                f"!= {expected_shape}"
            )

        lobby_actions = []

        for lobby_idx in range(
            self.num_envs
        ):

            players = []

            for player_idx in range(
                self.PLAYERS_PER_LOBBY
            ):

                agent_idx = (
                    lobby_idx
                    * self.PLAYERS_PER_LOBBY
                    + player_idx
                )

                action = actions[
                    agent_idx
                ]

                action_type = int(action[0])

                # Keep the six-value PPO action record unchanged, but decode
                # item arguments into the exact keys consumed by the native
                # adapter. Generic shop/bench keys are not aliases for items.
                if action_type == int(ActionType.EQUIP_FROM_INVENTORY):
                    players.append({
                        "type": action_type,
                        "item_slot": int(action[1]),
                        "item_target": int(action[2]),
                    })
                elif action_type == int(ActionType.CRAFT_AND_EQUIP):
                    players.append({
                        "type": action_type,
                        "component_first": int(action[1]),
                        "component_second": int(action[2]),
                        "item_target": int(action[3]),
                    })
                else:
                    players.append({
                        "type": action_type,
                        "shop_slot": int(action[1]),
                        "bench_slot": int(action[2]),
                        "board_target": int(action[3]),
                        "board_source": int(action[4]),
                        "board_move_target": int(action[5]),
                    })

            lobby_actions.append(
                players
            )

        return lobby_actions

    # ================================================================
    # 📊 REWARDS → FLAT
    # ================================================================

    def _flatten_vector(
        self,
        values,
        name
    ):
        """
        Converte:

            (num_lobbies, 8)

        para:

            (num_lobbies * 8,)
        """

        values = np.asarray(
            values,
            dtype=np.float32
        )

        expected_shape = (
            self.num_envs,
            self.PLAYERS_PER_LOBBY
        )

        if values.shape != expected_shape:

            raise ValueError(
                f"{name} possui shape "
                f"{values.shape}, "
                f"esperado {expected_shape}"
            )

        return values.reshape(
            self.num_agents
        )

    # ================================================================
    # 🧠 STRATEGY LOGGING
    # ================================================================

    def _collect_strategy_counts(
        self,
        strategies
    ):
        """
        strategies vem como:

            [
                [
                    strategy_p0,
                    ...
                    strategy_p7
                ],
                ...
            ]

        Conta todos os jogadores.
        """

        counts = np.zeros(
            len(Strategy),
            dtype=np.int32
        )

        for lobby_strategies in strategies:

            for strategy in lobby_strategies:

                if strategy is None:
                    continue

                try:

                    counts[
                        strategy.value
                    ] += 1

                except (
                    AttributeError,
                    IndexError
                ):

                    pass

        return counts

    # ================================================================
    # 🏋️ TRAIN
    # ================================================================

    def train(
        self,
        total_updates=1000,
        rollout_steps=128
    ):

        start = self.start_update

        end = (
            start
            + total_updates
        )

        print(
            f"🔄 Executando updates "
            f"de {start} até {end - 1} "
            f"(total de {total_updates} updates)"
        )

        print(
            f"🏟️ Lobbies simultâneas: "
            f"{self.num_envs}"
        )

        print(
            f"👥 Jogadores por lobby: "
            f"{self.PLAYERS_PER_LOBBY}"
        )

        print(
            f"🤖 Agentes simultâneos: "
            f"{self.num_agents}"
        )

        # ============================================================
        # 📦 ROLLOUT BUFFER
        # ============================================================

        rollout = RolloutBuffer(
            rollout_steps,
            self.num_agents,
            self.obs_dim,
            self.ACTION_DIM,
            self.device,
            self.MASK_SHAPES
        )

        # ============================================================
        # 🔄 RESET
        # ============================================================

        raw_obs = self.vec_env.reset()

        obs_np = self._flatten_observations(
            raw_obs
        )

        obs = torch.as_tensor(
            obs_np,
            dtype=torch.float32,
            device=self.device
        )

        # ============================================================
        # DONE INDIVIDUAL
        # ============================================================

        dones = torch.zeros(
            self.num_agents,
            dtype=torch.float32,
            device=self.device
        )

        # ============================================================
        # 📈 EPISODE RETURNS
        # ============================================================

        episode_returns = np.zeros(
            self.num_agents,
            dtype=np.float32
        )

        # Evita registrar várias vezes o mesmo episódio individual.
        episode_active = np.ones(
            self.num_agents,
            dtype=np.bool_,
        )

        # ☠️ Controle de jogadores que ainda podem gerar experiências.
        # Começam todos ativos no início das partidas.
        active_agents = np.ones(
            self.num_agents,
            dtype=np.bool_,
        )

        episode_history = []

        print(
            f"🚀 Iniciando treinamento em "
            f"{self.device}"
        )

        print(
            f"🏟️ {self.num_envs} lobbies "
            f"× {self.PLAYERS_PER_LOBBY} jogadores "
            f"= {self.num_agents} agentes"
        )

        # ============================================================
        # 🔁 UPDATE LOOP
        # ============================================================

        # 📊 Métricas das máscaras durante este update
        mask_valid_type_sum = 0.0
        mask_valid_board_move_sum = 0.0
        mask_valid_bench_move_sum = 0.0
        mask_samples = 0

        # 📊 Último snapshot acumulado da lobby
        anti_loop_totals = {}
        match_steps = np.zeros(self.num_envs, dtype=np.int64)
        completed_matches = 0
        completed_wins = 0
        placement_sum = 0.0
        placement_samples = 0
        outcome_sample_step = 0

        for update in range(
            start,
            end
        ):

            anti_loop_start_totals = dict(anti_loop_totals)
            mask_audit_counts = {
                "actions_checked": 0,
                "type_invalid": 0,
                "conditional_invalid": 0,
                "selected_invalid": 0,
            }
            rollout.reset()

            # --------------------------------------------------------
            # LOGGING
            # --------------------------------------------------------

            # Include item actions in the shared policy action histogram.
            action_type_counts = np.zeros(
                len(ActionType),
                dtype=np.int32
            )

            strategy_counts = np.zeros(
                len(Strategy),
                dtype=np.int32
            )

            self.policy.eval()

            # ========================================================
            # 📥 COLETA DE EXPERIÊNCIAS
            # ========================================================

            for step in range(
                rollout_steps
            ):

                # ====================================================
                # 🎭 MÁSCARAS
                # ====================================================

                gym_masks = (
                    self.vec_env.env_method(
                        "get_action_masks"
                    )
                )

                masks = self._flatten_masks(
                    gym_masks
                )

                # 📊 Quantas opções permaneceram válidas após as máscaras?
                valid_type_mean = (
                    masks["type_mask"].sum(dim=1).float().mean()
                )

                # Conta somente pares reais origem/destino; fallbacks técnicos
                # não contam quando o tipo de movimento está desabilitado.
                board_move_enabled = (
                    masks["type_mask"][:, 4].view(-1, 1, 1)
                    & masks["board_source_mask"].unsqueeze(-1)
                    & masks["board_move_target_masks"]
                )
                bench_move_enabled = (
                    masks["type_mask"][:, 3].view(-1, 1, 1)
                    & masks["bench_move_source_mask"].unsqueeze(-1)
                    & masks["bench_to_board_target_masks"]
                )

                valid_board_move_mean = (
                    board_move_enabled.sum(dim=(1, 2)).float().mean()
                )
                valid_bench_move_mean = (
                    bench_move_enabled.sum(dim=(1, 2)).float().mean()
                )

                # Transfer the three scalar diagnostics to the host together,
                # avoiding three separate device synchronizations per step.
                mask_metric_values = torch.stack((
                    valid_type_mean,
                    valid_board_move_mean,
                    valid_bench_move_mean,
                )).detach().cpu().tolist()
                mask_valid_type_sum += mask_metric_values[0]
                mask_valid_board_move_sum += mask_metric_values[1]
                mask_valid_bench_move_sum += mask_metric_values[2]

                mask_samples += 1

                # ====================================================
                # 🧠 STRATEGIES
                # ====================================================

                current_strategies = (
                    self.vec_env.env_method(
                        "get_strategies"
                    )
                )

                current_strategy_counts = (
                    self._collect_strategy_counts(
                        current_strategies
                    )
                )

                strategy_counts += (
                    current_strategy_counts
                )


                # 📸 Fotografa quem pode gerar experiência neste passo.
                # A cópia precisa acontecer ANTES da ação.
                transition_valid = active_agents.copy()

                # ====================================================
                # 🤖 POLICY
                # ====================================================

                head_entropy_diagnostics = None
                with torch.no_grad():
                    if step % 10 == 0:
                        (
                            actions,
                            logprobs,
                            _,
                            values,
                            head_entropy_diagnostics,
                        ) = self.policy.get_action_and_value_with_entropy_diagnostics(
                            obs, masks=masks
                        )
                    else:
                        actions, logprobs, _, values = self.policy.get_action(
                            obs, masks=masks
                        )

                # Sample entropy diagnostics every ten rollout steps to avoid
                # CPU synchronization/logging overhead on every action batch.
                if head_entropy_diagnostics:
                    entropy_by_head = {}
                    for player_records in head_entropy_diagnostics:
                        for record in player_records:
                            bucket = entropy_by_head.setdefault(record["head"], [[], []])
                            bucket[0].append(float(record["entropy_nats"]))
                            bucket[1].append(float(record["entropy_normalized"]))
                    entropy_step = update * rollout_steps + step
                    for head, (nats, normalized) in entropy_by_head.items():
                        if nats:
                            self.writer.add_scalar(
                                f"policy_entropy/{head}_nats", float(np.mean(nats)), entropy_step
                            )
                            self.writer.add_scalar(
                                f"policy_entropy/{head}_normalized", float(np.mean(normalized)), entropy_step
                            )

                # ====================================================
                # 📊 ACTION LOGGING
                # ====================================================

                action_np = (
                    actions.detach()
                    .cpu()
                    .numpy()
                )

                action_audit = self._audit_selected_action_masks(
                    actions, masks, action_array=action_np
                )
                for key, value in action_audit.items():
                    mask_audit_counts[key] += value

                # Vectorized equivalent of the per-agent histogram loop.
                # Ignore out-of-range action IDs exactly as the old loop did.
                action_types = action_np[:, 0].astype(np.int64, copy=False)
                valid_action_types = action_types[
                    (action_types >= 0) & (action_types < len(ActionType))
                ]
                action_type_counts += np.bincount(
                    valid_action_types,
                    minlength=len(ActionType),
                ).astype(np.int32, copy=False)

                # ====================================================
                # 🎮 CONVERTER PARA LOBBIES
                # ====================================================

                lobby_actions = (
                    self._actions_to_lobby_format(
                        actions, action_array=action_np
                    )
                )

                # ====================================================
                # 🏟️ EXECUTAR LOBBIES
                # ====================================================

                (
                    next_obs_raw,
                    rewards_raw,
                    lobby_dones_raw,
                    infos
                ) = self.vec_env.step(
                    lobby_actions
                )

                # Resultado final, colocação e duração de cada partida.
                for lobby_idx, info in enumerate(infos):
                    match_steps[lobby_idx] += 1
                    if not info.get("lobby_done", False):
                        continue

                    completed_matches += 1
                    final_state = info.get("final_state") or {}
                    final_players = final_state.get("players", [])
                    if not isinstance(final_players, list):
                        final_players = []

                    placements_by_player = {}
                    for player_idx, player_data in enumerate(final_players):
                        if not isinstance(player_data, dict):
                            continue
                        player_id = int(player_data.get("player_id", player_idx))
                        placement = player_data.get("placement")
                        try:
                            placement = int(placement) if placement is not None else None
                        except (TypeError, ValueError):
                            placement = None
                        if placement is not None and 1 <= placement <= self.PLAYERS_PER_LOBBY:
                            placements_by_player[player_id] = placement

                    ranking = final_state.get("ranking") or info.get("ranking")
                    if isinstance(ranking, list):
                        for rank_idx, ranked_player in enumerate(ranking, start=1):
                            if isinstance(ranked_player, dict):
                                ranked_player = ranked_player.get("player_id")
                            try:
                                player_id = int(ranked_player)
                            except (TypeError, ValueError):
                                continue
                            placements_by_player.setdefault(player_id, rank_idx)

                    placement_rewards = info.get("placement_rewards")
                    reward_values = None
                    if isinstance(placement_rewards, dict):
                        reward_values = {}
                        for player_id, value in placement_rewards.items():
                            try:
                                reward_values[int(player_id)] = float(value)
                            except (TypeError, ValueError):
                                continue
                    elif placement_rewards is not None:
                        placement_reward_array = np.asarray(
                            placement_rewards,
                            dtype=np.float32,
                        ).reshape(-1)
                        if (
                            placement_reward_array.size == self.PLAYERS_PER_LOBBY
                            and np.any(np.abs(placement_reward_array) > 1e-6)
                        ):
                            reward_values = {
                                idx: float(value)
                                for idx, value in enumerate(placement_reward_array)
                            }

                    # Usa placement_rewards apenas como fallback se ranking/placement
                    # não estiverem disponíveis; não inventa resultados ausentes.
                    if reward_values:
                        for player_id, placement_reward in reward_values.items():
                            if player_id not in placements_by_player and np.isfinite(placement_reward) and -1.001 <= placement_reward <= 1.001:
                                inferred = int(round((1.0 - placement_reward) * (self.PLAYERS_PER_LOBBY - 1) / 2.0)) + 1
                                if 1 <= inferred <= self.PLAYERS_PER_LOBBY:
                                    placements_by_player[player_id] = inferred

                    for player_id, placement in sorted(placements_by_player.items()):
                        if not 1 <= placement <= self.PLAYERS_PER_LOBBY:
                            continue
                        outcome_sample_step += 1
                        placement_samples += 1
                        placement_sum += placement
                        completed_wins += int(placement == 1)
                        self.writer.add_scalar("outcomes/final_placement", placement, outcome_sample_step)
                        self.writer.add_scalar("outcomes/win", float(placement == 1), outcome_sample_step)
                        self.writer.add_scalar("outcomes/mean_placement", placement_sum / placement_samples, outcome_sample_step)
                        self.writer.add_scalar("outcomes/win_rate", completed_wins / placement_samples, outcome_sample_step)

                    self.writer.add_scalar("outcomes/matches_completed", completed_matches, completed_matches)
                    self.writer.add_scalar("outcomes/match_duration_steps", int(match_steps[lobby_idx]), completed_matches)
                    final_round = final_state.get("round", info.get("round"))
                    if final_round is not None:
                        try:
                            self.writer.add_scalar("outcomes/match_duration_rounds", float(final_round), completed_matches)
                        except (TypeError, ValueError):
                            pass
                    match_steps[lobby_idx] = 0

                # 📊 Captura os contadores reais de todas as lobbies
                metrics_by_lobby = (
                    self.vec_env.env_method(
                        "get_anti_loop_metrics"
                    )
                )

                anti_loop_totals = {}

                for lobby_metrics in metrics_by_lobby:
                    for key, value in lobby_metrics.items():
                        anti_loop_totals[key] = (
                            anti_loop_totals.get(key, 0) + value
                        )

                # ====================================================
                # 👀 NEXT OBS
                # ====================================================

                next_obs_np = (
                    self._flatten_observations(
                        next_obs_raw
                    )
                )

                next_obs = torch.as_tensor(
                    next_obs_np,
                    dtype=torch.float32,
                    device=self.device
                )

                # ====================================================
                # ❤️ REWARDS
                # ====================================================

                rewards_np = (
                    self._flatten_vector(
                        rewards_raw,
                        "rewards"
                    )
                )

                rewards = torch.as_tensor(
                    rewards_np,
                    dtype=torch.float32,
                    device=self.device
                )

                # ====================================================
                # ☠️ PLAYER DONES
                # ====================================================

                player_dones_np = (
                    self._flatten_vector(
                        lobby_dones_raw,
                        "player_dones"
                    )
                )

                # ☠️ Atualiza a atividade depois da ação.
                # A transição deste passo já foi marcada em transition_valid.

                for lobby_idx, info in enumerate(infos):
                    start_idx = lobby_idx * self.PLAYERS_PER_LOBBY
                    end_idx = start_idx + self.PLAYERS_PER_LOBBY

                    if info.get("lobby_done", False):
                        # A partida terminou e a lobby foi reiniciada.
                        # Os oito jogadores podem gerar novas experiências.
                        active_agents[start_idx:end_idx] = True
                    else:
                        # Jogadores eliminados não geram experiências
                        # nos próximos passos da mesma partida.
                        active_agents[start_idx:end_idx] &= (
                            ~player_dones_np[start_idx:end_idx].astype(np.bool_)
                        )

                next_dones = torch.as_tensor(
                    player_dones_np,
                    dtype=torch.float32,
                    device=self.device
                )

                # ====================================================
                # 📦 ROLLOUT
                # ====================================================

                rollout.add(
                    obs,
                    actions,
                    logprobs,
                    rewards,
                    next_dones,
                    values,
                    masks,
                    valid=transition_valid,
                )

                # ====================================================
                # 🔄 UPDATE STATE
                # ====================================================

                obs = next_obs

                dones = next_dones

                episode_returns += (
                    rewards_np
                )

                
                # ============================================================
                # 📊 EPISODE LOG — UM REGISTRO POR EPISÓDIO
                # ============================================================

                for agent_idx, done in enumerate(player_dones_np):
                    if done and episode_active[agent_idx]:
                        ret = float(episode_returns[agent_idx])

                        self.writer.add_scalar(
                            "charts/episode_return",
                            ret,
                            len(episode_history),
                        )

                        episode_history.append(ret)
                        episode_returns[agent_idx] = 0.0
                        episode_active[agent_idx] = False

                # Quando a lobby termina, todos os oito jogadores iniciam
                # um novo episódio na próxima partida.
                for lobby_idx, info in enumerate(infos):
                    if info.get("lobby_done", False):
                        start_idx = lobby_idx * self.PLAYERS_PER_LOBBY
                        end_idx = start_idx + self.PLAYERS_PER_LOBBY

                        episode_active[start_idx:end_idx] = True
                        episode_returns[start_idx:end_idx] = 0.0

            # ========================================================
            # 🧮 BOOTSTRAP VALUE
            # ========================================================

            gym_masks = (
                self.vec_env.env_method(
                    "get_action_masks"
                )
            )

            next_masks = self._flatten_masks(
                gym_masks
            )

            with torch.no_grad():

                next_value = (
                    self.policy.get_value(
                        obs,
                        masks=next_masks
                    )
                )

            rollout.compute_returns_and_advantages(
                next_value,
                dones
            )

            # ========================================================
            # 🔥 ENTROPY COEFFICIENT
            # ========================================================

            initial_ent = 0.02

            final_ent = 0.005

            decay_rate = 2.0

            progress = (
                (update - start)
                / max(1, end - start - 1)
            )

            progress = min(
                progress,
                1.0
            )

            self.ppo.ent_coef = exponential_schedule_value(
                progress,
                initial_ent,
                final_ent,
                decay_rate,
            )

            self.writer.add_scalar(
                "charts/entropy_coef",
                self.ppo.ent_coef,
                update
            )

            
            # ========================================================
            # 📊 ENTROPY SAMPLE
            # ========================================================

            with torch.no_grad():

                # ----------------------------------------------------
                # Selecionar somente transições válidas
                # ----------------------------------------------------

                valid_indices = torch.nonzero(
                    rollout.valid[:rollout.ptr].reshape(-1),
                    as_tuple=False,
                ).squeeze(-1)

                if valid_indices.numel() > 0:

                    sample_obs = (
                        rollout.obs[:rollout.ptr]
                        .reshape(
                            -1,
                            rollout.obs.shape[-1]
                        )[valid_indices]
                    )

                    sample_actions = (
                        rollout.actions[:rollout.ptr]
                        .reshape(
                            -1,
                            rollout.actions.shape[-1]
                        )[valid_indices]
                    )

                    sample_masks = {
                        k: v[:rollout.ptr].reshape(
                            -1,
                            *v.shape[2:]
                        )[valid_indices]
                        for k, v in rollout.masks.items()
                    }

                    # ------------------------------------------------
                    # Limitar a amostra às primeiras 256 transições
                    # válidas, não às primeiras 256 posições do buffer.
                    # ------------------------------------------------

                    sample_size = min(
                        256,
                        sample_obs.shape[0]
                    )

                    sample_obs = sample_obs[:sample_size]
                    sample_actions = sample_actions[:sample_size]

                    sample_masks = {
                        k: v[:sample_size]
                        for k, v in sample_masks.items()
                    }

                    (
                        _,
                        entropy_sample,
                        _
                    ) = self.policy.evaluate_actions(
                        sample_obs,
                        sample_actions,
                        masks=sample_masks
                    )

                    self.writer.add_scalar(
                        "entropy/total_mean",
                        entropy_sample.mean().item(),
                        update
                    )

            # ========================================================
            # 🧠 PPO UPDATE
            # ========================================================

            self.policy.train()

            self.ppo.update(
                rollout,
                batch_size=64,
                epochs=4
            )

            # ========================================================
            # 📉 SCHEDULER
            # ========================================================

            lr_used_for_update = float(self.optimizer.param_groups[0]["lr"])
            self.writer.add_scalar(
                "charts/learning_rate_before_scheduler",
                lr_used_for_update,
                update,
            )
            self.scheduler.step()

            current_lrs = [float(group["lr"]) for group in self.optimizer.param_groups]
            current_lr = current_lrs[0]

            self.writer.add_scalar(
                "charts/learning_rate",
                current_lr,
                update
            )
            self.writer.add_scalar("charts/learning_rate_min", min(current_lrs), update)
            self.writer.add_scalar("charts/learning_rate_max", max(current_lrs), update)
            self.writer.add_scalar("ppo/target_kl", float(self.ppo.target_kl), update)
  
            # ========================================================
            # 📊 GENERAL LOGS
            # ========================================================
            mean_reward = None
            valid_mask = rollout.valid[:rollout.ptr]

            if valid_mask.any():

                valid_rewards = (
                    rollout.rewards[:rollout.ptr][valid_mask]
                )

                valid_values = (
                    rollout.values[:rollout.ptr][valid_mask]
                )

                valid_advantages = (
                    rollout.advantages[:rollout.ptr][valid_mask]
                )

                mean_reward = valid_rewards.mean().item()

                self.writer.add_scalar(
                    "charts/mean_reward",
                    mean_reward,
                    update
                )

                self.writer.add_scalar(
                    "charts/value_mean",
                    valid_values.mean().item(),
                    update
                )

                self.writer.add_scalar(
                    "charts/advantage_mean",
                    valid_advantages.mean().item(),
                    update
                )

                # ========================================================
                # 🔄 ANTI-LOOP — TENSORBOARD
                # ========================================================

                # Contadores cumulativos e deltas por update.
                anti_loop_delta = {}
                counter_reset_detected = False
                for key, value in anti_loop_totals.items():
                    previous_value = anti_loop_start_totals.get(key, 0)
                    if value < previous_value:
                        counter_reset_detected = True
                        delta_value = value
                    else:
                        delta_value = value - previous_value
                    anti_loop_delta[key] = delta_value
                    self.writer.add_scalar(f"anti_loop/{key}", value, update)
                    self.writer.add_scalar(f"anti_loop_delta/{key}", delta_value, update)

                self.writer.add_scalar("anti_loop/counter_reset_detected", float(counter_reset_detected), update)
                delta_attempts = anti_loop_delta.get("execution_attempts", 0)
                delta_blocks = anti_loop_delta.get("execution_blocks", 0)
                self.writer.add_scalar(
                    "anti_loop/execution_block_rate_update",
                    delta_blocks / delta_attempts if delta_attempts > 0 else 0.0,
                    update,
                )

                # 📉 Proporção cumulativa de tentativas bloqueadas
                attempts = anti_loop_totals.get(
                    "execution_attempts", 0
                )

                blocks = anti_loop_totals.get(
                    "execution_blocks", 0
                )

                block_rate = (
                    blocks / attempts
                    if attempts > 0
                    else 0.0
                )

                self.writer.add_scalar(
                    "anti_loop/execution_block_rate",
                    block_rate,
                    update,
                )

                # Bloqueios durante a criação da máscara são distintos dos
                # bloqueios na execução de uma ação amostrada.
                board_candidates = anti_loop_delta.get("mask_board_move_candidates", 0)
                board_blocked = (
                    anti_loop_delta.get("mask_board_move_blocked_anti_loop", 0)
                    + anti_loop_delta.get("mask_board_move_blocked_seen_state", 0)
                )
                bench_candidates = anti_loop_delta.get("mask_bench_move_candidates", 0)
                bench_blocked = (
                    anti_loop_delta.get("mask_bench_move_blocked_anti_loop", 0)
                    + anti_loop_delta.get("mask_bench_move_blocked_seen_state", 0)
                )
                self.writer.add_scalar(
                    "mask_audit/board_move_candidate_filter_rate",
                    board_blocked / board_candidates if board_candidates > 0 else 0.0,
                    update,
                )
                self.writer.add_scalar(
                    "mask_audit/bench_to_board_candidate_filter_rate",
                    bench_blocked / bench_candidates if bench_candidates > 0 else 0.0,
                    update,
                )
                self.writer.add_scalar(
                    "mask_audit/board_move_candidates_update",
                    board_candidates,
                    update,
                )
                self.writer.add_scalar(
                    "mask_audit/bench_to_board_candidates_update",
                    bench_candidates,
                    update,
                )

                # Auditoria das ações amostradas contra as máscaras.
                checked = max(1, mask_audit_counts["actions_checked"])
                for key in ("actions_checked", "type_invalid", "conditional_invalid", "selected_invalid"):
                    self.writer.add_scalar(f"mask_audit/{key}", mask_audit_counts[key], update)
                self.writer.add_scalar(
                    "mask_audit/selected_invalid_rate",
                    mask_audit_counts["selected_invalid"] / checked,
                    update,
                )

                # 🎭 Médias das máscaras neste update
                if mask_samples > 0:
                    self.writer.add_scalar(
                        "anti_loop/valid_action_types_mean",
                        mask_valid_type_sum / mask_samples,
                        update,
                    )

                    self.writer.add_scalar(
                        "mask_audit/valid_board_move_pairs_mean",
                        mask_valid_board_move_sum / mask_samples,
                        update,
                    )

                    self.writer.add_scalar(
                        "mask_audit/valid_bench_to_board_pairs_mean",
                        mask_valid_bench_move_sum / mask_samples,
                        update,
                    )

            # ========================================================
            # 👥 AGENTS
            # ========================================================

            self.writer.add_scalar(
                "selfplay/num_lobbies",
                self.num_envs,
                update
            )

            self.writer.add_scalar(
                "selfplay/players_per_lobby",
                self.PLAYERS_PER_LOBBY,
                update
            )

            self.writer.add_scalar(
                "selfplay/total_agents",
                self.num_agents,
                update
            )

            # ========================================================
            # 🎭 STRATEGIES
            # ========================================================

            for strat in Strategy:

                self.writer.add_scalar(
                    f"strategy/{strat.name}",
                    strategy_counts[
                        strat.value
                    ],
                    update
                )

            # ========================================================
            # 📈 EPISODE RETURN
            # ========================================================

            if len(episode_history) > 0:

                self.writer.add_scalar(
                    "charts/episode_return_mean_100",
                    np.mean(
                        episode_history[-100:]
                    ),
                    update
                )

            # ========================================================
            # 🏆 PRINT
            # ========================================================

            if update % 5 == 0 and mean_reward is not None:

                print(
                    f"📊 UPDATE {update} | "
                    f"Reward: "
                    f"{mean_reward:.3f} | "
                    f"Agents: {self.num_agents} | "
                    f"Ent: "
                    f"{self.ppo.ent_coef:.5f}"
                )

                # ----------------------------------------------------
                # ACTION COUNTS
                # ----------------------------------------------------

                for idx, count in enumerate(
                    action_type_counts
                ):

                    try:

                        action_name = (
                            ActionType(
                                idx
                            ).name
                        )

                    except ValueError:

                        action_name = (
                            f"UNKNOWN_{idx}"
                        )

                    self.writer.add_scalar(
                        f"actions/{action_name}",
                        count,
                        update
                    )

            # ========================================================
            # 💾 CHECKPOINT
            # ========================================================

            if update % 40 == 0:

                torch.save(
                    {
                        "policy":
                            self.policy.state_dict(),

                        "optimizer":
                            self.optimizer.state_dict(),

                        "scheduler":
                            self.scheduler.state_dict(),

                        "update":
                            update
                    },
                    "tft_checkpoint.pt"
                )

                print(
                    f"💾 Checkpoint salvo | "
                    f"update={update}"
                )

        # ============================================================
        # 🔚 CLOSE
        # ============================================================

        self.vec_env.close()

        self.writer.close()


# ====================================================================
# 🚀 MAIN
# ====================================================================

if __name__ == "__main__":

    refresh_opgg_meta_catalog()

    # ================================================================
    # 🏟️ IMPORTANTE
    # ================================================================
    #
    # Agora:
    #
    #     num_envs = número de LOBBIES
    #
    # Exemplo:
    #
    #     4 lobbies
    #     × 8 jogadores
    #     = 32 agentes
    #
    # ================================================================

    trainer = Trainer(
        num_envs=4,
        use_subprocess=True
    )

    trainer.train(
        total_updates=280,
        rollout_steps=128
    )
