from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SentimentAnalysisRunParams"]

class SentimentAnalysisRunParams(TypedDict, total=False):
    text: Required[str]
    lang_from: Required[str]
