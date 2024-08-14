# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GenerationDiffusionParams"]


class GenerationDiffusionParams(TypedDict, total=False):
    model_name: Required[Annotated[str, PropertyInfo(alias="modelName")]]

    guidance_scale: Annotated[float, PropertyInfo(alias="guidanceScale")]

    image_height: Annotated[Optional[int], PropertyInfo(alias="imageHeight")]

    image_width: Annotated[Optional[int], PropertyInfo(alias="imageWidth")]

    negative_prompt: Annotated[Union[str, List[str], None], PropertyInfo(alias="negativePrompt")]

    negative_prompt2: Annotated[Union[str, List[str], None], PropertyInfo(alias="negativePrompt2")]

    num_inference_steps: Annotated[int, PropertyInfo(alias="numInferenceSteps")]

    num_output_images: Annotated[Optional[int], PropertyInfo(alias="numOutputImages")]

    output_img_type: Annotated[Optional[str], PropertyInfo(alias="outputImgType")]

    prompt: Union[str, List[str]]

    prompt2: Union[str, List[str], None]

    seed: Optional[int]
