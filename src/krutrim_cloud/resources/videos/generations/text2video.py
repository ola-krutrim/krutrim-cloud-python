# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.videos.generations import text2video_create_params
from ....types.videos.cog_video_response import CogVideoResponse

__all__ = ["Text2videoResource", "AsyncText2videoResource"]


class Text2videoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> Text2videoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#accessing-raw-response-data-eg-headers
        """
        return Text2videoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Text2videoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#with_streaming_response
        """
        return Text2videoResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        model_name: str,
        prompt: List[str],
        guidance_scale: Optional[int] | NotGiven = NOT_GIVEN,
        num_frames: Optional[int] | NotGiven = NOT_GIVEN,
        num_inference_steps: Optional[int] | NotGiven = NOT_GIVEN,
        num_videos_per_prompt: Optional[int] | NotGiven = NOT_GIVEN,
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
            if not (0 < guidance_scale < 15):
                raise ValueError("'guidance_scale' must be greater than 0 and less than 20.")

        # Validate prompt
        if not isinstance(prompt, list):
            raise ValueError("'prompt' must be a list containing a single string.")
        if len(prompt) != 1:
            raise ValueError("'prompt' must contain exactly one string.")
        if not isinstance(prompt[0], str):
            raise ValueError("The item in 'prompt' must be a string.")

        # Validate num_inference_steps
        if num_inference_steps is not NOT_GIVEN:
            if not isinstance(num_inference_steps, int):
                raise ValueError("'num_inference_steps' must be an integer.")
            if not (1 <= num_inference_steps <= 100):
                raise ValueError("'num_inference_steps' must be between 1 and 100 (inclusive).")

        # Validate num_videos_per_prompt
        if num_videos_per_prompt is not NOT_GIVEN:
            if not isinstance(num_videos_per_prompt, int):
                raise ValueError("'num_videos_per_prompt' must be an integer.")
            if num_videos_per_prompt != 1:
                raise ValueError("'num_videos_per_prompt' must be equal to 1.")

        # Validate num_frames
        if num_frames is not NOT_GIVEN:
            if not isinstance(num_frames, int):
                raise ValueError("'num_frames' must be an integer.")
            if not (10 <= num_frames <= 49):
                raise ValueError("'num_frames' must be between 10 and 49 (inclusive)")

    def create(
        self,
        *,
        model_name: str,
        prompt: List[str],
        guidance_scale: Optional[int] | NotGiven = NOT_GIVEN,
        num_frames: Optional[int] | NotGiven = NOT_GIVEN,
        num_inference_steps: Optional[int] | NotGiven = NOT_GIVEN,
        num_videos_per_prompt: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CogVideoResponse:
        """
        Generate Video From Text

        Args:
            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        self.validate_parameters(
            model_name=model_name,
            prompt=prompt,
            guidance_scale=guidance_scale,
            num_frames=num_frames,
            num_inference_steps=num_inference_steps,
            num_videos_per_prompt=num_videos_per_prompt,
        )
        return self._post(
            "/v1/videos/generations/text2video",
            body=maybe_transform(
                {
                    "model_name": model_name,
                    "prompt": prompt,
                    "guidance_scale": guidance_scale,
                    "num_frames": num_frames,
                    "num_inference_steps": num_inference_steps,
                    "num_videos_per_prompt": num_videos_per_prompt,
                },
                text2video_create_params.Text2videoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CogVideoResponse,
        )


class AsyncText2videoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncText2videoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#accessing-raw-response-data-eg-headers
        """
        return AsyncText2videoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncText2videoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#with_streaming_response
        """
        return AsyncText2videoResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        model_name: str,
        prompt: List[str],
        guidance_scale: Optional[int] | NotGiven = NOT_GIVEN,
        num_frames: Optional[int] | NotGiven = NOT_GIVEN,
        num_inference_steps: Optional[int] | NotGiven = NOT_GIVEN,
        num_videos_per_prompt: Optional[int] | NotGiven = NOT_GIVEN,
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
            if not (0 < guidance_scale < 15):
                raise ValueError("'guidance_scale' must be greater than 0 and less than 20.")

        # Validate prompt
        if not isinstance(prompt, list):
            raise ValueError("'prompt' must be a list containing a single string.")
        if len(prompt) != 1:
            raise ValueError("'prompt' must contain exactly one string.")
        if not isinstance(prompt[0], str):
            raise ValueError("The item in 'prompt' must be a string.")

        # Validate num_inference_steps
        if num_inference_steps is not NOT_GIVEN:
            if not isinstance(num_inference_steps, int):
                raise ValueError("'num_inference_steps' must be an integer.")
            if not (1 <= num_inference_steps <= 100):
                raise ValueError("'num_inference_steps' must be between 1 and 100 (inclusive).")

        # Validate num_videos_per_prompt
        if num_videos_per_prompt is not NOT_GIVEN:
            if not isinstance(num_videos_per_prompt, int):
                raise ValueError("'num_videos_per_prompt' must be an integer.")
            if num_videos_per_prompt != 1:
                raise ValueError("'num_videos_per_prompt' must be equal to 1.")

        # Validate num_frames
        if num_frames is not NOT_GIVEN:
            if not isinstance(num_frames, int):
                raise ValueError("'num_frames' must be an integer.")
            if not (10 <= num_frames <= 49):
                raise ValueError("'num_frames' must be between 10 and 49 (inclusive)")

    async def create(
        self,
        *,
        model_name: str,
        prompt: List[str],
        guidance_scale: Optional[int] | NotGiven = NOT_GIVEN,
        num_frames: Optional[int] | NotGiven = NOT_GIVEN,
        num_inference_steps: Optional[int] | NotGiven = NOT_GIVEN,
        num_videos_per_prompt: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CogVideoResponse:
        """
        Generate Video From Text

        Args:
            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        await self.validate_parameters(
            model_name=model_name,
            prompt=prompt,
            guidance_scale=guidance_scale,
            num_frames=num_frames,
            num_inference_steps=num_inference_steps,
            num_videos_per_prompt=num_videos_per_prompt,
        )
        return await self._post(
            "/v1/videos/generations/text2video",
            body=await async_maybe_transform(
                {
                    "model_name": model_name,
                    "prompt": prompt,
                    "guidance_scale": guidance_scale,
                    "num_frames": num_frames,
                    "num_inference_steps": num_inference_steps,
                    "num_videos_per_prompt": num_videos_per_prompt,
                },
                text2video_create_params.Text2videoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CogVideoResponse,
        )


class Text2videoResourceWithRawResponse:
    def __init__(self, text2video: Text2videoResource) -> None:
        self._text2video = text2video

        self.create = to_raw_response_wrapper(
            text2video.create,
        )


class AsyncText2videoResourceWithRawResponse:
    def __init__(self, text2video: AsyncText2videoResource) -> None:
        self._text2video = text2video

        self.create = async_to_raw_response_wrapper(
            text2video.create,
        )


class Text2videoResourceWithStreamingResponse:
    def __init__(self, text2video: Text2videoResource) -> None:
        self._text2video = text2video

        self.create = to_streamed_response_wrapper(
            text2video.create,
        )


class AsyncText2videoResourceWithStreamingResponse:
    def __init__(self, text2video: AsyncText2videoResource) -> None:
        self._text2video = text2video

        self.create = async_to_streamed_response_wrapper(
            text2video.create,
        )
