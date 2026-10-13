
import pytest
from unittest.mock import Mock

from shop.ShopManager import ShopManager


@pytest.fixture
def shop_manager():
    """Cria um ShopManager isolado para testar roll e reroll."""
    unit_pool = Mock()

    # Simula o retorno de unidades disponíveis no pool.
    unit_pool.draw.return_value = None

    manager = ShopManager(
        unit_pool=unit_pool,
        shop_size=5,
        shop_odds={
            1: [100, 0, 0, 0, 0],
        },
    )

    return manager


def test_roll_returns_copy_by_default(shop_manager):
    """Por padrão, roll retorna uma cópia da loja interna."""
    result = shop_manager.roll(level=1)

    assert result is not shop_manager.shop
    assert result == shop_manager.shop


def test_roll_without_copy_returns_none(shop_manager):
    """Sem cópia, roll atualiza a loja e retorna None."""
    result = shop_manager.roll(
        level=1,
        copy_result=False,
    )

    assert result is None
    assert len(shop_manager.shop) == 5


def test_roll_locked_without_force_preserves_shop(shop_manager):
    """Uma loja bloqueada não deve ser atualizada por roll normal."""
    shop_manager.shop[0] = {"name": "unit_original"}
    shop_manager.set_locked(True)

    result = shop_manager.roll(level=1)

    assert result[0] == {"name": "unit_original"}
    assert shop_manager.shop[0] == {"name": "unit_original"}


def test_roll_locked_without_copy_returns_none(shop_manager):
    """Loja bloqueada e copy_result=False retorna None."""
    shop_manager.shop[0] = {"name": "unit_original"}
    shop_manager.set_locked(True)

    result = shop_manager.roll(
        level=1,
        copy_result=False,
    )

    assert result is None
    assert shop_manager.shop[0] == {"name": "unit_original"}


def test_reroll_returns_copy_by_default(shop_manager):
    """Reroll mantém o retorno em cópia por padrão."""
    result = shop_manager.reroll(level=1)

    assert result is not shop_manager.shop
    assert result == shop_manager.shop


def test_reroll_without_copy_returns_none(shop_manager):
    """Reroll sem cópia atualiza a loja e retorna None."""
    result = shop_manager.reroll(
        level=1,
        copy_result=False,
    )

    assert result is None
    assert len(shop_manager.shop) == 5


def test_reroll_forces_refresh_when_shop_is_locked(shop_manager):
    """Reroll deve continuar forçando a atualização mesmo bloqueada."""
    shop_manager.shop[0] = {"name": "unit_original"}
    shop_manager.set_locked(True)

    shop_manager.reroll(
        level=1,
        copy_result=False,
    )

    # A loja continua bloqueada, mas o reroll foi forçado.
    assert shop_manager.is_locked()
    shop_manager.unit_pool.draw.assert_called()
