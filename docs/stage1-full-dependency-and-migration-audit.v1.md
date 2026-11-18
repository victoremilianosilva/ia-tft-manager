# Stage 1 Full Dependency and Migration Audit v1

**Status:** source-backed audit with one implementation slice.  
**Implementation branch:** `stage1-full-strategic-independence`  
**Scope:** structure ownership, native strategic independence, item profiles, Viewer compatibility, PPO/reward boundaries, diagnostics, histories and end-to-end acceptance.

## 1. Executive decision

This audit distinguishes three classes:

1. **Safe and implemented now:** proven duplicate data with no consumer; removal of a one-entry vector wrapper; native trait evidence in Composition Intelligence; Viewer compatibility projection from canonical strategic owners. The PPO/reward item profile helper is isolated but intentionally not migrated.
2. **Required but intentionally retained:** distinct producer/namespace semantics, independently versioned event contracts, transformation/validation adapters, decision/event sequence domains, and legacy data still consumed by PPO/reward.
3. **Blocked by unapproved contracts:** concrete PPO tensor projection, reward coefficients/semantics, and Actor/Critic mask-side-input architecture. The existing projection and reward documents explicitly remain design drafts and do not approve runtime semantics.

No default, inferred score, or legacy alias is promoted as native evidence when the native owner has no value.

## 2. Structure disposition matrix

| Structure / fields | Producer → actual consumer | Decision | Reason / invariant |
|---|---|---|---|
| `AuditSnapshot.source_namespace` | TFTEngine snapshot producer → `cpp_lobby_env` strict schema/namespace validation, replay/Viewer snapshot readers | **Keep** | Stable logical identity namespace for the snapshot sequence. |
| `AuditSnapshot.producer` | `TFTEngine::get_audit_snapshot` → wrapper producer validation and diagnostics | **Keep** | Concrete implementation/source function; not interchangeable with a logical namespace. |
| Event `source_namespace` | EconomyEngine event producers → wrapper event-contract validation and consumers | **Keep** | Stable logical namespace for the event's source. |
| Event `producer` | `EconomyEngine::resolve_round` / `register_pvp_win` → wrapper provenance validation | **Keep** | Names the concrete producer operation. It may change independently of a logical source namespace. |
| Shared-pool `producer` | `UnitPool::available` → wrapper pool contract validation | **Keep** | Shared-pool snapshot inherits the parent namespace and identity; it has no redundant child namespace. |
| Snapshot `contract_id/version` | AuditSnapshot schema → wrapper validates native snapshot v3 | **Keep** | Defines the parent payload contract. |
| Economy/PvP event `contract_id/version` | Each event producer → wrapper validates event schema independently of parent snapshot | **Keep** | Event payloads have distinct semantics and may evolve independently of the containing snapshot. Parent snapshot version does not replace event schema version. |
| Combat event records | Combat producer → AuditSnapshot/wrapper/Viewer | **Keep inherited envelope** | They inherit parent identity/schema and retain combat-local sequence. Do not add repeated parent identity or a second event contract without independent transport/version needs. |
| `StrategicEvidenceContextInput::core_unit_ids` and `StrategicEvidenceContext::derived_core_unit_ids` | Builder copied the vector into the evidence object; no downstream read was found | **Eliminate — implemented** | It duplicated the same active native candidate unit IDs already represented per owned unit by `StrategicUnitCandidate::is_core`. Removed the unused input and stored copy. |
| `StrategicUnitCandidate::is_core` | Native owned-unit evidence builder → StrategicPlanner classification | **Keep** | Per-entity flag used by the planner. It is the consumed representation; no parallel aggregate ID vector is required. |
| `PlannerEvidenceAdapters` | BoardEvaluation/EconomicController/ItemEngine → typed, validated planner evidence | **Keep** | Performs unit conversion, finite/range checks, source metadata and identity/version correlation; not a pass-through DTO. |
| `StrategicEvidenceContextBuilder` | Native observed context + native commitment → validated StrategicEvidenceContext | **Keep** | Validates player/round/sequence, preserves provenance and explicitly marks missing/partial/incompatible context. |
| `StrategicContextBridge` | Validated strategic/economic/composition context → diagnostic JSON | **Keep** | Performs explicit origin/quality projection and serialization; diagnostic-only. |
| `CompositionDiagnosticSnapshot` | Recorder combines active composition, transition, priority, lineup, evidence and action evaluation → runtime snapshot list | **Keep** | It is an immutable Viewer/export diagnostic record, not a decision input. |
| Composition diagnostic runtime envelope | Per-player runtime owns match/player/round/player sequence; stage rows own stage sequence | **Keep** | Different sequence scopes. No additional parent identity is needed in stage rows. |
| `CompositionIntelligencePlayerRuntime.snapshots` | Recorder/runtime → `get_composition_diagnostics_jsonl` → pybind → `cpp_lobby_env` → Viewer Session JSONL → diagnostics widget | **Keep** | Concrete consumer chain exists. It is bounded by episode reset, deduplicates identical snapshots and preserves per-player sequence. |
| `StrategicCommitment` per player | StrategicPlanner mutates per-player commitment → subsequent strategic evidence and diagnostics | **Keep** | Canonical direction/commitment owner; reset at episode boundary. |
| `strategic_context_sequences` | Native evidence builder → context identity and strategic planner validation | **Keep** | Per-player sequence for strategic context; distinct from Engine decision and Composition runtime stage sequences. |
| Unified Strategic Shadow runtime | Viewer configures per-player audit runtime path → append-only strategic decision/action/economic audit records | **Keep pending consumer expansion** | Viewer session configures the sidecar; it is diagnostic-only and not consumed by PPO. Keep separate from Composition diagnostic snapshots because event payload and purpose differ. |
| AntiLoop operational histories | AntiLoop legality logic → move/state cycle prevention and metrics | **Keep** | Operational state affects legal move/mask behavior. |
| Typed AntiLoop diagnostic event tail | #475 had no application consumer; #485 removed it | **Eliminate — merged** | Parallel partial event history duplicated operational state and was not a complete action replay. |
| `PlayerEnv.strategy` one-entry vector | Legacy `update_strategy()` → PPO observation/reward and telemetry | **Simplify container — implemented; retain value as compatibility** | The vector was cleared/pushed once at reset and only `back()` was read/overwritten; it never accumulated history. Internal storage is now `optional<StrategyInfo>`. The public pybind shape remains a one-element list for compatibility. Its legacy values remain until approved PPO/reward migrations. |
| Legacy `CompositionPlanner` output | `update_strategy()` populates legacy `planned_*`; legacy PPO feature/reward paths still read those fields | **Keep temporarily as legacy PPO compatibility; exclude from new strategic owners** | New StrategicPlanner/Composition Intelligence already consume NativeStrategicCompositionGenerator and native evidence. The legacy planner must not feed active composition or Viewer canonical projections. Remove only when PPO/reward projection is approved and migrated. |
| Legacy `CompositionDirectionPolicy` output | Legacy `update_strategy()` updates old StrategyInfo direction; PPO observation/reward still consume it | **Keep temporarily as PPO compatibility; exclude from new strategic owners** | StrategicPlanner commitment is the canonical new direction. Viewer projection now reads that commitment. |
| Native composition candidate generator | Native catalog + board/bench/shop/pool facts → snapshot-bound candidates | **Keep** | New proposal producer; no StrategyInfo/CompositionPlanner input. |
| `ActiveCompositionManager` | TransitionManager-approved candidate → versioned active composition | **Keep** | Canonical active-composition owner. A candidate is not active until publication succeeds. |
| Composition Intelligence item binding profile | Native strategic context → `ItemUnitBinding` evidence in the new Composition Intelligence pipeline | **Native source — implemented in #486** | Preferred traits use `StrategicSharedContext::current_core_traits`; no StrategyInfo fallback inside the new strategic consumer. |
| `legacy_item_unit_profiles()` | Legacy StrategyInfo → PPO anvil observation and item action/reward evaluation | **Keep explicitly isolated; migrate under #286/#287** | Still reads legacy core/planned/direction/focus/active traits. It is now named and called explicitly as a legacy compatibility path so the new strategic pipeline cannot mistake it for canonical evidence. Do not change its values until projection/reward contracts are approved. |
| Viewer strategy/composition snapshot | `get_strategies()` → pybind → `cpp_lobby_env.get_strategy_snapshots()` → Viewer Session attaches to audit player; cards/dialog/logs consume that compatibility shape | **Compatibility projection — implemented** | Current snapshot is copied and projected from StrategicCommitment + ActiveCompositionManager. Projection source/status/version are explicit. Internal `PlayerEnv.strategy` remains unchanged for legacy PPO/reward until contract migration. |
| Trainer strategy count | `cpp_lobby_env.get_strategies()` → Trainer count telemetry | **Keep telemetry-only** | Audited use counts economic strategy enum values; it is not a policy/action/reward source. |
| PPO observation strategy features | `build_observations()` reads legacy `StrategyInfo`; `policy.py` reads core strategy one-hot and derived strategic branches | **Migrate later under projection contract** | Existing tensor layout is legacy and the target projection document explicitly says design-only. No offsets, dimensions, normalizers or semantics are approved for replacement. |
| PPO Critic masks | Actor action heads consume masks; `get_value()`/value head currently encodes observation without mask input | **Migrate later under PPO architecture contract** | Exact decision-correlated masks are required as independent Actor/Critic side inputs. This requires an explicit value-network/checkpoint architecture migration, not a hidden concatenation or unversioned tensor change. |
| Reward strategy branches | `PlayerEnv::step` uses legacy strategy IDs for XP/reroll/pass/sale/spending and other shaping | **Migrate later under Reward Contract** | Reward draft explicitly has no approved v1 coefficients and requires factual outcome accounting, no strategy-ID shaping and no recommendation-derived targets. Removing branches without the approved replacement changes reward meaning. |
| RewardManager helper path | `RewardManager.hpp`/state reward helpers | **Retain as separately audited legacy path** | The active Python training reward path is `PlayerEnv::step`; do not mistake an unused helper for the production reward source. |

## 3. Diagnostic consumer map

### Composition Intelligence diagnostics

`CompositionDiagnosticRecorder::capture`  
→ per-player `CompositionIntelligencePlayerRuntime.snapshots`  
→ `TFTEngine::get_composition_diagnostics_jsonl()`  
→ pybind  
→ `cpp_lobby_env.get_composition_diagnostics_jsonl()`  
→ `ViewerSession._persist_composition_diagnostics()` writes `composition_diagnostics.jsonl`  
→ `CompositionDiagnosticsWidget` loads and renders audit/snapshot detail.

The snapshot explicitly classifies observed evidence separately from inferred decisions, transition plans, unit intentions, lineup plans and action recommendations. It is diagnostic-only and not a PPO input.

### Strategy compatibility snapshots

`TFTEngine::get_strategies()`  
→ `strategies_to_list` pybind projection  
→ `cpp_lobby_env.get_strategy_snapshots()`  
→ `ViewerSession._refresh_audit_snapshot()` attaches each current strategy snapshot to the matching audit player  
→ Viewer cards/dialog/player logs.

Trainer's separate `get_strategies()` path is used for strategy-count telemetry; no policy, action or reward consumption was found in the audited callsite.

### Unified strategic Shadow sidecar

Viewer Session configures `set_strategic_direction_pivot_audit_path()`; the Engine owns per-player `UnifiedStrategicShadowRuntime` instances writing the session-local strategic direction/pivot audit sidecar. The sidecar is diagnostics, not an action source, PPO feature, reward target or imitation label.

## 4. Strategic independence: current implementation and limits

### Implemented in this branch

1. The new Composition Intelligence item binding uses `StrategicSharedContext::current_core_traits` (completed in #486) and does not read legacy StrategyInfo traits.
2. The separate `legacy_item_unit_profiles()` helper remains on PPO anvil-observation and item action/reward callsites. Its legacy semantics are preserved until #286/#287 approve the replacement; it is explicitly named so it cannot be mistaken for canonical strategic evidence.
3. Viewer-facing current composition fields are projected from the per-player StrategicCommitment and ActiveCompositionManager:
   - direction from the canonical commitment;
   - planned units/main carry/source score from the published active candidate;
   - core unit IDs from the published candidate's explicit `CompositionUnit::core` flags (currently main carry only);
   - core/planned traits from the champion catalog for those canonical unit IDs;
   - composition version from the active owner.
4. Fields with no canonical equivalent (lock, focus weights, legacy strength, prior-direction transition counters) are cleared rather than fabricated. Projection metadata exposes source, status and version.
5. The Viewer projection is made on the returned copy; it does not mutate the internal `PlayerEnv.strategy` value or alter PPO/reward behavior. Internal storage changed from a vector that never held more than one entry to `optional<StrategyInfo>`; the external pybind list shape is preserved.
6. The unused aggregate `derived_core_unit_ids` copy, the unwritten `StrategicCommitment::core_unit_ids` field, and the one-entry `PlayerEnv.strategy` vector wrapper were removed. The active composition's `CompositionUnit::core` is the consumed canonical subset; in the current native candidate producer this marks the main carry only. Other legacy core-unit rankings are not synthesized.

### Still legacy, deliberately isolated

- `update_strategy()` still calculates legacy economic strategy and legacy direction/focus/core/planned fields for the current PPO observation/reward compatibility path.
- Legacy `CompositionPlanner::build` still populates `StrategyInfo.planned_*` for that path. The new strategic planner and ActiveCompositionManager do not consume that output.
- The PPO projection and reward semantics must be migrated only after their contracts are concretely approved; until then those legacy values are not to be deleted or silently substituted.

## 5. Positioning and economy evidence

The new strategic context is assembled from native facts:
- board evaluation and board power;
- native HP/alive state;
- native gold, level, XP, interest and streak;
- native board/bench units, catalog traits, shop offers and pool availability;
- native opponent board/bench copies for contestation.

`EconomicController` and `ActionEvaluator` evaluate this context independently and remain Shadow-only. `PlannerEvidenceAdapters` converts native board/economic/item evidence into typed evidence with source quality and identity/version checks. Positioning recommendations remain proposals; the Engine's action masks and final legality remain authoritative.

This does not claim that the legacy PPO reward or observation path has already been migrated to these native evidence records.

## 6. PPO and reward contract blockers

### PPO observation projection

The current policy uses fixed legacy offsets, including the strategy one-hot at `[10:17]`, and derives further target-level/reserve behavior from it. The target projection contract explicitly remains design-only and does not approve feature order, shapes, offsets, normalization, categorical vocabulary, missingness or actor/critic sharing.

Therefore this implementation does **not** replace the tensor fields or alter `policy.py` offsets. The next PPO projection must provide a complete feature manifest, deterministic encoding, missingness/provenance, actor/critic consumer map, mask side-input map and checkpoint identity before runtime replacement.

### Actor/Critic masks

The Actor consumes exact native masks in its conditional action heads. The current value path `get_value(obs, masks)` ignores the supplied masks and the value head is computed from encoded observation only. This is a confirmed gap. It remains open until the Critic receives the exact same decision-correlated mask bundle as a separately declared side input with checkpoint lineage and tests.

### Reward

`PlayerEnv::step` still uses strategy IDs for action reward shaping. The Reward Contract draft explicitly states that v1 coefficients are not approved and requires an outcome/evidence-based, non-duplicative accounting model. A blind deletion or neutral strategy-ID substitution would change reward semantics without an approved replacement. This implementation therefore leaves the reward path unchanged and records the exact blocker.

## 7. Multi-round integrated acceptance gaps

The following have not been proven by this implementation:

- complete deterministic multi-round replay with old strategic producers disabled;
- producer → AuditSnapshot → Python → native strategic consumer field-by-field coverage for all entity families;
- exact mask delivery to both Actor and Critic;
- PPO observation projection replacement and checkpoint lineage;
- strategy-independent reward invariance under the approved Reward Contract;
- Viewer historical-log compatibility across old and new session versions;
- no-fallback tests for every unavailable strategic field across all consumers.

No synthetic values are inserted to make these cases pass.

## 8. Six-point architecture review

1. **Prior problem:** new strategic runtime and old PPO/Viewer compatibility state overlapped. The new Composition Intelligence item evidence was fixed in #486, but the separate PPO/reward item profile helper and Viewer consumers still observed legacy fields; unused aggregate core IDs and a one-entry StrategyInfo vector duplicated or obscured ownership.
2. **Technical rationale:** the active composition owner already contains the published candidate; StrategicCommitment owns direction/core unit IDs; the aggregate core-unit vector had no consumer. Producer function names, logical namespaces and event contract versions have different semantics and are retained.
3. **New responsibility:** ActiveCompositionManager supplies item target/trait evidence, lineup and explicit core flags; StrategicCommitment supplies direction; Viewer receives a one-way compatibility projection; PPO/reward retain explicitly marked legacy inputs until their own contracts are approved.
4. **Contracts/invariants:** no fallback from missing native composition; no mutation of PPO-facing StrategyInfo by Viewer projection; event and decision sequence namespaces remain distinct; Engine remains final legality authority; recommendations remain Shadow-only.
5. **Cross-component impact:** native Composition Intelligence evidence, explicit legacy item-profile compatibility naming/callsites, optional StrategyInfo storage, Viewer strategy snapshots, pybind compatibility adapter, strategic evidence tests and documentation. PPO tensors, reward values, action masks, checkpoint format and Engine legality are intentionally unchanged.
6. **Objective validation:** source-boundary tests verify the new Composition Intelligence path uses native traits, the legacy item profile is explicitly isolated to PPO/reward callsites, the one-entry vector is absent internally, and Viewer projection reads native owners; C++ StrategicEvidenceContext tests no longer construct unused duplicate core IDs; CI must pass native, strategic, Python and Viewer suites.

## 9. Stage 1 acceptance status

**Stage 1 remains not globally accepted.** The implementation closes the confirmed item-profile and Viewer compatibility leaks and removes one unused duplicate. The remaining hard blockers are the concrete PPO projection, reward contract approval/migration, Critic mask side input, and integrated multi-round replay with legacy strategic producers unavailable.
