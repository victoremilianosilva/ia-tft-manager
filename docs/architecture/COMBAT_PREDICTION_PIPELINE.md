# Combat prediction pipeline and economic evidence contract

## Previous problem

The combat runtime had an authoritative `CombatEngine`, but its input was not
persisted as a complete, identity-bound snapshot. Coverage was a placeholder,
and a completed simulation could be mistaken for a valid prediction even when
champion scripts, active trait effects, item passives, or other material
mechanics were missing.

The first evidence calibrator also treated a minimum sample count as
calibration, restricted observations to the target match, and did not preserve
a full calibration-report provenance chain into contextual evaluation.

## Technical rationale

Combat simulation is only a scenario generator. It is not a predictor of real
TFT outcomes until its input coverage and empirical calibration support that
claim. Unknown mechanics and unknown matchups must remain explicit. The
runtime must never invent opponent probabilities, fill missing champion data,
or convert a partial simulation into a valid economic signal.

Empirical calibration must generalize across independent matches within an
explicitly versioned cohort. Multi-round survival requires complete weighted
trajectories with explicit matchups and HP transitions; multiplying a
single-round mean is invalid.

## New responsibilities

- `CombatProjectionSnapshotBuilder` validates the full identity-bound
  `CombatInput`, team/player pairing, roster sizes, unit IDs, and board
  positions before projection.
- `CombatCoverageValidator::inspect` examines the actual simulator input:
  per-field unit provenance, ability metadata and unsupported ability features,
  active trait effect metadata, item effect metadata, and supported
  operation/trigger/target combinations. Engine fallbacks, incomplete
  provenance, malformed conditions, and unsupported effect combinations are
  unsupported rather than silently accepted.
- `CombatProjectionEngine` runs deterministic scenarios through the existing
  `CombatEngine`. It produces expected damage, P50/P90, sample values and
  uncertainty, but marks every result experimental and never decision-eligible
  until replay calibration approves it.
- `TftEngine::resolve_combats` emits `COMBAT_SNAPSHOT_V2` with the full
  simulator input, roster UUIDs, engine configuration, and measured coverage.
  It emits `COMBAT_OUTCOME_V1` with actual HP before/after and applied damage;
  the event is explicitly not calibration-eligible until replay infrastructure
  attaches immutable artifact and dataset identities.
- `CombatPredictionCalibrator::calibrate_for_cohort` uses independent matches
  and exact engine/composition/mechanics/round/horizon cohort identity. It
  rejects same-match leakage, duplicate match samples, mixed dataset versions,
  and insufficient independent matches. Multiple replay artifacts may belong
  to one immutable dataset version.
- `evaluate_calibration_predictions` joins experimental projection values
  with replay outcomes by match/player/round/sequence, rejects incomplete
  coverage and HP/provenance mismatches, verifies match- and replay-artifact-disjoint splits,
  and calculates held-out MAE, P90 coverage, and Brier score.
- `approve_calibration` requires an approved protocol, quantitative metrics,
  disjoint train/validation/test manifests, report and manifest hashes, and
  minimum sample counts. Sample count alone never promotes a distribution.
- `derive_survival_risk` derives next-combat risk from calibrated damage
  samples and observed HP. `derive_multi_round_survival_risk` requires
  complete, weighted trajectories with explicit opponent IDs, round/sequence,
  incoming damage, non-combat HP deltas, calibration report and replay
  provenance.
- `apply_to_economic_context`, `EconomicController`,
  `PlannerEvidenceAdapters`, and `ContextualActionEvaluator` preserve and
  validate source, calibration protocol/report, replay artifacts, dataset,
  horizon, sequence, and uncertainty.

## Callgraph and data flow

```text
TftEngine::resolve_combats
  -> append_combat_team
  -> CombatSnapshotBuilder + MatchupResolver
  -> CombatProjectionSnapshotBuilder
  -> CombatCoverageValidator::inspect
  -> COMBAT_SNAPSHOT_V2 event
  -> CombatEngine::simulate (authoritative environment outcome)
  -> COMBAT_OUTCOME_V1 event
  -> Replay Infrastructure (#518) attaches immutable replay/dataset identity
  -> CombatPredictionCalibrator::calibrate_for_cohort
  -> approve_calibration
  -> derive_survival_risk / derive_multi_round_survival_risk
  -> apply_to_economic_context
  -> EconomicController::evaluate
  -> PlannerEvidenceAdapters::economic
  -> ContextualActionEvaluator::evaluate / to_json
```

## Contracts and invariants

- Snapshot identity includes match, player, actual opponent, round,
  the decision and strategic-context sequences of both participants, the
  Engine decision sequence, observed HP and roster UUIDs. The canonical pair
  event can be oriented for either participant without guessing the opponent's
  sequence. The full CombatInput is retained as a simulator-input projection.
  The builder also rejects HP mismatches, non-deterministic or malformed
  simulator configuration, non-4x7 board geometry, invalid unit positions,
  and non-finite or out-of-range core unit statistics.
- The event distinguishes the authoritative Engine input projection from raw
  source values; catalog fallbacks are not relabeled as direct observations.
- Matchup resolution accepts only an actual opponent supplied by the lobby.
  No uniform or arbitrary future-opponent distribution is synthesized.
- Coverage is measured from mechanics and field provenance actually present
  in CombatInput. Missing champion ability metadata, active trait effect
  metadata, unknown/fallback simulator fields, or unsupported effect
  combinations make coverage partial/unsupported. Simulation completion does
  not override this status.
- The existing CombatEngine is the only simulator. The projection layer does
  not duplicate combat rules or mutate live game state.
- Projection output remains experimental and `decision_eligible=false`.
- A calibration cohort excludes the target match, requires distinct independent
  matches, exact cohort signatures, one dataset version and versioned replay
  artifacts.
- A calibrated risk carries report hash, protocol, dataset, replay artifacts,
  horizon, source sequence and uncertainty into economic consumers.
- Multi-round risk uses complete scenario trajectories with explicit weights,
  matchups and HP transitions. Incomplete or inconsistently sequenced
  trajectories are unavailable.
- Missing, unknown, partial, stale, unsupported and observed zero remain
  distinct states.
- PPO, reward, action dimensions, action masks, Engine legality and execution
  remain unchanged. The entire chain is Shadow/read-only.

## Current runtime limitations

The current `append_combat_team` path does not populate complete champion
ability metadata, active trait/item effect definitions, or every simulator
stat from an authoritative source. Several fields remain explicit engine
defaults or catalog fallbacks. The validator therefore marks current snapshots
partial/unsupported instead of claiming complete coverage. This is intentional
fail-closed behavior; the provenance strings preserve why each field is not
eligible.

The lobby resolves its actual opponent after the player decision cycle. It
does not currently expose a validated distribution over future opponents
before that cycle. The runtime consequently records the actual pair and its
outcome, but does not publish that post-decision simulation as a forecast for
the decision that already happened.

No real replay dataset or approved model calibration is present in this
implementation. The new replay cohort and approval contracts prepare that
path; they do not claim empirical accuracy.

## Impacts

- Adds read-only snapshot, projection, outcome and calibration contracts.
- Extends contextual output schema to version 5 with combat provenance.
- Makes economic consumption stricter: a numeric damage/risk value without
  approved provenance, matching sequence and explicit horizon is rejected.
- Does not activate damage/risk in current economic decisions because current
  runtime coverage and replay calibration are not sufficient.

## Validation criteria

- Snapshot builder rejects stale identities, wrong matchups, roster mismatch,
  duplicate unit IDs and invalid board positions.
- Coverage validator distinguishes complete from partial/unsupported input.
- Projection scenarios reuse CombatEngine and remain ineligible for economic
  consumption before calibration.
- Cohort calibration excludes target-match leakage, duplicate samples and
  mixed dataset versions while supporting multiple artifacts in one dataset.
- Calibration approval rejects unapproved protocols, invalid hashes,
  overlapping manifests, insufficient samples and out-of-threshold metrics.
- Single-round risk requires calibrated distribution and observed HP.
- Multi-round risk rejects missing steps, duplicate scenarios, invalid weights,
  mismatched round/sequence and incomplete provenance.
- EconomicController and contextual evaluation preserve and validate the
  calibration report, replay artifacts, horizon, sequence and uncertainty.
- Runtime emits full snapshot and factual outcome events with identity and
  mechanics coverage.
- No synthetic or partial result is published as valid evidence.

## Non-blocking empirical work

Replay collection, model training, quantitative calibration acceptance and
ablation require versioned datasets from #518. Under the project's agreed
merge rule, absence of those datasets/model is not a merge blocker. Until the
evidence exists, prediction remains experimental/unavailable and cannot
influence economic decisions.


## Field-level snapshot provenance

Every simulator unit now carries its source player-unit UUID and explicit
provenance for identity, star, board position, HP, max HP, attack damage,
attack speed, attack range, armor, magic resist, role, ability, items and
traits. Catalog combat-profile values, base catalog values, engine fallbacks,
and values derived for combat initialization remain distinguishable. Ability
name/description/level variables are preserved from the champion catalog, but
they do not mark the simulator mapping complete. Item and trait effect lists
also require explicit completeness flags; an empty or absent list is not
silently treated as “no effects”.

The snapshot serializes the UUID beside each unit, not only as a detached
roster list. The projection builder verifies that each simulator unit's UUID
matches the roster UUID at the same board-order index.

## Explicit candidate matchups

When the actual opponent is not available, `MatchupResolver::resolve_candidates`
accepts only an externally supplied candidate set with unique opponent IDs,
finite positive probabilities, and a total probability of one. An empty,
duplicate, incomplete, or non-normalized candidate set is unavailable.

`CombatProjectionEngine::project_matchups` runs each candidate through the
same CombatEngine and aggregates scenario damage using the supplied matchup
probabilities. It preserves each opponent and scenario weight in the output,
computes weighted expected damage/P50/P90, and includes matchup uncertainty.
It does not manufacture a uniform distribution. Results remain experimental
and ineligible for economic use until replay calibration is approved.

## Calibration cohort boundaries

Only cross-match cohort distributions can be promoted. The same-match
calibrator is retained for diagnostic summaries but emits
`experimental_same_match_diagnostic_distribution.v1`, which the approval
gate explicitly rejects. Cohort promotion requires exact engine,
composition/mechanics signature, round and single-round horizon; excludes the
target match; requires one independent sample per match; and permits multiple
replay artifacts only when they belong to the same immutable dataset version.
Multi-round risk is handled separately through complete weighted trajectories,
not through the single-round damage distribution.


## Item catalog completeness contract

The item adapter now carries an explicit `combat_effects_complete` assertion
from `ItemDefinition` into `CombatItem::effects_complete`. The default is
false: an empty vector is ambiguous and must not be interpreted as an
authoritative “no passive” declaration. The normalized JSON loader accepts this field only as a boolean and
rejects malformed values; omission preserves the conservative false default.
A set catalog loader may set the flag
true only after it has resolved the complete combat-relevant item metadata for
the active set, including an explicit empty effect list when the item truly has
no passive. This keeps coverage fail-closed and prevents an incomplete catalog
from silently qualifying an item for calibration.

Champion ability scripts are intentionally outside this change. Active trait
effect production and migration of all legacy item-name mechanics remain
separate implementation work; this PR does not claim those mechanics are
complete or replay-calibrated.

## Item completeness validation

- Adapter tests verify that missing metadata remains incomplete.
- Adapter tests verify that a catalog-declared complete effect list is copied
  without loss.
- Adapter tests verify that an explicitly complete empty list is distinct
  from missing metadata.
- Coverage validation continues to reject active traits whose effect metadata
  has not been explicitly populated.



## Native trait effect production

`TraitCombatCatalog` loads a versioned, set-scoped normalized catalog and
selects the highest tier whose minimum unit count is satisfied by the actual
active trait count. `TftEngine::append_combat_team` attaches those effects to
the factual trait instances before the combat input is built. Unknown traits,
missing tiers, inactive traits, and mismatched set catalogs remain incomplete.

The initial Set 18 mapping covers the Brawler health effects only. Its team
health contribution is divided across active Brawler sources so the team aura
is applied exactly once in aggregate; the trait's own health multiplier is
applied to Brawler units. This is not a claim that every Set 18 trait is
modeled. Other traits continue to fail closed until their full combat
semantics are normalized and tested.

## Native simulation trace versus authoritative replay

The lobby now emits `COMBAT_SIMULATION_REPLAY_V1` with the deterministic
native simulator input, set/trait/item effect metadata, simulator result
summary, stable artifact identity, and a versioned diagnostic dataset label.
The corresponding `COMBAT_OUTCOME_V1` references this simulation artifact
separately from the authoritative replay fields.

A native simulator trace is reproducible evidence about this simulator; it is
not an observed game replay. Therefore `replay_artifact_id` and the
authoritative `dataset_version` remain null, and
`calibration_eligible` remains false. Empirical calibration still requires
an authoritative replay collector/ingestor, immutable dataset manifests, and
held-out evaluation under the approved protocol.
