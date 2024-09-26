# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TaskCreateResponse"]


class TaskCreateResponse(BaseModel):
    id: Optional[str] = None
    """Task ID."""

    name: Optional[str] = None
    """Task name."""
