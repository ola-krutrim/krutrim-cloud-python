# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import os
import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.inference.checkpoint_del_response import CheckpointDelResponse
from ...types.inference.checkpoint_list_response import CheckpointListResponse
from ...types.inference.checkpoint_retrieve_response import CheckpointRetrieveResponse

__all__ = ["CheckpointsResource", "AsyncCheckpointsResource"]


class CheckpointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return CheckpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return CheckpointsResourceWithStreamingResponse(self)

    def _validate_retrieve_parameters(self, filename):
        # Validate 'filename'
        if filename is None or not isinstance(filename, str) or not filename.strip() or len(filename) == 0:
            raise ValueError("Invalid 'filename': It must be a non-empty string and not None.")
    
    def _validate_delete_parameters(self, filename):
        # Validate 'filename'
        if filename is None or not isinstance(filename, str) or not filename.strip() or len(filename) == 0:
            raise ValueError("Invalid 'filename': It must be a non-empty string and not None.")

    def retrieve(
        self,
        filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckpointRetrieveResponse:
        """
        Get inference task information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_retrieve_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/inference/checkpoints/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckpointRetrieveResponse,
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
    ) -> CheckpointListResponse:
        """
        List all fine_tuning checkpoints.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v1/inference/checkpoints",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckpointListResponse,
        )

    def delete(
        self,
        filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckpointDelResponse:
        """
        Delete the checkpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_delete_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/inference/checkpoints/{filename}/del",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckpointDelResponse,
        )


class AsyncCheckpointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return AsyncCheckpointsResourceWithStreamingResponse(self)

    async def _validate_retrieve_parameters(self, filename):
        # Validate 'filename'
        if filename is None or not isinstance(filename, str) or not filename.strip() or len(filename) == 0:
            raise ValueError("Invalid 'filename': It must be a non-empty string and not None.")

    async def _validate_delete_parameters(self, filename):
        # Validate 'filename'
        if filename is None or not isinstance(filename, str) or not filename.strip() or len(filename) == 0:
            raise ValueError("Invalid 'filename': It must be a non-empty string and not None.")

    async def retrieve(
        self,
        filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckpointRetrieveResponse:
        """
        Get inference task information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_retrieve_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/inference/checkpoints/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckpointRetrieveResponse,
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
    ) -> CheckpointListResponse:
        """
        List all fine_tuning checkpoints.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/v1/inference/checkpoints",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckpointListResponse,
        )

    async def delete(
        self,
        filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckpointDelResponse:
        """
        Delete the checkpoint

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_delete_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/inference/checkpoints/{filename}/del",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckpointDelResponse,
        )


class CheckpointsResourceWithRawResponse:
    def __init__(self, checkpoints: CheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = to_raw_response_wrapper(
            checkpoints.retrieve,
        )
        self.list = to_raw_response_wrapper(
            checkpoints.list,
        )
        self.delete = to_raw_response_wrapper(
            checkpoints.delete,
        )


class AsyncCheckpointsResourceWithRawResponse:
    def __init__(self, checkpoints: AsyncCheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = async_to_raw_response_wrapper(
            checkpoints.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            checkpoints.list,
        )
        self.delete = async_to_raw_response_wrapper(
            checkpoints.delete,
        )


class CheckpointsResourceWithStreamingResponse:
    def __init__(self, checkpoints: CheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = to_streamed_response_wrapper(
            checkpoints.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            checkpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            checkpoints.delete,
        )


class AsyncCheckpointsResourceWithStreamingResponse:
    def __init__(self, checkpoints: AsyncCheckpointsResource) -> None:
        self._checkpoints = checkpoints

        self.retrieve = async_to_streamed_response_wrapper(
            checkpoints.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            checkpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            checkpoints.delete,
        )
