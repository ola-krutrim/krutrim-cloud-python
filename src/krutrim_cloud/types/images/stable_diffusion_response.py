# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from ...lib.utils import convert_base64_to_PIL_img
from ...lib.utils import save_PIL_img
from ...lib.utils import get_current_time_string
from ..._models import BaseModel
from ..._exceptions import FileSaveError

__all__ = ["StableDiffusionResponse"]


class StableDiffusionResponse(BaseModel):
    created: int

    data: List[Dict[str, str]]

    error: Optional[str] = None

    def save(self, output_dirpath:str, filename:str=""):
        data_list = self.data
        try:
            for index, data in enumerate(data_list, start=1):
                PIL_img = convert_base64_to_PIL_img(data["b64_json"])
                if filename:
                    file_name = filename
                else:
                    file_name = f"StableDiffusionXL1-output-{index}-{get_current_time_string()}.png"

                # Save or display the image
                save_PIL_img(PIL_img, output_dirpath, file_name)
        except OSError as exc:
            raise FileSaveError(f"Exception occurred while saving output - {exc}")
        except Exception as exc:
            raise Exception(f"Exception occurred while saving output - {exc}")
