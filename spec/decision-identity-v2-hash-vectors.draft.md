# Decision Identity v2 — RFC 8785 SHA-256 Test Vectors

**Status:** documentary test vectors for the proposed `tft.decision-identity.v2` envelope.  
**Canonicalization:** RFC 8785 JSON Canonicalization Scheme (JCS), UTF-8 bytes, then SHA-256.  
**Prefix:** lowercase hexadecimal digest prefixed by `sha256:`.

The hash input contains exactly:
`identity_version`, `match_id`, `engine_match_id`, `player_id`, `round`, `decision_sequence.namespace`, `decision_sequence.value`, `snapshot_sequence.namespace`, `snapshot_sequence.value`.

The hash field, status, reason, timestamps, episode/session metadata, payload contents, masks, catalogs and policy metadata are excluded.

## Complete identity — baseline

Input object:

```json
{
  "identity_version": "tft.decision-identity.v2",
  "match_id": "match-001",
  "engine_match_id": "engine-match-001",
  "player_id": "player-2",
  "round": 12,
  "decision_sequence": {"namespace": "tft.engine.decision", "value": 184},
  "snapshot_sequence": {"namespace": "tft.engine.observation-snapshot", "value": 184}
}
```

Canonical UTF-8 JSON bytes (shown as text; no trailing newline):

```text
{"decision_sequence":{"namespace":"tft.engine.decision","value":184},"engine_match_id":"engine-match-001","identity_version":"tft.decision-identity.v2","match_id":"match-001","player_id":"player-2","round":12,"snapshot_sequence":{"namespace":"tft.engine.observation-snapshot","value":184}}
```

Expected digest: `sha256:db10775d5ce64a663a883591ba0303cf5da362b5b7719577216c0a0851d0c3bf`

## Mutation vectors

Each vector changes exactly one identity property from the baseline. The machine-readable companion `decision-identity-v2-hash-vectors.draft.json` includes the exact canonical UTF-8 bytes and expected digest for every vector, making each result independently reproducible.

| Case | Mutation | Expected digest |
|---|---|---|
| Different decision namespace, same value | `decision_sequence.namespace=tft.ci.player-sequence` | `sha256:1e61f3e46fc41ef8e06e788c8c8d877f4d7de3aa0a329f2676534566af1f2641` |
| Different match | `match_id=match-002` | `sha256:377850c58f27ba34fa1a73804e8631309e55b2c9fba45634f73ae681a20d04f1` |
| Different player | `player_id=player-3` | `sha256:9110083c919dfcf84f6eadfd607c20f4e0b6c98ee83549c0e4fba449bd1eeaa7` |
| Different round | `round=13` | `sha256:8dd34fc7be4c187df9a4762614116c8aa181ee0173ab3e1b81f1ba2678baf6eb` |
| Different snapshot namespace, same value | `snapshot_sequence.namespace=tft.viewer.session-sequence` | `sha256:8ff8e0a07808a6717e328a05f79ae55c2fb4e9dffe4339bf6c74d4610a1dc489` |
| New Engine match scope after reset | `engine_match_id=engine-match-002` | `sha256:19a52a24bb95bba9c187074618a92df26cf3e503e976e6f37f870a6ad2a0fe4a` |

## Incomplete identity

If any required complete-identity field is absent, null, invalid, stale, unsupported or conflicting, the envelope status must not be `complete`, `reason` is required, and `decision_identity_hash` is null. No canonical bytes or digest are produced for an incomplete identity.

## Required executable validation later

After Gate 8 and explicit authorization, runtime tests must:
- canonicalize the exact hash input with a conforming RFC 8785 implementation;
- verify all expected digests above;
- verify object key order and insignificant whitespace do not change the digest;
- verify changing either namespace changes the digest even when numeric values remain equal;
- verify payload-content changes do not change decision identity hash but do change their independent payload hashes;
- reject incomplete/unknown namespace/stale/mismatched/conflicting identities;
- verify reset changes Engine match scope and rejects delayed prior-match payloads.

These are expected values for tests, not evidence that current runtime producers compute or transport the v2 identity.
