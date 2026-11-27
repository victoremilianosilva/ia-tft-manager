# Native Decision Context

## Ownership and correlation

`NativeDecisionBatch.native_context(lobby_index)` returns a typed C++ context backed by the exact immutable `AuditSnapshot` captured with the lobby's observation and action masks. The batch retains the same `shared_ptr<const AuditSnapshot>` already created by `NativeAuditSnapshotHandle`; it does not create a second snapshot copy or query the champion pool independently.

The context exposes one shared pool per lobby and eight player records. Each player record is selected by stable seat index and retains the original board (28 slots), bench (9 slots), and shop (5 slots), including unoccupied slots, catalog IDs, physical UUIDs, static trait membership, stats, equipped-item ownership, item inventory, pending anvil data and native strategic-owner state.

## Explicit availability

`ContextAvailability` distinguishes `complete`, `partial`, `empty`, `unknown`, `missing`, `stale`, `incompatible` and `not_applicable`. The initial field classifiers cover strategic planner output, item inventory and pending anvil state. A default numeric zero is never used as the availability signal.

- Strategic outputs without a valid planner publication are `unknown`.
- Empty item collections are `empty` only when the item catalog is present; otherwise they are `unknown`.
- No pending anvil with no pending sequence/options is `not_applicable`; inconsistent pending data is `incompatible` or `partial`.
- A strategic record with mismatched player, episode, round or decision sequence is rejected as stale/incoherent at context construction.

## Traits and identity

Trait counts are derived in native code from the exact static catalog membership on occupied board and bench copies. The API reports `board_count`, `bench_count` and `board_bench_count` separately, deduplicating repeated trait names within a single unit. Item-granted trait ownership is explicitly `unknown` because the current engine snapshot does not publish that producer independently.

Champion catalog identity and physical unit UUID remain separate. Strategic priority/progress/opportunity-cost data remains keyed to champion identity when that is the producer's granularity; the context does not attach aggregate values to a physical UUID.

## Consumer API

The Python binding exposes:
- `NativeDecisionBatch.native_context(lobby_index)`;
- context identity/provenance and shared pool;
- `player(index)` for one player at a time;
- `trait_counts(player_index)` with explicit scopes;
- strategic, item-inventory and pending-anvil availability classifiers.

Player item arrays returned from the context are pinned to the context owner, so they remain valid while the returned views retain that owner. The context does not expose mutable references.

## Boundaries

The context transports authoritative facts. It does not promote shadow proposals, evaluator scores, diagnostic sidecars, uncommitted planner candidates, projected income, calibrated pressure/confidence, or synthetic item/anvil instance IDs into observations. Fields without an authoritative producer remain explicitly unknown or not applicable.

This is a structured transport API; it does not change the v8 neural feature order or turn audit-only values into PPO inputs. The semantic projection remains the separately versioned v8 contract.
