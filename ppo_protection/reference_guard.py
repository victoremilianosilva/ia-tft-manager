"""Trust-region projection around an immutable fine-tuned reference policy."""
from __future__ import annotations

import math
from typing import Mapping

import torch


def snapshot_parameters(policy) -> dict[str, torch.Tensor]:
    return {
        name: parameter.detach().clone()
        for name, parameter in policy.named_parameters()
    }


@torch.no_grad()
def project_to_reference(policy, reference: Mapping[str, torch.Tensor], max_relative_drift: float) -> dict:
    """Project the complete policy into an L2 trust region around its reference.

    The reference tensors are never mutated. Projection is global (not per-layer),
    so a large update in one head cannot hide behind many unchanged parameters.
    """
    limit = float(max_relative_drift)
    if not math.isfinite(limit) or limit <= 0.0 or limit > 1.0:
        raise ValueError("max_relative_drift deve estar no intervalo (0, 1].")
    current = dict(policy.named_parameters())
    if set(current) != set(reference):
        raise RuntimeError("A arquitetura da policy mudou em relação ao modelo de referência.")
    delta_sq = torch.zeros((), device=next(policy.parameters()).device, dtype=torch.float64)
    ref_sq = torch.zeros_like(delta_sq)
    for name, parameter in current.items():
        ref = reference[name].to(device=parameter.device, dtype=parameter.dtype)
        if parameter.shape != ref.shape:
            raise RuntimeError(f"Shape divergente no parâmetro de referência: {name}")
        delta_sq += (parameter.detach().double() - ref.double()).pow(2).sum()
        ref_sq += ref.double().pow(2).sum()
    drift = float(torch.sqrt(delta_sq).item())
    reference_norm = max(float(torch.sqrt(ref_sq).item()), 1.0)
    allowed = limit * reference_norm
    projected = drift > allowed
    if projected:
        scale = allowed / max(drift, 1e-12)
        for name, parameter in current.items():
            ref = reference[name].to(device=parameter.device, dtype=parameter.dtype)
            parameter.copy_(ref + (parameter - ref) * scale)
    after_sq = torch.zeros((), device=delta_sq.device, dtype=torch.float64)
    for name, parameter in current.items():
        ref = reference[name].to(device=parameter.device, dtype=parameter.dtype)
        after_sq += (parameter.detach().double() - ref.double()).pow(2).sum()
    after = float(torch.sqrt(after_sq).item())
    return {
        "relative_drift_before": drift / reference_norm,
        "relative_drift_after": after / reference_norm,
        "relative_drift_limit": limit,
        "projected": projected,
    }
