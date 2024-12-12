from typing import TypedDict

__all__ = ["LanguageDetectionRunParams"]

class LanguageDetectionRunParams(TypedDict):
    query: str  # The text to detect the language of
