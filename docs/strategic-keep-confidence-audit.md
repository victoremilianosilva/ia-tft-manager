# Strategic Planner KEEP confidence audit

The existing Viewer command `Executar auditoria` writes this analysis into
`audit/audit_estrategia.md`. It reuses the per-review `shadow_planning`
diagnostics and the current board/bench snapshot; it does not invoke the
Strategic Planner or reconstruct evidence from PPO actions.

## KEEP classifications

Each deduplicated Strategic Planner review with decision `KEEP` receives one
of three diagnostic classifications:

- `KEEP_SUPPORTED_BY_CURRENT_EVIDENCE`: the planner explicitly reports the
  current direction as viable, or an owned preserved/replaceable unit has an
  observable core-unit or current-direction/core-trait alignment signal.
- `KEEP_ASSOCIATED_WITH_PERSISTENCE`: current strategic support is not
  established, while a composition lock, a pending candidate with observed
  streak, or investment-only unit evidence (for example, upgrades/items without
  directional alignment) is present.
- `KEEP_INCONCLUSIVE`: neither current strategic support nor a persistence
  explanation can be established from the recorded fields.

Board presence alone is not considered directional alignment. A unit merely
being on the board does not prove that it supports the selected composition.
Investment proxies are reported separately and never treated as positive
strategic support. When explicit viability and persistence coexist, explicit
current viability takes precedence in the classification, while persistence
fields remain visible in the sample.

## Alternative and hysteresis diagnostics

The same KEEP review reports the best available classification for alternatives:

- rejected by the recorded strategic score;
- below the observed ADAPT threshold;
- below the observed PIVOT threshold;
- held/blocked while persistence is active;
- no alternative generated;
- alternative outcome unavailable or unclear.

Only recorded candidate diagnostics, advantage values, thresholds, candidate
state, lock and streak fields are used. Missing values remain unavailable.
The absence of a better candidate is never counted as positive evidence for
the current composition.

## Aggregation and interpretation

The report counts the three KEEP classes and shows each review by player and
round, including current-direction viability/score, aligned units,
investment-only units, lock/candidate state, alternative status and reasons.
The report is generated per Viewer session (one match); player/round rows
therefore remain scoped to that match. Existing follow-up outcome rows are
retained as temporal associations, not causal proof.

Heuristic confidence is not a calibrated probability. A persistence-associated
KEEP is not automatically wrong, and an inconclusive KEEP is not automatically
weak. This audit describes what the available snapshot supports and identifies
where evidence is missing; it does not change KEEP/ADAPT/PIVOT decisions,
thresholds, hysteresis, composition locks, PPO, training, observations, masks,
legal actions, rewards, checkpoints, rules or execution.
