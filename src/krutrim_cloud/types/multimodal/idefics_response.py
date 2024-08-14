# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from ...lib.utils import save_text_array_content
from ...lib.utils import get_current_time_string
from ..._models import BaseModel
from ..._exceptions import FileSaveError

__all__ = ["IdeficsResponse"]


class IdeficsResponse(BaseModel):
    generated_texts: List[str]

    def save(self, output_dirpath:str, filename:str=""):
        txt_data_list = self.generated_texts
        if filename:
            file_name = filename
        else:
            file_name = f"Idefics-output-{get_current_time_string()}.txt"
        try:
            save_text_array_content(txt_data_list, output_dirpath, file_name)

        except OSError as exc:
            raise FileSaveError(f"Exception occurred while saving output - {exc}")
        except Exception as exc:
            raise Exception(f"Exception occurred while saving output - {exc}")
