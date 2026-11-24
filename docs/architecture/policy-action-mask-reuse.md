# Policy and action-mask inference reuse

## Previous problem

The PPO replay path rebuilt the native semantic entity view independently in
encode(), _candidate_features() and _item_state_features(). Each view was a
slice/reshape of the same semantic numeric batch. The inference path already
shared the projection, but evaluate_actions() did not.

The C++ binding creates Python-owned NumPy arrays for each action mask. The
wrapper retained those arrays, then get_action_masks() detached every mask
again before returning them to the Trainer. The Trainer then validates and
batches the masks for tensor conversion.

## Technical rationale

Semantic input validation must remain at the Policy boundary, but a validated
batch should have one shared entity projection for all consumers in that call.
This avoids repeating shape-preserving tensor views without changing values.

The binding's NumPy arrays own their memory. Replacing the wrapper's current
references on the next step() or reset() does not overwrite an array already
held by a caller. The Trainer is a read-only consumer, so it can borrow those
buffers; callers that need mutable or independently retained masks continue
using the detached public API.

## Responsibilities

- TFTPolicy.evaluate_actions() validates finite semantic inputs once and
  creates one entity projection shared by encoder, candidate and item paths.
- CppTFTLobbyWrapper.get_action_masks_for_training() exposes read-only
  references to the Python-owned mask arrays captured with the current snapshot.
- CppTFTLobbyWrapper.get_action_masks() remains the detached, mutable-safe API.
- Trainer consumes the read-only training accessor and remains responsible for
  validating shape, dtype and binary values before batching and tensor conversion.
- The C++ ActionMaskEngine and binding mask production remain unchanged.

## Contracts and invariants

- Every action mask remains associated with the same observation/snapshot and
  decision sequence as before.
- Borrowed arrays are read-only; the wrapper never mutates or reuses their
  storage after publishing them.
- A subsequent step/reset replaces the wrapper's references but does not alter
  prior borrowed arrays.
- The detached public accessor continues to return independent mutable arrays.
- NaN/Inf checks remain at the PPO replay boundary for semantic numeric and
  floating item tensors; malformed inputs are still rejected.
- The exact legal-action set, action dimensions, conditional masks, logits,
  values, log probabilities, entropy and PPO loss semantics remain unchanged.
- Existing ActionMaskEngine and BoardEvaluationCache optimizations are not
  modified.

## Impact

The PPO replay path performs one semantic entity projection per batch instead
of independently reconstructing it for each feature consumer. The training
mask accessor removes the wrapper's per-call full-array detach; only the
mutable public API and the optional item-action ablation copy the arrays they
modify. No strategic context, action restriction, provenance field or PPO
component is removed.

## Validation criteria

- Count exactly one semantic entity projection during evaluate_actions().
- Reject NaN/Inf semantic inputs during PPO replay.
- Verify borrowed mask buffers are read-only and survive a subsequent snapshot.
- Verify the public accessor remains detached and mutable.
- Preserve existing action-mask validation, conditional-action, policy replay,
  and C++ action-mask tests.
- CI must pass before merge. Quantitative latency/allocation claims remain
  deferred until measured on the training workload.
