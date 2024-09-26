# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TaskListResponse"]


class TaskListResponse(BaseModel):
    count: Optional[int] = None
    """Total number of task."""

    offset: Optional[int] = None
    """List start offset."""

    task_list: Optional[List[object]] = None
    """Task List"""
