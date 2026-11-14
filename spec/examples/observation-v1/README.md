# Observation Schema v1 draft fixtures

These files are examples for the draft under `spec/observation-schema.v1.draft.json`.

- `valid-minimal.json`: structurally valid minimal snapshot fixture. It includes a zero-valued observed XP field, explicit empty slots, a complete engine identity, and a valid mask/critic reference.
- `invalid-missing-reason.json`: intentionally invalid because `player.health.status=missing` has no `reason`.
- `field-status-matrix.json`: examples of the `$defs.field` value states, including zero observed, missing, unknown, not applicable, stale, incompatible, partial, and estimated.

**Hash note:** the `sha256:000...` and `sha256:111...` strings are syntactically valid placeholders used to demonstrate the shape only. They are not computed hashes for the example payloads or catalogs. A real producer/loader must compute and verify canonical hashes according to the schema's hash scope and RFC 8785 rules.

**Validation note:** the fixtures have been parsed as JSON and checked with basic structural assertions. They have not yet been run through an official JSON Schema Draft 2020-12 validator or the C++/Python contract tests. Do not treat this draft as approved or production-ready.
