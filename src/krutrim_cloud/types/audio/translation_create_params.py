# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TranslationCreateParams"]


class TranslationCreateParams(TypedDict, total=False):
    file: str

    language: Optional[str]

    model_name: Annotated[str, PropertyInfo(alias="modelName")]

    task: str

    temperature: Optional[float]
