from typing import TypedDict

__all__ = ["TranscribeLfUploadParams"]

class TranscribeLfUploadParams(TypedDict, total=False):
    # Path to the audio file to be uploaded
    file: str  # Path to the audio file (e.g.,"/path/to/audio.wav")

    # Language code of the spoken content (e.g., 'eng' for English)
    lang_code: str