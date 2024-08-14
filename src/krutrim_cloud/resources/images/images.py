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

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self)


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self)


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._images.generations)


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._images.generations)


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._images.generations)


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._images.generations)
