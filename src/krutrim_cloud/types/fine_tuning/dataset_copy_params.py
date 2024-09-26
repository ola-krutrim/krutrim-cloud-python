# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DatasetCopyParams"]


class DatasetCopyParams(TypedDict, total=False):
    k_customer_id: Required[Annotated[str, PropertyInfo(alias="K-Customer-ID")]]

    filename: str
    """Filename for the copied dataset"""

    path: str
    """s3 path"""

    s3_access_key: str
    """s3 access key"""

    s3_endpoint: str
    """s3 endpoint"""

    s3_region: str
    """s3 region"""

    s3_secret: str
    """s3 secret"""
