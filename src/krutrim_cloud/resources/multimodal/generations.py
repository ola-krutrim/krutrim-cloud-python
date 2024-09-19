# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
from typing import List, Iterable, Optional, Union

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
from ...types.multimodal import generation_idefics_params
from ...types.multimodal.idefics_response import IdeficsResponse

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
        prompts: List[str],
        images: Iterable[List[str]] | Union[object, None],
        max_tokens: Optional[int] | Union[object, None],
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate model_name
        if not isinstance(model_name, str):  # type: ignore
            raise TypeError("'model_name' must be a string.")
        if not model_name:
            raise ValueError("'model_name' cannot be empty.")

        # Validate prompts
        if not isinstance(prompts, Iterable):  # Check if 'prompts' is an iterable
            raise TypeError("'prompts' must be an iterable.")
        if not all(isinstance(item, dict) for item in prompts):  # Ensure all items are dictionaries
            raise TypeError("All items in 'prompts' must be dictionaries.")
        for item in prompts:
            if "role" not in item or not isinstance(item["role"], str):
                raise ValueError("Each dictionary in 'prompts' must contain a 'role' key with a string value.")
            if "content" not in item or not isinstance(item["content"], Iterable):
                raise ValueError("Each dictionary in 'prompts' must contain a 'content' key with an iterable value.")
            for content_item in item["content"]:
                if not isinstance(content_item, dict):
                    raise TypeError("Each item in 'content' must be a dictionary.")
                if "type" not in content_item or not isinstance(content_item["type"], str):
                    raise ValueError("Each dictionary in 'content' must contain a 'type' key with a string value.")
                if "text" in content_item and not isinstance(content_item["text"], str):
                    raise TypeError("If 'text' is present in 'content', it must be a string.")

        # Validate images
        if not isinstance(images, Iterable):
            raise TypeError("'images' must be an iterable of lists of strings.")
        if not all(isinstance(image_set, list) for image_set in images):  # type: ignore
            raise TypeError("All items in 'images' must be lists of strings.")
        if not all(all(isinstance(image, str) for image in image_set) for image_set in images):  # type: ignore
            raise ValueError("All items in the lists within 'images' must be strings.")

        # Validate max_tokens
        if max_tokens is not NOT_GIVEN:
            if not isinstance(max_tokens, int):
                raise ValueError(f"Expected 'max_tokens' to be of type int, but got {type(max_tokens).__name__}")
            if max_tokens < 8 or max_tokens > 1024:
                raise ValueError("Please provide 'max_tokens' value between 8 to 1024 (inclusive)")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def idefics(
        self,
        *,
        model_name: str,
        prompts: List[str],
        images: Iterable[List[str]],
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdeficsResponse:
        """
        Generate Text From Image

        Args:
            model_name:"idefics" # DO NOT CHANGE THIS VALUE

            prompts: list[
                {
                    "role": "User",  # The role of the entity providing the prompt.
                    "content": [
                        {"type": "image"},  # Placeholder for image content.
                        {"type": "text", "text": "What is the city??"}  # The text prompt/question related to the image.
                    ]
                }
            ]

            images: [
                [<encoded image bytes here>], # Refer to Fetch byte-content from Image section
            ]

            max_tokens: int: 50 - Max tokens can be generated [8 - 1024]

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """

        self.validate_parameters(model_name, prompts, images, max_tokens, timeout)

        return self._post(
            "/v1/multimodal/generations/idefics",
            body=maybe_transform(
                {
                    "model_name": model_name,
                    "prompts": prompts,
                    "images": images,
                    "max_tokens": max_tokens,
                },
                generation_idefics_params.GenerationIdeficsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdeficsResponse,
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
        prompts: List[str],
        images: Iterable[List[str]] | Union[object, None],
        max_tokens: Optional[int] | Union[object, None],
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate model_name
        if not isinstance(model_name, str):  # type: ignore
            raise TypeError("'model_name' must be a string.")
        if not model_name:
            raise ValueError("'model_name' cannot be empty.")

        # Validate prompts
        if not isinstance(prompts, Iterable):  # Check if 'prompts' is an iterable
            raise TypeError("'prompts' must be an iterable.")
        if not all(isinstance(item, dict) for item in prompts):  # Ensure all items are dictionaries
            raise TypeError("All items in 'prompts' must be dictionaries.")
        for item in prompts:
            if "role" not in item or not isinstance(item["role"], str):
                raise ValueError("Each dictionary in 'prompts' must contain a 'role' key with a string value.")
            if "content" not in item or not isinstance(item["content"], Iterable):
                raise ValueError("Each dictionary in 'prompts' must contain a 'content' key with an iterable value.")
            for content_item in item["content"]:
                if not isinstance(content_item, dict):
                    raise TypeError("Each item in 'content' must be a dictionary.")
                if "type" not in content_item or not isinstance(content_item["type"], str):
                    raise ValueError("Each dictionary in 'content' must contain a 'type' key with a string value.")
                if "text" in content_item and not isinstance(content_item["text"], str):
                    raise TypeError("If 'text' is present in 'content', it must be a string.")

        # Validate images
        if not isinstance(images, Iterable):
            raise TypeError("'images' must be an iterable of lists of strings.")
        if not all(isinstance(image_set, list) for image_set in images):  # type: ignore
            raise TypeError("All items in 'images' must be lists of strings.")
        if not all(all(isinstance(image, str) for image in image_set) for image_set in images):  # type: ignore
            raise ValueError("All items in the lists within 'images' must be strings.")

        # Validate max_tokens
        if max_tokens is not NOT_GIVEN:
            if not isinstance(max_tokens, int):
                raise ValueError(f"Expected 'max_tokens' to be of type int, but got {type(max_tokens).__name__}")
            if max_tokens < 8 or max_tokens > 1024:
                raise ValueError("Please provide 'max_tokens' value between 8 to 1024 (inclusive)")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def idefics(
        self,
        *,
        model_name: str,
        prompts: List[str],
        images: Iterable[List[str]] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdeficsResponse:
        """
        Generate Text From Image

        Args:
            model_name:"idefics" # DO NOT CHANGE THIS VALUE

            prompts: list[
                {
                    "role": "User",  # The role of the entity providing the prompt.
                    "content": [
                        {"type": "image"},  # Placeholder for image content.
                        {"type": "text", "text": "What is the city??"}  # The text prompt/question related to the image.
                    ]
                }
            ]

            images: [
                [<encoded image bytes here>], # Refer to Fetch byte-content from Image section
            ]

            max_tokens: int: 50 - Max tokens can be generated [8 - 1024]

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """

        await self.validate_parameters(model_name, prompts, images, max_tokens, timeout)

        return await self._post(
            "/v1/multimodal/generations/idefics",
            body=await async_maybe_transform(
                {
                    "model_name": model_name,
                    "prompts": prompts,
                    "images": images,
                    "max_tokens": max_tokens,
                },
                generation_idefics_params.GenerationIdeficsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdeficsResponse,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.idefics = to_raw_response_wrapper(
            generations.idefics,
        )


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.idefics = async_to_raw_response_wrapper(
            generations.idefics,
        )


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.idefics = to_streamed_response_wrapper(
            generations.idefics,
        )


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.idefics = async_to_streamed_response_wrapper(
            generations.idefics,
        )
