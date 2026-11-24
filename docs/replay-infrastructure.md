# Replay and observed-match data infrastructure

This repository supports two intentionally separate evidence streams.

## Native lobby simulation replay

Set the output directory when running a training or evaluation process:

    TFT_REPLAY_OUTPUT_DIR=artifacts/native-replays python train.py

CppTFTLobbyWrapper records the exact native lobby boundary consumed by the agent:
- reset snapshot, observations and action masks;
- requested and normalized actions;
- native action traces, acceptance/rejection outcomes and action-outcome events;
- before/after native snapshots, observations, masks, rewards and terminal flags;
- native events, including COMBAT_SNAPSHOT_V2 and COMBAT_OUTCOME_V1 where emitted.

Files use TFT_NATIVE_LOBBY_REPLAY_V1, append-only JSONL and a SHA-256 hash chain. Package completed artifacts with:

    python scripts/build_replay_dataset.py artifacts/native-replays/*.jsonl --output datasets/native-lobby.json

The builder copies immutable artifacts into a sibling native-lobby_artifacts directory and creates match-disjoint train/validation/test splits. At least three independent matches are required. The version hash is stable for the same artifacts and split seed.

Deterministic re-execution is enabled only when the original seed, source revision and catalog hashes are present and still match the current checkout. replay/runner.py reports the first divergent transition/field. A replay without those identities remains observational and is not promoted to deterministic.

**Important:** native lobby results are simulator outcomes. They are not real-game observations. They must not be relabeled as authoritative live TFT replays or used as real-match calibration evidence.

## Live TFT GEP observation capture

The Overwolf app (tft-manager-ow) writes one TFT_GEP_OBSERVATION_CAPTURE_V1 file per detected TFT game session under the app's userData/tft-snapshots directory. The capture contains:
- sanitized raw GEP info/game-event records;
- canonical live-state snapshots with game-session ID, match ID, revision and completeness;
- lifecycle/error records and a terminal footer;
- a global sequence and SHA-256 hash chain across all record types.

The collector removes account identifiers, credentials, summoner names and roster display-name keys. It also excludes augment data and combat/damage telemetry. The required GEP feature list does not enable battle/combat telemetry.

Copy completed capture files to the AI repository and ingest at least three independent matches:

    python scripts/ingest_gep_replays.py captures/tft-gep-replay-*.jsonl --output datasets/live-tft-gep.json

The ingestor verifies the source chain and footer, match/game-session identity, increasing snapshot revisions, a complete baseline, and an observed game-exit boundary. It emits one immutable TFT_GEP_MATCH_REPLAY_V1 artifact per match and a versioned dataset manifest. Train/validation/test partitions are assigned by match ID, so snapshots from one match cannot leak across splits.

Consumers can iterate only the verified canonical observations:

    from replay.gep_ingest import iter_gep_observed_snapshots

    for snapshot in iter_gep_observed_snapshots("datasets/live-tft-gep.json", split="validation"):
        # snapshot carries replay_artifact_id and dataset_version
        # and explicitly declares observational-only provenance.
        process(snapshot)

### Evidence boundaries

A GEP snapshot is an authoritative observation of the fields the provider exposed at that moment. It is not a full game replay:
- it does not prove the exact player action that caused a state transition;
- a difference in HP between snapshots is not attributed to a specific combat;
- it does not expose per-combat damage in this capture contract;
- it cannot deterministically re-execute the live match.

The ingestor therefore sets authoritative_state_observation=true, authoritative_game_replay=false and combat_calibration_eligible=false. It does not attach these live artifacts to simulator COMBAT_OUTCOME_V1 records. The latter remain calibration_eligible=false until a source that actually observes the same combat outcome is available.

Missing fields stay missing. No HP delta is converted into combat damage, and no inferred action is promoted to an executed action.

## Integrity and recovery

- A missing footer means a capture is incomplete and cannot enter a dataset.
- Any broken sequence/hash link, duplicate match ID, changed artifact, or identity mismatch fails ingestion.
- Dataset files are created exclusively; existing manifests/artifacts are never overwritten.
- A new capture or changed split seed creates a new dataset version.
