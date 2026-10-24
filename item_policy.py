"""Optional autoregressive PPO head for the separate item-action contract.

This module intentionally does not change TFTPolicy's six-action checkpoint
schema. The trainer/runtime can adopt it when native item state and masks are
available. All action log-probabilities include only parameters relevant to the
selected operation.
"""
from __future__ import annotations

from typing import Mapping

import torch
from torch import nn
from torch.distributions import Categorical
import torch.nn.functional as F

from item_action_contract import ITEM_ACTION_DIMS, ItemActionType


class ItemPPOHead(nn.Module):
    """Masked categorical policy for WAIT/CRAFT/EQUIP/TRANSFER/UNEQUIP."""

    def __init__(self, feature_dim: int):
        super().__init__()
        self.feature_dim = int(feature_dim)
        self.type_head = nn.Linear(feature_dim, ITEM_ACTION_DIMS[0])
        self.first_component_head = nn.Linear(feature_dim + ITEM_ACTION_DIMS[0], ITEM_ACTION_DIMS[1])
        self.second_component_head = nn.Linear(feature_dim + ITEM_ACTION_DIMS[0] + ITEM_ACTION_DIMS[1], ITEM_ACTION_DIMS[2])
        self.item_head = nn.Linear(feature_dim + ITEM_ACTION_DIMS[0], ITEM_ACTION_DIMS[3])
        self.source_head = nn.Linear(feature_dim + ITEM_ACTION_DIMS[0], ITEM_ACTION_DIMS[4])
        self.target_head = nn.Linear(feature_dim + ITEM_ACTION_DIMS[0] + ITEM_ACTION_DIMS[4], ITEM_ACTION_DIMS[5])
        self.equipped_slot_head = nn.Linear(feature_dim + ITEM_ACTION_DIMS[0], ITEM_ACTION_DIMS[6])

    @staticmethod
    def _distribution(logits: torch.Tensor, mask: torch.Tensor | None) -> Categorical:
        if mask is not None:
            mask = torch.as_tensor(mask, device=logits.device, dtype=torch.bool)
            if mask.shape != logits.shape:
                raise ValueError(f"item mask shape {tuple(mask.shape)} != logits {tuple(logits.shape)}")
            if (~mask.any(dim=-1)).any():
                raise ValueError("item action mask has a row with no legal choices")
            logits = logits.masked_fill(~mask, torch.finfo(logits.dtype).min)
        if not torch.isfinite(logits).all():
            raise FloatingPointError("item action logits contain NaN or infinity")
        return Categorical(logits=logits)

    @staticmethod
    def _mask(masks: Mapping[str, torch.Tensor] | None, name: str, rows: torch.Tensor | None = None):
        if masks is None or name not in masks:
            return None
        value = masks[name]
        return value if rows is None else value[rows]

    def _select(self, logits, masks, name, deterministic):
        dist = self._distribution(logits, masks)
        action = logits.argmax(-1) if deterministic else dist.sample()
        return action, dist.log_prob(action), dist.entropy()

    def forward(self, features: torch.Tensor, masks: Mapping[str, torch.Tensor] | None = None,
                deterministic: bool = False):
        """Return [B,7] actions, joint log-probability, and summed entropy."""
        if features.ndim != 2 or features.shape[-1] != self.feature_dim:
            raise ValueError(f"expected [batch,{self.feature_dim}] item features")
        batch, device = features.shape[0], features.device
        type_action, logp, entropy = self._select(
            self.type_head(features), self._mask(masks, "type"), "type", deterministic)
        type_onehot = F.one_hot(type_action, ITEM_ACTION_DIMS[0]).to(features.dtype)
        conditioned = torch.cat([features, type_onehot], dim=-1)
        actions = torch.zeros((batch, 7), dtype=torch.long, device=device)
        actions[:, 0] = type_action

        def add_param(rows, head, head_input, mask_name, action_column):
            nonlocal logp, entropy
            if not rows.any():
                return torch.zeros(batch, dtype=torch.long, device=device)
            submask = self._mask(masks, mask_name, rows)
            action, sub_logp, sub_entropy = self._select(head(head_input[rows]), submask, mask_name, deterministic)
            logp[rows] += sub_logp
            entropy[rows] += sub_entropy
            result = torch.zeros(batch, dtype=torch.long, device=device)
            result[rows] = action
            actions[rows, action_column] = action
            return result

        craft = type_action == int(ItemActionType.CRAFT)
        first = add_param(craft, self.first_component_head, conditioned,
                          "first_component", 1)
        first_onehot = F.one_hot(first, ITEM_ACTION_DIMS[1]).to(features.dtype)
        second_input = torch.cat([conditioned, first_onehot], dim=-1)
        add_param(craft, self.second_component_head, second_input,
                  "second_component", 2)

        equip = type_action == int(ItemActionType.EQUIP)
        transfer = type_action == int(ItemActionType.TRANSFER)
        unequip = type_action == int(ItemActionType.UNEQUIP)
        add_param(equip, self.item_head, conditioned, "inventory_item", 3)
        source_rows = transfer | unequip
        source = add_param(source_rows, self.source_head, conditioned, "source_unit", 4)
        target_input = torch.cat([
            conditioned,
            F.one_hot(source, ITEM_ACTION_DIMS[4]).to(features.dtype)
        ], dim=-1)
        add_param(transfer, self.target_head, target_input, "target_unit", 5)
        add_param(unequip, self.equipped_slot_head, conditioned, "equipped_item", 6)
        return actions, logp, entropy

    def evaluate_actions(self, features: torch.Tensor, actions: torch.Tensor,
                         masks: Mapping[str, torch.Tensor] | None = None):
        """Recompute joint log-probability/entropy for PPO updates."""
        if actions.ndim != 2 or actions.shape != (features.shape[0], 7):
            raise ValueError("item actions must have shape [batch,7]")
        batch, device = features.shape[0], features.device
        types = actions[:, 0].long()
        type_dist = self._distribution(self.type_head(features), self._mask(masks, "type"))
        if ((types < 0) | (types >= ITEM_ACTION_DIMS[0])).any():
            raise ValueError("item action type out of range")
        if self._mask(masks, "type") is not None:
            if not self._mask(masks, "type").gather(1, types[:, None]).all():
                raise ValueError("selected item action type is masked")
        logp = type_dist.log_prob(types)
        entropy = type_dist.entropy()
        conditioned = torch.cat([features, F.one_hot(types, 5).to(features.dtype)], dim=-1)

        def evaluate(rows, logits, column, mask_name):
            nonlocal logp, entropy
            if not rows.any():
                return torch.zeros(batch, dtype=torch.long, device=device)
            mask = self._mask(masks, mask_name, rows)
            dist = self._distribution(logits[rows], mask)
            chosen = actions[rows, column].long()
            if ((chosen < 0) | (chosen >= logits.shape[-1])).any():
                raise ValueError(f"{mask_name} action index out of range")
            if mask is not None and not mask.gather(1, chosen[:, None]).all():
                raise ValueError(f"selected {mask_name} is masked")
            logp[rows] += dist.log_prob(chosen)
            entropy[rows] += dist.entropy()
            result = torch.zeros(batch, dtype=torch.long, device=device)
            result[rows] = chosen
            return result

        craft = types == int(ItemActionType.CRAFT)
        first_logits = self.first_component_head(conditioned)
        first = evaluate(craft, first_logits, 1, "first_component")
        second_input = torch.cat([conditioned, F.one_hot(first, 18).to(features.dtype)], dim=-1)
        evaluate(craft, self.second_component_head(second_input), 2, "second_component")
        equip, transfer, unequip = (types == int(ItemActionType.EQUIP),
                                    types == int(ItemActionType.TRANSFER),
                                    types == int(ItemActionType.UNEQUIP))
        evaluate(equip, self.item_head(conditioned), 3, "inventory_item")
        source = evaluate(transfer | unequip, self.source_head(conditioned), 4, "source_unit")
        target_input = torch.cat([conditioned, F.one_hot(source, 37).to(features.dtype)], dim=-1)
        evaluate(transfer, self.target_head(target_input), 5, "target_unit")
        evaluate(unequip, self.equipped_slot_head(conditioned), 6, "equipped_item")
        return logp, entropy
