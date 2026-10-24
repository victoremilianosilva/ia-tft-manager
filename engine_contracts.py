"""Enums de contrato entre o PPO Python e a engine nativa C++.

Este módulo contém apenas IDs estáveis da API. Regras de jogo, máscaras,
recompensas e estado da partida pertencem à engine C++.
"""
from enum import IntEnum


class ActionType(IntEnum):
    BUY = 0
    REROLL = 1
    BUY_XP = 2
    MOVE_BENCH = 3
    MOVE_BOARD = 4
    SELL = 5
    PASS = 6
    EQUIP_FROM_INVENTORY = 7
    CRAFT_AND_EQUIP = 8


class Strategy(IntEnum):
    ECON = 0
    STABILIZE = 1
    FAST8 = 2
    SLOWROLL = 3
    ALL_IN = 4
    WINSTREAK = 5
    LOSS_STREAK = 6
