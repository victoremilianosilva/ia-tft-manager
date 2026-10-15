# units/UnitPool.py

import random
from copy import deepcopy

from config.GameConfig import GameConfig


class UnitPool:
    """
    🌐 Pool GLOBAL de unidades.

    Existe uma única instância por TFTLobby.

    Exemplo:

        TFTLobby
            │
            └── UnitPool
                  ├── Teemo: 29
                  ├── Nasus: 22
                  ├── Pyke: 18
                  └── ...

    Todos os jogadores utilizam este mesmo pool.

    Responsabilidades:
        - controlar quantidade global de cópias
        - retirar cópias do pool
        - devolver cópias ao pool
        - informar disponibilidade

    NÃO é responsabilidade:
        - criar UUID
        - board
        - bench
        - shop
        - gold
        - reward
        - estratégia
        - combate
    """

    def __init__(
        self,
        unit_manager,
        copies_by_cost=None,
    ):
        self.unit_manager = unit_manager
        # =========================================================
        # ⚡ ÍNDICE ESTÁTICO: IDs agrupados por custo
        # =========================================================
        # O catálogo é considerado estático durante a partida.
        # O índice é reconstruído sempre que reset() é chamado.
        #
        # Exemplo:
        # {
        #     1: [0, 1, 4, 7],
        #     2: [2, 3, 8],
        #     3: [5, 6],
        # }
        #
        # Guardamos IDs, não cópias de campeões.
        self._champion_ids_by_cost = {}

        # =========================================================
        # 📦 QUANTIDADE DE CÓPIAS POR CUSTO
        # =========================================================

        self.copies_by_cost = (
            dict(copies_by_cost)
            if copies_by_cost is not None
            else {
                1: 30,
                2: 25,
                3: 18,
                4: 10,
                5: 9,
            }
        )

        # =========================================================
        # 📊 ESTADO
        # =========================================================

        # Quantidade atualmente disponível.
        #
        # Chave = ID interno do UnitManager
        #
        # Exemplo:
        #
        # {
        #     7: 24,
        #     8: 17,
        # }

        self.available = {}

        # Quantidade inicial de cada campeão.
        self.initial_counts = {}

        self.reset()

    # =============================================================
    # 🔄 RESET
    # =============================================================
    def reset(self):
        """
        Reconstrói o pool e o índice de campeões por custo.

        A cópia do catálogo acontece uma vez por reset,
        e não a cada sorteio da loja.
        """
        self.available.clear()
        self.initial_counts.clear()
        self._champion_ids_by_cost.clear()

        # Uma única leitura segura do catálogo.
        champions = self.unit_manager.get_all_champions()

        for champion in champions:
            champion_id = self.unit_manager.get_unit_id(
                champion
            )

            if champion_id is None:
                continue

            cost = int(champion.get("cost", 1))

            copies = int(
                self.copies_by_cost.get(cost, 0)
            )

            self.available[champion_id] = copies
            self.initial_counts[champion_id] = copies

            self._champion_ids_by_cost.setdefault(
                cost, []
            ).append(champion_id)
    # =============================================================
    # 📤 DRAW
    # =============================================================

    def draw(self, cost):
        """
        Retira uma cópia aleatória de determinado custo.

        Otimização:
        - Não copia o catálogo inteiro a cada sorteio.
        - Consulta somente os IDs do custo solicitado.
        - Copia profundamente apenas o campeão escolhido.
        """
        try:
            cost = int(cost)
        except (TypeError, ValueError):
            return None

        # ⚡ Filtra apenas IDs previamente indexados.
        candidate_ids = [
            champion_id
            for champion_id in self._champion_ids_by_cost.get(
                cost, ()
            )
            if self.available.get(champion_id, 0) > 0
        ]

        if not candidate_ids:
            return None

        # 🎲 Sorteia entre campeões com estoque disponível.
        champion_id = random.choice(candidate_ids)

        # O ID interno permite localizar o registro em O(1).
        champion = self.unit_manager.get_champion(
            champion_id
        )

        # Proteção caso o catálogo tenha sido alterado
        # externamente depois da construção do índice.
        if champion is None:
            return None

        # ➖ Retira uma cópia física do pool.
        self.available[champion_id] -= 1

        # 🛡️ Preserva o isolamento do catálogo.
        return self._copy_champion(champion)
    # =============================================================
    # 📥 RETURN UNIT
    # =============================================================

    def take_champion_for_testing(self, champion_api_name):
        """Retira uma cópia exata do pool para fixtures de paridade."""
        if not isinstance(champion_api_name, str) or not champion_api_name:
            return None
        for champion in self.unit_manager.get_all_champions():
            api_name = champion.get("apiName", champion.get("champion_id"))
            if api_name != champion_api_name:
                continue
            champion_id = self.unit_manager.get_unit_id(champion)
            if champion_id is None or self.available.get(champion_id, 0) <= 0:
                return None
            self.available[champion_id] -= 1
            return self._copy_champion(champion)
        return None

    def return_unit(self, unit):
        """
        🔄 Devolve uma unidade para o pool global.

        Quantidade devolvida depende da estrela:

            1★ → +1 cópia
            2★ → +3 cópias
            3★ → +9 cópias

        Isso representa a quantidade de cópias físicas
        que aquela unidade consumiu do pool.
        """

        if unit is None or not isinstance(unit, dict):
            return False

        champion_id = unit.get("id")

        if champion_id is None:
            return False

        if champion_id not in self.initial_counts:
            return False

        try:
            star = int(
                unit.get("star", 1)
            )
        except (TypeError, ValueError):
            star = 1

        copies_to_return = GameConfig.get_star_copies(
            star
        )

        if copies_to_return <= 0:
            return False

        return self.return_copies(
            champion_id,
            copies_to_return
        )

    # =============================================================
    # 📥 RETURN COPIES
    # =============================================================

    def return_copies(
        self,
        champion_id,
        amount,
    ):
        """
        Devolve uma quantidade EXATA de cópias físicas.

        Exemplo:

            return_copies(teemo_id, 3)

        → devolve 3 cópias.

        Nunca ultrapassa o estoque inicial.
        """

        if champion_id not in self.initial_counts:
            return False

        try:
            amount = int(amount)
        except (TypeError, ValueError):
            return False

        if amount <= 0:
            return False

        current = self.available.get(
            champion_id,
            0
        )

        initial = self.initial_counts.get(
            champion_id,
            0
        )

        # 🛡️ Nunca ultrapassar o estoque inicial.
        new_value = min(
            current + amount,
            initial
        )

        returned = new_value - current

        if returned <= 0:
            return False

        self.available[champion_id] = new_value

        return True

    # =============================================================
    # 📊 DISPONIBILIDADE
    # =============================================================

    def get_available(self, champion_id):
        """
        Retorna a quantidade disponível de um campeão.
        """

        return self.available.get(
            champion_id,
            0
        )

    def get_initial_count(self, champion_id):
        """
        Retorna a quantidade inicial de um campeão.
        """

        return self.initial_counts.get(
            champion_id,
            0
        )

    def get_taken_count(self, champion_id):
        """
        Retorna quantas cópias estão fora do pool.

        Inclui:
            - shops
            - boards
            - benches
        """

        initial = self.get_initial_count(
            champion_id
        )

        available = self.get_available(
            champion_id
        )

        return max(
            0,
            initial - available
        )

    # =============================================================
    # 🔎 VERIFICAÇÕES
    # =============================================================

    def has_available(self, champion_id):
        """
        Verifica se existe pelo menos uma cópia disponível.
        """

        return (
            self.get_available(
                champion_id
            ) > 0
        )

    def has_available_cost(self, cost):
        """
        Verifica se existe pelo menos um campeão disponível
        de determinado custo, sem copiar ou percorrer o catálogo.
        """
        try:
            cost = int(cost)
        except (TypeError, ValueError):
            return False

        return any(
            self.available.get(champion_id, 0) > 0
            for champion_id in self._champion_ids_by_cost.get(
                cost, ()
            )
        )
    # =============================================================
    # 📈 ESTATÍSTICAS
    # =============================================================

    def get_total_available(self):
        """
        Quantidade total de cópias atualmente disponíveis.
        """

        return sum(
            self.available.values()
        )

    def get_total_initial(self):
        """
        Quantidade total existente no início da partida.
        """

        return sum(
            self.initial_counts.values()
        )

    def get_total_taken(self):
        """
        Quantidade total de cópias atualmente fora do pool.
        """

        return max(
            0,
            self.get_total_initial()
            - self.get_total_available()
        )

    # =============================================================
    # 📋 ESTADO
    # =============================================================

    def get_state(self):
        """
        Retorna uma cópia do estado atual do pool.
        """

        return dict(
            self.available
        )

    def get_initial_state(self):
        """
        Retorna uma cópia do estado inicial.
        """

        return dict(
            self.initial_counts
        )

    # =============================================================
    # 🧪 VALIDAÇÃO
    # =============================================================

    def validate(self):
        """
        Verifica se o pool está consistente.

        Nenhum campeão pode possuir:

            available < 0

        ou:

            available > initial
        """

        # Não podem existir IDs desconhecidos.
        for champion_id in self.available:

            if champion_id not in self.initial_counts:
                return False

        # Verifica limites.
        for champion_id, available in self.available.items():

            initial = self.initial_counts.get(
                champion_id,
                0
            )

            if available < 0:
                return False

            if available > initial:
                return False

        # Todos os campeões precisam ter entrada.
        for champion_id in self.initial_counts:

            if champion_id not in self.available:
                return False

        return True

    # =============================================================
    # 🧹 COPIAR CAMPEÃO
    # =============================================================

    @staticmethod
    def _copy_champion(champion):
        """
        Cria uma cópia independente dos dados estáticos.

        O catálogo do UnitManager nunca deve ser alterado
        diretamente por uma unidade retirada do pool.
        """

        return deepcopy(
            champion
        )

    # =============================================================
    # 🐛 DEBUG
    # =============================================================

    def debug_print(self):
        """
        Exibe o estado global do pool.
        """

        print(
            "\n========== UNIT POOL =========="
        )

        for champion in self.unit_manager.get_all_champions():

            champion_id = self.unit_manager.get_unit_id(
                champion
            )

            available = self.get_available(
                champion_id
            )

            initial = self.get_initial_count(
                champion_id
            )

            print(
                f"[{champion_id:>3}] "
                f"{champion.get('name', '?'):<15} "
                f"Custo {champion.get('cost', '?')} | "
                f"{available}/{initial}"
            )

        print(
            "==============================="
        )
