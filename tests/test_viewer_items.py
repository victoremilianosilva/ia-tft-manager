from viewer.session import unit_label


def test_unit_label_includes_equipped_items():
    unit = {
        "occupied": True,
        "champion_id": "TFT_Test_Carry",
        "star": 2,
        "items": ["test_blade", "test_bow"],
    }
    label = unit_label(unit)
    assert "TFT_Test_Carry" in label
    assert "★★" in label
    assert "Itens: test_blade, test_bow" in label


def test_unit_label_without_items_stays_readable():
    unit = {
        "occupied": True,
        "champion_id": "TFT_Test_Tank",
        "star": 1,
        "items": [],
    }
    assert unit_label(unit) == "TFT_Test_Tank ★"


def test_unit_label_ignores_empty_item_names():
    unit = {
        "occupied": True,
        "champion_id": "TFT_Test_Unit",
        "star": 1,
        "items": ["", "test_item"],
    }
    assert unit_label(unit).endswith("Itens: test_item")
