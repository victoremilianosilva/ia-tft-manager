# Implementation Issue Roadmap v1

**Status:** approved to begin Gate 8 Stage 0; runtime work remains gated by Stage 0 acceptance.  
**Canonical branch:** `new-arquiteture`.  
**Canonical architecture:** Shadow supplies strategic context and recommendations; PPO remains the learning and action-selection algorithm. Native Engine rules and exact action masks remain the final legality authority.  
**Scope:** main repository `ia-tft-manager`. Overwolf/GEP validation is deferred to Stage 7.

## 1. Purpose and planning rule

This roadmap orders every currently open implementation/gate issue in the main repository, reconciles them with the accepted Gate 8 staged plan, and identifies prerequisites and exit evidence. It does not close issues merely because their documentation exists.

The current open issue inventory is #281–#295 (excluding #296–#301, already completed) plus #346. The six audit issues #296–#301 are treated as completed inputs, not implementation tasks. Closed documentary issues and merged PRs remain evidence, not work to repeat.

**Execution rule:** work proceeds by stage and dependency, not by issue number. An issue may contain design already completed and runtime acceptance still pending; its remaining scope must be split mentally and in its progress comments rather than repeating its completed documentation.

## 2. Ordered execution plan

### Stage 0 — Semantic design freeze (authorized now; design/documentation only)

**Goal:** approve a concrete, internally consistent design before runtime changes.

| Issue | Stage 0 responsibility | Stage 0 exit evidence |
|---|---|---|
| #293 Observation Schema | Reconcile Schema v2 with source map, entity manifest, identity envelope and typed missingness; freeze semantic fields and compatibility/version policy | Machine-readable schema and hash; all fields have explicit producer status, missingness and consumers |
| #294 Action Contract | Freeze native action semantics, parameter interpretation, conditional masks, identity correlation and rejection semantics | Versioned action/mask contract and cross-contract compatibility checks |
| #288 Checkpoint Contract | Freeze semantic lineage metadata and compatibility/failure policy against schema, reward, action, catalog and architecture manifests | Checkpoint manifest specification and load/save compatibility matrix |
| #286 PPO Migration | Complete the design portion only: feature-to-projection manifest, Actor/Critic ownership, candidate/excluded/unavailable dispositions, and architecture decision after projection | Reviewed projection manifest and Actor/Critic map; no PPO runtime change |
| #295 PPO Evaluation | Use the already documented evaluation protocol as a design constraint for lineage, metrics, ablations and promotion; no experiments yet | Evaluation contract referenced by the design manifests |

**Stage 0 tasks, in order:**
1. Reconcile the 223 Schema v2 paths against the 77-entry source map, 66 historical PPO feature mappings, 17 entity kinds and current producer audit.
2. Resolve schema identity naming against actual native identity semantics. Engine-instance scope, episode, player, round, decision, observation and mask sequence remain distinct namespaces; do not equate GEP or Viewer IDs with native decision identity.
3. Freeze the decision envelope and exact observation/mask binding, including content-hash inputs, canonical serialization, stale/mismatch behavior and missingness.
4. Produce the concrete projection manifest: stable feature IDs, source paths, evidence status, provenance, formula/version, unit, cardinality, ordering, missingness, normalization, projection shape and deterministic hash.
5. Finalize Actor/Critic consumer ownership. Both consume the exact same decision-correlated masks as a separate side input. Shared factual item/component and unit-target evidence may feed both; raw action-conditioning matrices remain Actor-specific initially. No untyped AntiLoop history in the initial Critic.
6. Select encoder/heads only after the manifest is complete. Do not inherit legacy dimensions or offsets by accident.
7. Reconcile action, reward, schema and checkpoint contract versions into one compatibility matrix.

**Stage 0 exit gate:** domain-owner review of the complete immutable design package. Until accepted, no native, Python, PPO, reward, checkpoint, Viewer or Overwolf runtime implementation.

### Stage 1 — Native identity and atomic decision snapshot

**Issues:** #293, #294; identity/producer evidence from #346.

- Add Engine-instance scope and typed lifecycle/decision sequences.
- Bind observation and exact action masks atomically to one decision envelope.
- Define reset/move semantics, content hashes, stale rejection and deterministic identity behavior.
- Preserve Engine-side legality as final authority.

**Exit:** native tests prove unique Engine scope, reset/move behavior, monotonic typed sequences, exact mask-observation correlation and stale/mismatch rejection.

### Stage 2 — Native structured evidence and Shadow strategic integration

**Issues:** #281, #282, #283, #284, #291, #346.

Recommended implementation order:

1. **#346 — producer/identity substrate:** implement only verified structured producers and lifecycle guarantees required by downstream work. Preserve unavailable states where no authoritative producer exists.
2. **#283 — copies, pairs and star progress:** establish one canonical owned/shop/pool distinction and progression calculation before planners consume it.
3. **#291 — unit and item evidence:** remove hidden dependence on planned carry/core traits; derive factual profiles from observed unit/item evidence and active composition contracts.
4. **#282 — economic evidence:** repair field-level provenance/default handling; only produce projected income, incoming damage and elimination risk when an authoritative source exists. Ensure economic urgency/cost evidence reaches the intended contextual evaluation path.
5. **#284 — strategic owner synchronization:** enforce direction, active composition, pivot candidate and transition ownership/version boundaries.
6. **#281 — real action candidates:** only after evidence and owner snapshots are available, produce concrete snapshot-bound BUY, XP, REROLL, HOLD/PASS, SELL and DEPLOY/MOVE candidates. No ambiguous physical parameters, no fake candidate set, no confident HOLD for an empty set.

**Important constraints:**
- Keep baseline ActionEvaluator and ContextualActionEvaluator semantically distinct unless a reviewed decision changes their authority. Record disagreements; do not force agreement with PPO.
- Candidate identity, shop slot/offer, exact unit instance, source/destination, horizon, evidence and cost/benefit must belong to the same snapshot.
- SELL must respect copies, star progress, items, active traits and bridge/transition value.
- Deploy/move must use an explicit destination producer.
- Eliminated-player items are terminally discarded: no transfer, return or redistribution to any player, inventory, pool, shop or PvE source.
- Shadow remains read-only; no candidate executes gameplay actions.

**Exit:** producer and integration tests prove valid evidence, explicit unknown/partial states, synchronized owners, real candidate sets, and no item transfer/redistribution.

### Stage 3 — Python transport and rollout identity

**Issues:** #293, #294, #346; implementation ownership follows the Stage 1/2 native envelope.

- Preserve native identity and exact masks through pybind, wrapper, vector environment, Trainer and RolloutBuffer.
- Bind terminal reward/done to the old episode; bind auto-reset observations/masks to the new episode.
- Preserve player/seat mapping, transition validity, truncation/terminal status and reward-component references.
- Make vector-lobby failure behavior explicit; prevent partial progress from being silently committed as a valid batch.
- Ensure Actor and Critic receive the same decision-bound mask snapshot.

**Exit:** deterministic tests cover normal step, reset, auto-reset, terminal boundaries, vector failure, seat order and rollout/minibatch identity.

### Stage 4 — PPO projection and checkpoint implementation

**Issues:** #286, #288, with #293/#294 contracts as prerequisites.

- Implement only the Stage 0-approved projection manifest.
- Implement Actor/Critic consumers and exact mask side-input semantics.
- Remove legacy policy-side nominal strategy/reserve derivations only when their approved replacements are connected and tested.
- Implement checkpoint manifests, loader validation, save/load/resume and immutable legacy-baseline handling.
- Do not silently transfer optimizer/scheduler state across incompatible lineages.

**Exit:** projection fixtures, Actor/Critic/action-head tests and checkpoint compatibility tests pass. Mechanical smoke runs, if any, are non-evaluative. No promotable training run or performance claim yet.

### Stage 5 — Reward migration and legacy isolation

**Issues:** #287, #290, #285; #288 checkpoint/reward lineage is a prerequisite.

Order:
1. #290 consumer-by-consumer migration map is the shutdown control ledger; refresh it against actual code before each removal.
2. #287 migrate reward inputs to authoritative consequence events, preserving immediate/combat/placement distinctions, temporal attribution, deduplication and per-player GAE boundaries.
3. #285 remove old strategic leakage from Shadow/Composition Intelligence once factual replacements are proven; do not remove shared legacy fields while external consumers still need them.
4. Retire active StrategyInfo/CompositionDirectionPolicy/CompositionPlanner-derived PPO/reward consumers only after replacements and regression evidence exist.

**Exit:** reward regression suite passes; event identity/temporal attribution and GAE are proven; no active decision/reward path depends on retired strategic semantics. Historical readers/checkpoints remain intact where required.

### Stage 6 — Viewer, integrated replay and PPO evaluation

**Issues:** #292, #289, #295.

- #292 provide a read-only compatibility projection for Viewer fields; Viewer is never a strategic authority.
- #289 execute deterministic multi-round replay across evidence → candidates → transitions → units/lineup → economy → evaluator → positioning → executor diagnostics. Include incomplete/stale snapshots, empty candidates and consecutive matches.
- #295 run baseline comparisons, paired seeds, seat rotation, held-out test sets, uncertainty, ablations and promotion/rollback gates only after Stage 5 reward migration is accepted.

**Exit:** integrated replay and evaluation reports are reproducible; Gates 1–7 have runtime acceptance evidence. No claim of improvement from reward curves or Shadow agreement alone.

### Stage 7 — Overwolf/GEP live integration (deferred)

**Issue coordination:** separate Overwolf integration workstream; not a current main-repository precondition.

- Validate sanitized real GEP captures, actual match-ID leaf, consecutive matches, reconnect/reset and missing/stale behavior.
- Bind GEP source metadata to the live-state adapter without treating GEP session/revision as native Engine decision identity.
- Prove live path is read-only and never calls simulation reset/step or executes gameplay actions.

## 3. Open issue disposition

| Issue | Planned stage(s) | Current disposition |
|---|---|---|
| #281 Strategic Action Candidates | 2 | Open; depends on structured evidence, economic context and owner snapshots |
| #282 Economic Controller | 2 | Open; missing/default fields and contextual-consumer path must be resolved |
| #283 Copies/Pairs/Star Progress | 2 | Open; foundational shared semantics for planners and SELL safety |
| #284 Strategic Ownership/Sync | 2 | Open; authority contracts documented, runtime synchronization proof pending |
| #285 Legacy Leakage in Composition Intelligence | 5 (design checks may be used in 2) | Open; migrate only after factual replacement sources exist |
| #286 PPO Observation Migration | 0 design, 4 runtime | Open; projection/consumer design first, implementation later |
| #287 Reward Migration | 5 | Open; Reward Contract documented, active runtime migration pending |
| #288 Checkpoint Contract | 0 design, 4 runtime | Open; manifest/loader implementation pending |
| #289 Strategic Multi-round Replay | 6 | Open; executable integrated replay pending |
| #290 Legacy Consumer Inventory | 5 | Open; audit completed in part, migration/shutdown ledger remains live |
| #291 Unit/Item Evidence | 2 | Open; remove legacy carry/core-trait dependency using authoritative facts |
| #292 Viewer Compatibility | 6 | Open; read-only projection and regression proof pending |
| #293 Observation Schema | 0 design, 1/3 runtime | Open; semantic contract exists, runtime producer/correlation pending |
| #294 Action/Mask Contract | 0 design, 1/3 runtime | Open; action semantics documented, exact runtime correlation pending |
| #295 PPO Evaluation Protocol | 0 design constraint, 6 execution | Open; protocol documented, experiments intentionally deferred |
| #346 Structured Entity Producer Audit | 1/2/3 | Open; documentary audits substantially advanced, end-to-end producer and delivery acceptance remains pending |

## 4. Completed inputs — do not repeat

The following are accepted documentary/source-audit inputs to the plan:
- Audits #296–#301 (A–F), including observation, action/mask, reward/GAE, PPO architecture, strategic ownership and legacy consumer inventory.
- Gate contracts and reconciliation PRs #306–#421, including Schema v2/identity, Actor/Critic semantics, producer/source maps, entity/temporal contract, reward/checkpoint/evaluation protocols, replay contract, elimination item terminal policy and Gate 8 staged plan.
- User decision: eliminated-player items are discarded terminally with no transfer or redistribution.
- User direction: real GEP validation is handled during Overwolf integration.

A completed documentation issue does not imply runtime acceptance. An open issue does not mean its already-merged documentation should be recreated.

## 5. Cross-stage invariants and stop conditions

- No second AI; PPO remains the learning algorithm; Shadow remains canonical strategic context and read-only.
- Native Engine rules and exact masks remain final legality authority.
- No automatic gameplay execution.
- No fabricated identities, candidates, offers, items, pool counts, positions, history, income, damage or risk.
- Observed zero, empty, missing, unknown, partial, stale, incompatible and not-applicable remain distinct.
- Board, bench, shop and pool remain separate ownership/availability domains.
- No transfer or redistribution of eliminated-player items.
- Historical checkpoints/artifacts remain immutable.
- Stage 4 cannot produce promotable training results before Stage 5 reward migration and Stage 6 evaluation acceptance.
- GEP work remains deferred to Stage 7.
- Stop a downstream issue if its upstream contract/evidence is not accepted; record the blocker instead of filling it with a default or parallel implementation.

## 6. First execution batch

The first batch is **Stage 0 only**:
1. Build and review the projection manifest from existing schema/source/consumer artifacts.
2. Reconcile identity, action/mask, reward and checkpoint versions.
3. Finalize the Actor/Critic feature ownership map and the architecture decision.
4. Publish a Stage 0 acceptance checklist and request review before opening any runtime implementation PR.

This roadmap itself does not freeze tensor dimensions by copying the old PPO layout and does not authorize implementation beyond Stage 0.
