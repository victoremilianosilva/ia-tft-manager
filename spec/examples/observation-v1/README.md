# Observation Schema v1 draft fixtures

These files are examples for the draft under `spec/observation-schema.v1.draft.json`.

- `valid-minimal.json`: structurally valid minimal snapshot fixture. It includes a zero-valued observed XP field, explicit empty slots, a complete engine identity, and a valid mask/critic reference.
- `invalid-missing-reason.json`: intentionally invalid because `player.health.status=missing` has no `reason`.
- `field-status-matrix.json`: examples of the `$defs.field` value states, including zero observed, missing, unknown, not applicable, stale, incompatible, partial, and estimated.

**Hash note:** fixture hash strings are placeholders. The contract validation script replaces the schema and projection placeholders with RFC 8785 canonical SHA-256 values before validating the fixture. Catalog fingerprints remain externally supplied identifiers; their content/order must be verified by the catalog owner at runtime.

**Validation:** `scripts/validate_observation_schema.py` is run by the dedicated GitHub Actions workflow. It checks the Draft 2020-12 meta-schema, validates the valid and invalid snapshots, exercises every field-status case, and tests zero-versus-missing, incomplete identity, occupied-slot constraints, and schema/projection hash integrity. A green CI run is required before this draft can be approved.

This remains a draft: CI proves the machine-readable contract and its fixtures, not runtime producer/consumer alignment or architectural approval.
