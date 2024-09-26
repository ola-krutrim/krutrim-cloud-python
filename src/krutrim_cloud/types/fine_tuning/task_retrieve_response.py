# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TaskRetrieveResponse"]


class TaskRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """Task ID."""

    batch: Optional[int] = None
    """Batch Size"""

    checkpoints: Optional[List[object]] = None
    """Checkpoints"""

    ctime: Optional[str] = None
    """Task creation time."""

    dataset: Optional[str] = None
    """Dataset name used by the task."""

    dataset_size: Optional[int] = None
    """Dataset size"""

    epoch: Optional[int] = None
    """Epoch Number"""

    lora_alpha: Optional[int] = None
    """Lora alpha"""

    lora_rank: Optional[int] = None
    """Lora rank"""

    lr: Optional[int] = None
    """Learn Rate"""

    mode: Optional[str] = None
    """Fine_tuning mode used by the task."""

    model: Optional[str] = None
    """Model name used by the task."""

    name: Optional[str] = None
    """Task name."""

    namespace: Optional[str] = None
    """Task namespace."""

    ngpu: Optional[int] = None
    """Number of GPU."""

    priority: Optional[int] = None
    """Task priority."""

    reason: Optional[str] = None
    """Task fail reason."""

    seed: Optional[int] = None
    """Random Seed"""

    status: Optional[str] = None
    """Task status."""

    test_dataset: Optional[str] = None
    """Test dataset name used by the task."""

    test_dataset_size: Optional[int] = None
    """Test dataset size"""

    total_checkpoint: Optional[int] = None
    """total checkpoint saved"""

    version: Optional[str] = None
    """Version String."""
