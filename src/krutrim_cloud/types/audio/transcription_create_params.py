# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TranscriptionCreateParams"]


class TranscriptionCreateParams(TypedDict, total=False):
    chunk_type: Annotated[Optional[str], PropertyInfo(alias="chunkType")]

    file: str

    language: Optional[str]

    model_name: Annotated[str, PropertyInfo(alias="modelName")]

    response_format: Annotated[Optional[str], PropertyInfo(alias="responseFormat")]

    task: str

    temperature: Optional[float]
