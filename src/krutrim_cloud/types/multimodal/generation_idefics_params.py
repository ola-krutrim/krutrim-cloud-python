# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GenerationIdeficsParams"]


class GenerationIdeficsParams(TypedDict, total=False):
    model_name: Required[Annotated[str, PropertyInfo(alias="modelName")]]

    prompts: Required[List[str]]

    images: Iterable[List[str]]

    max_tokens: Annotated[Optional[int], PropertyInfo(alias="maxTokens")]
