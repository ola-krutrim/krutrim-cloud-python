# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CheckpointDelResponse"]


class CheckpointDelResponse(BaseModel):
    reason: Optional[str] = None
    """Describe the error"""

    uid: Optional[str] = FieldInfo(alias="UID", default=None)
    """UID of the error"""
