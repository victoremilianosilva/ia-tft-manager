from copy import deepcopy

from units.UnitPool import UnitPool


class FakeUnitManager:
    """UnitManager mínimo para testar o comportamento do pool."""

    def __init__(self, champions):
        self.champions = deepcopy(champions)
        self.catalog_reads = 0

        self.index_by_id = {
            champion["id"]: index
            for index, champion in enumerate(self.champions)
        }

    def get_all_champions(self):
        self.catalog_reads += 1
        return deepcopy(self.champions)

    def get_unit_id(self, champion):
        return self.index_by_id.get(champion.get("id"))

    def get_champion(self, champion_id):
        if not isinstance(champion_id, int):
            return None

        if not 0 <= champion_id < len(self.champions):
            return None

        return self.champions[champion_id]


def make_champions():
    return [
        {
            "id": "A",
            "name": "Champion A",
            "cost": 1,
            "traits": ["TraitA"],
            "combat_profile": {"damage": {"base": 10}},
        },
        {
            "id": "B",
            "name": "Champion B",
            "cost": 1,
            "traits": ["TraitB"],
            "combat_profile": {"damage": {"base": 20}},
        },
        {
            "id": "C",
            "name": "Champion C",
            "cost": 2,
            "traits": ["TraitC"],
            "combat_profile": {"damage": {"base": 30}},
        },
    ]


def test_draw_does_not_copy_catalog_for_every_roll():
    manager = FakeUnitManager(make_champions())

    pool = UnitPool(
        unit_manager=manager,
        copies_by_cost={1: 30, 2: 25},
    )

    # A construção do pool lê o catálogo uma vez.
    reads_after_reset = manager.catalog_reads
    assert reads_after_reset == 1

    for _ in range(20):
        unit = pool.draw(1)
        assert unit is not None
        assert unit["cost"] == 1

    # Nenhuma nova leitura do catálogo durante os sorteios.
    assert manager.catalog_reads == reads_after_reset


def test_draw_returns_an_independent_copy():
    manager = FakeUnitManager(make_champions())

    pool = UnitPool(
        unit_manager=manager,
        copies_by_cost={1: 30, 2: 25},
    )

    unit = pool.draw(1)
    assert unit is not None

    unit["combat_profile"]["damage"]["base"] = -999
    unit["traits"].append("Modified")

    # A unidade sorteada não pode modificar o catálogo.
    original = manager.get_champion(
        manager.index_by_id[unit["id"]]
    )

    assert original["combat_profile"]["damage"]["base"] > 0
    assert "Modified" not in original["traits"]


def test_has_available_cost_uses_cached_index():
    manager = FakeUnitManager(make_champions())

    pool = UnitPool(
        unit_manager=manager,
        copies_by_cost={1: 1, 2: 1},
    )

    reads_after_reset = manager.catalog_reads

    assert pool.has_available_cost(1)
    assert pool.has_available_cost(2)
    assert not pool.has_available_cost(3)

    # Consultas de disponibilidade não relêem o catálogo.
    assert manager.catalog_reads == reads_after_reset



def test_draw_respects_stock_and_cost():
    manager = FakeUnitManager(make_champions())

    pool = UnitPool(
        unit_manager=manager,
        copies_by_cost={1: 1, 2: 0},
    )

    # Existem dois campeões de custo 1, com uma cópia cada.
    first = pool.draw(1)
    second = pool.draw(1)

    assert first is not None
    assert second is not None

    assert first["cost"] == 1
    assert second["cost"] == 1

    # Os dois sorteios precisam consumir campeões diferentes.
    assert first["id"] != second["id"]

    # As duas cópias foram consumidas: o pool está esgotado.
    assert pool.draw(1) is None

    # Campeões de custo 2 não possuem estoque.
    assert pool.draw(2) is None

    assert pool.validate()
