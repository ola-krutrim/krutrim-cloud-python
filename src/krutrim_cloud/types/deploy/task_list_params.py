# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict


__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):

    limit: int
    """Limit the max number of item to be return."""

    offset: int
    """Offset index."""
