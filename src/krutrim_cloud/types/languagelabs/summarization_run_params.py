from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SummarizationRunParams"]

class SummarizationRunParams(TypedDict, total=False):
    text: Required[str]
    input_language: Required[str]
    summary_size: Required[int]
