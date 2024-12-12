from typing import List
from ..._models import BaseModel
from ...lib.utils import get_current_time_string,save_text_array_content
from ..._exceptions import FileSaveError

__all__ = ["TranscribeUploadResponse", "TranscribeData"]

class TranscribeData(BaseModel):
    text: List[str]  # A list of strings containing the transcribed text

class TranscribeUploadResponse(BaseModel):
    status: str  # Indicates whether the request was successful (e.g., "success")
    data: TranscribeData  # Contains the transcribed text
    def save(self, output_dirpath:str, filename:str=""):
        txt_output_data = self.data.text
        if filename:
            file_name = filename
        else:
            file_name = f"transcribe-output-{get_current_time_string()}.txt"
        try:
            save_text_array_content(txt_output_data, output_dirpath, file_name)

        except OSError as exc:
            raise FileSaveError(f"Exception occurred while saving output - {exc}")
        except Exception as exc:
            raise Exception(f"Exception occurred while saving output - {exc}")
