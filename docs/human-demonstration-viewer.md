# Human Demonstration Viewer

The human demonstration interface is an independent desktop entrypoint. It does not replace
or modify the evaluation Viewer.

## Run

From the repository root, after installing the existing project and Viewer dependencies and
building the native extension:

```powershell
python -m pip install -r requirements.txt -r viewer/requirements.txt
python scripts/build_native.py
$env:PYTHONPATH = "$PWD\cpp\build\bin\Release;$PWD"
python -m viewer.human_main
```

Choose a trained checkpoint, a seed, and the player seat. The selected seat is controlled
manually; the other seven living seats receive one action from the loaded policy at each
joint lobby step. The engine still resolves the eight actions together.

## Isolation guarantees

- This entrypoint creates no `Trainer`, `PPOTrainer`, optimizer, or training loop.
- The checkpoint is loaded for inference only; policy parameters have gradients disabled.
- The C++ engine and its reward implementation are used unchanged.
- No PPO configuration, reward, policy weights, or training data is modified.
- The existing Viewer session writer is reused for state/action/reward snapshots. Human
  decisions additionally emit a `human_decision` event with the selected action and optional
  free-text rationale. Bot decisions are marked `frozen_policy`.
- Sessions are written under `viewer/human_sessions/`.

## Decision workflow

Each click submits exactly one action for the human seat and one policy action for each
other living seat. Eliminated seats submit PASS. The action selector is refreshed from the
native `type_mask`; the complete current masks are visible for reference. Action arguments
are entered as numeric indices and must match the native action contract shown in the UI.

The rationale field is optional. It is useful for recording intent that cannot be inferred
from state transitions alone (for example, why a player held gold or chose a flexible unit).

## Important limitations

This first version is a demonstration recorder, not an imitation trainer. It does not change
the PPO policy or rewards and does not claim to teach from a match automatically. Logs are
collected for later review and dataset design. A human action can still be rejected or become
a no-op if its numeric arguments do not describe a legal target; consult the displayed masks.

The simulator advances in joint action batches, so the seven agents also act once every time
you submit a human action. This is not a real-time pause/resume implementation of a live TFT
client.
