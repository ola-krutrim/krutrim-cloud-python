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
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.fine_tuning.engines.model_retrieve_response import ModelRetrieveResponse

__all__ = ["ModelResource", "AsyncModelResource"]


class ModelResource(SyncAPIResource):
    @cached_property
    def mode(self) -> ModeResource:
        return ModeResource(self._client)

    @cached_property
    def with_raw_response(self) -> ModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return ModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return ModelResourceWithStreamingResponse(self)

    def _validate_retrieve_paramaters(self, model: str):
         # Validate model
        if model and not isinstance(model, str):
            raise TypeError("'model' must be of type string.")

    def retrieve(
        self,
        model: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelRetrieveResponse:
        """
        List fine_tuning engine(framework) by the given model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_retrieve_paramaters(model=model)

        if not model:
            raise ValueError(f"Expected a non-empty value for `model` but received {model!r}")
        return self._get(
            f"/api/v1/fine_tuning/engines/{model}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRetrieveResponse,
        )


class AsyncModelResource(AsyncAPIResource):
    @cached_property
    def mode(self) -> AsyncModeResource:
        return AsyncModeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncModelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncModelResourceWithStreamingResponse(self)
    async def _validate_retrieve_paramaters(self, model: str):
        # Validate model
        if model and not isinstance(model, str):
            raise TypeError("'model' must be of type string.")

    async def retrieve(
        self,
        model: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelRetrieveResponse:
        """
        List fine_tuning engine(framework) by the given model.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_retrieve_paramaters(model=model)
        if not model:
            raise ValueError(f"Expected a non-empty value for `model` but received {model!r}")
        return await self._get(
            f"/api/v1/fine_tuning/engines/{model}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRetrieveResponse,
        )


class ModelResourceWithRawResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

        self.retrieve = to_raw_response_wrapper(
            model.retrieve,
        )

    @cached_property
    def mode(self) -> ModeResourceWithRawResponse:
        return ModeResourceWithRawResponse(self._model.mode)


class AsyncModelResourceWithRawResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

        self.retrieve = async_to_raw_response_wrapper(
            model.retrieve,
        )

    @cached_property
    def mode(self) -> AsyncModeResourceWithRawResponse:
        return AsyncModeResourceWithRawResponse(self._model.mode)


class ModelResourceWithStreamingResponse:
    def __init__(self, model: ModelResource) -> None:
        self._model = model

        self.retrieve = to_streamed_response_wrapper(
            model.retrieve,
        )

    @cached_property
    def mode(self) -> ModeResourceWithStreamingResponse:
        return ModeResourceWithStreamingResponse(self._model.mode)


class AsyncModelResourceWithStreamingResponse:
    def __init__(self, model: AsyncModelResource) -> None:
        self._model = model

        self.retrieve = async_to_streamed_response_wrapper(
            model.retrieve,
        )

    @cached_property
    def mode(self) -> AsyncModeResourceWithStreamingResponse:
        return AsyncModeResourceWithStreamingResponse(self._model.mode)
