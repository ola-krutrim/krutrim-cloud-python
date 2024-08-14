# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from ...lib.utils import save_text_content
from ...lib.utils import get_current_time_string
from ..._models import BaseModel
from ..._exceptions import FileSaveError

__all__ = ["CompletionCreateResponse", "Choice", "ChoiceMessage"]


class ChoiceMessage(BaseModel):
    content: str

    role: str


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    message: Optional[ChoiceMessage] = None


class CompletionCreateResponse(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    object: str

    def save(self, output_dirpath:str, filename:str=""):
        txt_output_data = self.choices[0].message.content
        if filename:
            file_name = filename
        else:
            file_name = f"{self.model}-output-{get_current_time_string()}.txt"
        try:
            save_text_content(txt_output_data, output_dirpath, file_name)

        except OSError as exc:
            raise FileSaveError(f"Exception occurred while saving output - {exc}")
        except Exception as exc:
            raise Exception(f"Exception occurred while saving output - {exc}")
