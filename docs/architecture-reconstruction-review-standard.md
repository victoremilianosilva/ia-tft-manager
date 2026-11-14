# Architecture Reconstruction and Change Review Standard

**Status:** normative project-wide documentation rule
**Applies to:** all architecture documents, specifications, issues, migration plans, and implementation proposals in the Shadow architecture.
**Architecture authority:** Shadow is the canonical target architecture. Legacy code and documents are evidence sources only; they are not normative design authority.

## 1. Reconstruction principle

The goal is not to port, preserve, or modernize the legacy implementation mechanically. The goal is to identify valuable capabilities and rebuild the correct solution inside the canonical Shadow architecture.

Every legacy capability must be critically classified as:
- **Preserve:** the capability remains valid and necessary; its implementation is still redesigned to satisfy current contracts.
- **Improve:** the purpose remains valid, but the former solution has defects or limitations.
- **Redesign:** ownership, data model, boundaries, or workflow must materially change.
- **Discard:** the capability is unnecessary, harmful, duplicated, or conflicts with the target architecture.

No legacy class, API, data shape, default, algorithm, or ownership decision is automatically retained. Functional continuity does not imply implementation continuity.

## 2. Mandatory six-part justification for every relevant change

Any material architectural/documentary change, including a decision to preserve, improve, redesign, or discard a legacy capability, must record:

1. **Prior problem:** the concrete defect, limitation, ambiguity, coupling, missing behavior, or risk in the previous solution. If no legacy equivalent exists, state that the capability is newly introduced and why.
2. **Technical rationale:** why the proposed solution is technically preferable and which alternatives or trade-offs were considered when material.
3. **New responsibility:** the single accountable owner, producer, consumer, and authority boundary, including what the component must not own.
4. **Contract and invariants:** inputs, outputs, identity, provenance, freshness, lifecycle, failure/missing behavior, versioning, and invariants necessary to prevent ambiguity or invalid state.
5. **Cross-component impact:** affected contracts, components, data flows, issues, Viewer/telemetry, replay, training/inference, migration dependencies, and compatibility implications. Explicitly state when there is no impact.
6. **Objective validation:** observable acceptance criteria, negative cases, tests/replay evidence, artifacts, and conditions that prove success or failure. Documentary approval must be distinguished from executable acceptance.

A change is incomplete if any applicable item is absent. Do not invent a legacy defect for a genuinely new capability; explicitly mark the prior implementation as absent.

## 3. Required decision record template

For each material decision, use this structure:

- **Decision and classification:** preserve / improve / redesign / discard / new capability.
- **Prior solution and problem:** evidence-backed description, or explicit statement that no prior capability existed.
- **Technical rationale:** chosen design and material trade-offs.
- **New owner and boundaries:** accountable owner, producers, consumers, and prohibited responsibilities.
- **Contract and invariants:** normative semantics and failure behavior.
- **Impact analysis:** upstream/downstream contracts, migration, compatibility, telemetry, and training/inference effects.
- **Validation:** documentary checks now and executable criteria at the authorized implementation phase.
- **Legacy disposition:** retain temporarily, replace after migration proof, preserve for historical reads, or remove only after dependency proof and approval.

## 4. Evidence and authority rules

- Distinguish audited facts, approved design decisions, proposals, and executable evidence.
- A merged document approves only the documentary decisions it explicitly states; it does not prove runtime conformance.
- A closed audit issue closes its stated audit deliverable, not every migration or runtime acceptance item.
- Legacy checkpoints and historical logs may remain immutable baselines/readable artifacts without defining the new architecture.
- Never preserve a legacy dependency solely for backward compatibility. Any compatibility path must have a named consumer, bounded purpose, owner, and retirement condition.
- Do not label missing/default values as observed facts; preserve unknown/unavailable semantics and provenance.
- Do not merge distinct owners or semantic concepts merely to simplify the model.
- Shadow remains read-only. Engine rules and native masks remain final legality authority. Shadow proposals are not executed actions, PPO labels, or reward targets.

## 5. Gate and implementation boundary

This standard is documentary and does not authorize runtime changes. All implementation remains blocked until Gate 8 and explicit user approval. Any later migration must be incremental, evidence-backed, reversible, and must prove that legacy consumers have moved before legacy producers/APIs are removed.

## 6. Review checklist

A reviewer must reject or return a material change when:
- its legacy premise is treated as correct without evidence;
- any of the six justification elements is missing;
- ownership or authority is ambiguous;
- missing/stale/invalid evidence can silently become a valid default;
- cross-component identity, provenance, sequence, or lifecycle is underspecified;
- acceptance criteria are subjective or only assert that a class/document exists;
- documentary status is represented as runtime completion;
- the change introduces a second strategic authority or permits live-game execution.
