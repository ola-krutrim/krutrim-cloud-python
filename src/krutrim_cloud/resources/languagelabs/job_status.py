from __future__ import annotations
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
from ...types.languagelabs.job_status_response import JobStatusResponse as JobStatusResponse

__all__ = ["JobStatusResource", "AsyncJobStatusResource"]

class JobStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobStatusResourceWithRawResponse:
        return JobStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobStatusResourceWithStreamingResponse:
        return JobStatusResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        request_id: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate request_id
        if not isinstance(request_id, str):
            raise TypeError("'request_id' must be a string.")
        if not request_id:
            raise ValueError("'request_id' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
        self,
        *,
        request_id: str,
        # Optional additional parameters for extra headers, query, or body
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobStatusResponse:
        """
        Get Job Status (GET request)

        Args:
            request_id: The unique identifier for the job whose status is being requested.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request (ignored in GET requests)

            timeout: Override the client-level default timeout for this request, in seconds
        """
        self.validate_parameters(request_id=request_id, timeout=timeout)

        return self._get(
            f"/api/v1/languagelabs/job_status/{request_id}",  # Updated endpoint with request_id in the URL
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobStatusResponse,  # The response type for the job status
        )


class AsyncJobStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobStatusResourceWithRawResponse:
        return AsyncJobStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobStatusResourceWithStreamingResponse:
        return AsyncJobStatusResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        request_id: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate request_id
        if not isinstance(request_id, str):
            raise TypeError("'request_id' must be a string.")
        if not request_id:
            raise ValueError("'request_id' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
        self,
        *,
        request_id: str,
        # Optional additional parameters for extra headers, query, or body
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobStatusResponse:
        """
        Get Job Status (Asynchronous, GET request)

        Args:
            request_id: The unique identifier for the job whose status is being requested.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request (ignored in GET requests)

            timeout: Override the client-level default timeout for this request, in seconds
        """
        await self.validate_parameters(request_id=request_id, timeout=timeout)

        return await self._get(
            f"/api/v1/languagelabs/job_status/{request_id}",  # Updated endpoint with request_id in the URL
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobStatusResponse,  # The response type for the job status
        )


class JobStatusResourceWithRawResponse:
    def __init__(self, job_status: JobStatusResource) -> None:
        self._job_status = job_status
        self.job_status = to_raw_response_wrapper(job_status.run)


class AsyncJobStatusResourceWithRawResponse:
    def __init__(self, job_status: AsyncJobStatusResource) -> None:
        self._job_status = job_status
        self.job_status = async_to_raw_response_wrapper(job_status.run)


class JobStatusResourceWithStreamingResponse:
    def __init__(self, job_status: JobStatusResource) -> None:
        self._job_status = job_status
        self.job_status = to_streamed_response_wrapper(job_status.run)


class AsyncJobStatusResourceWithStreamingResponse:
    def __init__(self, job_status: AsyncJobStatusResource) -> None:
        self._job_status = job_status
        self.job_status = async_to_streamed_response_wrapper(job_status.run)
