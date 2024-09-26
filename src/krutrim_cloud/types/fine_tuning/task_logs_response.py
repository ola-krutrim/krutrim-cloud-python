# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["TaskLogsResponse", "TaskLogsResponseItem"]


class TaskLogsResponseItem(BaseModel):
    idx: Optional[int] = None
    """Index of the current log."""

    logs: Optional[object] = None
    """Logs."""

    stage: Optional[str] = None
    """Task stage."""

    task_name: Optional[str] = None
    """Task Name."""

    ts: Optional[str] = None
    """Timestampe."""

    user: Optional[str] = None
    """User name."""


TaskLogsResponse: TypeAlias = List[TaskLogsResponseItem]
