from typing import TypedDict

__all__ = ["TranscribeUploadParams"]

class TranscribeUploadParams(TypedDict, total=False):
    # Path to the audio file to be uploaded
    file: str  # This will be the local path to the audio file

    # Language code (e.g., 'eng' for English)
    lang_code: str
