from ..._models import BaseModel
from ...lib.utils import get_current_time_string,save_text_content
from ..._exceptions import FileSaveError

__all__ = ["SttTransUploadResponse", "SttTransData"]

class SttTransData(BaseModel):
    translated_text: str  # The translated text as a string

class SttTransUploadResponse(BaseModel):
    status: str  # Indicates whether the request was successful (e.g., "success")
    data: SttTransData  # Contains the translated text

    def save(self, output_dirpath:str, filename:str=""):
        txt_output_data = self.data.translated_text
        if filename:
            file_name = filename
        else:
            file_name = f"speech_to_text_translation-output-{get_current_time_string()}.txt"
        try:
            save_text_content(txt_output_data, output_dirpath, file_name)

        except OSError as exc:
            raise FileSaveError(f"Exception occurred while saving output - {exc}")
        except Exception as exc:
            raise Exception(f"Exception occurred while saving output - {exc}")
