# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from .text2video import (
    Text2videoResource,
    AsyncText2videoResource,
    Text2videoResourceWithRawResponse,
    AsyncText2videoResourceWithRawResponse,
    Text2videoResourceWithStreamingResponse,
    AsyncText2videoResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def text2video(self) -> Text2videoResource:
        return Text2videoResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#accessing-raw-response-data-eg-headers
        """
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#with_streaming_response
        """
        return GenerationsResourceWithStreamingResponse(self)


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def text2video(self) -> AsyncText2videoResource:
        return AsyncText2videoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#with_streaming_response
        """
        return AsyncGenerationsResourceWithStreamingResponse(self)


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

    @cached_property
    def text2video(self) -> Text2videoResourceWithRawResponse:
        return Text2videoResourceWithRawResponse(self._generations.text2video)


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

    @cached_property
    def text2video(self) -> AsyncText2videoResourceWithRawResponse:
        return AsyncText2videoResourceWithRawResponse(self._generations.text2video)


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

    @cached_property
    def text2video(self) -> Text2videoResourceWithStreamingResponse:
        return Text2videoResourceWithStreamingResponse(self._generations.text2video)


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

    @cached_property
    def text2video(self) -> AsyncText2videoResourceWithStreamingResponse:
        return AsyncText2videoResourceWithStreamingResponse(self._generations.text2video)
