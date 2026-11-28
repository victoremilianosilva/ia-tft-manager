"""Causal provenance checks for native PPO reward components.

This module is audit-only: it never changes the scalar reward consumed by PPO.
Reward v1 keeps action shaping neutral and attributes delayed outcomes to their
authoritative native events; GAE remains responsible for temporal credit.
"""
from __future__ import annotations

import math
from typing import Any, Mapping, Sequence

import numpy as np


REWARD_AUDIT_CONTRACT_ID = "tft.ppo.reward-audit.v1"
REWARD_AUDIT_CONTRACT_VERSION = 1
_PLAYERS_PER_LOBBY = 8


def _reward_vector(name: str, values: Any) -> np.ndarray:
    try:
        vector = np.asarray(values, dtype=np.float64).reshape(-1)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} deve ser um vetor numérico.") from exc
    if vector.shape != (_PLAYERS_PER_LOBBY,):
        raise ValueError(
            f"{name} deve conter {_PLAYERS_PER_LOBBY} valores; "
            f"recebido shape={vector.shape}."
        )
    if not np.isfinite(vector).all():
        raise ValueError(f"{name} contém valor não finito.")
    return vector


class RewardAuditLedger:
    """Validates reward decomposition and deduplicates native outcome events."""

    def __init__(self, tolerance: float = 1e-5) -> None:
        if not math.isfinite(tolerance) or tolerance <= 0.0:
            raise ValueError("tolerance deve ser positivo e finito.")
        self._tolerance = float(tolerance)
        self._scope: tuple[str, int] | None = None
        self._seen_outcome_event_ids: set[str] = set()

    def reset(self, engine_instance_id: str, episode_id: int) -> None:
        engine = str(engine_instance_id).strip()
        episode = int(episode_id)
        if not engine or episode < 0:
            raise ValueError("Identidade de Engine/episódio inválida para reward audit.")
        self._scope = (engine, episode)
        self._seen_outcome_event_ids.clear()

    def build_record(
        self,
        *,
        rewards: Any,
        action_rewards: Any,
        combat_rewards: Any,
        placement_rewards: Any,
        action_traces: Sequence[Mapping[str, Any]],
        action_outcome_events: Sequence[Mapping[str, Any]],
        players: Sequence[Mapping[str, Any]],
        decision_snapshot: Mapping[str, Any],
        source_decision_snapshot: Mapping[str, Any],
    ) -> dict[str, Any]:
        if self._scope is None:
            raise RuntimeError("RewardAuditLedger precisa ser resetado antes do step.")

        engine_id = str(decision_snapshot.get("engine_instance_id", "")).strip()
        episode_id = int(decision_snapshot.get("episode_id", -1))
        decision_sequence = int(decision_snapshot.get("decision_sequence", -1))
        player_sequences = decision_snapshot.get("player_decision_sequences")
        native = decision_snapshot.get("native_state_snapshot")
        if (engine_id, episode_id) != self._scope:
            raise RuntimeError("Reward audit recebeu identidade de outro episódio.")
        if decision_sequence <= 0 or not isinstance(native, Mapping):
            raise RuntimeError("Snapshot de reward sem identidade nativa válida.")
        if (
            str(native.get("engine_instance_id", "")) != engine_id
            or int(native.get("episode_id", -1)) != episode_id
            or int(native.get("snapshot_sequence", -1)) != decision_sequence
            or int(native.get("round", -1)) != int(decision_snapshot.get("round", -2))
        ):
            raise RuntimeError("Reward audit e snapshot nativo estão desalinhados.")
        if not isinstance(player_sequences, Sequence) or len(player_sequences) != _PLAYERS_PER_LOBBY:
            raise RuntimeError("Sequências de decisão por jogador inválidas.")
        native_player_sequences = native.get("player_decision_sequences")
        if (
            not isinstance(native_player_sequences, Sequence)
            or list(map(int, native_player_sequences)) != list(map(int, player_sequences))
        ):
            raise RuntimeError("Reward audit e sequências nativas por jogador estão desalinhados.")

        source_engine_id = str(source_decision_snapshot.get("engine_instance_id", "")).strip()
        source_episode_id = int(source_decision_snapshot.get("episode_id", -1))
        source_sequence = int(source_decision_snapshot.get("decision_sequence", -1))
        source_player_sequences = source_decision_snapshot.get("player_decision_sequences")
        source_native = source_decision_snapshot.get("native_state_snapshot")
        if (source_engine_id, source_episode_id) != (engine_id, episode_id):
            raise RuntimeError("Snapshot pré-ação pertence a outra Engine/episódio.")
        if (
            source_sequence < 0 or source_sequence >= decision_sequence
            or not isinstance(source_native, Mapping)
            or int(source_native.get("snapshot_sequence", -1)) != source_sequence
            or str(source_native.get("engine_instance_id", "")) != engine_id
            or int(source_native.get("episode_id", -1)) != episode_id
            or int(source_native.get("round", -1)) != int(source_decision_snapshot.get("round", -2))
        ):
            raise RuntimeError("Snapshot pré-ação sem identidade nativa correlacionada.")
        source_native_sequences = source_native.get("player_decision_sequences")
        if (
            not isinstance(source_player_sequences, Sequence)
            or len(source_player_sequences) != _PLAYERS_PER_LOBBY
            or not isinstance(source_native_sequences, Sequence)
            or list(map(int, source_native_sequences)) != list(map(int, source_player_sequences))
        ):
            raise RuntimeError("Sequências do snapshot pré-ação estão desalinhadas.")
        if not isinstance(action_traces, Sequence) or len(action_traces) != _PLAYERS_PER_LOBBY:
            raise RuntimeError("Action traces incompletos para reward audit.")
        if not isinstance(action_outcome_events, Sequence) or len(action_outcome_events) != _PLAYERS_PER_LOBBY:
            raise RuntimeError("ActionOutcomeEvent nativo incompleto para reward audit.")
        if not isinstance(players, Sequence) or len(players) != _PLAYERS_PER_LOBBY:
            raise RuntimeError("Player facts incompletos para reward audit.")

        total = _reward_vector("rewards", rewards)
        action = _reward_vector("action_rewards", action_rewards)
        combat = _reward_vector("combat_rewards", combat_rewards)
        placement = _reward_vector("placement_rewards", placement_rewards)
        if not np.allclose(total, action + combat + placement, rtol=0.0, atol=self._tolerance):
            raise ValueError("Reward total diverge da soma action + combat + placement.")
        if np.any(np.abs(action) > self._tolerance):
            raise ValueError(
                "Reward Contract v1 exige action_reward neutro; "
                "um novo shaping exige novo contrato versionado."
            )

        combat_sequence = int(native.get("combat_sequence", 0))
        round_number = int(decision_snapshot.get("round", native.get("round", 0)))
        pending_event_ids: list[str] = []
        player_records: list[dict[str, Any]] = []

        for player_id in range(_PLAYERS_PER_LOBBY):
            trace = action_traces[player_id]
            action_event = action_outcome_events[player_id]
            player = players[player_id]
            if not isinstance(trace, Mapping) or int(trace.get("player_id", -1)) != player_id:
                raise RuntimeError(f"Action trace desalinhado para player_id={player_id}.")
            if not isinstance(player, Mapping) or int(player.get("player_id", -1)) != player_id:
                raise RuntimeError(f"Player facts desalinhados para player_id={player_id}.")
            if not isinstance(action_event, Mapping):
                raise RuntimeError(f"ActionOutcomeEvent inválido para player_id={player_id}.")
            if (
                action_event.get("contract_id") != "tft.engine.action-outcome-event"
                or int(action_event.get("contract_version", 0)) != 1
                or action_event.get("engine_instance_id") != engine_id
                or int(action_event.get("episode_id", -1)) != episode_id
                or int(action_event.get("player_id", -1)) != player_id
            ):
                raise RuntimeError(f"ActionOutcomeEvent sem identidade nativa para player_id={player_id}.")
            outcome_player_sequence = int(player_sequences[player_id])
            player_sequence = int(source_player_sequences[player_id])
            if player_sequence < 0 or outcome_player_sequence <= player_sequence:
                raise RuntimeError(f"Sequência pré/pós-ação inválida para player_id={player_id}.")
            expected_action_event_id = (
                f"{engine_id}/episode/{episode_id}/decision/{player_sequence}/player/{player_id}/action"
            )
            if (
                int(action_event.get("source_player_decision_sequence", -1)) != player_sequence
                or int(action_event.get("outcome_player_decision_sequence", -1)) != outcome_player_sequence
                or action_event.get("event_id") != expected_action_event_id
                or not isinstance(action_event.get("mask_permitted"), bool)
                or action_event.get("preflight_accepted") is not True
                or action_event.get("decision_advanced") is not True
                or not isinstance(action_event.get("execution_status"), str)
                or not action_event.get("execution_status", "").strip()
                or not isinstance(action_event.get("handler_applied"), bool)
                or not isinstance(action_event.get("status_reason"), str)
                or not action_event.get("status_reason", "").strip()
                or action_event.get("requested_action") != trace.get("requested_action")
                or action_event.get("effective_action") != trace.get("effective_action")
                or action_event.get("normalized_action") != action_event.get("requested_action")
            ):
                raise RuntimeError(f"ActionOutcomeEvent desalinhado ou incompleto para player_id={player_id}.")
            affected_entities = action_event.get("affected_unit_uuids")
            if not isinstance(affected_entities, Sequence) or isinstance(affected_entities, (str, bytes)):
                raise RuntimeError(f"ActionOutcomeEvent sem referências de entidade válidas para player_id={player_id}.")
            expected_execution_status = (
                "applied" if action_event["handler_applied"] else
                ("not_processed" if action_event["status_reason"] == "player_eliminated" else
                 ("partial" if len(affected_entities) else "no_effect"))
            )
            if action_event["execution_status"] != expected_execution_status:
                raise RuntimeError(f"Status de execução inconsistente para player_id={player_id}.")
            event_id = str(action_event["event_id"])
            if event_id in self._seen_outcome_event_ids:
                raise RuntimeError("Reward audit detectou ActionOutcomeEvent repetido: " + event_id)
            pending_event_ids.append(event_id)

            combat_value = float(combat[player_id])
            placement_value = float(placement[player_id])
            combat_event = None
            placement_event = None

            if abs(combat_value) > self._tolerance:
                if combat_sequence <= 0:
                    raise RuntimeError("Combat reward sem combat_sequence autoritativa.")
                event_id = (
                    f"{engine_id}/episode/{episode_id}/combat/"
                    f"{combat_sequence}/player/{player_id}"
                )
                combat_event = {
                    "event_id": event_id,
                    "source": "native_pvp_resolution",
                    "combat_sequence": combat_sequence,
                    "round": round_number,
                    "reward": combat_value,
                }
                pending_event_ids.append(event_id)

            if abs(placement_value) > self._tolerance:
                raw_placement = player.get("placement")
                if raw_placement is None:
                    raise RuntimeError(
                        f"Placement reward sem colocação validada para player_id={player_id}."
                    )
                final_placement = int(raw_placement)
                if not 1 <= final_placement <= _PLAYERS_PER_LOBBY:
                    raise RuntimeError("Colocação fora do intervalo válido.")
                event_id = (
                    f"{engine_id}/episode/{episode_id}/placement/player/{player_id}"
                )
                placement_event = {
                    "event_id": event_id,
                    "source": "validated_terminal_placement",
                    "placement": final_placement,
                    "reward": placement_value,
                }
                pending_event_ids.append(event_id)

            player_records.append({
                "player_id": player_id,
                "player_decision_sequence": player_sequence,
                "outcome_player_decision_sequence": outcome_player_sequence,
                "action_decision": {
                    "source": "native_action_outcome_event",
                    "event": dict(action_event),
                    "source_snapshot_sequence": source_sequence,
                    "player_decision_sequence": player_sequence,
                    "outcome_snapshot_sequence": decision_sequence,
                    "outcome_player_decision_sequence": outcome_player_sequence,
                    "trace": dict(trace),
                    "reward": float(action[player_id]),
                },
                "combat_outcome": combat_event,
                "terminal_placement": placement_event,
                "components": {
                    "action": float(action[player_id]),
                    "combat": combat_value,
                    "placement": placement_value,
                    "total": float(total[player_id]),
                },
            })

        if len(pending_event_ids) != len(set(pending_event_ids)):
            raise RuntimeError("Reward audit encontrou evento duplicado no mesmo StepResult.")
        duplicates = self._seen_outcome_event_ids.intersection(pending_event_ids)
        if duplicates:
            raise RuntimeError(
                "Reward audit detectou crédito repetido para evento nativo: "
                + ", ".join(sorted(duplicates))
            )

        self._seen_outcome_event_ids.update(pending_event_ids)
        return {
            "contract_id": REWARD_AUDIT_CONTRACT_ID,
            "contract_version": REWARD_AUDIT_CONTRACT_VERSION,
            "engine_instance_id": engine_id,
            "episode_id": episode_id,
            "source_decision_sequence": source_sequence,
            "decision_sequence": decision_sequence,
            "source_round": int(source_decision_snapshot.get("round", 0)),
            "round": round_number,
            "temporal_credit_owner": "per_player_gae",
            "player_rewards": player_records,
        }
