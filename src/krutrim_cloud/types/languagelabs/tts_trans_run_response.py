from ..._models import BaseModel

__all__ = ["TtsTransRunResponse", "TtsTransData"]

class TtsTransData(BaseModel):
    audio_file: str  # The URL to download the translated speech audio file

class TtsTransRunResponse(BaseModel):
    status: str  # Indicates whether the request was successful (e.g., "success")
    data: TtsTransData  # Contains the audio file download link
