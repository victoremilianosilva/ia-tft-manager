# ai/AntiLoopManager.py

from collections import deque


class AntiLoopManager:
    """
    🔄 Impede a IA de ficar repetindo movimentos inúteis.

    Responsabilidades:
        - guardar histórico de posições
        - detectar repetição de board
        - detectar movimento inverso
        - detectar oscilação A -> B -> A
        - bloquear movimentos recentes
        - detectar loops de bench <-> board
        - detectar swaps repetitivos

    NÃO é responsabilidade:
        - escolher estratégia
        - calcular reward
        - executar movimento
        - criar action mask
        - combate
    """

    def __init__(
        self,
        history_size=20,
        blocked_move_size=10,
        loop_threshold=2,
    ):
        self.history_size = history_size
        self.blocked_move_size = (
            blocked_move_size
        )
        self.loop_threshold = loop_threshold

        # 📊 Métricas acumuladas durante a vida do ambiente.
        # Não são apagadas quando o histórico de movimentos é resetado.
        self.execution_metrics = {
            "execution_attempts": 0,
            "execution_blocks": 0,
            "blocked_reverse": 0,
            "blocked_oscillation": 0,
            "blocked_explicit": 0,
            "blocked_bench_board_loop": 0,
            "board_moves_executed": 0,
            "bench_to_board_executed": 0,
            "blocked_cycle": 0,
        }

        self.reset()

    # =============================================================
    # 🔄 RESET
    # =============================================================
    def reset(self):
        """Reseta todo o histórico."""

        self.position_history = deque(
            maxlen=self.history_size
        )

        self.move_history = deque(
            maxlen=self.history_size
        )

        self.blocked_moves = deque(
            maxlen=self.blocked_move_size
        )

        self.state_visits = {}

        self.last_board_signature = None
        self.blocked_move_states = {}
        self.last_move = None

    # =============================================================
    # 📸 BOARD SIGNATURE
    # =============================================================
    def make_board_signature(
        self,
        board,
        bench=None,
    ):
        """
        Cria uma assinatura do estado de posicionamento.

        IMPORTANTE:

        UUID é preferido porque identifica uma unidade individual.

        Caso UUID não exista, usamos:
            id + star
        """

        board_signature = []

        for position, unit in enumerate(
            board or []
        ):

            if unit is None:
                board_signature.append(
                    (
                        position,
                        None,
                    )
                )
                continue

            board_signature.append(
                (
                    position,
                    self._unit_identity(
                        unit
                    ),
                )
            )

        bench_signature = []

        for position, unit in enumerate(
            bench or []
        ):

            if unit is None:
                bench_signature.append(
                    (
                        position,
                        None,
                    )
                )
                continue

            bench_signature.append(
                (
                    position,
                    self._unit_identity(
                        unit
                    ),
                )
            )

        return (
            tuple(board_signature),
            tuple(bench_signature),
        )

    @staticmethod
    def _unit_identity(
        unit,
    ):
        """Identidade estável de uma unidade."""

        if not isinstance(
            unit,
            dict,
        ):
            return None

        uuid = unit.get(
            "uuid"
        )

        if uuid is not None:
            return (
                "uuid",
                uuid,
            )

        return (
            "unit",
            unit.get("id"),
            unit.get("star", 1),
        )

    # =============================================================
    # 📥 REGISTRAR ESTADO
    # =============================================================
    def register_state(
        self,
        board,
        bench=None,
    ):
        """
        Registra o estado atual do board/bench.

        Retorna:

            {
                "signature": ...,
                "repeated": bool,
                "visits": int
            }
        """

        signature = (
            self.make_board_signature(
                board,
                bench,
            )
        )

        self.position_history.append(
            signature
        )

        visits = (
            self.state_visits.get(
                signature,
                0
            )
            + 1
        )

        self.state_visits[
            signature
        ] = visits

        repeated = (
            visits >= self.loop_threshold
        )

        self.last_board_signature = (
            signature
        )

        return {
            "signature": signature,
            "repeated": repeated,
            "visits": visits,
        }

    # =============================================================
    # 🔄 REGISTRAR MOVIMENTO
    # =============================================================
    def register_move(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Registra um movimento.

        Exemplo:

            MOVE_BENCH
            source=2
            target=17
        """

        move = (
            move_type,
            source,
            target,
            self._unit_identity(
                unit
            ),
        )

        self.move_history.append(
            move
        )

        self.last_move = move

        return move
   
    # =============================================================
    # 🚫 MOVIMENTO BLOQUEADO
    # =============================================================
    def block_move(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Bloqueia um movimento no estado atual do tabuleiro/banco.

        O bloqueio deixa de valer quando register_state()
        registra uma assinatura de estado diferente.
        """
        key = self.make_move_key(
            move_type,
            source,
            target,
            unit,
        )

        # Evita entradas duplicadas para a mesma chave.
        if key in self.blocked_moves:
            self.blocked_moves.remove(key)

        # Controla a remoção da assinatura associada quando
        # o histórico atingir o limite.
        elif len(self.blocked_moves) >= self.blocked_move_size:
            expired_key = self.blocked_moves.popleft()
            self.blocked_move_states.pop(expired_key, None)

        self.blocked_moves.append(key)
        self.blocked_move_states[key] = self.last_board_signature

        return key

    # =============================================================
    # 🚫 VERIFICAR BLOQUEIO
    # =============================================================
    def is_move_blocked(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Retorna True somente se o movimento estiver bloqueado
        no estado de posicionamento atualmente registrado.
        """
        key = self.make_move_key(
            move_type,
            source,
            target,
            unit,
        )

        if key not in self.blocked_moves:
            return False

        blocked_state = self.blocked_move_states.get(key)

        return blocked_state == self.last_board_signature

    # =============================================================
    # 🔑 MOVE KEY
    # =============================================================
    def make_move_key(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """Cria uma chave estável para um movimento."""

        return (
            move_type,
            source,
            target,
            self._unit_identity(
                unit
            ),
        )

    # =============================================================
    # 🚫 VERIFICAR BLOQUEIO
    # =============================================================
    def is_move_blocked(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Verifica se determinado movimento foi bloqueado.
        """

        key = self.make_move_key(
            move_type,
            source,
            target,
            unit,
        )

        return key in self.blocked_moves

    # =============================================================
    # 🔁 MOVIMENTO INVERSO
    # =============================================================
    def is_reverse_move(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Detecta movimentos inversos.

        Para board_swap, identifica a mesma dupla de posições
        independentemente de qual unidade ficou na origem.
        """

        if not self.last_move:
            return False

        last_type, last_source, last_target, last_unit = (
            self.last_move
        )

        # Uma troca entre as mesmas duas posições pode ser
        # desfeita com a mesma origem/destino, pois as unidades
        # trocaram de lugar. Por isso, não depende da identidade.
        if (
            move_type == "board_swap"
            and last_type == "board_swap"
        ):
            return (
                {last_source, last_target}
                == {source, target}
            )

        # Para movimentos normais, mantém a validação original.
        current_unit = self._unit_identity(unit)

        if last_unit != current_unit:
            return False

        if last_type != move_type:
            return False

        return (
            last_source == target
            and last_target == source
        )

    # =============================================================
    # 🔄 OSCILAÇÃO
    # =============================================================      
    def is_oscillating(
        self,
        unit,
        source,
        target,
        move_type=None,
    ):
        """
        Detecta movimentos inversos e ciclos recentes de posições.

        Para board_move, acompanha a mesma unidade.
        Para board_swap, considera que as duas unidades mudam
        de posição e examina a sequência de swaps.
        """

        identity = self._unit_identity(unit)
        recent = list(self.move_history)[-6:]

        if identity is None or not recent:
            return False

        # ---------------------------------------------------------
        # 🔀 Selecionar movimentos relevantes
        # ---------------------------------------------------------

        if move_type == "board_swap":
            relevant = [
                (src, dst)
                for recorded_type, src, dst, move_unit in recent
                if (
                    move_unit == identity
                    and recorded_type in ("board_swap", "board_move")
                )
            ]
        else:
            relevant = [
                (src, dst)
                for recorded_type, src, dst, move_unit in recent
                if (
                    move_unit == identity
                    and recorded_type == "board_move"
                )
            ]

        if not relevant:
            return False

        # ---------------------------------------------------------
        # 🔗 Reconstruir a sequência contínua
        # ---------------------------------------------------------

        # O último movimento registrado deve chegar à origem atual.
        if relevant[-1][1] != source:
            return False

        chain = [
            relevant[-1][0],
            relevant[-1][1],
        ]

        for previous_source, previous_target in reversed(
            relevant[:-1]
        ):
            if previous_target != chain[0]:
                break

            chain.insert(0, previous_source)

        # ---------------------------------------------------------
        # 🚫 O destino fecharia um ciclo?
        # ---------------------------------------------------------

        return target in chain[:-1]

    # =============================================================
    # 🔁 BENCH <-> BOARD
    # ============================================================= 
    def is_bench_board_loop(
        self,
        unit,
        move_type=None,
        source=None,
        target=None,
    ):
        """
        Detecta se a ação candidata repete uma transição
        banco <-> tabuleiro que acabou de ser desfeita.
        """

        identity = self._unit_identity(unit)

        if identity is None or move_type is None:
            return False

        move_aliases = {
            "MOVE_BENCH_TO_BOARD": "bench_to_board",
            "bench_to_board": "bench_to_board",
            "MOVE_BOARD_TO_BENCH": "board_to_bench",
            "board_to_bench": "board_to_bench",
        }

        candidate_type = move_aliases.get(move_type)

        if candidate_type is None:
            return False

        recent = []

        for recorded_type, src, dst, move_unit in self.move_history:
            if move_unit != identity:
                continue

            normalized_type = move_aliases.get(recorded_type)

            if normalized_type is not None:
                recent.append((normalized_type, src, dst))

        # Precisamos dos dois últimos movimentos da unidade.
        if len(recent) < 2:
            return False

        previous, last = recent[-2], recent[-1]

        previous_type, previous_source, previous_target = previous
        last_type, last_source, last_target = last

        # O histórico precisa representar uma ida e uma volta
        # pelas mesmas posições, em sequência cronológica.
        reversed_transition = (
            previous_type != last_type
            and previous_source == last_target
            and previous_target == last_source
        )

        if not reversed_transition:
            return False

        # Bloqueia somente a repetição da transição anterior.
        return (
            candidate_type == previous_type
            and source == previous_source
            and target == previous_target
        )

    # =============================================================
    # 🧠 ESTADO JÁ VISITADO
    # =============================================================
    def was_state_seen(
        self,
        board,
        bench=None,
    ):
        """
        Verifica se o estado já apareceu anteriormente.
        """

        signature = (
            self.make_board_signature(
                board,
                bench,
            )
        )

        return signature in (
            self.state_visits
        )

    def get_state_visits(
        self,
        board,
        bench=None,
    ):
        """Retorna quantidade de vezes que o estado apareceu."""

        signature = (
            self.make_board_signature(
                board,
                bench,
            )
        )

        return self.state_visits.get(
            signature,
            0
        )

    # =============================================================
    # 🧮 AVALIAÇÃO DE MOVIMENTO
    # =============================================================
    def evaluate_move_risk(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Retorna risco de loop.

        0.0 = seguro
        1.0 = extremamente suspeito
        """

        risk = 0.0

        # ---------------------------------------------------------
        # 🚫 Já bloqueado
        # ---------------------------------------------------------

        if self.is_move_blocked(
            move_type,
            source,
            target,
            unit,
        ):
            return 1.0

        # ---------------------------------------------------------
        # 🔄 Movimento inverso
        # ---------------------------------------------------------

        if self.is_reverse_move(
            move_type,
            source,
            target,
            unit,
        ):
            risk += 0.7

        # ---------------------------------------------------------
        # 🔁 Oscilação
        # ---------------------------------------------------------

        if self.is_oscillating(
            unit,
            source,
            target,
            move_type=move_type,
        ):
            risk += 0.8

        # ---------------------------------------------------------
        # ↔️ Bench <-> Board
        # ---------------------------------------------------------

        if self.is_bench_board_loop(
            unit,
            move_type=move_type,
            source=source,
            target=target,
        ):
            risk += 0.9


        return min(
            1.0,
            risk
        )

    # =============================================================
    # 🚦 DEVE BLOQUEAR?
    # =============================================================
    def should_block_move(
        self,
        move_type,
        source,
        target,
        unit=None,
        board=None,
        bench=None,
    ):
        """
        Consulta sem efeitos colaterais.
        Não incrementa métricas durante a construção das máscaras.
        """

        return self.get_block_reason(
            move_type=move_type,
            source=source,
            target=target,
            unit=unit,
        ) is not None
    
    # =============================================================
    # 🧹 LIMPEZA
    # =============================================================
    def clear_old_blocks(self):
        """
        Limpa bloqueios antigos.

        Como blocked_moves é deque com maxlen,
        os mais antigos saem automaticamente.
        """

        while len(
            self.blocked_moves
        ) > self.blocked_move_size:

            self.blocked_moves.popleft()

    # =============================================================
    # 📊 ESTADO
    # =============================================================
    def get_state(self):
        """Retorna informações úteis para debug."""

        return {
            "history_size": len(
                self.position_history
            ),

            "move_history_size": len(
                self.move_history
            ),

            "blocked_moves": len(
                self.blocked_moves
            ),

            "known_states": len(
                self.state_visits
            ),

            "last_move": self.last_move,
        }

    # =============================================================
    # 📊 MÉTRICAS PARA TENSORBOARD
    # =============================================================    
    def get_block_reason(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Retorna o motivo do bloqueio ou None.

        Não altera histórico nem contadores.
        Pode ser consultado durante a criação das máscaras.
        """

        # 🚫 Bloqueio explícito
        if self.is_move_blocked(
            move_type, source, target, unit
        ):
            return "explicit"

        # 🔄 Movimento inverso
        if self.is_reverse_move(
            move_type, source, target, unit
        ):
            return "reverse"

        # 🔁 Oscilação, considerando o tipo de movimento
        if self.is_oscillating(
            unit,
            source,
            target,
            move_type=move_type,
        ):
            return "oscillation"


        # 🪑 O histórico banco ↔ tabuleiro só deve
        # bloquear candidatos que envolvam esse ciclo.
        if (
            move_type in ("bench_to_board", "board_to_bench",
                        "MOVE_BENCH_TO_BOARD", "MOVE_BOARD_TO_BENCH")
                        and self.is_bench_board_loop(
                unit,
                move_type=move_type,
                source=source,
                target=target,
            )
        ):
            return "bench_board_loop"

        # ♻️ Ciclo envolvendo múltiplos movimentos no tabuleiro
        if self.is_cycle_move(
            move_type, source, target, unit
        ):
            return "cycle"

        return None

    def record_execution_attempt(self):
        """Registra uma tentativa real de movimentação."""
        self.execution_metrics["execution_attempts"] += 1

    def record_execution_block(self, reason):
        """
        Registra um bloqueio ocorrido durante a execução.
        Não chamar para candidatos descartados pela máscara.
        """

        self.execution_metrics["execution_blocks"] += 1

        key = f"blocked_{reason}"

        if key in self.execution_metrics:
            self.execution_metrics[key] += 1

    def record_successful_move(self, move_type):
        """Registra uma movimentação concluída com sucesso."""

        if move_type in ("board_move", "board_swap"):
            self.execution_metrics["board_moves_executed"] += 1

        elif move_type == "bench_to_board":
            self.execution_metrics["bench_to_board_executed"] += 1

    def get_metrics(self):
        """Devolve uma cópia segura dos contadores."""
        return dict(self.execution_metrics)

    def is_cycle_move(
        self,
        move_type,
        source,
        target,
        unit=None,
    ):
        """
        Detecta quando um movimento fecha um ciclo de posições
        da mesma unidade, por exemplo:
            3 -> 10 -> 12 -> 3

        Considera somente o histórico recente da unidade.
        """

        if move_type not in ("board_move", "board_swap"):
            return False

        identity = self._unit_identity(unit)

        recent = [
            (src, dst)
            for kind, src, dst, move_unit in self.move_history
            if (
                kind in ("board_move", "board_swap")
                and move_unit == identity
            )
        ][-8:]


        if not recent:
            return False

        # 🔗 Reconstrói uma sequência cronológica contínua
        # iniciada na posição para a qual o movimento tentaria voltar.
        started = False
        expected_position = None

        for src, dst in recent:
            if not started:
                if src == target:
                    started = True
                    expected_position = dst
                continue

            # Uma transição desconexa invalida a sequência.
            if src != expected_position:
                return False

            expected_position = dst

        # Só bloqueia se o histórico contínuo terminar
        # exatamente na origem do movimento candidato.
        return started and expected_position == source

    # =============================================================
    # 🐛 DEBUG
    # =============================================================
    def debug_print(self):
        """Imprime estado do AntiLoop."""

        print(
            "\n========== ANTI LOOP =========="
        )

        print(
            f"📸 States: "
            f"{len(self.position_history)}"
        )

        print(
            f"🔄 Moves: "
            f"{len(self.move_history)}"
        )

        print(
            f"🚫 Blocked: "
            f"{len(self.blocked_moves)}"
        )

        print(
            f"🧠 Known states: "
            f"{len(self.state_visits)}"
        )

        print(
            f"➡️ Last move: "
            f"{self.last_move}"
        )

        print(
            "==============================="
        )