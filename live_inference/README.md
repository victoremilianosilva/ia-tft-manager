# Live inference service (read-only)

This package is an isolated inference boundary. It loads the same `TFTPolicy`
architecture and compatible checkpoint format used by the Viewer, but it does
not instantiate `ViewerSession`, create a lobby, step the C++ engine, train,
or execute TFT actions.

## Start

From the repository root, with the project's Python dependencies and native
extension available only if required by the existing policy environment:

```powershell
$env:TFT_LIVE_CHECKPOINT = "C:\\path\\to\\tft_checkpoint.pt"
python -m live_inference.server
```

The service binds to loopback only (default `127.0.0.1:8765`).

- `GET /health`: model readiness, checkpoint digest and expected observation dimension.
- `POST /v1/recommendation`: deterministic inference from one observation and its
  exact native action masks.

## Request contract

```json
{
  "requestId": "unique-request-id",
  "revision": 125,
  "observation": [0.0],
  "masks": {
    "type_mask": [1, 0, 0, 0, 0, 0, 0, 0, 0]
  }
}
```

The example arrays above are illustrative only. Production callers must send the
complete observation vector with exactly the dimension reported by `/health`,
plus every mask required by the current policy's action heads, in the shapes
produced by the native engine. The service rejects missing masks rather than
creating permissive masks.

The response echoes `requestId` and `revision`, includes the six-component
policy action and native policy diagnostics, and explicitly declares
`"execution": "none"`. The caller must discard responses whose revision is no
longer current.

## Important integration boundary

**This service does not accept raw Overwolf GEP snapshots.** GEP state is not a
PPO observation: the native C++ observation builder and legal-action mask
generator must first convert a complete, supported live state into the exact
training-time representation. That adapter is intentionally not faked here.
Until the separate native live-state adapter exists and is parity-tested, this
endpoint is an inference transport foundation, not an end-to-end in-game coach.

Unknown or unavailable live fields must not be inferred. Do not use test-only
engine setters or advance a simulated lobby to manufacture live state.
