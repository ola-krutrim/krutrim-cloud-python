# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ...lib.utils import convert_base64_to_PIL_img
from ...lib.utils import save_video_clip  # type: ignore
from ..._exceptions import FileSaveError

__all__ = ["CogVideoResponse"]


class CogVideoResponse(BaseModel):
    data: List[object]

    error: Optional[str] = None

    def save(self, output_dirpath: str, filename: str = "", fps: int = 8):
        data_list = self.data
        try:
            # Decode video frames
            video_frames = []
            for data in data_list:
                frame = convert_base64_to_PIL_img(data["b64_json"])  # type: ignore
                video_frames.append(frame)  # type: ignore

            # Store the generated video frames as a video
            save_video_clip(video_frames, output_dirpath=output_dirpath, filename=filename, fps=fps)
        except OSError as exc:
            raise FileSaveError(f"Exception occurred while saving output - {exc}")
        except Exception as exc:
            raise Exception(f"Exception occurred while saving output - {exc}")
