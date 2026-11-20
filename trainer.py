import torch
import torch.optim as optim
import numpy as np
import os
import json
import copy
import hashlib

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

from training_config import TrainingConfig, cosine_lr_factor
from decision_identity import build_player_identity_envelopes

from cpp_lobby_env import CppTFTLobbyWrapper

from torch.utils.tensorboard import SummaryWriter


from vector_lobby_env import LobbyVectorEnv

from policy import TFTPolicy
from action_contract import (
    MASK_SHAPES,
    MASK_SNAPSHOT_HASH_ALGORITHM,
    ACTION_CONTRACT_ID, ACTION_CONTRACT_VERSION, ACTION_CONTRACT_HASH,
    MASK_CONTRACT_ID, MASK_CONTRACT_VERSION, MASK_CONTRACT_HASH,
    build_action_mask_checkpoint_contract, hash_mask_rows,
    validate_action_mask_checkpoint_contract,
    build_critic_mask_input_checkpoint_contract,
    validate_critic_mask_input_checkpoint_contract,
)
from rollout import RolloutBuffer
from checkpoint_contract import (
    build_checkpoint_lineage_contract,
    validate_checkpoint_lineage_contract,
)
from reward_contract import (
    build_reward_checkpoint_contract,
    validate_reward_checkpoint_contract,
)
from ppo import PPOTrainer, exponential_schedule_value
from semantic_observation import (
    build_semantic_batch,
    build_semantic_state_checkpoint_contract,
    catalog_identity,
    validate_semantic_state_checkpoint_contract,
)

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

    MASK_SHAPES = MASK_SHAPES

    def __init__(
        self,
        num_envs=None,
        use_subprocess=True,
        item_catalog_path=None,
        config=None,
    ):
        self.config = TrainingConfig.from_env(config)
        self.config.validate()
        print("⚙️ Configuração efetiva do treinamento:")
        print(json.dumps(self.config.to_dict(), indent=2, ensure_ascii=False))


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
        self.num_envs = self.config.num_lobbies if num_envs is None else int(num_envs)
        if self.num_envs <= 0:
            raise ValueError("num_envs/num_lobbies deve ser > 0.")
        self.config.num_lobbies = self.num_envs

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
            "tft_logs/AkameIA_V4"
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
        catalog_maps = self.vec_env.env_method("get_champion_id_map")
        if not catalog_maps or any(not isinstance(item, dict) for item in catalog_maps):
            raise RuntimeError("Native champion catalog map is required for semantic PPO projection.")
        canonical_catalog = catalog_maps[0]
        if any(item != canonical_catalog for item in catalog_maps[1:]):
            raise RuntimeError("Vector lobbies expose different champion catalog identities.")
        self.champion_id_map = dict(canonical_catalog)
        self.semantic_state_contract = build_semantic_state_checkpoint_contract(
            self.champion_id_map
        )
        self.semantic_vocab_size = catalog_identity(self.champion_id_map)["vocab_size"]

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
            self.ACTION_DIMS,
            semantic_vocab_size=self.semantic_vocab_size,
        ).to(self.device)

        # ============================================================
        # 💾 CHECKPOINT / OPTIMIZER / SCHEDULER
        # ============================================================

        self.start_update = 1
        checkpoint_path = self.config.checkpoint_path
        checkpoint = None
        migrated_checkpoint = False

        legacy_action_mask_checkpoint = False
        legacy_reward_checkpoint = False
        if os.path.exists(checkpoint_path):
            print(f"📂 Carregando checkpoint: {checkpoint_path}")
            checkpoint = torch.load(checkpoint_path, map_location=self.device)
            saved_contract = checkpoint.get("action_mask_contract")
            if saved_contract is None:
                allow_legacy = os.environ.get(
                    "TFT_ALLOW_UNVERSIONED_ACTION_MASK_CHECKPOINT", ""
                ).strip().lower() in {"1", "true", "yes"}
                if not allow_legacy:
                    raise RuntimeError(
                        "Checkpoint sem identidade independente de Action Contract e Mask Contract. "
                        "Para carregar somente pesos legados de forma explícita, defina "
                        "TFT_ALLOW_UNVERSIONED_ACTION_MASK_CHECKPOINT=1; optimizer/scheduler "
                        "não serão restaurados."
                    )
                legacy_action_mask_checkpoint = True
            else:
                validate_action_mask_checkpoint_contract(saved_contract)

            saved_critic_mask_contract = checkpoint.get("critic_mask_input_contract")
            checkpoint_has_critic_mask_encoder = any(
                key.startswith("critic_mask_encoder.")
                for key in checkpoint.get("policy", {})
            )
            if saved_critic_mask_contract is None:
                if checkpoint_has_critic_mask_encoder:
                    raise RuntimeError(
                        "Checkpoint contém pesos do Critic mask encoder sem "
                        "critic_mask_input_contract; a semântica da entrada não pode ser inferida."
                    )
                # Historical checkpoint: load only through the explicit neutral
                # weight migration in TFTPolicy; optimizer/scheduler are reset.
            else:
                validate_critic_mask_input_checkpoint_contract(saved_critic_mask_contract)
                if not checkpoint_has_critic_mask_encoder:
                    raise RuntimeError(
                        "Checkpoint declara critic_mask_input_contract, mas não contém "
                        "os pesos do Critic mask encoder."
                    )

            saved_reward_contract = checkpoint.get("reward_contract")
            if saved_reward_contract is None:
                allow_legacy_reward = os.environ.get(
                    "TFT_ALLOW_UNVERSIONED_REWARD_CHECKPOINT", ""
                ).strip().lower() in {"1", "true", "yes"}
                if not allow_legacy_reward:
                    raise RuntimeError(
                        "Checkpoint sem identidade do Reward Contract. Para carregar "
                        "somente os pesos como baseline explícito, defina "
                        "TFT_ALLOW_UNVERSIONED_REWARD_CHECKPOINT=1; optimizer/scheduler "
                        "não serão restaurados."
                    )
                legacy_reward_checkpoint = True
            else:
                validate_reward_checkpoint_contract(saved_reward_contract)

            saved_semantic_contract = checkpoint.get("semantic_state_contract")
            semantic_state_keys = {
                key for key in self.policy.state_dict()
                if key.startswith(("semantic_id_embedding.", "semantic_encoder."))
            }
            present_semantic_state_keys = {
                key for key in checkpoint.get("policy", {})
                if key.startswith(("semantic_id_embedding.", "semantic_encoder."))
            }
            checkpoint_has_semantic_weights = bool(present_semantic_state_keys)
            if (
                present_semantic_state_keys
                and present_semantic_state_keys != semantic_state_keys
            ):
                raise RuntimeError(
                    "Checkpoint contém um encoder semântico parcial; "
                    "todos os pesos do contrato devem estar presentes."
                )
            if saved_semantic_contract is None:
                if checkpoint_has_semantic_weights:
                    raise RuntimeError(
                        "Checkpoint contém pesos sem semantic_state_contract; "
                        "a origem/layout do estado semântico não pode ser inferida."
                    )
                # Historical checkpoint: semantic branch migrates from its
                # neutral initialization; optimizer/scheduler are reset.
            else:
                validate_semantic_state_checkpoint_contract(
                    saved_semantic_contract, self.champion_id_map
                )
                if not checkpoint_has_semantic_weights:
                    raise RuntimeError(
                        "Checkpoint declara semantic_state_contract, mas não contém "
                        "os pesos do encoder semântico."
                    )

            saved_lineage_contract = checkpoint.get("checkpoint_contract")
            if saved_lineage_contract is None:
                allow_unversioned_lineage = os.environ.get(
                    "TFT_ALLOW_UNVERSIONED_CHECKPOINT_LINEAGE", ""
                ).strip().lower() in {"1", "true", "yes"}
                if not allow_unversioned_lineage:
                    raise RuntimeError(
                        "Checkpoint sem identidade agregada de linhagem. Para carregar "
                        "somente os pesos como baseline explícito, defina "
                        "TFT_ALLOW_UNVERSIONED_CHECKPOINT_LINEAGE=1; optimizer/scheduler "
                        "não serão restaurados."
                    )
                legacy_checkpoint_lineage = True
            else:
                if any(value is None for value in (
                    saved_contract, saved_critic_mask_contract, saved_semantic_contract,
                    saved_reward_contract,
                )):
                    raise RuntimeError(
                        "Checkpoint declara linhagem agregada, mas um contrato componente está ausente."
                    )
                validate_checkpoint_lineage_contract(
                    saved_lineage_contract,
                    self.policy.state_dict(),
                    saved_contract,
                    saved_critic_mask_contract,
                    saved_semantic_contract,
                    saved_reward_contract,
                )

            migrated_checkpoint = self.policy.load_compatible_state_dict(checkpoint["policy"])
            print("⚠️ Checkpoint migrado; optimizer/scheduler serão reiniciados." if migrated_checkpoint
                  else "✅ Pesos da policy carregados.")

        self.optimizer = optim.Adam(
            self.policy.parameters(),
            lr=self.config.learning_rate,
            eps=self.config.adam_eps,
            betas=(self.config.adam_beta1, self.config.adam_beta2),
            weight_decay=self.config.weight_decay,
        )

        saved_config = checkpoint.get("training_config", {}) if checkpoint else {}
        saved_schedule = (
            saved_config.get("lr_schedule_updates"),
            saved_config.get("min_learning_rate"),
            saved_config.get("learning_rate"),
        )
        current_schedule = (
            self.config.lr_schedule_updates,
            self.config.min_learning_rate,
            self.config.learning_rate,
        )
        can_restore_optimizer = bool(
            checkpoint and "optimizer" in checkpoint
            and not migrated_checkpoint and not legacy_action_mask_checkpoint
            and not legacy_reward_checkpoint and not legacy_checkpoint_lineage
        )
        if can_restore_optimizer:
            self.optimizer.load_state_dict(checkpoint["optimizer"])
            # Restaura os momentos do Adam, mas o LR solicitado nesta execução
            # sempre prevalece sobre o valor salvo no checkpoint.
            for group in self.optimizer.param_groups:
                group["lr"] = self.config.learning_rate
                group["eps"] = self.config.adam_eps
                group["betas"] = (self.config.adam_beta1, self.config.adam_beta2)
                group["weight_decay"] = self.config.weight_decay
            print("✅ Momentos do Adam restaurados; hiperparâmetros atuais aplicados.")

        self.scheduler = optim.lr_scheduler.LambdaLR(
            self.optimizer,
            lr_lambda=lambda step: cosine_lr_factor(
                step,
                self.config.learning_rate,
                self.config.min_learning_rate,
                self.config.lr_schedule_updates,
            ),
        )
        restore_scheduler = bool(
            can_restore_optimizer and "scheduler" in checkpoint
            and checkpoint.get("scheduler_type") == "cosine_clamped"
            and saved_schedule == current_schedule
        )
        if restore_scheduler:
            self.scheduler.load_state_dict(checkpoint["scheduler"])
            # load_state_dict restaura o estado interno, mas não atualiza
            # automaticamente o LR do optimizer para o último valor agendado.
            for group, scheduled_lr in zip(self.optimizer.param_groups, self.scheduler.get_last_lr()):
                group["lr"] = scheduled_lr
            print(
                f"✅ Scheduler restaurado | step={self.scheduler.last_epoch} | "
                f"LR={self.optimizer.param_groups[0]['lr']:.3e}"
            )
        elif checkpoint:
            print("ℹ️ Scheduler reiniciado: LR/schedule mudou ou checkpoint incompatível.")

        if checkpoint:
            if legacy_checkpoint_lineage:
                self.start_update = 1
                print("ℹ️ Checkpoint histórico carregado como baseline de pesos; nova linhagem começa no update 1.")
            else:
                self.start_update = int(checkpoint.get("update", 0)) + 1
                print(f"▶️ Retomando do update {self.start_update}")
        else:
            print("⚠️ Nenhum checkpoint encontrado; iniciando do zero.")

        self.ppo = PPOTrainer(
            self.policy,
            self.optimizer,
            self.writer,
            clip_coef=self.config.clip_coef,
            ent_coef=self.config.entropy_coef_initial,
            vf_coef=self.config.vf_coef,
            max_grad_norm=self.config.max_grad_norm,
            target_kl=self.config.target_kl,
        )
        self.ppo.update_step = self.start_update
        self.writer.add_text(
            "training/config",
            json.dumps(self.config.to_dict(), indent=2, ensure_ascii=False),
            self.start_update,
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

    @staticmethod
    def _expand_lobby_snapshot_metadata(lobby_snapshots, players_per_lobby, label):
        """Expand one lobby snapshot identity into stable per-player rollout rows."""
        expanded = []
        for lobby_idx, snapshot in enumerate(lobby_snapshots):
            if not isinstance(snapshot, dict):
                raise RuntimeError(
                    f"Lobby {lobby_idx} não forneceu metadata de {label}."
                )
            player_sequences = snapshot.get("player_decision_sequences")
            if not isinstance(player_sequences, (list, tuple)) or len(player_sequences) != players_per_lobby:
                raise RuntimeError(
                    f"Lobby {lobby_idx} não forneceu sequências individuais para {players_per_lobby} jogadores."
                )
            native_snapshot = snapshot.get("native_state_snapshot")
            native_players = None
            if native_snapshot is not None:
                if not isinstance(native_snapshot, dict):
                    raise RuntimeError(f"Snapshot estruturado inválido para lobby {lobby_idx}.")
                for field in ("engine_instance_id", "episode_id"):
                    if native_snapshot.get(field) != snapshot.get(field):
                        raise RuntimeError(f"Snapshot estruturado diverge em {field} na lobby {lobby_idx}.")
                if native_snapshot.get("snapshot_sequence") != snapshot.get("decision_sequence"):
                    raise RuntimeError(f"Snapshot estruturado diverge na sequência da lobby {lobby_idx}.")
                if native_snapshot.get("player_decision_sequences") != player_sequences:
                    raise RuntimeError(f"Snapshot estruturado diverge nas sequências individuais da lobby {lobby_idx}.")
                native_players = native_snapshot.get("players")
                if not isinstance(native_players, list) or len(native_players) != players_per_lobby:
                    raise RuntimeError(f"Snapshot estruturado sem {players_per_lobby} jogadores na lobby {lobby_idx}.")
            for player_idx, player_sequence in enumerate(player_sequences):
                if (
                    isinstance(player_sequence, bool)
                    or not isinstance(player_sequence, int)
                    or player_sequence < 0
                ):
                    raise RuntimeError(
                        f"Sequência individual inválida para lobby {lobby_idx}, jogador {player_idx}."
                    )
                metadata = dict(snapshot)
                metadata.pop("player_decision_sequences", None)
                metadata.pop("native_state_snapshot", None)
                if native_players is not None:
                    native_player = native_players[player_idx]
                    if not isinstance(native_player, dict) or native_player.get("player_id") != player_idx:
                        raise RuntimeError(f"Registro estruturado desalinhado para lobby {lobby_idx}, jogador {player_idx}.")
                    metadata["native_player_state"] = copy.deepcopy(native_player)
                    metadata["native_state_contract_id"] = native_snapshot.get("contract_id")
                    metadata["native_state_contract_version"] = native_snapshot.get("contract_version")
                    metadata["native_state_producer"] = native_snapshot.get("producer")
                    metadata["native_state_source_namespace"] = native_snapshot.get("source_namespace")
                metadata["player_decision_sequence"] = player_sequence
                metadata["lobby_index"] = lobby_idx
                metadata["player_id"] = player_idx
                envelopes = snapshot.get("player_identity_envelopes")
                # Isolated fake environments without native snapshots may build
                # deterministic fixtures; production native adapters must provide
                # envelopes from their authoritative Engine result.
                if envelopes is None and native_snapshot is None:
                    envelopes = build_player_identity_envelopes(snapshot)
                if not isinstance(envelopes, (list, tuple)) or len(envelopes) != players_per_lobby:
                    raise RuntimeError(
                        f"Lobby {lobby_idx} não forneceu envelopes canônicos para {players_per_lobby} jogadores."
                    )
                envelope = envelopes[player_idx]
                if not isinstance(envelope, dict):
                    raise RuntimeError(
                        f"Envelope canônico inválido para lobby {lobby_idx}, jogador {player_idx}."
                    )
                expected_engine_match_id = f"{snapshot.get('engine_instance_id')}/episode/{snapshot.get('episode_id')}"
                if (
                    envelope.get("engine_match_id") != expected_engine_match_id
                    or envelope.get("player_id") != f"player-{player_idx}"
                    or envelope.get("decision_sequence") != {
                        "namespace": "tft.engine.decision", "value": player_sequence,
                    }
                    or envelope.get("snapshot_sequence") != {
                        "namespace": "tft.engine.observation-snapshot",
                        "value": snapshot.get("decision_sequence"),
                    }
                ):
                    raise RuntimeError(
                        f"Envelope canônico diverge da identidade nativa para lobby {lobby_idx}, jogador {player_idx}."
                    )
                metadata.pop("player_identity_envelopes", None)
                metadata["identity"] = copy.deepcopy(envelope)
                expanded.append(metadata)
        return expanded

    @staticmethod
    def _attach_native_action_traces(result_snapshot_metadata, infos, players_per_lobby):
        """Bind each native execution trace to its exact lobby/player result row."""
        if len(result_snapshot_metadata) != len(infos) * players_per_lobby:
            raise RuntimeError(
                "Quantidade de snapshots de resultado não corresponde às lobbies/traces."
            )

        for lobby_idx, info in enumerate(infos):
            if not isinstance(info, dict):
                raise RuntimeError(
                    f"Info nativa inválida para lobby {lobby_idx}: esperado objeto."
                )
            traces = info.get("action_trace")
            if not isinstance(traces, list) or len(traces) != players_per_lobby:
                raise RuntimeError(
                    f"Lobby {lobby_idx} não forneceu {players_per_lobby} registros nativos de execução de ação."
                )
            start = lobby_idx * players_per_lobby
            for player_id, trace in enumerate(traces):
                if not isinstance(trace, dict) or not {
                    "player_id", "requested_action", "effective_action",
                    "handler_applied", "status_reason",
                }.issubset(trace):
                    raise RuntimeError(
                        f"Trace de ação inválido para lobby {lobby_idx}, jogador {player_id}."
                    )
                trace_player_id = trace.get("player_id")
                if (
                    isinstance(trace_player_id, bool)
                    or not isinstance(trace_player_id, int)
                    or trace_player_id != player_id
                ):
                    raise RuntimeError(
                        f"Trace de ação da lobby {lobby_idx} pertence ao jogador "
                        f"{trace_player_id}, esperado {player_id}."
                    )
                row = result_snapshot_metadata[start + player_id]
                if not isinstance(row, dict):
                    raise RuntimeError(
                        f"Snapshot de resultado inválido para lobby {lobby_idx}, jogador {player_id}."
                    )
                row_lobby = row.get("lobby_index")
                row_player = row.get("player_id")
                if (
                    isinstance(row_lobby, bool)
                    or not isinstance(row_lobby, int)
                    or row_lobby != lobby_idx
                    or isinstance(row_player, bool)
                    or not isinstance(row_player, int)
                    or row_player != player_id
                ):
                    raise RuntimeError(
                        f"Snapshot de resultado desalinhado para lobby {lobby_idx}, jogador {player_id}."
                    )
                row["action_trace"] = dict(trace)

        return result_snapshot_metadata

    @classmethod
    def _hash_mask_rows(cls, masks):
        """Hash each exact per-agent mask payload with the canonical v1 helper."""
        return hash_mask_rows(masks, cls.MASK_SHAPES)

    @staticmethod
    def _hash_observation_rows(observations):
        """Hash each exact float32 observation row independently and deterministically."""
        if not isinstance(observations, torch.Tensor) or observations.ndim != 2:
            raise TypeError("Observations para correlação devem ser tensor [batch, features].")
        if observations.dtype != torch.float32:
            raise TypeError("Observations para correlação devem usar torch.float32.")
        rows = observations.detach().to(device="cpu").contiguous().numpy()
        shape_identity = f"{rows.shape[1]}:float32".encode("ascii")
        hashes = []
        for row in rows:
            digest = hashlib.sha256()
            digest.update(b"tft-ppo-observation-row-v1\\x00")
            digest.update(shape_identity)
            digest.update(b"\\x00")
            digest.update(row.tobytes(order="C"))
            hashes.append(digest.hexdigest())
        return hashes


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
        gym_masks,
        lobby_player_alive=None,
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

        Jogadores eliminados recebem PASS quando a Engine publica uma
        type_mask vazia. Uma máscara vazia para jogador ainda ativo é erro
        de contrato e nunca pode ser convertida silenciosamente em PASS.

        PASS = ActionType.PASS = 6
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
            if lobby_player_alive is None:
                raise RuntimeError(
                    "A Engine publicou type_mask vazia, mas o estado de "
                    "vida dos jogadores não foi fornecido; fallback PASS "
                    "não pode ser inferido."
                )
            if len(lobby_player_alive) != self.num_envs:
                raise ValueError(
                    "Quantidade de lobbies no estado de vida "
                    f"({len(lobby_player_alive)}) != num_envs ({self.num_envs})."
                )

            alive_rows = []
            for lobby_idx, players_alive in enumerate(lobby_player_alive):
                if len(players_alive) != self.PLAYERS_PER_LOBBY:
                    raise ValueError(
                        f"Lobby {lobby_idx} possui {len(players_alive)} "
                        "estados de vida; eram esperados "
                        f"{self.PLAYERS_PER_LOBBY}."
                    )
                alive_rows.extend(bool(value) for value in players_alive)

            alive_agents = torch.as_tensor(
                alive_rows, dtype=torch.bool, device=self.device
            )
            invalid_active_agents = invalid_agents & alive_agents
            if bool(invalid_active_agents.any()):
                indices = torch.nonzero(
                    invalid_active_agents, as_tuple=False
                ).flatten().tolist()
                raise RuntimeError(
                    "A Engine publicou type_mask vazia para jogador(es) "
                    f"ativo(s): {indices}. Nenhuma ação substituta será "
                    "fabricada; verifique o produtor nativo de masks."
                )

            eliminated_agents = invalid_agents & ~alive_agents
            # PASS is a transport-safe no-op only for players explicitly
            # reported as eliminated by the authoritative lobby state.
            type_mask[eliminated_agents] = False
            type_mask[eliminated_agents, int(ActionType.PASS)] = True

            flat_masks["shop_mask"][eliminated_agents] = False
            flat_masks["shop_mask"][eliminated_agents, 0] = True

            flat_masks["bench_source_mask"][eliminated_agents] = False
            flat_masks["bench_source_mask"][eliminated_agents, 0] = True

            flat_masks["board_target_mask"][eliminated_agents] = False
            flat_masks["board_target_mask"][eliminated_agents, 0] = True

            flat_masks["board_source_mask"][eliminated_agents] = False
            flat_masks["board_source_mask"][eliminated_agents, 0] = True

            flat_masks["board_move_target_masks"][eliminated_agents] = False
            flat_masks["board_move_target_masks"][eliminated_agents, 0, 0] = True

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
                f"Shape de actions inválido: {actions.shape} != {expected_shape}"
            )
        if actions.dtype != np.int64:
            raise TypeError("Ações encaminhadas à Engine devem ser registros PPO int64.")
        TFTPolicy._validate_canonical_action_parameters(torch.from_numpy(actions))

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
    # 🏋️ TRAIN
    # ================================================================

    def train(
        self,
        total_updates=None,
        rollout_steps=None
    ):

        total_updates = self.config.total_updates if total_updates is None else int(total_updates)
        rollout_steps = self.config.rollout_steps if rollout_steps is None else int(rollout_steps)
        if rollout_steps <= 0:
            raise ValueError("rollout_steps deve ser > 0.")
        self.config.rollout_steps = rollout_steps
        self.writer.add_text(
            "training/config",
            json.dumps(self.config.to_dict(), indent=2, ensure_ascii=False),
            self.start_update,
        )
        total_updates = int(total_updates)
        if total_updates <= 0:
            raise ValueError("total_updates deve ser > 0.")
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

        progress = Progress(
            TextColumn("{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
            console=Console(),
            refresh_per_second=4,
            redirect_stdout=True,
            redirect_stderr=True,
        )
        progress.start()
        progress_task = progress.add_task(
            "Preparando treinamento",
            total=total_updates,
        )

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

                # Capture identity for the exact observation/masks used by
                # this policy decision, before any lobby is advanced.
                lobby_snapshots = self.vec_env.get_snapshot_metadata()
                flat_snapshot_metadata = self._expand_lobby_snapshot_metadata(
                    lobby_snapshots,
                    self.PLAYERS_PER_LOBBY,
                    "snapshot da decisão PPO",
                )
                for metadata, observation_hash in zip(
                    flat_snapshot_metadata,
                    self._hash_observation_rows(obs),
                ):
                    metadata["observation_snapshot_hash"] = observation_hash
                    metadata["observation_snapshot_hash_algorithm"] = "tft-ppo-observation-row-v1"

                semantic_batch = build_semantic_batch(
                    flat_snapshot_metadata, self.champion_id_map
                )
                semantic_state = {
                    "numeric": torch.as_tensor(
                        semantic_batch["numeric"], dtype=torch.float32, device=self.device
                    ),
                    "champion_ids": torch.as_tensor(
                        semantic_batch["champion_ids"], dtype=torch.long, device=self.device
                    ),
                }
                for metadata, semantic_hash in zip(
                    flat_snapshot_metadata, semantic_batch["hashes"]
                ):
                    metadata["semantic_projection_hash"] = semantic_hash
                    metadata["semantic_projection_contract_id"] = (
                        self.semantic_state_contract["contract"]["contract_id"]
                    )
                    metadata["semantic_projection_contract_hash"] = (
                        self.semantic_state_contract["sha256"]
                    )
                semantic_entities = np.asarray(
                    semantic_batch["numeric"], dtype=np.float32
                )[:, 17:].reshape(-1, 42, 6)
                unknown_semantic_champions = int(
                    ((semantic_entities[:, :, 0] > 0.5) &
                     (semantic_entities[:, :, 5] < 0.5)).sum()
                )
                self.writer.add_scalar(
                    "semantic/unknown_occupied_champion_slots",
                    unknown_semantic_champions,
                    update * rollout_steps + step,
                )

                gym_masks = (
                    self.vec_env.env_method(
                        "get_action_masks"
                    )
                )

                lobby_player_alive = self.vec_env.env_method(
                    "get_player_liveness"
                )
                masks = self._flatten_masks(
                    gym_masks,
                    lobby_player_alive=lobby_player_alive,
                )

                # Hash the exact post-ablation masks consumed by Actor and
                # persisted with this action; each player has an independent payload.
                for metadata, mask_hash in zip(
                    flat_snapshot_metadata,
                    self._hash_mask_rows(masks),
                ):
                    metadata["mask_snapshot_hash"] = mask_hash
                    metadata["mask_snapshot_hash_algorithm"] = MASK_SNAPSHOT_HASH_ALGORITHM
                    metadata["action_contract_id"] = ACTION_CONTRACT_ID
                    metadata["action_contract_version"] = ACTION_CONTRACT_VERSION
                    metadata["action_contract_hash"] = ACTION_CONTRACT_HASH
                    metadata["mask_contract_id"] = MASK_CONTRACT_ID
                    metadata["mask_contract_version"] = MASK_CONTRACT_VERSION
                    metadata["mask_contract_hash"] = MASK_CONTRACT_HASH

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

                # Strategy labels are diagnostics only; PPO collection does
                # not query the legacy get_strategies() compatibility API.

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
                            obs, masks=masks, semantic_state=semantic_state
                        )
                    else:
                        actions, logprobs, _, values = self.policy.get_action(
                            obs, masks=masks, semantic_state=semantic_state
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

                # Reward/done belong to the Engine step result; next_obs may
                # instead belong to a freshly auto-reset episode.
                flat_result_snapshot_metadata = self._expand_lobby_snapshot_metadata(
                    [info.get("step_result_snapshot") for info in infos],
                    self.PLAYERS_PER_LOBBY,
                    "snapshot de resultado da transição",
                )
                # Keep native action provenance beside the exact StepResult identity.
                self._attach_native_action_traces(
                    flat_result_snapshot_metadata,
                    infos,
                    self.PLAYERS_PER_LOBBY,
                )

                flat_next_snapshot_metadata = self._expand_lobby_snapshot_metadata(
                    [info.get("next_snapshot") for info in infos],
                    self.PLAYERS_PER_LOBBY,
                    "snapshot da próxima observação",
                )
                next_semantic_batch = build_semantic_batch(
                    flat_next_snapshot_metadata, self.champion_id_map
                )
                next_semantic_state = {
                    "numeric": torch.as_tensor(
                        next_semantic_batch["numeric"], dtype=torch.float32, device=self.device
                    ),
                    "champion_ids": torch.as_tensor(
                        next_semantic_batch["champion_ids"], dtype=torch.long, device=self.device
                    ),
                }
                for metadata, semantic_hash in zip(
                    flat_next_snapshot_metadata, next_semantic_batch["hashes"]
                ):
                    metadata["semantic_projection_hash"] = semantic_hash
                    metadata["semantic_projection_contract_id"] = (
                        self.semantic_state_contract["contract"]["contract_id"]
                    )
                    metadata["semantic_projection_contract_hash"] = (
                        self.semantic_state_contract["sha256"]
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
                for metadata, observation_hash in zip(
                    flat_next_snapshot_metadata,
                    self._hash_observation_rows(next_obs),
                ):
                    metadata["observation_snapshot_hash"] = observation_hash
                    metadata["observation_snapshot_hash_algorithm"] = "tft-ppo-observation-row-v1"

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
                    snapshot_metadata=flat_snapshot_metadata,
                    result_snapshot_metadata=flat_result_snapshot_metadata,
                    next_snapshot_metadata=flat_next_snapshot_metadata,
                    semantic_state=semantic_state,
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

            lobby_player_alive = self.vec_env.env_method(
                "get_player_liveness"
            )
            next_masks = self._flatten_masks(
                gym_masks,
                lobby_player_alive=lobby_player_alive,
            )

            with torch.no_grad():

                next_value = (
                    self.policy.get_value(
                        obs,
                        masks=next_masks,
                        semantic_state=next_semantic_state,
                    )
                )

            rollout.compute_returns_and_advantages(
                next_value,
                dones,
                gamma=self.config.gamma,
                gae_lambda=self.config.gae_lambda,
            )

            # ========================================================
            # 🔥 ENTROPY COEFFICIENT — PROGRESSO GLOBAL
            # ========================================================

            entropy_progress = min(
                1.0,
                max(0.0, (update - 1) / max(1, self.config.entropy_schedule_updates - 1)),
            )
            self.ppo.ent_coef = exponential_schedule_value(
                entropy_progress,
                self.config.entropy_coef_initial,
                self.config.entropy_coef_final,
                self.config.entropy_decay_rate,
            )
            self.writer.add_scalar("charts/entropy_coef", self.ppo.ent_coef, update)
            self.writer.add_scalar("training/entropy_schedule_progress", entropy_progress, update)

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
                    sample_semantic_state = {
                        "numeric": rollout.semantic_numeric[:rollout.ptr].reshape(
                            -1, rollout.semantic_numeric_dim
                        )[valid_indices],
                        "champion_ids": rollout.semantic_champion_ids[:rollout.ptr].reshape(
                            -1, rollout.semantic_entity_slots
                        )[valid_indices],
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
                    sample_semantic_state = {
                        k: v[:sample_size]
                        for k, v in sample_semantic_state.items()
                    }

                    (
                        _,
                        entropy_sample,
                        _
                    ) = self.policy.evaluate_actions(
                        sample_obs,
                        sample_actions,
                        masks=sample_masks,
                        semantic_state=sample_semantic_state,
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

            ppo_metrics = self.ppo.update(
                rollout,
                batch_size=self.config.batch_size,
                epochs=self.config.ppo_epochs,
            ) or {}
            self.writer.add_scalar("training/optimizer_steps", ppo_metrics.get("optimizer_steps", 0), update)
            self.writer.add_scalar("training/grad_norm_mean", ppo_metrics.get("grad_norm_mean", 0.0), update)
            self.writer.add_scalar("training/grad_norm_max", ppo_metrics.get("grad_norm_max", 0.0), update)
            self.writer.add_scalar("training/attempted_minibatches", ppo_metrics.get("attempted_batches", 0), update)
            self.writer.add_scalar("training/processed_minibatches", ppo_metrics.get("batches_processed", 0), update)
            self.writer.add_scalar("training/early_stop", float(ppo_metrics.get("early_stop", False)), update)
            self.writer.add_scalar("training/early_stop_kl", ppo_metrics.get("early_stop_kl", 0.0), update)
            self.writer.add_scalar("training/approx_kl_max", ppo_metrics.get("approx_kl_max", 0.0), update)

            # ========================================================
            # 📉 SCHEDULER
            # ========================================================

            lr_used_for_update = float(self.optimizer.param_groups[0]["lr"])
            self.writer.add_scalar(
                "charts/learning_rate_before_scheduler",
                lr_used_for_update,
                update,
            )
            if int(ppo_metrics.get("optimizer_steps", 0)) > 0:
                self.scheduler.step()
                self.writer.add_scalar("training/scheduler_stepped", 1.0, update)
            else:
                self.writer.add_scalar("training/scheduler_stepped", 0.0, update)

            current_lrs = [float(group["lr"]) for group in self.optimizer.param_groups]
            current_lr = current_lrs[0]

            self.writer.add_scalar(
                "charts/learning_rate",
                current_lr,
                update
            )
            self.writer.add_scalar("charts/learning_rate_min", min(current_lrs), update)
            self.writer.add_scalar("charts/learning_rate_max", max(current_lrs), update)
            if self.ppo.target_kl is not None:
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

            self.writer.add_scalar(
                "semantic/catalog_vocab_size",
                self.semantic_vocab_size,
                update,
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
                            update,
                        "training_config":
                            self.config.to_dict(),
                        "scheduler_type":
                            "cosine_clamped",
                        "action_mask_contract":
                            build_action_mask_checkpoint_contract(),
                        "critic_mask_input_contract":
                            build_critic_mask_input_checkpoint_contract(),
                        "semantic_state_contract": self.semantic_state_contract,
                        "reward_contract": build_reward_checkpoint_contract(),
                        "checkpoint_contract": build_checkpoint_lineage_contract(
                            self.policy.state_dict(),
                            build_action_mask_checkpoint_contract(),
                            build_critic_mask_input_checkpoint_contract(),
                            self.semantic_state_contract,
                            build_reward_checkpoint_contract(),
                        ),
                    },
                    self.config.checkpoint_path
                )

                print(
                    f"💾 Checkpoint salvo | "
                    f"update={update}"
                )

            # Atualiza a barra uma vez por update, usando métricas já calculadas.
            reward_label = f"{mean_reward:.3f}" if mean_reward is not None else "n/a"
            kl_value = ppo_metrics.get("approx_kl_max")
            kl_label = f"{float(kl_value):.4f}" if kl_value is not None else "n/a"
            progress.update(
                progress_task,
                completed=update - start + 1,
                description=(
                    f"Treino | reward {reward_label} | "
                    f"LR {current_lr:.2e} | Ent {self.ppo.ent_coef:.4f} | "
                    f"KL {kl_label}"
                ),
            )

        progress.stop()

        # Salva o último update mesmo quando não for múltiplo de 40.
        torch.save(
            {
                "policy": self.policy.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "scheduler": self.scheduler.state_dict(),
                "update": end - 1,
                "training_config": self.config.to_dict(),
                "scheduler_type": "cosine_clamped",
                "action_mask_contract": build_action_mask_checkpoint_contract(),
                "critic_mask_input_contract": build_critic_mask_input_checkpoint_contract(),
                "semantic_state_contract": self.semantic_state_contract,
                "reward_contract": build_reward_checkpoint_contract(),
                "checkpoint_contract": build_checkpoint_lineage_contract(
                    self.policy.state_dict(),
                    build_action_mask_checkpoint_contract(),
                    build_critic_mask_input_checkpoint_contract(),
                    self.semantic_state_contract,
                    build_reward_checkpoint_contract(),
                ),
            },
            self.config.checkpoint_path,
        )
        print(f"💾 Checkpoint final salvo | update={end - 1}")

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

    trainer = Trainer(use_subprocess=True)
    trainer.train()
