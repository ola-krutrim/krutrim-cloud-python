# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TaskRetrieveResponse"]


class TaskRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """Task ID."""

    checkpoint: Optional[str] = None
    """Checkpoints."""

    inference_svc_name: Optional[str] = None
    """Inference service name."""

    name: Optional[str] = None
    """Task name."""

    namespace: Optional[str] = None
    """Task namespace."""

    priority: Optional[int] = None
    """Task priority."""

    status: Optional[str] = None
    """Task status."""
