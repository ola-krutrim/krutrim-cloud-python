from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TranslationRunParams"]

class TranslationRunParams(TypedDict):
    text: Required[str]
    src_language: Required[str]
    tgt_language: Required[str]
    model: Required[str]
