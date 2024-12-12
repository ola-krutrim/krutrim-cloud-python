from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EntityExtractionRunParams"]

class EntityExtractionRunParams(TypedDict):
    text: Required[str]
    param_list: Required[List[str]]
    lang_from: Required[str]