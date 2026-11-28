from collections.abc import Mapping, Sequence

import torch
import torch.optim as optim
import numpy as np
import os
import json
import copy
import hashlib
import random
from pathlib import Path

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
from immutable_snapshot import FrozenDict, freeze_snapshot

from cpp_lobby_env import CppTFTLobbyWrapper, _NativeLobbyBatchManager

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
    build_training_resume_contract,
    validate_training_resume_contract,
)
from reward_contract import (
    build_reward_checkpoint_contract,
    validate_reward_checkpoint_contract,
)
from ppo import PPOTrainer, exponential_schedule_value
from semantic_observation import (
    SEMANTIC_ENTITY_FEATURES,
    SEMANTIC_ENTITY_SLOTS,
    SEMANTIC_TRAIT_SLOTS,
    SEMANTIC_GLOBAL_FEATURES,
    SEMANTIC_ITEM_OFFSET,
    build_semantic_batch,
    semantic_item_state_tensors,
    build_semantic_state_checkpoint_contract,
    catalog_identity,
    validate_semantic_state_checkpoint_contract,
    validate_semantic_batch_alignment,
    semantic_batch_matches_snapshot_rows,
)

from engine_contracts import ActionType
from training_run_manifest import build_training_run_manifest, write_training_run_manifest

def project_semantic_batch(
    vec_env, metadata_rows, catalog_map, contract, lobby_snapshots=None
):
    """Project from pinned native snapshots; Python projection is fixture-only.

    Production vector environments must never silently fall back to rebuilding
    semantic rows from Python player dictionaries. The C++ producer owns the
    projection and returns contiguous buffers whose lifetime is pinned by the
    NativeDecisionBatch / native snapshot handles.
    """
    projected = None
    native_project = getattr(vec_env, "semantic_projection", None)
    if callable(native_project):
        projected = native_project(catalog_map, contract["sha256"])

    if projected is None and lobby_snapshots is not None:
        snapshot_project = getattr(vec_env, "semantic_projection_from_snapshots", None)
        if callable(snapshot_project):
            projected = snapshot_project(
                lobby_snapshots, catalog_map, contract["sha256"]
            )

    native_required = bool(
        getattr(vec_env, "semantic_projection_supported", lambda: False)()
    )
    if projected is None and native_required:
        raise RuntimeError(
            "Native semantic v8 projection was unavailable for a production "
            "NativeDecisionBatch; refusing the Python reconstruction fallback."
        )

    if projected is not None:
        numeric = np.asarray(projected["numeric"])
        champion_ids = np.asarray(projected["champion_ids"])
        if numeric.dtype != np.float32 or not numeric.flags.c_contiguous:
            raise RuntimeError(
                "Native semantic numeric buffer must be contiguous float32."
            )
        if champion_ids.dtype != np.int64 or not champion_ids.flags.c_contiguous:
            raise RuntimeError(
                "Native semantic champion ID buffer must be contiguous int64."
            )
        if numeric.ndim != 3 or numeric.shape[1:] != (8, 7958):
            raise RuntimeError(
                f"Native semantic numeric shape is invalid: {numeric.shape}"
            )
        if champion_ids.shape != (numeric.shape[0], 8, 42):
            raise RuntimeError(
                f"Native semantic champion ID shape is invalid: {champion_ids.shape}"
            )
        trait_ids = np.asarray(projected.get("trait_ids"))
        if (
            trait_ids.dtype != np.int64
            or trait_ids.shape != (numeric.shape[0], 8, 42, 10)
            or not trait_ids.flags.c_contiguous
            or trait_ids.flags.writeable
        ):
            raise RuntimeError(
                "Native semantic trait IDs must be readonly contiguous int64 "
                "with shape [lobby, 8, 42, 10]."
            )
        item_blocks = projected.get("item_blocks")
        expected_item_shapes = {
            "components": (numeric.shape[0], 8, 10),
            "inventory": (numeric.shape[0], 8, 9, 17),
            "recipes": (numeric.shape[0], 8, 100, 17),
            "inventory_target_fit": (numeric.shape[0], 8, 9, 37),
            "recipe_target_fit": (numeric.shape[0], 8, 100, 37),
            "anvil_options": (numeric.shape[0], 8, 9, 11),
            "anvil_state": (numeric.shape[0], 8, 3),
        }
        if not isinstance(item_blocks, Mapping) or set(item_blocks) != set(expected_item_shapes):
            raise RuntimeError("Native semantic item block views are incomplete.")
        for name, expected_shape in expected_item_shapes.items():
            block = np.asarray(item_blocks[name])
            itemsize = np.dtype(np.float32).itemsize
            inner_shape = expected_shape[2:]
            expected_inner_strides = tuple(
                itemsize * int(np.prod(inner_shape[index + 1:], dtype=np.int64))
                for index in range(len(inner_shape))
            )
            if (
                block.dtype != np.float32
                or block.shape != expected_shape
                or block.flags.writeable
                or not np.shares_memory(block, numeric)
                or block.strides[0] != numeric.strides[0]
                or block.strides[1] != numeric.strides[1]
                or block.strides[2:] != expected_inner_strides
            ):
                raise RuntimeError(
                    f"Native semantic item block {name!r} must be a readonly "
                    "float32 strided view over the v8 carrier."
                )
            flattened = block.reshape(
                (numeric.shape[0] * 8,) + expected_shape[2:]
            )
            if not np.shares_memory(flattened, numeric):
                raise RuntimeError(
                    f"Native semantic item block {name!r} cannot be flattened "
                    "without copying the v8 carrier."
                )
            item_blocks[name] = flattened
        projected["item_blocks"] = item_blocks
        projected["numeric"] = numeric.reshape(-1, numeric.shape[-1])
        projected["champion_ids"] = champion_ids.reshape(
            -1, champion_ids.shape[-1]
        )
        projected["trait_ids"] = trait_ids.reshape(-1, 42, 10)
        return projected

    # Lightweight Python environments and isolated fixtures may still use the
    # reference implementation. The production native manager is fail-closed.
    return build_semantic_batch(metadata_rows, catalog_map, contract=contract)


def slice_batch_structure(value, selection):
    """Slice every tensor leaf in a nested semantic batch structure."""
    if isinstance(value, dict):
        return {
            key: slice_batch_structure(child, selection)
            for key, child in value.items()
        }
    if isinstance(value, torch.Tensor):
        return value[selection]
    raise TypeError(
        "Semantic batch structures may contain only dictionaries and tensors; "
        f"received {type(value).__name__}."
    )



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
        random.seed(self.config.seed)
        np.random.seed(self.config.seed)
        torch.manual_seed(self.config.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.config.seed)
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

        Path(self.config.log_dir).mkdir(parents=True, exist_ok=True)
        Path(self.config.checkpoint_path).expanduser().resolve().parent.mkdir(
            parents=True, exist_ok=True
        )
        Path(self.config.run_manifest_path).expanduser().resolve().parent.mkdir(
            parents=True, exist_ok=True
        )
        self.writer = SummaryWriter(self.config.log_dir)

        # ============================================================
        # 🏭 ENV FACTORY / ENGINE BACKEND
        # ============================================================

        print("🧩 Engine selecionada: C++ (única engine)")

        # PPO consumes the native strategic-owner projection directly.
        # Diagnostic JSONL sidecars are not enabled as a side effect of training.
        resolved_item_catalog = item_catalog_path or os.environ.get("TFT_ITEM_CATALOG_PATH")
        self._lobby_batch_manager = _NativeLobbyBatchManager(
            self.num_envs,
            self.config.seed,
            "",
            str(
                Path(resolved_item_catalog).expanduser().resolve()
                if resolved_item_catalog
                else Path(__file__).resolve().parent / "data" / "itens.json"
            ),
        )
        env_fns = [
            (
                lambda lobby_index=lobby_index:
                CppTFTLobbyWrapper(
                    seed=self.config.seed + lobby_index,
                    item_catalog_path=resolved_item_catalog,
                    native_engine=self._lobby_batch_manager.engine(lobby_index),
                )
            )
            for lobby_index in range(self.num_envs)
        ]

        # Reset/step are submitted as one native batch. Python retains
        # semantic projection, reward audit, and PPO ownership.
        self.vec_env = LobbyVectorEnv(
            env_fns,
            batch_manager=self._lobby_batch_manager,
        )
        dummy_obs = self.vec_env.reset(seed=self.config.seed)
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
            require_semantic_state=True,
        ).to(self.device)

        # ============================================================
        # 💾 CHECKPOINT / OPTIMIZER / SCHEDULER
        # ============================================================

        self.start_update = 1
        checkpoint_path = self.config.checkpoint_path
        checkpoint = None
        if os.path.exists(checkpoint_path):
            print(f"📂 Carregando checkpoint nativo: {checkpoint_path}")
            checkpoint = torch.load(checkpoint_path, map_location=self.device)
            if not isinstance(checkpoint, dict):
                raise RuntimeError("Checkpoint inválido: esperado um manifesto de execução nativo.")

            required_fields = (
                "policy",
                "optimizer",
                "scheduler",
                "scheduler_type",
                "update",
                "action_mask_contract",
                "critic_mask_input_contract",
                "semantic_state_contract",
                "reward_contract",
                "training_resume_contract",
                "checkpoint_contract",
                "training_run_manifest",
            )
            missing_fields = [name for name in required_fields if name not in checkpoint]
            if missing_fields:
                raise RuntimeError(
                    "Checkpoint não pertence à linhagem PPO nativa; campos ausentes: "
                    + ", ".join(missing_fields)
                )

            validate_action_mask_checkpoint_contract(checkpoint["action_mask_contract"])
            validate_critic_mask_input_checkpoint_contract(checkpoint["critic_mask_input_contract"])
            validate_reward_checkpoint_contract(checkpoint["reward_contract"])
            validate_semantic_state_checkpoint_contract(
                checkpoint["semantic_state_contract"], self.champion_id_map
            )
            validate_checkpoint_lineage_contract(
                checkpoint["checkpoint_contract"],
                self.policy.state_dict(),
                checkpoint["action_mask_contract"],
                checkpoint["critic_mask_input_contract"],
                checkpoint["semantic_state_contract"],
                checkpoint["reward_contract"],
            )
            if not validate_training_resume_contract(
                checkpoint["training_resume_contract"], self.config.to_dict()
            ):
                raise RuntimeError(
                    "Checkpoint pertence a outra configuração de treinamento. "
                    "Inicie uma nova execução em outro diretório."
                )
            if checkpoint["scheduler_type"] != "cosine_clamped":
                raise RuntimeError("Checkpoint usa um scheduler incompatível com a linhagem nativa.")
            if isinstance(checkpoint["update"], bool) or not isinstance(checkpoint["update"], int) or checkpoint["update"] < 0:
                raise RuntimeError("Checkpoint contém índice de update inválido.")

            self.policy.load_state_dict(checkpoint["policy"], strict=True)
            print("✅ Pesos nativos carregados com contratos semânticos exatos.")
        else:
            print("⚠️ Nenhum checkpoint nativo encontrado; iniciando do zero.")

        self.optimizer = optim.Adam(
            self.policy.parameters(),
            lr=self.config.learning_rate,
            eps=self.config.adam_eps,
            betas=(self.config.adam_beta1, self.config.adam_beta2),
            weight_decay=self.config.weight_decay,
        )
        if checkpoint is not None:
            self.optimizer.load_state_dict(checkpoint["optimizer"])
            print("✅ Estado completo do Adam restaurado.")

        self.scheduler = optim.lr_scheduler.LambdaLR(
            self.optimizer,
            lr_lambda=lambda step: cosine_lr_factor(
                step,
                self.config.learning_rate,
                self.config.min_learning_rate,
                self.config.lr_schedule_updates,
            ),
        )
        if checkpoint is not None:
            self.scheduler.load_state_dict(checkpoint["scheduler"])
            self.start_update = int(checkpoint["update"]) + 1
            print(f"▶️ Retomando execução nativa no update {self.start_update}")

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
        self.training_run_manifest = build_training_run_manifest(
            config=self.config,
            policy=self.policy,
            semantic_state_contract=self.semantic_state_contract,
            engine=self.vec_env.envs[0]._engine,
        )
        manifest_path = Path(self.config.run_manifest_path)
        saved_run_manifest = None
        if checkpoint is not None:
            saved_run_manifest = checkpoint.get("training_run_manifest")
            if (
                not isinstance(saved_run_manifest, dict)
                or saved_run_manifest.get("identity_sha256")
                != self.training_run_manifest.get("identity_sha256")
            ):
                raise RuntimeError(
                    "Checkpoint sem manifesto de execução nativo compatível. "
                    "Checkpoints históricos não podem ser retomados nesta linhagem."
                )
            self.training_run_manifest = saved_run_manifest
        if manifest_path.exists():
            import json as _json
            with manifest_path.open("r", encoding="utf-8") as source:
                existing_manifest = _json.load(source)
            if (
                existing_manifest.get("identity_sha256") != self.training_run_manifest.get("identity_sha256")
                or (
                    saved_run_manifest is not None
                    and existing_manifest.get("manifest_sha256") != saved_run_manifest.get("manifest_sha256")
                )
            ):
                raise RuntimeError(
                    "O diretório de execução já contém um manifesto divergente. "
                    "Use um diretório de saída novo; não sobrescreva artefatos de treino."
                )
            self.training_run_manifest = existing_manifest
        else:
            write_training_run_manifest(manifest_path, self.training_run_manifest)
        self.writer.add_text(
            "training/manifest",
            json.dumps(self.training_run_manifest, indent=2, ensure_ascii=False),
            self.start_update,
        )
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
    def _expand_lobby_snapshot_metadata(
        lobby_snapshots, players_per_lobby, label, native_state_cache=None,
        include_native_player_state=True,
    ):
        """Expand lobby identity while reusing immutable state for an exact native revision."""
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
                if not isinstance(native_snapshot, Mapping):
                    raise RuntimeError(f"Snapshot estruturado inválido para lobby {lobby_idx}.")
                for field in ("engine_instance_id", "episode_id"):
                    if native_snapshot.get(field) != snapshot.get(field):
                        raise RuntimeError(f"Snapshot estruturado diverge em {field} na lobby {lobby_idx}.")
                if native_snapshot.get("snapshot_sequence") != snapshot.get("decision_sequence"):
                    raise RuntimeError(f"Snapshot estruturado diverge na sequência da lobby {lobby_idx}.")
                if native_snapshot.get("round") != snapshot.get("round"):
                    raise RuntimeError(f"Snapshot estruturado diverge no round da lobby {lobby_idx}.")
                if native_snapshot.get("player_decision_sequences") != player_sequences:
                    raise RuntimeError(f"Snapshot estruturado diverge nas sequências individuais da lobby {lobby_idx}.")
                native_contract = (
                    native_snapshot.get("contract_id"),
                    native_snapshot.get("contract_version"),
                    native_snapshot.get("producer"),
                    native_snapshot.get("source_namespace"),
                )
                if include_native_player_state:
                    native_players = native_snapshot.get("players")
                    if not isinstance(native_players, Sequence) or len(native_players) != players_per_lobby:
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
                if native_snapshot is not None:
                    metadata["native_state_contract_id"] = native_contract[0]
                    metadata["native_state_contract_version"] = native_contract[1]
                    metadata["native_state_producer"] = native_contract[2]
                    metadata["native_state_source_namespace"] = native_contract[3]
                    metadata["temporal_contract_id"] = native_snapshot.get("temporal_contract_id")
                    metadata["temporal_contract_version"] = native_snapshot.get("temporal_contract_version")
                    metadata["temporal_history_complete"] = native_snapshot.get("temporal_history_complete")
                    metadata["temporal_retention_events"] = native_snapshot.get("temporal_retention_events")
                if native_players is not None:
                    native_player = native_players[player_idx]
                    if not isinstance(native_player, Mapping) or native_player.get("player_id") != player_idx:
                        raise RuntimeError(f"Registro estruturado desalinhado para lobby {lobby_idx}, jogador {player_idx}.")
                    # A native snapshot identity names one immutable revision.
                    # Result and next-observation envelopes may expose that same
                    # revision through separate Python mappings; share the frozen
                    # player subtree instead of materializing it twice.
                    cache_key = (
                        lobby_idx,
                        snapshot.get("engine_instance_id"),
                        snapshot.get("episode_id"),
                        snapshot.get("decision_sequence"),
                        snapshot.get("round"),
                        player_sequence,
                        player_idx,
                    )
                    cached_state = (
                        native_state_cache.get(cache_key)
                        if native_state_cache is not None
                        else None
                    )
                    if cached_state is not None:
                        cached_contract, frozen_player = cached_state
                        if cached_contract != native_contract:
                            raise RuntimeError(
                                f"Contrato nativo diverge para a mesma identidade de snapshot "
                                f"na lobby {lobby_idx}, jogador {player_idx}."
                            )
                    else:
                        frozen_player = (
                            native_player
                            if isinstance(native_player, FrozenDict)
                            else freeze_snapshot(native_player)
                        )
                        if native_state_cache is not None:
                            native_state_cache[cache_key] = (native_contract, frozen_player)
                    metadata["native_player_state"] = frozen_player
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
                metadata["identity"] = freeze_snapshot(envelope)
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
            action_events = info.get("action_outcome_events")
            if not isinstance(action_events, list) or len(action_events) != players_per_lobby:
                raise RuntimeError(
                    f"Lobby {lobby_idx} não forneceu {players_per_lobby} ActionOutcomeEvent nativos."
                )
            temporal_events = info.get("temporal_events")
            if not isinstance(temporal_events, list):
                raise RuntimeError(
                    f"Lobby {lobby_idx} não forneceu o fluxo temporal nativo do StepResult."
                )
            start = lobby_idx * players_per_lobby
            for player_id, (trace, action_event) in enumerate(zip(traces, action_events)):
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
                if not isinstance(action_event, dict) or not {
                    "contract_id", "contract_version", "event_id", "engine_instance_id",
                    "episode_id", "player_id", "outcome_player_decision_sequence",
                    "mask_permitted", "preflight_accepted", "handler_applied", "decision_advanced", "execution_status", "affected_unit_uuids", "status_reason",
                }.issubset(action_event):
                    raise RuntimeError(
                        f"ActionOutcomeEvent inválido para lobby {lobby_idx}, jogador {player_id}."
                    )
                if (
                    action_event["contract_id"] != "tft.engine.action-outcome-event"
                    or int(action_event["contract_version"]) != 1
                    or action_event["engine_instance_id"] != row.get("engine_instance_id")
                    or int(action_event["episode_id"]) != int(row.get("episode_id", -1))
                    or int(action_event["player_id"]) != player_id
                    or int(action_event["outcome_player_decision_sequence"]) != int(row.get("player_decision_sequence", -1))
                    or action_event["preflight_accepted"] is not True
                    or action_event["decision_advanced"] is not True
                    or not isinstance(action_event["execution_status"], str)
                    or not action_event["execution_status"].strip()
                ):
                    raise RuntimeError(
                        f"ActionOutcomeEvent desalinhado para lobby {lobby_idx}, jogador {player_id}."
                    )
                row["action_trace"] = dict(trace)
                row["action_outcome_event"] = dict(action_event)
                # Each PPO row owns only its player's temporal facts; the single
                # lobby-scoped event is assigned to player 0 to avoid 8x duplication.
                row["temporal_events"] = [
                    dict(event) for event in temporal_events
                    if isinstance(event, Mapping)
                    and (
                        event.get("player_id") == player_id
                        or (event.get("scope") == "lobby" and player_id == 0)
                    )
                ]

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

        A Engine é a autoridade das máscaras, inclusive para jogadores
        eliminados (PASS-only). O Trainer apenas valida e converte buffers.
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

        # A native packed lobby matrix bypasses the per-player dictionary
        # reconstruction. Legacy mapping fixtures keep the validation path below.
        packed_inputs = [isinstance(value, np.ndarray) for value in gym_masks]
        if any(packed_inputs) and not all(packed_inputs):
            raise TypeError("Não misture buffers compactos e mappings de action masks.")
        if all(packed_inputs):
            packed_rows = []
            expected_lobby_shape = (
                self.PLAYERS_PER_LOBBY,
                CppTFTLobbyWrapper._PACKED_ACTION_MASK_WIDTH,
            )
            for lobby_idx, lobby_buffer in enumerate(gym_masks):
                if (
                    lobby_buffer.dtype != np.bool_
                    or lobby_buffer.shape != expected_lobby_shape
                ):
                    raise ValueError(
                        f"Buffer compacto inválido na lobby {lobby_idx}: "
                        f"dtype={lobby_buffer.dtype}, shape={lobby_buffer.shape}, "
                        f"esperado bool{expected_lobby_shape}."
                    )
                packed_rows.append(lobby_buffer)
            packed = np.concatenate(packed_rows, axis=0)
            # Transfer the packed contract once. Each policy head receives a
            # strided tensor view over this one storage instead of a new copy.
            packed_tensor = torch.as_tensor(
                packed, dtype=torch.bool, device=self.device
            )
            flat_masks = {}
            offset = 0
            for key, shape in self.MASK_SHAPES.items():
                width = int(np.prod(shape))
                flat_masks[key] = packed_tensor[:, offset:offset + width].view(
                    self.num_envs * self.PLAYERS_PER_LOBBY, *shape
                )
                offset += width
            if offset != CppTFTLobbyWrapper._PACKED_ACTION_MASK_WIDTH:
                raise RuntimeError("Layout compacto de action masks diverge do contrato Python.")
        else:
            # Legacy mappings are retained for fixtures and external adapters.
            for lobby_idx in range(self.num_envs):
                lobby_masks = gym_masks[lobby_idx]
                if len(lobby_masks) != self.PLAYERS_PER_LOBBY:
                    raise ValueError(
                        f"Lobby {lobby_idx} possui {len(lobby_masks)} jogadores nas máscaras."
                    )

            for key, shape in self.MASK_SHAPES.items():
                values = []
                for lobby_idx in range(self.num_envs):
                    lobby_masks = gym_masks[lobby_idx]
                    for player_idx in range(self.PLAYERS_PER_LOBBY):
                        raw_mask = np.asarray(lobby_masks[player_idx][key])
                        if raw_mask.shape != shape:
                            raise ValueError(
                                f"Máscara '{key}' inválida para lobby={lobby_idx}, "
                                f"player={player_idx}: shape recebido={raw_mask.shape}, "
                                f"esperado={shape}"
                            )
                        if not (
                            np.issubdtype(raw_mask.dtype, np.bool_)
                            or np.issubdtype(raw_mask.dtype, np.number)
                        ):
                            raise TypeError(
                                f"Máscara '{key}' possui tipo inválido: {raw_mask.dtype}"
                            )
                        if not np.issubdtype(raw_mask.dtype, np.bool_):
                            if not np.all(np.isfinite(raw_mask)):
                                raise ValueError(f"Máscara '{key}' contém NaN ou infinito.")
                            if not np.all((raw_mask == 0) | (raw_mask == 1)):
                                raise ValueError(f"Máscara '{key}' deve conter somente 0 e 1.")
                        values.append(raw_mask.astype(np.bool_, copy=False))
                flat_masks[key] = torch.as_tensor(
                    np.asarray(values, dtype=np.bool_),
                    dtype=torch.bool,
                    device=self.device,
                )

        # The native Engine publishes PASS-only masks for eliminated players.
        # Python never synthesizes legality or consults a second liveness channel.
        type_mask = flat_masks["type_mask"]
        invalid_agents = ~type_mask.any(dim=1)
        if bool(invalid_agents.any()):
            indices = torch.nonzero(invalid_agents, as_tuple=False).flatten().tolist()
            raise RuntimeError(
                "A Engine publicou type_mask vazia para jogador(es) "
                f"{indices}; o contrato nativo deve publicar PASS para eliminados."
            )

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
        if total_updates != self.config.total_updates:
            raise ValueError("total_updates deve corresponder à configuração registrada no manifesto.")
        if rollout_steps != self.config.rollout_steps:
            raise ValueError("rollout_steps deve corresponder à configuração registrada no manifesto.")
        if rollout_steps <= 0:
            raise ValueError("rollout_steps deve ser > 0.")
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
            self.MASK_SHAPES,
            require_semantic_state=True,
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

            semantic_cache = None
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
                    include_native_player_state=not self.vec_env.semantic_projection_supported(),
                )
                for metadata, observation_hash in zip(
                    flat_snapshot_metadata,
                    self._hash_observation_rows(obs),
                ):
                    metadata["observation_snapshot_hash"] = observation_hash
                    metadata["observation_snapshot_hash_algorithm"] = "tft-ppo-observation-row-v1"

                # The previous transition's next snapshot is the current decision
                # snapshot when its immutable native revision identity still matches.
                can_reuse_semantic = (
                    semantic_cache is not None
                    and semantic_batch_matches_snapshot_rows(
                        semantic_cache["batch"],
                        flat_snapshot_metadata,
                        self.semantic_state_contract,
                    )
                )
                if can_reuse_semantic:
                    semantic_batch = semantic_cache["batch"]
                    semantic_state = semantic_cache["state"]
                else:
                    semantic_batch = project_semantic_batch(
                        self.vec_env, flat_snapshot_metadata, self.champion_id_map,
                        self.semantic_state_contract, lobby_snapshots=lobby_snapshots,
                    )
                    semantic_numeric = torch.as_tensor(
                        semantic_batch["numeric"], dtype=torch.float32, device=self.device
                    )
                    native_trait_ids = torch.as_tensor(
                        semantic_batch["trait_ids"], dtype=torch.long, device=self.device
                    )
                    semantic_items = semantic_item_state_tensors(
                        semantic_numeric, trait_ids=native_trait_ids
                    )
                    semantic_state = {
                        "numeric": semantic_numeric,
                        "items": semantic_items,
                        "champion_ids": torch.as_tensor(
                            semantic_batch["champion_ids"], dtype=torch.long, device=self.device
                        ),
                        "entity_identity": semantic_batch["entity_identity"],
                        "identities": semantic_batch["identities"],
                        "hashes": semantic_batch["hashes"],
                        "contract_id": semantic_batch["contract_id"],
                        "contract_hash": semantic_batch["contract_hash"],
                    }
                for metadata, semantic_hash, semantic_identity, entity_identity in zip(
                    flat_snapshot_metadata, semantic_batch["hashes"], semantic_batch["identities"],
                    semantic_batch["entity_identity"],
                ):
                    metadata["semantic_entity_identity"] = entity_identity
                    metadata["semantic_identity"] = semantic_identity
                    metadata["semantic_projection_hash"] = semantic_hash
                    metadata["semantic_projection_contract_id"] = (
                        self.semantic_state_contract["contract"]["contract_id"]
                    )
                    metadata["semantic_projection_contract_hash"] = (
                        self.semantic_state_contract["sha256"]
                    )
                validate_semantic_batch_alignment(
                    semantic_batch, flat_snapshot_metadata, self.semantic_state_contract,
                    self.champion_id_map, reproject=False, verify_catalog=False,
                )
                semantic_entities = np.asarray(
                    semantic_batch["numeric"], dtype=np.float32
                )[:, SEMANTIC_GLOBAL_FEATURES:SEMANTIC_ITEM_OFFSET].reshape(
                    -1, SEMANTIC_ENTITY_SLOTS, SEMANTIC_ENTITY_FEATURES
                )
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
                        "get_packed_action_masks_for_training"
                    )
                )

                masks = self._flatten_masks(gym_masks)

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
                # Scope interning to this transition only: a native revision
                # can be shared between StepResult and next-observation metadata,
                # but never across different transitions or episodes.
                transition_native_state_cache = {}
                flat_result_snapshot_metadata = self._expand_lobby_snapshot_metadata(
                    [info.get("step_result_snapshot") for info in infos],
                    self.PLAYERS_PER_LOBBY,
                    "snapshot de resultado da transição",
                    native_state_cache=transition_native_state_cache,
                    include_native_player_state=False,
                )
                # Keep native action provenance beside the exact StepResult identity.
                self._attach_native_action_traces(
                    flat_result_snapshot_metadata,
                    infos,
                    self.PLAYERS_PER_LOBBY,
                )

                next_lobby_snapshots = [info.get("next_snapshot") for info in infos]
                flat_next_snapshot_metadata = self._expand_lobby_snapshot_metadata(
                    next_lobby_snapshots,
                    self.PLAYERS_PER_LOBBY,
                    "snapshot da próxima observação",
                    native_state_cache=transition_native_state_cache,
                    include_native_player_state=not self.vec_env.semantic_projection_supported(),
                )
                next_semantic_batch = project_semantic_batch(
                    self.vec_env, flat_next_snapshot_metadata, self.champion_id_map,
                    self.semantic_state_contract, lobby_snapshots=next_lobby_snapshots,
                )
                next_semantic_numeric = torch.as_tensor(
                    next_semantic_batch["numeric"], dtype=torch.float32, device=self.device
                )
                next_native_trait_ids = torch.as_tensor(
                    next_semantic_batch["trait_ids"], dtype=torch.long, device=self.device
                )
                next_semantic_state = {
                    "numeric": next_semantic_numeric,
                    "items": semantic_item_state_tensors(
                        next_semantic_numeric, trait_ids=next_native_trait_ids
                    ),
                    "champion_ids": torch.as_tensor(
                        next_semantic_batch["champion_ids"], dtype=torch.long, device=self.device
                    ),
                    "entity_identity": next_semantic_batch["entity_identity"],
                    "identities": next_semantic_batch["identities"],
                    "hashes": next_semantic_batch["hashes"],
                    "contract_id": next_semantic_batch["contract_id"],
                    "contract_hash": next_semantic_batch["contract_hash"],
                }
                for metadata, semantic_hash, semantic_identity, entity_identity in zip(
                    flat_next_snapshot_metadata, next_semantic_batch["hashes"], next_semantic_batch["identities"],
                    next_semantic_batch["entity_identity"],
                ):
                    metadata["semantic_entity_identity"] = entity_identity
                    metadata["semantic_identity"] = semantic_identity
                    metadata["semantic_projection_hash"] = semantic_hash
                    metadata["semantic_projection_contract_id"] = (
                        self.semantic_state_contract["contract"]["contract_id"]
                    )
                    metadata["semantic_projection_contract_hash"] = (
                        self.semantic_state_contract["sha256"]
                    )
                validate_semantic_batch_alignment(
                    next_semantic_batch, flat_next_snapshot_metadata, self.semantic_state_contract,
                    self.champion_id_map, reproject=False, verify_catalog=False,
                )
                semantic_cache = {
                    "identities": next_semantic_batch["identities"],
                    "batch": next_semantic_batch,
                    "state": next_semantic_state,
                }

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
                    trajectory_valid=transition_valid,
                    optimization_valid=transition_valid,
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
                    "get_packed_action_masks_for_training"
                )
            )

            next_masks = self._flatten_masks(gym_masks)

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
                next_state_valid=torch.ones(
                    self.num_agents, dtype=torch.bool, device=self.device
                ),
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
                    rollout.optimization_valid[:rollout.ptr].reshape(-1),
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
                    sample_semantic_numeric = rollout.semantic_numeric[:rollout.ptr].reshape(
                        -1, rollout.semantic_numeric_dim
                    )[valid_indices]
                    sample_semantic_state = {
                        "numeric": sample_semantic_numeric,
                        "items": semantic_item_state_tensors(
                            sample_semantic_numeric,
                            trait_ids=rollout.semantic_trait_ids[:rollout.ptr].reshape(
                                -1, rollout.semantic_entity_slots, SEMANTIC_TRAIT_SLOTS
                            )[valid_indices],
                        ),
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
                    sample_semantic_state = slice_batch_structure(
                        sample_semantic_state,
                        slice(0, sample_size),
                    )

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
            valid_mask = rollout.optimization_valid[:rollout.ptr]

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
                        "training_resume_contract": build_training_resume_contract(self.config.to_dict()),
                        "training_run_manifest": self.training_run_manifest,
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
                "training_resume_contract": build_training_resume_contract(self.config.to_dict()),
                "training_run_manifest": self.training_run_manifest,
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
    raise SystemExit(
        "O módulo trainer.py é uma biblioteca. Use "
        "'python train_native.py --output-dir <diretorio> --seed <seed>' "
        "para iniciar uma execução nativa reproduzível."
    )
