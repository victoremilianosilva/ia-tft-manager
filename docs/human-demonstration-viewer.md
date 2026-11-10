# Human Demonstration Viewer

This is a separate interactive desktop Viewer. It reuses the visual components of
`viewer/main.py` and the existing `ViewerSession`; it does not replace the normal
evaluation Viewer.

## Run

From the repository root, after installing the project and Viewer dependencies and
building the native extension:

```powershell
python -m pip install -r requirements.txt -r viewer/requirements.txt
python scripts/build_native.py
$env:PYTHONPATH = "$PWD\cpp\build\bin\Release;$PWD"
python -m viewer.human_main
```

Choose a checkpoint, seed and human seat, then start a new match.

## Playing

The human mode now follows the normal Viewer's preparation cadence:

- Preparation lasts **6 seconds**, matching `ViewerConfig.preparation_seconds`.
- Agent inference ticks run at the normal Viewer cadence of approximately **700 ms**.
- There is no manual PASS / "conclude decision" button. PASS is sent as an idle action
  while waiting; it does not end preparation early.
- Your clicks are queued and submitted on the next shared decision tick. Each tick
  batches your action (or idle PASS) with one inference action from each of the other
  seven living agents.
- At the preparation deadline, the Viewer submits the timeout batch and the native
  engine resolves the round. A last click queued just before the deadline is flushed
  once before timeout; a backlog cannot extend the preparation window.

Controls:

- Click a shop champion to buy it.
- Use **Comprar XP** and **Atualizar loja** for economy actions.
- Click a bench unit and then an empty board cell to deploy it.
- Click a board unit and then another board cell to reposition it.
- Select a bench unit and use **Vender unidade selecionada** to sell it.
- Select a completed item from the inventory, then click a board/bench unit to equip it.
- Select two components in sequence, then click a target unit to craft and equip.
- The native action masks are checked before every human action. The UI does not send
  actions that are illegal according to the current masks.
- Shop portraits are rendered whenever offers exist in the native snapshot. A slot is
  clickable only when its unit is occupied and the native shop mask allows BUY.
- If offers exist but none can currently be bought (for example, insufficient gold),
  the UI keeps them visible but explains that no purchase is legal.
- If the native snapshot itself contains no offers in 1-1, the UI reports that state
  and waits for the next preparation. The current C++ initializer does call
  `ShopEngine::roll` when players are created, so an actually empty 1-1 snapshot
  should be diagnosed from the runtime snapshot rather than assumed by the UI.

Every human action is submitted in one simultaneous lobby batch with one inference action
from each of the other seven living agents. The seven policies remain in inference/eval
mode; there is no optimizer, PPO update, or checkpoint mutation.

## Logging

Sessions are saved under `viewer/human_sessions/` using the existing per-player `.tft`
and structured `.json` logs. Human decisions are marked with `source: human`, idle
preparation ticks with `source: human_idle`, the other seats with `source: frozen_policy`,
and each completed step records `human_player_id`, the eight actions, state snapshots,
rewards and engine events. The optional note field records the human's rationale.

## Isolation and current engine limitation

- No C++ source, PPO code, reward implementation, policy weights, or training configuration
  is modified by this feature.
- The game state and action legality remain owned by the native C++ engine.
- The current native lobby action contract exposes BUY, REROLL, BUY_XP, movement, SELL,
  PASS and item actions. It does **not** expose a carousel-pick action. The Viewer displays
  a notice if a carousel state is present, but cannot honestly implement a clickable
  carousel selection until the engine exports that action and its legal-choice mask.
- Moving units between two bench slots and moving a board unit back to the bench are also
  not exposed by the action contract used here.
- This is a turn-by-turn simulator Viewer, not a live client for the official TFT game.
- This PR has not been validated against the user's Windows native build yet. A complete
  match smoke test is required before merging.
