# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["Text2videoCreateParams"]


class Text2videoCreateParams(TypedDict, total=False):
    model_name: Required[Annotated[str, PropertyInfo(alias="modelName")]]

    prompt: Required[List[str]]

    guidance_scale: Annotated[Optional[int], PropertyInfo(alias="guidanceScale")]

    num_frames: Annotated[Optional[int], PropertyInfo(alias="numFrames")]

    num_inference_steps: Annotated[Optional[int], PropertyInfo(alias="numInferenceSteps")]

    num_videos_per_prompt: Annotated[Optional[int], PropertyInfo(alias="numVideosPerPrompt")]
