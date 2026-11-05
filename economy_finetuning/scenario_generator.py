"""Scenario definitions and observation-only matching for economic fine-tuning.

The current native engine exposes reset(seed), observations and masks, but no
public state-injection API. Therefore scenarios are mined from naturally
reached, authoritative C++ states; this module never fabricates observations.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

STRATEGY_NAMES = {
    0: "ECON",
    1: "STABILIZE",
    2: "FAST8",
    3: "SLOWROLL",
    4: "ALL_IN",
    5: "WINSTREAK",
    6: "LOSS_STREAK",
}


@dataclass(frozen=True)
class ScenarioSpec:
    scenario_id: str
    title: str
    description: str
    stage_min: int = 1
    stage_max: int = 7
    gold_min: float = 0.0
    gold_max: float = 250.0
    level_min: float = 1.0
    level_max: float = 10.0
    hp_min: float = 1.0
    hp_max: float = 100.0
    strategies: tuple[int, ...] = ()
    trainable: bool = False
    objective: str = "monitor"
    reward_buy_xp: float = 0.0
    reward_pass: float = 0.0
    reward_roll: float = 0.0

    def matches(self, state: dict[str, Any]) -> bool:
        strategy = int(state["strategy"])
        return (
            self.stage_min <= int(state["stage"]) <= self.stage_max
            and self.gold_min <= float(state["gold"]) <= self.gold_max
            and self.level_min <= float(state["level"]) <= self.level_max
            and self.hp_min <= float(state["hp"]) <= self.hp_max
            and (not self.strategies or strategy in self.strategies)
        )

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["strategies"] = [STRATEGY_NAMES.get(x, str(x)) for x in self.strategies]
        return value


# The scenarios below are explicit acceptance targets discussed for this
# project. They are matched against real observations emitted by the C++ engine.
# Only scenarios with a conservative, unambiguous action-level shaping signal
# are trainable. Monitor-only cases remain visible in the audit and are not
# assigned invented rewards.
SCENARIOS: tuple[ScenarioSpec, ...] = (
    ScenarioSpec(
        "s4_fast8_lvl6_gold60_hp_ok",
        "4-1 / FAST8 / nível 6 / 60+ ouro / HP preservado",
        "Detecta jogador FAST8 abaixo do nível-alvo, com ouro suficiente e HP acima de 40.",
        4, 4, 60, 250, 1, 6.99, 40.01, 100, (2,), True,
        "priorizar_progressao_comedida", 0.055, -0.012, -0.018,
    ),
    ScenarioSpec(
        "s4_fast8_lvl6_gold80",
        "4-1 / FAST8 / nível 6 / 80+ ouro",
        "Caso severo de acumulação: grande reserva de ouro e atraso de nível.",
        4, 4, 80, 250, 1, 6.99, 20.01, 100, (2,), True,
        "reduzir_hoarding", 0.075, -0.018, -0.025,
    ),
    ScenarioSpec(
        "s4_fast8_lvl7_gold60",
        "4-1 / FAST8 / nível 7 / 60+ ouro",
        "Avalia progressão adicional sem obrigar nível 9/10 ou gasto indiscriminado.",
        4, 4, 60, 250, 7, 7.99, 30.01, 100, (2,), True,
        "avaliar_progressao_para_nivel8", 0.035, -0.006, -0.008,
    ),
    ScenarioSpec(
        "late_game_high_gold_underleveled",
        "Estágio 4-5 a 5-5 / nível abaixo do alvo / 60+ ouro",
        "Detecta acúmulo de ouro em meio/fim de jogo quando a estratégia não é SLOWROLL.",
        4, 5, 60, 250, 1, 7.99, 30.01, 100, (0, 1, 2, 4, 5, 6), True,
        "evitar_passividade_economica", 0.035, -0.008, -0.010,
    ),
    ScenarioSpec(
        "critical_hp_high_gold",
        "HP crítico / 50+ ouro",
        "Estado de risco: audita se o modelo continua guardando ouro com pouca vida.",
        3, 7, 50, 250, 1, 10, 0, 30, (), False,
        "monitorar_estabilizacao_sem_forcar_xp",
    ),
    ScenarioSpec(
        "low_hp_fast8_high_gold",
        "FAST8 / HP baixo / 50+ ouro",
        "Verifica se a pressão econômica não faz o modelo ignorar a necessidade de estabilização.",
        3, 7, 50, 250, 1, 8, 0, 40, (2,), False,
        "monitorar_tradeoff_xp_estabilizacao",
    ),
    ScenarioSpec(
        "slowroll_gold_reserve",
        "SLOWROLL / nível 5-7 / 50+ ouro",
        "Proteção explícita: não ensinar BUY_XP indiscriminadamente em SLOWROLL.",
        2, 5, 50, 250, 5, 7.99, 20, 100, (3,), True,
        "preservar_slowroll", -0.055, 0.0, 0.0,
    ),
    ScenarioSpec(
        "all_in_gold_hoarding",
        "ALL_IN / 50+ ouro",
        "Investiga estados ALL_IN que ainda preservam reservas elevadas.",
        3, 7, 50, 250, 1, 10, 0, 100, (4,), False,
        "investigar_all_in_sem_recompensa_artificial",
    ),
    ScenarioSpec(
        "gold_above_50_any_strategy",
        "Qualquer estratégia / ouro acima de 50",
        "Cohort geral para medir compras úteis, XP, roll e PASS sem presumir que gastar sempre é correto.",
        1, 7, 50.01, 250, 1, 10, 0, 100, (), False,
        "auditoria_geral_do_excedente",
    ),
    ScenarioSpec(
        "useful_shop_opportunity",
        "Oportunidade de compra útil com ouro acima de 50",
        "Monitor-only: requer semântica confiável dos candidatos da loja para definir utilidade.",
        1, 7, 50.01, 250, 1, 10, 0, 100, (), False,
        "monitorar_compra_util",
    ),
)


def decode_observation(observation) -> dict[str, Any]:
    """Decode only stable, documented core observation fields."""
    obs = observation.tolist() if hasattr(observation, "tolist") else list(observation)
    if len(obs) < 17:
        raise ValueError(f"Observação curta para cenário econômico: {len(obs)} < 17")
    hp = max(0.0, min(100.0, float(obs[0]) * 100.0))
    gold = max(0.0, float(obs[1]) * 50.0)
    level = max(1.0, min(10.0, float(obs[2]) * 9.0))
    round_fraction = max(0.0, min(0.999, float(obs[6])))
    round_number = max(1.0, min(42.0, 10.0 * round_fraction / (1.0 - round_fraction)))
    if round_number <= 4:
        stage = 1
    else:
        stage = min(7, 2 + int((round_number - 5) // 7))
    strategy = max(range(7), key=lambda idx: float(obs[10 + idx]))
    return {
        "hp": hp,
        "gold": gold,
        "level": level,
        "stage": stage,
        "round_number": round_number,
        "strategy": strategy,
        "strategy_name": STRATEGY_NAMES.get(strategy, "UNKNOWN"),
    }


def matching_scenarios(state: dict[str, Any]) -> list[ScenarioSpec]:
    return [scenario for scenario in SCENARIOS if scenario.matches(state)]


def scenario_catalog() -> list[dict[str, Any]]:
    return [scenario.to_dict() for scenario in SCENARIOS]


def shaped_action_reward(state: dict[str, Any], action_type: int) -> tuple[float, list[str]]:
    """Return small, context-gated shaping and matched trainable scenario IDs."""
    matched = matching_scenarios(state)
    trainable = [scenario for scenario in matched if scenario.trainable]
    reward = 0.0
    for scenario in trainable:
        if action_type == 2:       # BUY_XP
            reward += scenario.reward_buy_xp
        elif action_type == 6:     # PASS
            reward += scenario.reward_pass
        elif action_type == 1:     # REROLL
            reward += scenario.reward_roll
    # A hard safety gate: never reward BUY_XP in critical-HP cohorts.
    if state["hp"] <= 30.0 and action_type == 2:
        reward = min(reward, -0.02)
    return float(max(-0.08, min(0.08, reward))), [item.scenario_id for item in matched]
