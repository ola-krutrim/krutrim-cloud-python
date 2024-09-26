# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskListParams"]


class TaskListParams(TypedDict, total=False):
    k_customer_id: Required[Annotated[str, PropertyInfo(alias="K-Customer-ID")]]

    limit: int
    """Limit the max number of item to be return."""

    offset: int
    """Offset index."""
