from typing import TypedDict, Optional

__all__ = ["TtsRunParams"]

class TtsRunParams(TypedDict, total=False):
    # The text that needs to be converted to speech.
    # This is the main content you want to be read out loud.
    input_text: str

    # The language of the input text.
    # This is used to determine the appropriate language model for speech synthesis.
    # For example: "eng" for English,
    input_language: str

    # The speaker identity to use for the TTS (Text-to-Speech) synthesis.
    # This could refer to a particular voice model (like a male or female voice, or a specific accent).
    # Example values might be "male", "female".
    input_speaker: str

