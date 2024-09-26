# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    k_customer_id: Required[Annotated[str, PropertyInfo(alias="K-Customer-ID")]]

    file: FileTypes
