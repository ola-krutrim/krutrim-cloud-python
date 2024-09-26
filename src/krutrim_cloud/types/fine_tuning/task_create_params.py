# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    k_customer_id: Required[Annotated[str, PropertyInfo(alias="K-Customer-ID")]]

    batch: int
    """Batch Size."""

    dataset: str
    """Dataset Name."""

    engine: str
    """Engine type."""

    epoch: int
    """Epoch Number."""

    lora_alpha: int
    """Lora alpha"""

    lora_rank: int
    """Lora rank"""

    lr: int
    """Learn Rate."""

    mode: str
    """Mode Name."""

    model: str
    """Model Name."""

    namespace: str
    """Task Name."""

    ngpu: int
    """Number of GPU."""

    priority: int
    """Task priority."""

    seed: int
    """Random Seed."""

    task_name: str
    """Task Name."""

    test_dataset: str
    """Test Dataset Name."""

    total_checkpoint: int
    """total checkpoint saved"""

    version: str
    """Version String."""
