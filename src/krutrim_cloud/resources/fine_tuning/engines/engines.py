# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .model import (
    ModelResource,
    AsyncModelResource,
    ModelResourceWithRawResponse,
    AsyncModelResourceWithRawResponse,
    ModelResourceWithStreamingResponse,
    AsyncModelResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from .model.model import ModelResource, AsyncModelResource
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.fine_tuning.engine_list_response import EngineListResponse

__all__ = ["EnginesResource", "AsyncEnginesResource"]


class EnginesResource(SyncAPIResource):
    @cached_property
    def model(self) -> ModelResource:
        return ModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnginesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return EnginesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnginesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return EnginesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EngineListResponse:
        """List fine_tuning engine(framework) name"""
        return self._get(
            "/api/v1/fine_tuning/engines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineListResponse,
        )


class AsyncEnginesResource(AsyncAPIResource):
    @cached_property
    def model(self) -> AsyncModelResource:
        return AsyncModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnginesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnginesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnginesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncEnginesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EngineListResponse:
        """List fine_tuning engine(framework) name"""
        return await self._get(
            "/api/v1/fine_tuning/engines",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EngineListResponse,
        )


class EnginesResourceWithRawResponse:
    def __init__(self, engines: EnginesResource) -> None:
        self._engines = engines

        self.list = to_raw_response_wrapper(
            engines.list,
        )

    @cached_property
    def model(self) -> ModelResourceWithRawResponse:
        return ModelResourceWithRawResponse(self._engines.model)


class AsyncEnginesResourceWithRawResponse:
    def __init__(self, engines: AsyncEnginesResource) -> None:
        self._engines = engines

        self.list = async_to_raw_response_wrapper(
            engines.list,
        )

    @cached_property
    def model(self) -> AsyncModelResourceWithRawResponse:
        return AsyncModelResourceWithRawResponse(self._engines.model)


class EnginesResourceWithStreamingResponse:
    def __init__(self, engines: EnginesResource) -> None:
        self._engines = engines

        self.list = to_streamed_response_wrapper(
            engines.list,
        )

    @cached_property
    def model(self) -> ModelResourceWithStreamingResponse:
        return ModelResourceWithStreamingResponse(self._engines.model)


class AsyncEnginesResourceWithStreamingResponse:
    def __init__(self, engines: AsyncEnginesResource) -> None:
        self._engines = engines

        self.list = async_to_streamed_response_wrapper(
            engines.list,
        )

    @cached_property
    def model(self) -> AsyncModelResourceWithStreamingResponse:
        return AsyncModelResourceWithStreamingResponse(self._engines.model)
