# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CheckpointListResponse", "CheckpointListResponseItem"]


class CheckpointListResponseItem(BaseModel):
    model: Optional[str] = None
    """Checkpoint name."""

    name: Optional[str] = None
    """Checkpoint name."""

    version: Optional[str] = None
    """Checkpoint name."""


CheckpointListResponse: TypeAlias = List[CheckpointListResponseItem]
