# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .mode import (
    ModeResource,
    AsyncModeResource,
    ModeResourceWithRawResponse,
    AsyncModeResourceWithRawResponse,
    ModeResourceWithStreamingResponse,
    AsyncModeResourceWithStreamingResponse,
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
from ....types.fine_tuning.model_list_response import ModelListResponse
from ....types.fine_tuning.model_retrieve_response import ModelRetrieveResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def mode(self) -> ModeResource:
        return ModeResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)
    
    def _validate_retrieve_parameters(self, engine):
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
    ) -> ModelRetrieveResponse:
        """
        List all models supported by the given engine.

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
            f"/api/v1/fine_tuning/models/{engine}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRetrieveResponse,
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
    ) -> ModelListResponse:
        """List all supported models."""
        return self._get(
            "/api/v1/fine_tuning/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelListResponse,
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def mode(self) -> AsyncModeResource:
        return AsyncModeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)
    
    async def _validate_retrieve_parameters(self, engine):
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
    ) -> ModelRetrieveResponse:
        """
        List all models supported by the given engine.

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
            f"/api/v1/fine_tuning/models/{engine}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRetrieveResponse,
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
    ) -> ModelListResponse:
        """List all supported models."""
        return await self._get(
            "/api/v1/fine_tuning/models",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelListResponse,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.retrieve = to_raw_response_wrapper(
            models.retrieve,
        )
        self.list = to_raw_response_wrapper(
            models.list,
        )

    @cached_property
    def mode(self) -> ModeResourceWithRawResponse:
        return ModeResourceWithRawResponse(self._models.mode)


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.retrieve = async_to_raw_response_wrapper(
            models.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            models.list,
        )

    @cached_property
    def mode(self) -> AsyncModeResourceWithRawResponse:
        return AsyncModeResourceWithRawResponse(self._models.mode)


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.retrieve = to_streamed_response_wrapper(
            models.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            models.list,
        )

    @cached_property
    def mode(self) -> ModeResourceWithStreamingResponse:
        return ModeResourceWithStreamingResponse(self._models.mode)


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.retrieve = async_to_streamed_response_wrapper(
            models.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            models.list,
        )

    @cached_property
    def mode(self) -> AsyncModeResourceWithStreamingResponse:
        return AsyncModeResourceWithStreamingResponse(self._models.mode)
