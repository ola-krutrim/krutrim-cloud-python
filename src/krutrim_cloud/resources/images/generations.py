# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.images import generation_diffusion_params
from ...types.images.stable_diffusion_response import StableDiffusionResponse

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        model_name: str,
        guidance_scale: float | Union[object, None],
        image_height: int,
        image_width: int,
        negative_prompt: Union[str, List[str], None] | Union[object, None],
        negative_prompt2: Union[str, List[str], None] | Union[object, None],
        num_inference_steps: int | Union[object, None],
        num_output_images: Optional[int] | Union[object, None],
        output_img_type: Optional[str] | Union[object, None],
        prompt: Union[str, List[str]] | Union[object, None],
        prompt2: Union[str, List[str], None] | Union[object, None],
        seed: Optional[int] | Union[object, None],
        timeout: Union[float, httpx.Timeout, None, object],
    ):
        # Validate model_name
        if not isinstance(model_name, str):  # type: ignore
            raise ValueError("'model_name' must be a string.")
        if not model_name:
            raise ValueError("'model_name' cannot be empty.")

        # Validate guidance_scale
        if guidance_scale is not NOT_GIVEN:
            if not isinstance(guidance_scale, (float, int)):
                raise ValueError("'guidance_scale' must be a float.")
            if not (0 < guidance_scale < 20):
                raise ValueError("'guidance_scale' must be greater than 0 and less than 20.")

        # Validate image_height
        if not isinstance(image_height, int):  # type: ignore
            raise ValueError("'image_height' must be an integer.")
        if not (8 <= image_height <= 1024):
            raise ValueError("'image_height' must be between 8 and 1024.")

        # Validate image_width
        if not isinstance(image_width, int):  # type: ignore
            raise ValueError("'image_width' must be an integer.")
        if not (8 <= image_width <= 1024):
            raise ValueError("'image_width' must be between 8 and 1024.")

        # Validate negative_prompt
        if negative_prompt is not NOT_GIVEN:
            if not isinstance(negative_prompt, (str, list)):
                raise ValueError("'negative_prompt' must be a string or a list of strings.")
            if isinstance(negative_prompt, list) and not all(
                isinstance(p, str) for p in negative_prompt  # type: ignore
            ):  # type : ignore
                raise ValueError("All items in 'negative_prompt' must be strings.")

        # Validate negative_prompt2
        if negative_prompt2 is not NOT_GIVEN:
            if not isinstance(negative_prompt2, (str, list)):
                raise ValueError("'negative_prompt2' must be a string or a list of strings.")
            if isinstance(negative_prompt2, list) and not all(
                isinstance(p, str) for p in negative_prompt2  # type: ignore
            ):
                raise ValueError("All items in 'negative_prompt2' must be strings.")

        # Validate num_inference_steps
        if num_inference_steps is not NOT_GIVEN:
            if not isinstance(num_inference_steps, int):
                raise ValueError("'num_inference_steps' must be an integer.")
            if not (1 <= num_inference_steps <= 100):
                raise ValueError("'num_inference_steps' must be between 1 and 100.")

        # Validate num_output_images
        if num_output_images is not NOT_GIVEN:
            if not isinstance(num_output_images, int):
                raise ValueError("'num_output_images' must be an integer.")
            if not (1 <= num_output_images <= 5):
                raise ValueError("'num_output_images' must be between 1 and 5.")

        # Validate output_img_type
        if output_img_type is not NOT_GIVEN:
            if output_img_type not in (None, "pil", "latent"):
                raise ValueError("'output_img_type' must be 'pil', 'latent', or None.")

        # Validate prompt
        if prompt is not NOT_GIVEN:
            if not isinstance(prompt, (str, list)):
                raise ValueError("'prompt' must be a string or a list of strings.")
            if isinstance(prompt, list) and not all(isinstance(p, str) for p in prompt):  # type: ignore
                raise ValueError("All items in 'prompt' must be strings.")

        # Validate prompt2
        if prompt2 is not NOT_GIVEN:
            if not isinstance(prompt2, (str, list)):
                raise ValueError("'prompt2' must be a string or a list of strings.")
            if isinstance(prompt2, list) and not all(isinstance(p, str) for p in prompt2):  # type: ignore
                raise ValueError("All items in 'prompt2' must be strings.")

        # Validate seed
        if seed is not NOT_GIVEN:
            if not isinstance(seed, int):
                raise ValueError("'seed' must be an integer.")
            if seed <= 0:
                raise ValueError("'seed' must be greater than 0.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def diffusion(
        self,
        *,
        model_name: str,
        guidance_scale: float | NotGiven = NOT_GIVEN,
        image_height: int,
        image_width: int,
        negative_prompt: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        negative_prompt2: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        num_inference_steps: int | NotGiven = NOT_GIVEN,
        num_output_images: Optional[int] | NotGiven = NOT_GIVEN,
        output_img_type: Optional[str] | NotGiven = NOT_GIVEN,
        prompt: Union[str, List[str]],
        prompt2: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StableDiffusionResponse:
        """
        Generate Image

        Args:

            model_name: str: "diffusion1XL", # DO NOT CHANGE THIS VALUE

            prompt: str or List[str]: Specify the prompt

            prompt2: str or List[str]: Optional -  Specify any additional prompt details if required

            image_height: int: 1024, # 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well

            image_width: int : 1024, # 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well

            negative_prompt: str or List[str]: Optional, mention aspects (if any) to be ignored in the output image

            negative_prompt2: stror List[str]: Optional, mention aspects (if any) to be ignored in the output image

            num_output_images: int: Optional, Defaults to 1. Max value is 5.

            guidance_scale: float: Optional, Defaults to 5. Optimal values are < 15.

            num_inference_steps: int: Optional, Defaults to 50. Max value is 100.

            seed: int: Optional -  Leave it empty to generate a random value. Use the same value if you wish to get the same image. Modify the remaining parameters to get variants of the image

            output_img_type: str: Optional, Defaults to pil. Supported: pil, latent.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """

        self.validate_parameters(
            model_name=model_name,
            guidance_scale=guidance_scale,
            image_height=image_height,
            image_width=image_width,
            negative_prompt=negative_prompt,
            negative_prompt2=negative_prompt2,
            num_inference_steps=num_inference_steps,
            num_output_images=num_output_images,
            output_img_type=output_img_type,
            prompt=prompt,
            prompt2=prompt2,
            seed=seed,
            timeout=timeout,
        )

        return self._post(
            "/v1/images/generations/diffusion",
            body=maybe_transform(
                {
                    "model_name": model_name,
                    "guidance_scale": guidance_scale,
                    "image_height": image_height,
                    "image_width": image_width,
                    "negative_prompt": negative_prompt,
                    "negative_prompt2": negative_prompt2,
                    "num_inference_steps": num_inference_steps,
                    "num_output_images": num_output_images,
                    "output_img_type": output_img_type,
                    "prompt": prompt,
                    "prompt2": prompt2,
                    "seed": seed,
                },
                generation_diffusion_params.GenerationDiffusionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StableDiffusionResponse,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        model_name: str,
        guidance_scale: float | Union[object, None],
        image_height: int,
        image_width: int,
        negative_prompt: Union[str, List[str], None] | Union[object, None],
        negative_prompt2: Union[str, List[str], None] | Union[object, None],
        num_inference_steps: int | Union[object, None],
        num_output_images: Optional[int] | Union[object, None],
        output_img_type: Optional[str] | Union[object, None],
        prompt: Union[str, List[str]] | Union[object, None],
        prompt2: Union[str, List[str], None] | Union[object, None],
        seed: Optional[int] | Union[object, None],
        timeout: Union[float, httpx.Timeout, None, object],
    ):
        # Validate model_name
        if not isinstance(model_name, str):  # type: ignore
            raise ValueError("'model_name' must be a string.")
        if not model_name:
            raise ValueError("'model_name' cannot be empty.")

        # Validate guidance_scale
        if guidance_scale is not NOT_GIVEN:
            if not isinstance(guidance_scale, (float, int)):
                raise ValueError("'guidance_scale' must be a float.")
            if not (0 < guidance_scale < 20):
                raise ValueError("'guidance_scale' must be greater than 0 and less than 20.")

        # Validate image_height
        if not isinstance(image_height, int):  # type: ignore
            raise ValueError("'image_height' must be an integer.")
        if not (8 <= image_height <= 1024):
            raise ValueError("'image_height' must be between 8 and 1024.")

        # Validate image_width
        if not isinstance(image_width, int):  # type: ignore
            raise ValueError("'image_width' must be an integer.")
        if not (8 <= image_width <= 1024):
            raise ValueError("'image_width' must be between 8 and 1024.")

        # Validate negative_prompt
        if negative_prompt is not NOT_GIVEN:
            if not isinstance(negative_prompt, (str, list)):
                raise ValueError("'negative_prompt' must be a string or a list of strings.")
            if isinstance(negative_prompt, list) and not all(
                isinstance(p, str) for p in negative_prompt  # type: ignore
            ):
                raise ValueError("All items in 'negative_prompt' must be strings.")

        # Validate negative_prompt2
        if negative_prompt2 is not NOT_GIVEN:
            if not isinstance(negative_prompt2, (str, list)):
                raise ValueError("'negative_prompt2' must be a string or a list of strings.")
            if isinstance(negative_prompt2, list) and not all(
                isinstance(p, str) for p in negative_prompt2  # type: ignore
            ):
                raise ValueError("All items in 'negative_prompt2' must be strings.")

        # Validate num_inference_steps
        if num_inference_steps is not NOT_GIVEN:
            if not isinstance(num_inference_steps, int):
                raise ValueError("'num_inference_steps' must be an integer.")
            if not (1 <= num_inference_steps <= 100):
                raise ValueError("'num_inference_steps' must be between 1 and 100.")

        # Validate num_output_images
        if num_output_images is not NOT_GIVEN:
            if not isinstance(num_output_images, int):
                raise ValueError("'num_output_images' must be an integer.")
            if not (1 <= num_output_images <= 5):
                raise ValueError("'num_output_images' must be between 1 and 5.")

        # Validate output_img_type
        if output_img_type is not NOT_GIVEN:
            if output_img_type not in (None, "pil", "latent"):
                raise ValueError("'output_img_type' must be 'pil', 'latent', or None.")

        # Validate prompt
        if prompt is not NOT_GIVEN:
            if not isinstance(prompt, (str, list)):
                raise ValueError("'prompt' must be a string or a list of strings.")
            if isinstance(prompt, list) and not all(isinstance(p, str) for p in prompt):  # type: ignore
                raise ValueError("All items in 'prompt' must be strings.")

        # Validate prompt2
        if prompt2 is not NOT_GIVEN:
            if not isinstance(prompt2, (str, list)):
                raise ValueError("'prompt2' must be a string or a list of strings.")
            if isinstance(prompt2, list) and not all(isinstance(p, str) for p in prompt2):  # type: ignore
                raise ValueError("All items in 'prompt2' must be strings.")

        # Validate seed
        if seed is not NOT_GIVEN:
            if not isinstance(seed, int):
                raise ValueError("'seed' must be an integer.")
            if seed <= 0:
                raise ValueError("'seed' must be greater than 0.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def diffusion(
        self,
        *,
        model_name: str,
        guidance_scale: float | NotGiven = NOT_GIVEN,
        image_height: int,
        image_width: int,
        negative_prompt: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        negative_prompt2: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        num_inference_steps: int | NotGiven = NOT_GIVEN,
        num_output_images: Optional[int] | NotGiven = NOT_GIVEN,
        output_img_type: Optional[str] | NotGiven = NOT_GIVEN,
        prompt: Union[str, List[str]],
        prompt2: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StableDiffusionResponse:
        """
        Generate Image

        Args:
            model_name: str: "diffusion1XL", # DO NOT CHANGE THIS VALUE

            prompt: str or List[str]: Specify the prompt

            prompt2: str or List[str]: Optional -  Specify any additional prompt details if required

            image_height: int: 1024, # 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well

            image_width: int : 1024, # 1024 gives the best output. Although, modify this based on your requirement. Range: 8 to 1024. Although, anything below 512 pixels won't work well

            negative_prompt: str or List[str]: Optional, mention aspects (if any) to be ignored in the output image

            negative_prompt2: stror List[str]: Optional, mention aspects (if any) to be ignored in the output image

            num_output_images: int: Optional, Defaults to 1. Max value is 5.

            guidance_scale: float: Optional, Defaults to 5. Optimal values are < 15.

            num_inference_steps: int: Optional, Defaults to 50. Max value is 100.

            seed: int: Optional -  Leave it empty to generate a random value. Use the same value if you wish to get the same image. Modify the remaining parameters to get variants of the image

            output_img_type: str: Optional, Defaults to pil. Supported: pil, latent.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """

        await self.validate_parameters(
            model_name=model_name,
            guidance_scale=guidance_scale,
            image_height=image_height,
            image_width=image_width,
            negative_prompt=negative_prompt,
            negative_prompt2=negative_prompt2,
            num_inference_steps=num_inference_steps,
            num_output_images=num_output_images,
            output_img_type=output_img_type,
            prompt=prompt,
            prompt2=prompt2,
            seed=seed,
            timeout=timeout,
        )

        return await self._post(
            "/v1/images/generations/diffusion",
            body=await async_maybe_transform(
                {
                    "model_name": model_name,
                    "guidance_scale": guidance_scale,
                    "image_height": image_height,
                    "image_width": image_width,
                    "negative_prompt": negative_prompt,
                    "negative_prompt2": negative_prompt2,
                    "num_inference_steps": num_inference_steps,
                    "num_output_images": num_output_images,
                    "output_img_type": output_img_type,
                    "prompt": prompt,
                    "prompt2": prompt2,
                    "seed": seed,
                },
                generation_diffusion_params.GenerationDiffusionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StableDiffusionResponse,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.diffusion = to_raw_response_wrapper(
            generations.diffusion,
        )


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.diffusion = async_to_raw_response_wrapper(
            generations.diffusion,
        )


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.diffusion = to_streamed_response_wrapper(
            generations.diffusion,
        )


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.diffusion = async_to_streamed_response_wrapper(
            generations.diffusion,
        )
