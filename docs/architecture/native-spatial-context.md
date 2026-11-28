# Native Spatial Context

`NativeSpatialContext` (`tft.native-spatial-context@1`) is an immutable player-scoped projection over the exact `AuditSnapshot` retained by `NativeDecisionBatch`. It publishes 28 slots as contiguous typed buffers (row, column, occupancy, catalog ID, role, five combat stats), physical UUID/catalog strings as side metadata, and board-evaluation metrics from the same Engine snapshot.

Geometry is `tft.board-grid.rectangular-4x7` v1. The contract does not claim TFT hex adjacency, facing, or attack-range reachability.

Relations include only occupied pairs neighboring under the same bounded 8-neighbor rectangular relation used by `BoardEvaluation`. `RectangularNeighbor` is stored once with ordered slots. `FrontlineSupportsBackline` is directional and emitted only when an adjacent tank/fighter has a smaller row index than a carry/support. Endpoints are slot indices backed by physical UUIDs, never champion IDs.

Unknown geometry versions are `incompatible` and publish no relations. Shadow positioning proposals are excluded. Neural encoder integration consumes these typed buffers in the Trainer/PPO cutover (#590); this issue establishes the native producer and parity contract.