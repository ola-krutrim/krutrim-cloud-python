# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(BaseModel):
    name: Optional[str] = None
    """Filename."""


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
