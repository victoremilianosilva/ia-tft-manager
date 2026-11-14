# Observation Schema v1 draft fixtures

These files are examples for the draft under `spec/observation-schema.v1.draft.json`.

- `valid-minimal.json`: structurally valid minimal snapshot fixture. It includes a zero-valued observed XP field, explicit empty slots, a complete engine identity, and a valid mask/critic reference.
- `invalid-missing-reason.json`: intentionally invalid because `player.health.status=missing` has no `reason`.
- `field-status-matrix.json`: examples of the `$defs.field` value states, including zero observed, missing, unknown, not applicable, stale, incompatible, partial, and estimated.

**Hash note:** fixture hash strings are placeholders. The contract validation script replaces the schema and projection placeholders with RFC 8785 canonical SHA-256 values before validating the fixture. Catalog fingerprints remain externally supplied identifiers; their content/order must be verified by the catalog owner at runtime.

**Validation:** `scripts/validate_observation_schema.py` is run by the dedicated GitHub Actions workflow. It checks the Draft 2020-12 meta-schema, validates the valid and invalid snapshots, exercises every field-status case, and tests zero-versus-missing, incomplete identity, occupied-slot constraints, and schema/projection hash integrity. A green CI run is required before this draft can be approved.

Three independent strategic owners are represented separately: planner commitment, Composition Intelligence active state, and UnifiedStrategicStateMachine. Each carries its own availability and source sequence; this does not select a global authority.\n\nThe decision identity hash is computed over match_id, engine_match_id, player_id, round, decision_sequence and snapshot_sequence. The mask reference must carry the same hash. A complete anti-loop context includes position history, move history, blocked move records and state visits; an incomplete aggregate legal context must be marked partial with a reason. The critic receives exact masks as a separate Action/Mask Contract side input, never as a replacement for Engine legality.\n\nThe source map covers all 97 typed-field references and the legacy crosswalk covers exactly 66/66 inventoried features.\n\nThis remains a draft: CI proves the machine-readable contract and its fixtures, not runtime producer/consumer alignment or architectural approval.
