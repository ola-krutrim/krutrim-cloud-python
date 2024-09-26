# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from .....types.fine_tuning.engines.model.mode_retrieve_response import ModeRetrieveResponse

__all__ = ["ModeResource", "AsyncModeResource"]


class ModeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return ModeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return ModeResourceWithStreamingResponse(self)

    def _validate_retrieve_parameters(self, mode: str, model: str):
        # Validate mode
        if mode and not isinstance(mode, str):
            raise TypeError("'mode' must be of type string.")
        # Validate model
        if model and not isinstance(model, str):
            raise TypeError("'model' must be of type string.")

    def retrieve(
        self,
        mode: str,
        *,
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModeRetrieveResponse:
    
        """
        List fine_tuning engine(framework) by the given model and mode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_retrieve_parameters(mode=mode, model=model)
        if not model:
            raise ValueError(f"Expected a non-empty value for `model` but received {model!r}")
        if not mode:
            raise ValueError(f"Expected a non-empty value for `mode` but received {mode!r}")
        return self._get(
            f"/api/v1/fine_tuning/engines/{model}/{mode}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeRetrieveResponse,
        )


class AsyncModeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncModeResourceWithStreamingResponse(self)

    async def _validate_retrieve_parameters(self, mode: str, model: str):
        # Validate mode
        if mode and not isinstance(mode, str):
            raise TypeError("'mode' must be of type string.")
        # Validate model
        if model and not isinstance(model, str):
            raise TypeError("'model' must be of type string.")

    async def retrieve(
        self,
        mode: str,
        *,
        model: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModeRetrieveResponse:
        """
        List fine_tuning engine(framework) by the given model and mode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_retrieve_parameters(mode=mode, model=model)

        if not model:
            raise ValueError(f"Expected a non-empty value for `model` but received {model!r}")
        if not mode:
            raise ValueError(f"Expected a non-empty value for `mode` but received {mode!r}")
        return await self._get(
            f"/api/v1/fine_tuning/engines/{model}/{mode}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModeRetrieveResponse,
        )


class ModeResourceWithRawResponse:
    def __init__(self, mode: ModeResource) -> None:
        self._mode = mode

        self.retrieve = to_raw_response_wrapper(
            mode.retrieve,
        )


class AsyncModeResourceWithRawResponse:
    def __init__(self, mode: AsyncModeResource) -> None:
        self._mode = mode

        self.retrieve = async_to_raw_response_wrapper(
            mode.retrieve,
        )


class ModeResourceWithStreamingResponse:
    def __init__(self, mode: ModeResource) -> None:
        self._mode = mode

        self.retrieve = to_streamed_response_wrapper(
            mode.retrieve,
        )


class AsyncModeResourceWithStreamingResponse:
    def __init__(self, mode: AsyncModeResource) -> None:
        self._mode = mode

        self.retrieve = async_to_streamed_response_wrapper(
            mode.retrieve,
        )
