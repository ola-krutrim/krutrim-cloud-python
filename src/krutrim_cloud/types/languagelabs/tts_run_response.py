from typing import Optional
from ..._models import BaseModel
from ..._exceptions import FileSaveError
from ...lib.utils import get_current_time_string

__all__ = ["TtsRunResponse", "TtsData"]

class TtsData(BaseModel):
    audio_file: str  # The URL link to download the generated audio file

class TtsRunResponse(BaseModel):
    status: str  # Indicates whether the request was successful (e.g., "success")
    data: TtsData  # Contains the audio file download link

