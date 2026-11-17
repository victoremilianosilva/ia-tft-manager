# Observation Schema v1 fixtures

These files are validation examples for the machine-readable contract at `spec/observation-schema.v1.draft.json`. The filename retains its historical `draft` suffix; the schema is an **approved documentary specification**. Runtime producer/consumer migration and executable acceptance remain pending until Gate 8 and explicit authorization.

- `valid-minimal.json`: structurally valid minimal snapshot fixture. It includes a zero-valued observed XP field, explicit empty slots, a complete engine identity, and a valid mask/critic reference.
- `invalid-missing-reason.json`: intentionally invalid because `player.health.status=missing` has no `reason`.
- `field-status-matrix.json`: examples of the `$defs.field` value states, including zero observed, missing, unknown, not applicable, stale, incompatible, partial, and estimated.

**Hash note:** fixture hash strings are placeholders. The contract validation script replaces the schema and projection placeholders with RFC 8785 canonical SHA-256 values before validating the fixture. Catalog fingerprints remain externally supplied identifiers; their content/order must be verified by the catalog owner at runtime.

**Structural validation:** `scripts/validate_observation_schema.py` is run by the dedicated GitHub Actions workflow. It checks the Draft 2020-12 meta-schema, validates the valid and invalid snapshots, exercises every field-status case, and tests zero-versus-missing, incomplete identity, occupied-slot constraints, and schema/projection hash integrity. A green CI run proves these structural checks for the tested revision only. It does not grant architectural approval or prove runtime producer/consumer alignment.

**Strategic ownership boundary:** the fixture/schema represents planner commitment, Composition Intelligence active state, and UnifiedStrategicStateMachine as distinct streams, each with its own availability and source sequence. This preserves their separate identities; it does not select or create a competing global authority. Canonical ownership is defined by the approved Strategic Ownership and Integration Contract.

**Decision identity and masks:** the decision identity hash is computed over match_id, engine_match_id, player_id, round, decision_sequence and snapshot_sequence. The mask reference must carry the same hash. A complete anti-loop context includes position history, move history, blocked move records and state visits; an incomplete aggregate legal context must be marked partial with a reason. The critic receives exact masks as a separate Action/Mask Contract side input, never as a replacement for Engine legality.

The source map covers all 97 typed-field references and the legacy crosswalk covers exactly 66/66 inventoried features.

## Status and gate boundary

- Documentary Observation Schema v1 approval: complete.
- Machine-readable schema and fixture validation: established by the dedicated workflow for the revision it tests.
- Runtime producer/consumer alignment, tensor projection implementation, and executable acceptance: pending Gate 8 and explicit authorization.
- The schema and fixtures do not authorize changes to observations, PPO, masks, training, checkpoints, Engine, or Viewer.

## Architecture reconstruction review

1. **Prior problem:** this README described documentary approval as pending even though Gate 1 and the schema's documentary specification had been approved. It also said the three strategic streams did not select a global authority without pointing to the separate contract that defines canonical ownership.
2. **Technical rationale:** structural fixture validation, documentary approval, and runtime conformance are independent forms of evidence and must not be conflated. Strategic stream identity must remain distinct while canonical ownership is resolved by its dedicated contract.
3. **New responsibility:** this README explains fixture purpose, structural validation scope, and status boundaries only. The Observation Schema owns the semantic data contract; the Strategic Ownership and Integration Contract owns canonical strategic authority; runtime components own executable conformance.
4. **Contract and invariants:** a green fixture-validation workflow proves only schema/fixture checks for that revision; it does not prove runtime alignment. Distinct strategic snapshots remain separately identified and sequenced; this README cannot redefine ownership.
5. **Cross-component impact:** documentation navigation and interpretation for Observation Schema, strategic ownership, PPO projection, and Gate 1. No schema fields, projection definitions, runtime producers/consumers, masks, or checkpoints are changed.
6. **Objective validation:** compare the revised status with Gate 1/#293 and the approved ownership contract; run the existing schema/fixture workflow; verify that no schema or fixture file changed. Runtime acceptance remains explicitly post-Gate 8.
