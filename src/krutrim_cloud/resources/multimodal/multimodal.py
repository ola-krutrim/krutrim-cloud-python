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

__all__ = ["MultimodalResource", "AsyncMultimodalResource"]


class MultimodalResource(SyncAPIResource):
    @cached_property
    def generations(self) -> GenerationsResource:
        return GenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MultimodalResourceWithRawResponse:
        return MultimodalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MultimodalResourceWithStreamingResponse:
        return MultimodalResourceWithStreamingResponse(self)


class AsyncMultimodalResource(AsyncAPIResource):
    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        return AsyncGenerationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMultimodalResourceWithRawResponse:
        return AsyncMultimodalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMultimodalResourceWithStreamingResponse:
        return AsyncMultimodalResourceWithStreamingResponse(self)


class MultimodalResourceWithRawResponse:
    def __init__(self, multimodal: MultimodalResource) -> None:
        self._multimodal = multimodal

    @cached_property
    def generations(self) -> GenerationsResourceWithRawResponse:
        return GenerationsResourceWithRawResponse(self._multimodal.generations)


class AsyncMultimodalResourceWithRawResponse:
    def __init__(self, multimodal: AsyncMultimodalResource) -> None:
        self._multimodal = multimodal

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithRawResponse:
        return AsyncGenerationsResourceWithRawResponse(self._multimodal.generations)


class MultimodalResourceWithStreamingResponse:
    def __init__(self, multimodal: MultimodalResource) -> None:
        self._multimodal = multimodal

    @cached_property
    def generations(self) -> GenerationsResourceWithStreamingResponse:
        return GenerationsResourceWithStreamingResponse(self._multimodal.generations)


class AsyncMultimodalResourceWithStreamingResponse:
    def __init__(self, multimodal: AsyncMultimodalResource) -> None:
        self._multimodal = multimodal

    @cached_property
    def generations(self) -> AsyncGenerationsResourceWithStreamingResponse:
        return AsyncGenerationsResourceWithStreamingResponse(self._multimodal.generations)
