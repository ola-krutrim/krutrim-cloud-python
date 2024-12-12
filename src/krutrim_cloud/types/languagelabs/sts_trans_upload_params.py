import requests
from typing import TypedDict

__all__ = ["StsTransUploadParams"]


class StsTransUploadParams(TypedDict, total=False):
    # Path to the audio file to be uploaded
    file: str  # Path to the audio file (e.g., "/path/to/audio.wav")

    # Source language code of the audio (e.g., 'eng' for English)
    src_lang_code: str

    # Target language code for the translation (e.g., 'hin' for Hindi)
    tgt_lang_code: str

    # Speaker's voice (e.g., 'male')
    input_speaker: str
