import random
from copy import deepcopy

from config.GameConfig import GameConfig


class ShopManager:
    """
    🛒 Shop individual do jogador.

    O UnitPool é global.
    O ShopManager apenas retira/devolve cópias.
    """

    def __init__(
        self,
        unit_pool,
        shop_size=None,
        shop_odds=None,
    ):
        self.unit_pool = unit_pool

        self.shop_size = (
            shop_size
            if shop_size is not None
            else GameConfig.SHOP_SIZE
        )

        self.shop_odds = (
            shop_odds
            if shop_odds is not None
            else GameConfig.SHOP_ODDS
        )

        self.shop = self._create_empty_shop()

        self.locked = False
        self._next_roll_for_testing = None

    # =============================================================
    # 🧱 ESTRUTURA
    # =============================================================

    def _create_empty_shop(self):
        return [None] * self.shop_size

    def reset(self):
        self.shop = self._create_empty_shop()
        self.locked = False

        self._next_roll_for_testing = None
    # =============================================================
    # 🔎 CONSULTA
    # =============================================================

    def get_unit(self, slot):
        if not self.is_valid_slot(slot):
            return None

        return self.shop[slot]

    def get_shop(self):
        return [
            deepcopy(unit)
            if unit is not None
            else None
            for unit in self.shop
        ]

    def is_empty(self, slot):
        if not self.is_valid_slot(slot):
            return False

        return self.shop[slot] is None

    def is_valid_slot(self, slot):
        return (
            isinstance(slot, int)
            and 0 <= slot < self.shop_size
        )

    # =============================================================
    # 🎲 ROLL
    # =============================================================

    def roll(self, level, force=False, copy_result=True):
        """
        Gera uma nova loja.

        copy_result=True:
            Mantém o comportamento original e retorna uma cópia.

        copy_result=False:
            Atualiza a loja interna sem copiar o resultado
            para quem chamou o método.
        """
        if self.locked and not force:
            return self.get_shop() if copy_result else None

        previous_shop = self.get_shop()
        self.return_current_shop()

        if self._next_roll_for_testing is not None:
            names = self._next_roll_for_testing
            if len(names) != self.shop_size:
                raise ValueError("Fixture de reroll deve conter cinco campeoes.")
            reserved = []
            try:
                for name in names:
                    unit = self.unit_pool.take_champion_for_testing(name)
                    if unit is None:
                        raise ValueError("Campeao indisponivel na fixture de reroll: %s" % name)
                    reserved.append(unit)
            except Exception:
                for unit in reserved:
                    self._return_to_pool(unit)
                restored = []
                for old_unit in previous_shop:
                    if old_unit is None:
                        restored.append(None)
                    else:
                        name = old_unit.get("apiName", old_unit.get("champion_id"))
                        restored_unit = self.unit_pool.take_champion_for_testing(name)
                        if restored_unit is None:
                            raise RuntimeError("Falha ao restaurar loja apos fixture invalida.")
                        restored.append(restored_unit)
                self.shop = restored
                raise
            self.shop = reserved
            self._next_roll_for_testing = None
            return self.get_shop() if copy_result else None

        odds = self._get_shop_odds(level)
        for slot in range(self.shop_size):
            cost = self._roll_cost(odds)
            self.shop[slot] = self._draw_from_pool(cost)

        return self.get_shop() if copy_result else None

    # =============================================================
    # 🎯 ODDS
    # =============================================================
    def set_offer_for_testing(self, slot, champion_api_name):
        """Substitui uma oferta reservando/devolvendo a cópia no pool."""
        if not self.is_valid_slot(slot):
            return False
        unit = self.unit_pool.take_champion_for_testing(champion_api_name)
        if unit is None:
            return False
        previous = self.shop[slot]
        if previous is not None and not self._return_to_pool(previous):
            self._return_to_pool(unit)
            return False
        self.shop[slot] = unit
        return True

    def set_next_roll_for_testing(self, champion_api_names):
        """Força a próxima loja a conter exatamente cinco campeões informados."""
        names = list(champion_api_names)
        if len(names) != self.shop_size or any(not isinstance(name, str) or not name for name in names):
            return False
        self._next_roll_for_testing = names
        return True

    def _get_shop_odds(self, level):
        """
        Retorna as probabilidades configuradas para o nível.

        Prioridade:
        1. Configuração recebida pelo ShopManager.
        2. Configuração padrão do GameConfig, se estiver vazia.
        """
        level = int(level)

        odds_config = self.shop_odds

        if not odds_config:
            odds_config = GameConfig.SHOP_ODDS

        if level in odds_config:
            return list(odds_config[level])

        # Mantém o comportamento anterior para níveis
        # que não existem na configuração: usa o maior nível.
        max_level = max(odds_config)

        return list(odds_config[max_level])


    def _roll_cost(self, odds):
        costs = list(
            range(
                1,
                len(odds) + 1
            )
        )

        return random.choices(
            costs,
            weights=odds,
            k=1,
        )[0]

    # =============================================================
    # 🌐 UNIT POOL
    # =============================================================

    def _draw_from_pool(self, cost):
        if self.unit_pool is None:
            raise RuntimeError(
                "ShopManager precisa de um UnitPool."
            )

        return self.unit_pool.draw(
            cost
        )

    # =============================================================
    # 🛒 COMPRA
    # =============================================================

    def take_unit(self, slot):
        """
        Remove a unidade da loja.

        A cópia NÃO retorna ao pool.
        Ela passa a pertencer ao jogador.
        """

        if not self.is_valid_slot(slot):
            return None

        unit = self.shop[slot]

        if unit is None:
            return None

        self.shop[slot] = None

        return unit

    # =============================================================
    # ↩️ DEVOLVER SHOP
    # =============================================================

    def return_current_shop(self):
        for slot in range(self.shop_size):

            unit = self.shop[slot]

            if unit is None:
                continue

            self._return_to_pool(
                unit
            )

            self.shop[slot] = None


    def _return_to_pool(self, unit):
        if self.unit_pool is None:
            raise RuntimeError(
                "ShopManager precisa de um UnitPool."
            )

        # 🆔 Ofertas da loja vêm do catálogo e podem não ter "id".
        # Convertemos o campeão para o identificador interno do pool.
        unit_manager = getattr(
            self.unit_pool,
            "unit_manager",
            None,
        )

        if unit_manager is not None:
            champion_id = unit_manager.get_unit_id(unit)

            if champion_id is not None:
                return self.unit_pool.return_copies(
                    champion_id,
                    1,
                )

        # Compatibilidade com unidades que já possuem ID interno.
        return self.unit_pool.return_unit(unit)


    # =============================================================
    # 🔄 REROLL
    # =============================================================
    def reroll(self, level, copy_result=True):
        """
        Força uma nova loja.

        copy_result=True mantém o comportamento padrão:
        retorna uma cópia independente da loja.

        copy_result=False evita criar essa cópia quando o
        chamador só precisa atualizar a loja interna.
        """
        return self.roll(
            level,
            force=True,
            copy_result=copy_result,
        )


    # =============================================================
    # 🔒 LOCK
    # =============================================================

    def set_locked(self, locked=True):
        self.locked = bool(locked)

    def is_locked(self):
        return self.locked

    def toggle_lock(self):
        self.locked = not self.locked

        return self.locked

    # =============================================================
    # 📊 STATE
    # =============================================================

    def get_state(self):
        return {
            "shop": self.get_shop(),
            "locked": self.locked,
        }