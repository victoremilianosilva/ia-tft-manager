
"""Integra o motor nativo de decisões ao ambiente Python.

O backend Python continua sendo o padrão.
O runtime C++ não registra histórico durante a geração de máscaras.
O histórico nativo é atualizado nos mesmos pontos em que o ambiente
atualiza o AntiLoopManager Python.
"""

from __future__ import annotations

import numpy as np

from ai.DecisionEngineProvider import get_decision_engine_backend
from ai.DecisionStateAdapter import build_player_state


class DecisionEngineRuntime:
    """Coordena máscaras e histórico do backend selecionado."""

    def __init__(self, python_anti_loop_manager):
        self.backend = get_decision_engine_backend()
        self.is_cpp = self.backend.is_cpp

        self.native_module = None
        self.mask_engine = None
        self.anti_loop_engine = None

        if not self.is_cpp:
            return

        self.native_module = self.backend.require_native_module()

        config = self.native_module.AntiLoopConfig()
        config.history_size = int(
            getattr(python_anti_loop_manager, "history_size", 20)
        )
        config.blocked_move_size = int(
            getattr(python_anti_loop_manager, "blocked_move_size", 10)
        )
        config.loop_threshold = int(
            getattr(python_anti_loop_manager, "loop_threshold", 2)
        )

        self.mask_engine = self.native_module.ActionMaskEngine()
        self.anti_loop_engine = self.native_module.AntiLoopEngine(config)

    def reset(self):
        """Limpa o histórico nativo, preservando as métricas do motor."""
        if self.is_cpp:
            self.anti_loop_engine.reset()

    def _native_identity(self, unit):
        """Converte a identidade Python para a identidade nativa."""
        if not isinstance(unit, dict):
            return None

        identity = self.native_module.UnitIdentity()

        raw_uuid = unit.get("uuid")
        raw_id = unit.get("id")

        if raw_uuid is not None:
            identity.uuid = str(raw_uuid)
        elif isinstance(raw_id, int) and not isinstance(raw_id, bool):
            identity.id = raw_id
        else:
            return None

        star = unit.get("star", 1)
        if isinstance(star, bool):
            star = 1

        identity.star = max(1, min(255, int(star)))

        if not identity.has_identity():
            return None

        return identity

    def register_move(self, move_type, source, target, unit=None):
        """Registra no C++ um movimento já executado com sucesso."""
        if not self.is_cpp:
            return

        self.anti_loop_engine.register_move(
            str(move_type),
            int(source),
            int(target),
            self._native_identity(unit),
        )

    def register_state(self, env, is_alive=True):
        """Sincroniza no C++ o posicionamento após a atualização Python."""
        if not self.is_cpp:
            return

        state = build_player_state(
            env,
            is_alive=is_alive,
            native_module=self.native_module,
        )
        signature = self.anti_loop_engine.make_board_signature(state)
        self.anti_loop_engine.register_state(signature)

    def get_action_masks(
        self,
        env,
        is_alive=True,
        include_conditioned_board_target=True,
        include_board_target=True,
        board_source_mask=None,
        board_move_available=None,
        bench_move_available=None,
    ):
        """Retorna as seis máscaras no mesmo formato do ActionMaskManager."""
        if not self.is_cpp:
            raise RuntimeError(
                "get_action_masks() do runtime exige o backend C++."
            )

        state = build_player_state(
            env,
            is_alive=is_alive,
            native_module=self.native_module,
        )

        batch = self.mask_engine.generate_masks(
            state,
            self.anti_loop_engine,
        )

        type_mask = np.asarray(batch.type_mask, dtype=np.float32)
        shop_mask = np.asarray(batch.shop_mask, dtype=np.float32)
        bench_mask = np.asarray(batch.bench_source_mask, dtype=np.float32)

        board_target_mask = np.asarray(
            batch.board_target_mask,
            dtype=np.float32,
        )

        native_board_source_mask = np.asarray(
            batch.board_source_mask,
            dtype=np.float32,
        )

        # A máscara condicionada é a união dos destinos das origens
        # que realmente possuem movimentos válidos. Não somamos os
        # fallbacks técnicos das linhas sem movimentos.
        conditioned_target_mask = np.zeros(28, dtype=np.float32)

        if batch.board_move_available:
            matrix = batch.board_move_target_masks

            for source in range(28):
                if native_board_source_mask[source] <= 0:
                    continue

                conditioned_target_mask = np.maximum(
                    conditioned_target_mask,
                    np.asarray(matrix[source], dtype=np.float32),
                )

        if not conditioned_target_mask.any():
            conditioned_target_mask[0] = 1.0

        if not include_board_target:
            board_target_mask = np.zeros(28, dtype=np.float32)
            board_target_mask[0] = 1.0

        if not include_conditioned_board_target:
            conditioned_target_mask = np.zeros(28, dtype=np.float32)
            conditioned_target_mask[0] = 1.0

        if board_source_mask is not None:
            native_board_source_mask = np.asarray(
                board_source_mask,
                dtype=np.float32,
            )

        # Os overrides precisam manter o contrato do Python:
        # eles alteram a disponibilidade informada ao tipo de ação.
        if not is_alive:
            type_mask[:] = 0.0
            type_mask[6] = 1.0
        else:
            if board_move_available is not None:
                type_mask[4] = float(bool(board_move_available))

            if bench_move_available is not None:
                type_mask[3] = float(bool(bench_move_available))

        return [
            type_mask,
            shop_mask,
            bench_mask,
            board_target_mask,
            native_board_source_mask,
            conditioned_target_mask,
        ]
