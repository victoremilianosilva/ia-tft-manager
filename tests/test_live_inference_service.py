import unittest

from live_inference.server import _checkpoint_metadata
from policy import ACTION_DIMS


class CheckpointMetadataTests(unittest.TestCase):
    def test_current_metadata_is_preserved(self):
        state = {"global_mlp.0.weight": type("Weight", (), {"shape": (256, 1000)})()}
        payload = {
            "policy_state_dict": state,
            "obs_dim": 1140,
            "action_dims": ACTION_DIMS,
            "hidden_size": 256,
        }
        resolved, obs_dim, action_dims, hidden_size = _checkpoint_metadata(payload)
        self.assertIs(resolved, state)
        self.assertEqual(obs_dim, 1140)
        self.assertEqual(action_dims, ACTION_DIMS)
        self.assertEqual(hidden_size, 256)

    def test_legacy_observation_dimension_uses_viewer_fallback(self):
        state = {"global_mlp.0.weight": type("Weight", (), {"shape": (256, 900)})()}
        _, obs_dim, _, _ = _checkpoint_metadata({"state_dict": state})
        self.assertEqual(obs_dim, 1040)

    def test_rejects_incompatible_action_dimensions(self):
        state = {"global_mlp.0.weight": type("Weight", (), {"shape": (256, 900)})()}
        with self.assertRaises(ValueError):
            _checkpoint_metadata({"state_dict": state, "action_dims": [7, 5, 9, 28, 28, 28]})


if __name__ == "__main__":
    unittest.main()
