# Decision and Anti-Loop History Scope Audit v1 — Draft

**Status:** source-backed static audit; documentation only.  
**Tracking:** [Issue #346](https://github.com/victoremilianosilva/ia-tft-manager/issues/346).  
**Base:** `new-arquiteture`.  
**Related:** [Native Engine Instance and Episode Identity Scope Audit](native-engine-instance-episode-identity-scope-audit.v1.draft.md); [PPO Evaluation Protocol](ppo-evaluation-protocol.v1.draft.md).

## 1. Purpose

Trace the native decision/anti-loop history, per-player action counters, recent-purchase credit-assignment records and temporal observation features. Determine which are actual ordered history, which are bounded local state or reward bookkeeping, and which reach PPO.

Documentation only; no decision engine, masks, observation, reward, PPO or runtime changes.

## 2. AntiLoopEngine history model

The native `AntiLoopEngine` owns an `AntiLoopHistory` containing:
- `position_history`: bounded sequence of board/bench position signatures;
- `move_history`: bounded successful movement records;
- `blocked_moves`: bounded move keys paired with the board signature at which they were blocked;
- `state_visits`: position signatures, visit count, repeated flag and last-seen round;
- an index for state visits;
- last board signature and last move;
- execution/mask diagnostics metrics;
- current round and an eight-round state-visit retention window.

A `PositionSignature` is an exact board/bench array of optional `UnitIdentity`. A `UnitIdentity` prefers UUID when present and also includes star tier in equality; otherwise it compares catalog/numeric identity and star. This is state identity for anti-loop comparison, not a decision or episode identity.

A `MoveRecord` stores move type, source slot, target slot, moved unit identity and optional displaced unit identity. It does not store an action ID, decision sequence, timestamp, episode ID or player ID. The AntiLoopEngine instance is held inside one `PlayerEnv`, so player scope is implicit in object ownership rather than encoded in each record.

## 3. History mutation and retention

### 3.1 Successful moves and blocked moves

Native BUY/MOVE execution calls the AntiLoopEngine in the real action path:
- execution attempts are recorded for movement attempts;
- invalid/looping movement can create a blocked-move record and increment block metrics;
- successful board/bench movement records a `MoveRecord` and movement metrics;
- mask generation performs anti-loop queries and accumulates mask diagnostics, but query methods are documented as side-effect-free for history.

Only successful moves enter `move_history`; blocked candidates live separately. This is not a complete record of all decisions/actions taken by the player.

### 3.2 Round boundary

`begin_round(round_number)`:
- updates the current round;
- clears position history for the current preparation;
- retains at most the latest six movement records across round boundaries;
- clears blocked moves;
- restores last move from the retained movement tail;
- clears last board signature;
- expires state visits older than the configured eight-round window and rebuilds the index.

This is intentionally cross-round movement memory, not an episode-global immutable event log.

### 3.3 Episode reset

`AntiLoopEngine::reset()` replaces history with a fresh `AntiLoopHistory`, but preserves accumulated execution/mask metrics and the configured state-window length. Engine player initialization invokes this reset for each player at episode start. Therefore:
- movement/state/block history is episode-local and cleared;
- metrics survive across episode resets for the lifetime of the PlayerEnv's AntiLoopEngine object;
- records themselves carry no episode identity or sequence namespace.

The distinction between episode-local state and lifetime-accumulated metrics must be preserved in any future telemetry contract.

## 4. Other temporal/action bookkeeping is not decision history

### 4.1 Per-player `action_serial` and `recent_purchases`

The Engine maintains a per-player `action_serial` incremented in the native PlayerEnv action path and a bounded-by-age `recent_purchases` vector. A purchase record includes physical unit UUID, champion ID, star tier, action serial, cost, pair/upgrade flags and reward/composition bookkeeping.

These records support purchase→deployment/sale and reward credit-assignment logic. They are not a complete action history:
- they track selected purchase events, not every action;
- they are removed after the configured recent-purchase action horizon;
- `action_serial` resets to zero at episode initialization;
- neither record nor serial includes Engine-instance scope, episode ID, player ID or a globally typed decision ID;
- they are not emitted as a typed ordered history input to PPO.

### 4.2 PPO temporal observation features

The current native observation contains a dedicated temporal block with:
- normalized actions remaining/used in the current round, derived from `actions_taken_this_round`;
- normalized age of each board-slot occupant, derived from `board_move_age`.

These are bounded scalar temporal summaries. They are not the AntiLoopEngine's movement records, state-visit history, recent purchases or action event sequence. They do not identify which decisions caused the current state.

The PPO observation therefore has limited temporal context, but not a typed decision-history entity.

## 5. Producer-to-PPO boundary

| Surface | Current status | Identity/sequence semantics |
|---|---|---|
| AntiLoop position/move/block history | Native internal state | No explicit episode/player/decision IDs in records |
| AntiLoop metrics | Exposed as diagnostics through native API | Counters accumulate across episode reset; not decision events |
| Mask diagnostics | Native metrics aggregated during mask generation | Counts, not ordered candidate/decision records |
| `action_serial` | Native reward bookkeeping | Per-player action counter; reset per episode; no Engine scope |
| `recent_purchases` | Native reward bookkeeping | Purchase-only, short horizon, physical UUID + action serial |
| PPO temporal feature block | Native observation → PPO flat vector | Bounded scalar summaries only |
| PPO rollout | Stores observation/action/reward/done/masks | No typed ordered decision history or source identity envelope |

The current action masks remain independent legality inputs. Anti-loop history influences legality/mask generation and native movement validation; it is not itself a replacement for action masks and must not be collapsed into the PPO temporal features.

## 6. Field status and contract gaps

- Position signatures: **native observed/internal**, player-scoped by owning AntiLoopEngine; no explicit episode field.
- Successful movement records: **native observed/internal**, bounded and not individually decision-sequenced; the separate #475 JSONL stream records correlated MoveRegistered/MoveSucceeded events.
- Blocked movement records: **native derived/internal**, tied to a board signature; the operational record has no decision ID, while the separate #475 MoveBlocked event carries decision identity.
- State visit counts: **native derived/internal**, round-windowed.
- Execution/mask metrics: **native derived diagnostics**, lifetime-accumulated across episode reset.
- Recent purchase records: **native derived reward bookkeeping**, purchase-only and horizon-limited.
- Action serial: **native derived control metadata**, per player and reset each episode.
- PPO temporal scalars: **native derived and delivered**, but not lossless history.
- Typed ordered decision history delivered to Actor/Critic: **not delivered to PPO**. A bounded typed diagnostic event tail is exposed separately through pybind (#475).
- Explicit linkage: operational AntiLoop records remain uncorrelated to a decision envelope; #475 JSONL events are correlated to Engine/episode/player/decision sequence, but are not linked into Viewer or PPO rollout.

## 7. Required post-Gate-8 acceptance

1. Keep AntiLoop legality state, temporal observation summaries, reward-credit bookkeeping and any future decision history as distinct semantic surfaces.
2. Before any typed history is promoted beyond diagnostics, define event completeness, source sequence, horizon, reset/stale behavior and exact Actor/Critic/replay consumers; #475 is a bounded diagnostic subset, not a complete action history.
3. Preserve Engine scope, episode, player and decision identity for every #475 JSONL event; do not imply that the operational AntiLoop state records carry those fields.
4. Distinguish the JSONL event kinds (state observed, move registered, move blocked, move succeeded); do not interpret them as a complete record of all player actions.
5. Bind any history-derived observation to the same immutable observation/mask decision envelope.
6. Preserve the existing independent native masks as the final legality authority.
7. Test round boundary, episode reset, consecutive episodes, same-seed UUID repetition, player isolation, bounded eviction and metrics accumulation.
8. Prove Actor/Critic delivery separately; do not infer it from native diagnostic exposure or the existence of scalar temporal features.

No runtime implementation or tensor-layout decision is authorized by this audit.

## 8. Architecture reconstruction review

1. **Prior problem:** the schema/source audit identified decision-history gaps, but AntiLoop history, reward purchase bookkeeping and scalar temporal observations needed to be separated by actual producer and lifecycle.
2. **Technical justification:** these systems have different event inclusion, retention, reset and consumer semantics; treating them as one history would invent completeness and causal sequence that the code does not provide.
3. **New responsibility:** this note owns the native anti-loop and temporal-history source map, including the distinction between movement history, reward bookkeeping and PPO scalar summaries.
4. **Contract and invariants:** operational AntiLoop state is episode-local while metrics accumulate; recent purchases are not all actions; scalar temporal features are not typed history; the #475 JSONL stream is bounded and per-event decision-correlated but diagnostic-only.
5. **Cross-component impacts:** AntiLoopEngine, DecisionHistory, PlayerEnv, action masks, reward credit assignment, observation builder, pybind diagnostics, PPO Actor/Critic and RolloutBuffer.
6. **Objective validation:** history structures, mutation callsites, round/episode reset behavior, recent-purchase fields and temporal observation projection are source-traced; all surfaces have explicit status; no runtime/tensor changes are made.

Issue #346 remains open. Gate 7 executable acceptance remains pending. Gate 8 remains blocked.


## 9. Post-#475 correction — separate sequence-bound diagnostic stream

PR #475 added a second, deliberately separate surface:

- AntiLoopHistory::temporal_events retains up to 64 typed events (StateObserved, MoveRegistered, MoveBlocked, MoveSucceeded).
- Every exported event carries Engine instance, episode, player, per-player decision sequence and round identity.
- TFTEngine::get_anti_loop_history_jsonl() serializes the bounded event tail as JSONL, and pybind exposes it through get_anti_loop_history_jsonl.
- This stream is not part of AuditSnapshot, ResetResult/StepResult structured state, PPO observations, Actor/Critic inputs, or action masks.
- It is not equivalent to position_history, move_history, blocked_moves or state_visits: those operational structures answer anti-loop queries and have their own retention/reset behavior. The JSONL stream records a compact, decision-correlated diagnostic timeline.

**Consolidation decision:** keep this stream. Its per-event identity is necessary because it is exported independently of the parent AuditSnapshot envelope, and its event ordering/identity is not reconstructible from the operational AntiLoop state or aggregate metrics. Do not copy this event envelope into AuditSnapshot or promote the stream to PPO without a separate projection/replay contract.

The earlier statements in Sections 5–7 that AntiLoop history is not exposed to Python refer to the operational position/move/block/state-visit structures. They do not apply to the later #475 JSONL diagnostic stream.
