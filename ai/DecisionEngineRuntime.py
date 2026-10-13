
"""Integra o motor nativo de decisões ao ambiente Python.

O backend Python continua sendo o padrão.
O runtime C++ não registra histórico durante a geração de máscaras.
O histórico nativo é atualizado nos mesmos pontos em que o ambiente
atualiza o AntiLoopManager Python.
"""

from __future__ import annotations

import numpy as np

from ai.DecisionEngineProvider import get_decision_engine_backend
from ai.DecisionStateAdapter import (
    build_player_state,
    build_position_signature,
)

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
            identity.id = int(raw_id)
        elif isinstance(raw_id, str):
            identity.textual_id = raw_id

        star = unit.get("star", 1)
        if isinstance(star, bool):
            star = 1

        identity.star = max(1, min(255, int(star)))

        # Retornamos a identidade mesmo quando id e UUID estão ausentes.
        # Assim, o campo star continua disponível e o comportamento
        # se aproxima da identidade Python ("unit", None, star).
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
        """Sincroniza somente a assinatura de posicionamento no C++."""
        if not self.is_cpp:
            return

        signature = build_position_signature(
            env,
            native_module=self.native_module,
        )

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
        """Retorna as seis máscaras no mesmo formato do ActionMaskManager.

        A máscara condicionada dos destinos é calculada no C++.
        Os overrides continuam sendo aplicados em Python para preservar
        o contrato da interface utilizada pelo PPO.
        """
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
            include_board_target,
        )

        # ---------------------------------------------------------
        # 1. Máscaras básicas vindas diretamente do C++
        # ---------------------------------------------------------
        type_mask = np.asarray(
            batch.type_mask,
            dtype=np.float32,
        ).copy()

        shop_mask = np.asarray(
            batch.shop_mask,
            dtype=np.float32,
        ).copy()

        bench_mask = np.asarray(
            batch.bench_source_mask,
            dtype=np.float32,
        ).copy()

        board_target_mask = np.asarray(
            batch.board_target_mask,
            dtype=np.float32,
        ).copy()

        native_board_source_mask = np.asarray(
            batch.board_source_mask,
            dtype=np.float32,
        ).copy()

        # ---------------------------------------------------------
        # 2. Destinos condicionados calculados pelo C++
        # ---------------------------------------------------------
        conditioned_target_mask = np.asarray(
            batch.conditioned_board_target_mask,
            dtype=np.float32,
        ).copy()

        # ---------------------------------------------------------
        # 3. Aplicação dos overrides de compatibilidade
        # ---------------------------------------------------------
        if not include_board_target:
            board_target_mask[:] = 0.0
            board_target_mask[0] = 1.0

        if not include_conditioned_board_target:
            conditioned_target_mask[:] = 0.0
            conditioned_target_mask[0] = 1.0

        if board_source_mask is not None:
            native_board_source_mask = np.asarray(
                board_source_mask,
                dtype=np.float32,
            ).copy()

        # ---------------------------------------------------------
        # 4. Disponibilidade dos tipos de ação
        # ---------------------------------------------------------
        if not is_alive:
            type_mask[:] = 0.0
            type_mask[6] = 1.0  # PASS
        else:
            if board_move_available is not None:
                type_mask[4] = float(bool(board_move_available))

            if bench_move_available is not None:
                type_mask[3] = float(bool(bench_move_available))

        # Mantém o contrato: seis máscaras, na ordem esperada pelo PPO.
        return [
            type_mask,
            shop_mask,
            bench_mask,
            board_target_mask,
            native_board_source_mask,
            conditioned_target_mask,
        ]


    def get_action_mask_batch(
        self,
        env,
        is_alive=True,
        include_board_target=True,
    ):
        """Gera o lote completo de máscaras diretamente no C++."""
        if not self.is_cpp:
            raise RuntimeError(
                "get_action_mask_batch() exige o backend C++."
            )

        state = build_player_state(
            env,
            is_alive=is_alive,
            native_module=self.native_module,
        )

        return self.mask_engine.generate_masks(
            state,
            self.anti_loop_engine,
            include_board_target,
        )