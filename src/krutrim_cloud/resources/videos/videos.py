# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .generations import (
    GenerationsResource,
    AsyncGenerationsResource,
    GenerationsResourceWithRawResponse,
    AsyncGenerationsResourceWithRawResponse,
    GenerationsResourceWithStreamingResponse,
    AsyncGenerationsResourceWithStreamingResponse,
)
from .generations.generations import GenerationsResource, AsyncGenerationsResource

__all__ = ["VideosResource", "AsyncVideosResource"]


class VideosResource(SyncAPIResource):
    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#accessing-raw-response-data-eg-headers
        """
        return VideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#with_streaming_response
        """
        return VideosResourceWithStreamingResponse(self)


class AsyncVideosResource(AsyncAPIResource):
    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVideosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVideosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVideosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/cogvideo-python#with_streaming_response
        """
        return AsyncVideosResourceWithStreamingResponse(self)


class VideosResourceWithRawResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._videos.generations)


class AsyncVideosResourceWithRawResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._videos.generations)


class VideosResourceWithStreamingResponse:
    def __init__(self, videos: VideosResource) -> None:
        self._videos = videos

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._videos.generations)


class AsyncVideosResourceWithStreamingResponse:
    def __init__(self, videos: AsyncVideosResource) -> None:
        self._videos = videos

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._videos.generations)
