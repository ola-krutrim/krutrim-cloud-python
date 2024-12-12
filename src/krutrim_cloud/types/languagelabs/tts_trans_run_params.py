from typing import TypedDict

__all__ = ["TtsTransRunParams"]

class TtsTransRunParams(TypedDict, total=False):
    # The input text to be translated and converted to speech
    input_text: str

    # Source language code of the input text (e.g., 'eng' for English)
    src_lang_code: str

    # Target language code for the translation (e.g., 'hin' for Hindi)
    tgt_lang_code: str

    # Speaker's voice (e.g., 'male')
    input_speaker: str
