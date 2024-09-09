# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompletionCreateParams", "Message", "ResponseFormat"]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]

    frequency_penalty: float

    logit_bias: Dict[str, int]

    logprobs: bool

    max_tokens: int

    n: int

    presence_penalty: float

    response_format: ResponseFormat

    stop: Optional[str]

    stream: bool

    temperature: float

    top_logprobs: int

    top_p: float

    skip_special_tokens: bool


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


class ResponseFormat(TypedDict, total=False):
    type: str
