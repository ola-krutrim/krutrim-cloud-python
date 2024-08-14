# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from ...lib.utils import save_text_content
from ...lib.utils import get_current_time_string
from ..._models import BaseModel
from ..._exceptions import FileSaveError
import json

__all__ = ["WhisperResponse"]


class WhisperResponse(BaseModel):
    predictions: object

    def save(self, output_dirpath:str, filename:str=""):
        txt_data_dict = self.predictions
        if filename:
            file_name = filename
        else:
            file_name = f"WhisperLargeV3-{get_current_time_string()}-output.txt"
        try:

            save_text_content(
                json.dumps(txt_data_dict),
                output_dirpath,
                file_name,
            )

        except OSError as exc:
            raise FileSaveError(f"Exception occurred while saving output - {exc}")
        except Exception as exc:
            raise Exception(f"Exception occurred while saving output - {exc}")
