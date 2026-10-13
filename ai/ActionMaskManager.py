# 🤖 ai/ActionMaskManager.py
#
# Responsável por:
# - Gerar máscaras das ações válidas
# - Impedir ações impossíveis
# - Impedir movimentos inúteis/loops
# - Garantir que PASS continue disponível
#
# Action dimensions:
# [7, 5, 9, 28, 28, 28]
#
# 0 = action type
# 1 = shop slot
# 2 = bench slot
# 3 = board target
# 4 = board source
# 5 = conditioned board target

from enum import IntEnum
import logging
import numpy as np
logger = logging.getLogger(__name__)

class ActionType(IntEnum):
    BUY = 0
    REROLL = 1
    BUY_XP = 2
    MOVE_BENCH = 3
    MOVE_BOARD = 4
    SELL = 5
    PASS = 6


class ActionMaskManager:

    def __init__(
        self,
        board_manager,
        bench_manager,
        shop_manager,
        economy_manager,
        composition_manager,
        positioning_manager,
        anti_loop_manager,
        unit_manager,
        decision_engine_runtime=None,
        env=None,
    ):
        self.board_manager = board_manager
        self.bench_manager = bench_manager
        self.shop_manager = shop_manager
        self.economy_manager = economy_manager
        self.composition_manager = composition_manager
        self.positioning_manager = positioning_manager
        self.anti_loop_manager = anti_loop_manager
        self.unit_manager = unit_manager

        self.decision_engine_runtime = decision_engine_runtime
        self.env = env

        self.board_size = 28
        self.bench_size = 9
        self.shop_size = 5
        self._anti_loop_error_count = 0
    # ============================================================
    # 🔹 API PRINCIPAL
    # ============================================================
    def get_action_masks(
        self,
        is_alive=True,
        include_conditioned_board_target=True,
        include_board_target=True,
        board_source_mask=None,
        board_move_available=None,
        bench_move_available=None,
    ):

        runtime = self.decision_engine_runtime

        if runtime is not None and runtime.is_cpp:
            if self.env is None:
                raise RuntimeError(
                    "O backend C++ precisa da referência ao ambiente."
                )

            return runtime.get_action_masks(
                env=self.env,
                is_alive=is_alive,
                include_conditioned_board_target=(
                    include_conditioned_board_target
                ),
                include_board_target=include_board_target,
                board_source_mask=board_source_mask,
                board_move_available=board_move_available,
                bench_move_available=bench_move_available,
            )

        # 🛒 Calcula a loja uma vez.
        shop_mask, buy_available = (
            self._get_shop_mask_and_availability()
        )

        # 🪑 Calcula a máscara do banco e verifica SELL
        # na mesma passagem pela lista de unidades.
        bench_mask, sell_available = (
            self._get_bench_source_mask_and_sell_availability()
        )

        type_mask = self.get_type_mask(
            is_alive=is_alive,
            buy_available=buy_available,
            sell_available=sell_available,
            board_move_available=board_move_available,
            bench_move_available=bench_move_available,
        )

        if include_board_target:
            board_target_mask = self.get_board_target_mask()
        else:
            board_target_mask = np.zeros(
                self.board_size, dtype=np.float32
            )
            board_target_mask[0] = 1.0

        if board_source_mask is None:
            board_source_mask = self.get_board_source_mask()
        else:
            board_source_mask = np.asarray(
                board_source_mask, dtype=np.float32
            )

        if include_conditioned_board_target:
            conditioned_target_mask = (
                self.get_conditioned_board_target_mask()
            )
        else:
            conditioned_target_mask = np.zeros(
                self.board_size, dtype=np.float32
            )
            conditioned_target_mask[0] = 1.0

        return [
            type_mask,
            shop_mask,
            bench_mask,
            board_target_mask,
            board_source_mask,
            conditioned_target_mask,
        ]

    # ============================================================
    # 🔹 ACTION TYPE
    # ============================================================

    def get_type_mask(
        self,
        is_alive=True,
        buy_available=None,
        sell_available=None,  # 🪙 Resultado pré-calculado
        board_move_available=None,
        bench_move_available=None,
    ):
        """Máscara: BUY, REROLL, BUY_XP, MOVE_BENCH,
        MOVE_BOARD, SELL e PASS.
        """
        mask = np.zeros(7, dtype=np.float32)

        if not is_alive:
            mask[ActionType.PASS] = 1.0
            return mask

        # 🛒 Usa o resultado pré-calculado, se disponível.
        if buy_available is None:
            buy_available = self._has_valid_buy()

        if buy_available:
            mask[ActionType.BUY] = 1.0

        if self._has_valid_reroll():
            mask[ActionType.REROLL] = 1.0

        if self._has_valid_buy_xp():
            mask[ActionType.BUY_XP] = 1.0

        # ⚡ Usa o resultado pré-calculado quando disponível.
        if bench_move_available is None:
            bench_move_available = self._has_valid_bench_move()

        if bench_move_available:
            mask[ActionType.MOVE_BENCH] = 1.0

        if board_move_available is None:
            board_move_available = self._has_valid_board_move()

        if board_move_available:
            mask[ActionType.MOVE_BOARD] = 1.0

        # 🪙 Reutiliza a verificação do banco quando disponível.
        if sell_available is None:
            sell_available = self._has_valid_sell()

        if sell_available:
            mask[ActionType.SELL] = 1.0

        mask[ActionType.PASS] = 1.0
        return mask

    # ============================================================
    # 🛒 BUY
    # ============================================================
    def _get_shop_mask_and_availability(self):
        """
        🛒 Gera a máscara da loja e informa se existe compra real.
        O fallback técnico não conta como compra válida.
        """
        mask = np.zeros(self.shop_size, dtype=np.float32)

        shop = self._get_shop()

        # ⚡ Verifica espaço no banco apenas uma vez.
        has_bench_space = self.bench_manager.has_free_slot()
        buy_available = False

        if has_bench_space:
            for slot in range(min(len(shop), self.shop_size)):
                unit = shop[slot]

                if unit is None:
                    continue

                if not self.economy_manager.can_spend(
                    unit.get("cost", 1)
                ):
                    continue

                mask[slot] = 1.0
                buy_available = True

        # ⚠️ Fallback para manter a distribuição categórica válida.
        if not mask.any():
            mask[0] = 1.0

        return mask, buy_available

    def get_shop_mask(self):
        """Máscara dos cinco slots da loja."""
        mask, _ = self._get_shop_mask_and_availability()
        return mask

    def _has_valid_buy(self):
        """Informa se existe uma compra real disponível."""
        _, buy_available = self._get_shop_mask_and_availability()
        return buy_available
    
    # ============================================================
    # 🔄 REROLL
    # ============================================================
    def _has_valid_reroll(self):
        try:
            return self.economy_manager.can_spend(2)
        except Exception:
            return False

    # ============================================================
    # ⭐ BUY XP
    # ============================================================

    def _has_valid_buy_xp(self):
        try:
            return self.economy_manager.can_buy_xp()
        except Exception:
            return False

    # ============================================================
    # 🪑 BENCH
    # ============================================================
    def _get_bench_source_mask_and_sell_availability(self):
        """
        🪑 Gera a máscara do banco e verifica SELL
        em uma única passagem.

        O fallback técnico da máscara não habilita SELL.
        """
        mask = np.zeros(self.bench_size, dtype=np.float32)
        bench = self._get_bench()
        sell_available = False

        for slot, unit in enumerate(
            bench[:self.bench_size]
        ):
            if unit is None:
                continue

            mask[slot] = 1.0
            sell_available = True

        # ⚠️ Fallback técnico: não representa unidade real.
        if not mask.any():
            mask[0] = 1.0

        return mask, sell_available

    def get_bench_source_mask(self):
        """Máscara dos slots ocupados do banco."""
        mask, _ = (
            self._get_bench_source_mask_and_sell_availability()
        )
        return mask

    def _has_valid_sell(self):
        """Informa se existe alguma unidade real para vender."""
        _, sell_available = (
            self._get_bench_source_mask_and_sell_availability()
        )
        return sell_available
    # ============================================================
    # 🪑 -> BOARD
    # ============================================================

    def get_board_target_mask(self):
        """
        União dos destinos válidos para MOVE_BENCH.
        A política usará a máscara condicionada à origem
        selecionada para filtrar os destinos de verdade.
        """
        mask = np.zeros(self.board_size, dtype=np.float32)
        bench = self._get_bench()

        if self._has_free_board_slot():
            empty_positions = self.board_manager.get_empty_positions()

            for slot, unit in enumerate(bench[:self.bench_size]):
                if unit is None:
                    continue

                for target in empty_positions:
                    if self._is_valid_bench_board_move(slot, target):
                        mask[target] = 1.0

        # Evita uma distribuição vazia nas cabeças auxiliares.
        if not mask.any():
            mask[0] = 1.0

        return mask


    def get_bench_to_board_target_mask(self, bench_slot):
        """
        Destinos válidos para uma origem específica do banco.
        """
        mask = np.zeros(self.board_size, dtype=np.float32)
        bench = self._get_bench()

        if not (0 <= bench_slot < min(len(bench), self.bench_size)):
            mask[0] = 1.0
            return mask

        if bench[bench_slot] is None or not self._has_free_board_slot():
            mask[0] = 1.0
            return mask

        for target in self.board_manager.get_empty_positions():
            if self._is_valid_bench_board_move(bench_slot, target):
                mask[target] = 1.0

        if not mask.any():
            mask[0] = 1.0

        return mask
    

    def _has_valid_bench_move(self):
        """
        Existe alguma unidade no bench que possa entrar no board?
        """

        if not self._has_free_board_slot():
            return False

        bench = self._get_bench()

        # ⚡ Calcula as posições vazias uma única vez.
        empty_positions = self.board_manager.get_empty_positions()

        for slot, unit in enumerate(bench):
            if unit is None:
                continue

            for target in empty_positions:
                if self._is_valid_bench_board_move(
                    bench_slot=slot,
                    target=target,
                ):
                    return True

        return False


    def _is_valid_bench_board_move(self, bench_slot, target, bench=None):
        if bench is None:
            bench = self._get_bench()

        if bench_slot < 0 or bench_slot >= len(bench):
            return False

        unit = bench[bench_slot]

        if unit is None:
            return False

        if not self._is_valid_board_position(target):
            return False

        if self._should_block_anti_loop(
            move_type="bench_to_board",
            source=bench_slot,
            target=target,
            unit=unit,
        ):
            return False

        return True

    # ============================================================
    # 🔀 BOARD -> BOARD
    # ============================================================

    def get_board_source_mask(self):
        """
        Máscara das origens do tabuleiro que possuem
        pelo menos um destino real válido.
        """
        mask = np.zeros(self.board_size, dtype=np.float32)

        for source in range(self.board_size):
            # O fallback [0] não conta como destino real
            # quando a origem não possui movimento válido.
            board = self._get_board()
            if source >= len(board) or board[source] is None:
                continue

            if any(
                target != source and self._is_valid_board_move(source, target)
                for target in range(self.board_size)
            ):
                mask[source] = 1.0

        # Fallback técnico para a distribuição categórica.
        # A ação MOVE_BOARD precisa continuar desabilitada
        # se não existir nenhuma origem válida.
        if not mask.any():
            mask[0] = 1.0

        return mask

    def get_conditioned_board_target_mask(self):
        """
        Destinos para MOVE_BOARD.

        Aqui usamos o board source atual para decidir os destinos.
        Como a política é autoregressiva, essa máscara é refinada
        posteriormente pelo source selecionado.
        """

        mask = np.zeros(self.board_size, dtype=np.float32)

        board = self._get_board()

        occupied = [
            index
            for index, unit in enumerate(board)
            if unit is not None
        ]

        for source in occupied:

            for target in range(self.board_size):

                if source == target:
                    continue

                if self._is_valid_board_move(source, target):
                    mask[target] = 1.0

        if not mask.any():
            mask[0] = 1.0

        return mask

    def _is_valid_board_move(self, source, target, board=None):
        if board is None:
            board = self._get_board()

        if source < 0 or source >= len(board):
            return False

        if target < 0 or target >= len(board):
            return False

        if source == target:
            return False

        source_unit = board[source]

        if source_unit is None:
            return False

        target_unit = board[target]

        # ========================================================
        # 🔁 Swap
        # ========================================================

        if target_unit is not None:

            if self._should_block_anti_loop(
                move_type="board_swap",
                source=source,
                target=target,
                unit=source_unit,
            ):
                return False

            return True

        # ========================================================
        # 📦 Movimento para espaço vazio
        # ========================================================

        if self._should_block_anti_loop(
            move_type="board_move",
            source=source,
            target=target,
            unit=source_unit,
        ):
            return False

        return True

    def _has_valid_board_move(self):
        """
        Verifica se existe pelo menos um movimento BOARD -> BOARD
        que realmente faça sentido.

        Não basta existir uma troca.
        O AntiLoopManager precisa poder bloquear movimentos
        repetitivos.
        """

        board = self._get_board()

        occupied = [
            index
            for index, unit in enumerate(board)
            if unit is not None
        ]

        for source in occupied:

            for target in range(self.board_size):

                if source == target:
                    continue

                if self._is_valid_board_move(source, target):
                    return True

        return False

    # ============================================================
    # 🧠 MOVIMENTO CONDICIONADO
    # ============================================================

    def get_board_move_target_mask(self, source):
        """
        Retorna os destinos válidos para uma origem específica.

        Isso é importante porque a política possui heads
        autoregressivas:

            source -> target
        """

        mask = np.zeros(self.board_size, dtype=np.float32)

        if source < 0 or source >= self.board_size:
            mask[0] = 1.0
            return mask

        board = self._get_board()

        if board[source] is None:
            mask[0] = 1.0
            return mask

        for target in range(self.board_size):

            if target == source:
                continue

            if self._is_valid_board_move(source, target):
                mask[target] = 1.0

        if not mask.any():
            mask[0] = 1.0

        return mask

    def get_bench_move_source_mask(self):
        """
        Máscara exclusiva das unidades do banco que podem
        entrar no tabuleiro em pelo menos uma posição válida.

        Diferente de get_bench_source_mask(), esta máscara
        NÃO é usada para vender unidades.
        """
        mask = np.zeros(self.bench_size, dtype=np.float32)
        bench = self._get_bench()

        if self._has_free_board_slot():
            empty_positions = self.board_manager.get_empty_positions()

            for slot, unit in enumerate(bench[:self.bench_size]):
                if unit is None:
                    continue

                for target in empty_positions:
                    if self._is_valid_bench_board_move(slot, target):
                        mask[slot] = 1.0
                        break

        # Fallback técnico: não representa um movimento válido.
        # MOVE_BENCH precisa estar desabilitado se não houver
        # nenhuma origem real válida.
        if not mask.any():
            mask[0] = 1.0

        return mask

    # ============================================================
    # 🔍 HELPERS
    # ============================================================

    def _get_board(self):
        board = getattr(self.board_manager, "board", None)

        if board is None:
            return [None] * self.board_size

        return board

    def _get_bench(self):
        bench = getattr(self.bench_manager, "bench", None)

        if bench is None:
            return [None] * self.bench_size

        return bench

    def _get_shop(self):
        try:
            return self.shop_manager.get_shop()
        except Exception:
            shop = getattr(self.shop_manager, "shop", None)

            if shop is None:
                return [None] * self.shop_size

            return shop

    def _has_free_board_slot(self):
        try:
            return len(self.board_manager.get_empty_positions()) > 0
        except Exception:
            return any(unit is None for unit in self._get_board())

    def _is_valid_board_position(self, position):
        try:
            return self.board_manager.is_valid_position(position)
        except Exception:
            return 0 <= position < self.board_size

    def _should_block_anti_loop(
        self,
        move_type,
        source,
        target,
        unit,
    ):
        """
        Consulta o AntiLoopManager sem permitir que uma falha
        de diagnóstico invalide a construção da máscara.

        Em caso de exceção, permite o candidato nesta camada,
        preservando o comportamento atual, e registra a falha.
        As regras básicas de legalidade continuam sendo verificadas
        pelos métodos chamadores.
        """
        try:
            return bool(
                self.anti_loop_manager.should_block_move(
                    move_type=move_type,
                    source=source,
                    target=target,
                    unit=unit,
                )
            )
        except Exception:
            self._anti_loop_error_count = (
                getattr(self, "_anti_loop_error_count", 0) + 1
            )

            # Registra a primeira ocorrência com traceback.
            # Evita repetir o mesmo traceback para cada candidato.
            if self._anti_loop_error_count == 1:
                logger.exception(
                    "Falha ao consultar AntiLoopManager.should_block_move. "
                    "O candidato será permitido nesta camada. "
                    "Verifique a legalidade no ambiente. "
                    "Falhas registradas: %d",
                    self._anti_loop_error_count,
                )
            elif self._anti_loop_error_count % 100 == 0:
                logger.warning(
                    "AntiLoopManager continua falhando durante a "
                    "construção das máscaras. Total de falhas: %d",
                    self._anti_loop_error_count,
                )

            return False

    def get_board_move_masks(self):
        """
        ⚡ Calcula a matriz de destinos e a máscara de origens
        em uma única passagem pelos pares origem/destino.

        Retorna:
            source_mask: (28,)
            target_masks: (28, 28)
            has_valid_move: bool
        """
        board = self._get_board()

        source_mask = np.zeros(self.board_size, dtype=np.float32)
        target_masks = np.zeros(
            (self.board_size, self.board_size),
            dtype=np.float32,
        )

        has_valid_move = False

        for source in range(self.board_size):
            if source >= len(board) or board[source] is None:
                target_masks[source, 0] = 1.0
                continue

            for target in range(self.board_size):
                if source == target:
                    continue

                # ♻️ Cada par é validado uma vez nesta geração.
                if self._is_valid_board_move(
                    source, target, board=board
                ):
                    target_masks[source, target] = 1.0
                    source_mask[source] = 1.0
                    has_valid_move = True

            # 🎯 Fallback para a distribuição categórica.
            if not target_masks[source].any():
                target_masks[source, 0] = 1.0

        # ⚠️ Fallback não deve habilitar MOVE_BOARD.
        if not has_valid_move:
            source_mask[0] = 1.0

        return source_mask, target_masks, has_valid_move


    def get_bench_move_masks(self):
        """
        ⚡ Calcula as origens do bench e seus destinos válidos
        em uma única passagem.

        Retorna:
            source_mask: (9,)
            target_masks: (9, 28)
            has_valid_move: bool
        """
        bench = self._get_bench()

        source_mask = np.zeros(self.bench_size, dtype=np.float32)
        target_masks = np.zeros(
            (self.bench_size, self.board_size),
            dtype=np.float32,
        )

        # ⚡ Obtém as posições vazias uma única vez.
        # ⚡ Uma consulta basta: sem posições vazias,
        # não existe movimento possível do banco para o tabuleiro.
        empty_positions = self.board_manager.get_empty_positions()

        has_valid_move = False

        for slot, unit in enumerate(bench[:self.bench_size]):
            if unit is None:
                target_masks[slot, 0] = 1.0
                continue

            for target in empty_positions:
                if self._is_valid_bench_board_move(
                    slot, target, bench=bench
                ):
                    target_masks[slot, target] = 1.0
                    source_mask[slot] = 1.0
                    has_valid_move = True

            # 🎯 Fallback técnico; não indica movimento real.
            if not target_masks[slot].any():
                target_masks[slot, 0] = 1.0

        if not has_valid_move:
            source_mask[0] = 1.0

        return source_mask, target_masks, has_valid_move
        
    # ============================================================
    # 🧪 DEBUG
    # ============================================================

    def debug_print(self, is_alive=True):
        masks = self.get_action_masks(is_alive=is_alive)

        print("\n========== ACTION MASK ==========")

        print(
            "TYPE:",
            [
                ActionType(i).name
                if value > 0
                else "X"
                for i, value in enumerate(masks[0])
            ]
        )

        print("SHOP :", np.where(masks[1] > 0)[0].tolist())
        print("BENCH:", np.where(masks[2] > 0)[0].tolist())
        print("BOARD TARGET:", np.where(masks[3] > 0)[0].tolist())
        print("BOARD SOURCE:", np.where(masks[4] > 0)[0].tolist())
        print(
            "CONDITIONED TARGET:",
            np.where(masks[5] > 0)[0].tolist()
        )

        print("=================================")