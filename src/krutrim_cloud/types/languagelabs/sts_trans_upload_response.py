from ..._models import BaseModel

__all__ = ["StsTransUploadResponse", "SpeechToSpeechData"]

class SpeechToSpeechData(BaseModel):
    audio_file: str  #The URL to download the generated speech audio file

class StsTransUploadResponse(BaseModel):
    status: str  # Indicates whether the request was successful (e.g., "success")
    data: SpeechToSpeechData  # Contains the audio file download link

