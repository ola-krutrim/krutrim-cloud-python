# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DatasetCopyResponse"]


class DatasetCopyResponse(BaseModel):
    name: Optional[str] = None
    """Name of the copied dataset"""
