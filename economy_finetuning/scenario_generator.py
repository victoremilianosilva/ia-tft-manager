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
    6: "LEGACY_UNUSED",
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
    player_ids: tuple[int, ...] = ()
    win_streak_min: int = 0
    round_min: float = 1.0
    round_max: float = 42.0
    requires_candidate_semantics: bool = False
    reward_mode: str = "shaped"
    trainable_heads: tuple[str, ...] = ("type_head", "value_head")

    def matches(self, state: dict[str, Any]) -> bool:
        if self.requires_candidate_semantics:
            return False
        strategy = int(state["strategy"])
        return (
            (not self.player_ids or int(state.get("player_id", -1)) in self.player_ids)
            and self.round_min <= float(state.get("round_number", 1.0)) <= self.round_max
            and self.stage_min <= int(state["stage"]) <= self.stage_max
            and self.gold_min <= float(state["gold"]) <= self.gold_max
            and self.level_min <= float(state["level"]) <= self.level_max
            and self.hp_min <= float(state["hp"]) <= self.hp_max
            and (not self.strategies or strategy in self.strategies)
            and float(state.get("win_streak", 0.0)) >= self.win_streak_min
        )

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["strategies"] = [STRATEGY_NAMES.get(x, str(x)) for x in self.strategies]
        value["player_ids"] = list(self.player_ids)
        value["trainable_heads"] = list(self.trainable_heads)
        return value


# The scenarios below are explicit acceptance targets discussed for this
# project. They are matched against real observations emitted by the C++ engine.
# Only scenarios with a conservative, unambiguous action-level shaping signal
# are trainable. Monitor-only cases remain visible in the audit and are not
# assigned invented rewards.
SCENARIOS: tuple[ScenarioSpec, ...] = (
    # Historical runs: keep their IDs and checkpoints in the approval chain.
    ScenarioSpec(
        "critical_hp_high_gold",
        "HP crítico / 50+ ouro",
        "Treino histórico preservado: escolher compra útil, XP, roll ou PASS sob pressão real de vida.",
        3, 7, 50, 250, 1, 10, 0, 30, (0, 1, 2, 3, 4, 5), True,
        "historico_estabilizacao_com_reward_nativo", reward_mode="native",
    ),
    ScenarioSpec(
        "late_game_high_gold_underleveled",
        "Late game / 60+ ouro / abaixo do nível-alvo",
        "Treino histórico preservado: converter reserva em força sem gastar indiscriminadamente.",
        4, 5, 60, 250, 1, 7.99, 30.01, 100, (0, 1, 2, 4, 5), True,
        "historico_conversao_tardia_com_reward_nativo",
        round_min=23, round_max=30, reward_mode="native",
    ),
    ScenarioSpec(
        "econ_gold_reserve",
        "ECON / acumular até 50 comprando peças úteis",
        "Proteger breakpoints de juros até 50, mas comprar pares, upgrades e peças de composição com valor real.",
        1, 7, 0, 49.99, 1, 10, 1, 100, (0,), True,
        "preservar_juros_e_comprar_unidades_uteis", reward_mode="native",
    ),
    ScenarioSpec(
        "econ_surplus_strong_board",
        "ECON / excedente acima de 50 / tabuleiro forte",
        "Com board forte, converter apenas o excedente acima de 50 em XP; manter compra útil como prioridade quando houver oportunidade.",
        3, 7, 50.01, 250, 1, 10, 1, 100, (0,), True,
        "upar_com_excedente_sem_quebrar_reserva", reward_mode="native",
    ),
    ScenarioSpec(
        "stabilize_weak_board",
        "STABILIZE / tabuleiro fraco sob pressão",
        "Com board fraco e sob pressão, gastar seletivamente em XP, roll melhorado e peças que fortaleçam o board.",
        2, 7, 0, 250, 1, 10, 1, 65, (1,), True,
        "estabilizar_board_com_gasto_seletivo", reward_mode="native",
    ),
    ScenarioSpec(
        "fast8_strong_board",
        "FAST8 / tabuleiro forte / caminho ao nível 8",
        "Combinar economia, board forte e XP; não ativar FAST8 com tabuleiro fraco.",
        3, 7, 0, 250, 6, 7.99, 38.01, 100, (2,), True,
        "fast8_com_board_forte", reward_mode="native",
    ),
    ScenarioSpec(
        "all_in_emergency",
        "ALL_IN / converter recursos para sobreviver",
        "Em HP crítico, gastar o ouro restante em compras, roll melhorado, XP e implantação para tentar estabilizar imediatamente.",
        3, 7, 0, 250, 1, 10, 0, 25, (4,), True,
        "all_in_para_sobreviver", reward_mode="native",
    ),
    ScenarioSpec(
        "slowroll_winstreak",
        "SLOWROLL / alvo de 3 estrelas / winstreak",
        "Padrão do exemplo Kha'Zix: buscar cópias úteis e gastar controladamente em nível, peças e implantação para prolongar a winstreak.",
        3, 4, 30, 250, 5, 6.99, 38.01, 100, (3,), True,
        "slowroll_com_winstreak_e_gasto_controlado",
        win_streak_min=2, reward_mode="native",
    ),
)


def decode_observation(observation, player_id: int | None = None) -> dict[str, Any]:
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
        "win_streak": max(0.0, float(obs[4]) * 10.0),
        "loss_streak": max(0.0, float(obs[5]) * 10.0),
        "player_id": int(player_id) if player_id is not None else -1,
    }


def matching_scenarios(state: dict[str, Any]) -> list[ScenarioSpec]:
    return [scenario for scenario in SCENARIOS if scenario.matches(state)]


def scenario_catalog() -> list[dict[str, Any]]:
    return [scenario.to_dict() for scenario in SCENARIOS]


def shaped_action_reward(
    state: dict[str, Any], action_type: int, selected_scenario_id: str | None = None
) -> tuple[float, list[str]]:
    """Return shaping for exactly one selected scenario; retain all matches for audit."""
    matched = matching_scenarios(state)
    trainable = [
        scenario for scenario in matched
        if scenario.trainable and scenario.reward_mode == "shaped" and (
            selected_scenario_id is None or scenario.scenario_id == selected_scenario_id
        )
    ]
    rewards = []
    for scenario in trainable:
        if action_type == 2:       # BUY_XP
            rewards.append(scenario.reward_buy_xp)
        elif action_type == 6:     # PASS
            rewards.append(scenario.reward_pass)
        elif action_type == 1:     # REROLL
            rewards.append(scenario.reward_roll)
    # Scenarios overlap by design; use the strongest single matching signal
    # rather than summing bonuses and accidentally magnifying reward shaping.
    reward = max(rewards, key=lambda value: abs(value)) if rewards else 0.0
    return float(max(-0.08, min(0.08, reward))), [item.scenario_id for item in matched]
