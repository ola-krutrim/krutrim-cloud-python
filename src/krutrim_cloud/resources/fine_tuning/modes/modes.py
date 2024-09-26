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
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.fine_tuning.mode_list_response import ModeListResponse
from ....types.fine_tuning.mode_retrieve_response import ModeRetrieveResponse

__all__ = ["ModesResource", "AsyncModesResource"]


class ModesResource(SyncAPIResource):
    @cached_property
    def model(self) -> ModelResource:
        return ModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return ModesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return ModesResourceWithStreamingResponse(self)
    
    def _validate_retrieve_parameters(self, engine: str):
        # Validate engine
        if engine and not isinstance(engine, str):
            raise TypeError("'engine' must be of type string.")

    def retrieve(
        self,
        engine: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModeRetrieveResponse:
        """
        List all modes supported by the given engine.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_retrieve_parameters(engine=engine)
        if not engine:
            raise ValueError(f"Expected a non-empty value for `engine` but received {engine!r}")
        return self._get(
            f"/api/v1/fine_tuning/modes/{engine}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModeListResponse:
        """List all supported fine_tuning modes."""
        return self._get(
            "/api/v1/fine_tuning/modes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeListResponse,
        )


class AsyncModesResource(AsyncAPIResource):
    @cached_property
    def model(self) -> AsyncModelResource:
        return AsyncModelResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncModesResourceWithStreamingResponse(self)
    
    async def _validate_retrieve_parameters(self, engine: str):
        # Validate engine
        if engine and not isinstance(engine, str):
            raise TypeError("'engine' must be of type string.")

    async def retrieve(
        self,
        engine: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModeRetrieveResponse:
        """
        List all modes supported by the given engine.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_retrieve_parameters(engine=engine)
        if not engine:
            raise ValueError(f"Expected a non-empty value for `engine` but received {engine!r}")
        return await self._get(
            f"/api/v1/fine_tuning/modes/{engine}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModeListResponse:
        """List all supported fine_tuning modes."""
        return await self._get(
            "/api/v1/fine_tuning/modes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeListResponse,
        )


class ModesResourceWithRawResponse:
    def __init__(self, modes: ModesResource) -> None:
        self._modes = modes

        self.retrieve = to_raw_response_wrapper(
            modes.retrieve,
        )
        self.list = to_raw_response_wrapper(
            modes.list,
        )

    @cached_property
    def model(self) -> ModelResourceWithRawResponse:
        return ModelResourceWithRawResponse(self._modes.model)


class AsyncModesResourceWithRawResponse:
    def __init__(self, modes: AsyncModesResource) -> None:
        self._modes = modes

        self.retrieve = async_to_raw_response_wrapper(
            modes.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            modes.list,
        )

    @cached_property
    def model(self) -> AsyncModelResourceWithRawResponse:
        return AsyncModelResourceWithRawResponse(self._modes.model)


class ModesResourceWithStreamingResponse:
    def __init__(self, modes: ModesResource) -> None:
        self._modes = modes

        self.retrieve = to_streamed_response_wrapper(
            modes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            modes.list,
        )

    @cached_property
    def model(self) -> ModelResourceWithStreamingResponse:
        return ModelResourceWithStreamingResponse(self._modes.model)


class AsyncModesResourceWithStreamingResponse:
    def __init__(self, modes: AsyncModesResource) -> None:
        self._modes = modes

        self.retrieve = async_to_streamed_response_wrapper(
            modes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            modes.list,
        )

    @cached_property
    def model(self) -> AsyncModelResourceWithStreamingResponse:
        return AsyncModelResourceWithStreamingResponse(self._modes.model)
