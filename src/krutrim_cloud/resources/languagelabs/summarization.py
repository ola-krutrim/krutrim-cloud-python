from __future__ import annotations
import httpx
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource,AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.languagelabs.summarization_response import SummarizationResponse as SummarizationResponse

__all__ = ["SummarizationResource", "AsyncSummarizationResource"]

class SummarizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummarizationResourceWithRawResponse:
        return SummarizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummarizationResourceWithStreamingResponse:
        return SummarizationResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        text: str,
        input_language: str,
        summary_size: int,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate input_language
        if not isinstance(input_language, str):
            raise TypeError("'input_language' must be a string.")
        if not input_language:
            raise ValueError("'input_language' cannot be empty.")

        # Validate summary_size
        if not isinstance(summary_size, int):
            raise TypeError("'summary_size' must be an integer.")
        if summary_size <= 0:
            raise ValueError("'summary_size' must be greater than 0.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
        self,
        *,
        text: str,
        input_language: str,
        summary_size: int,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizationResponse:
        """
        Summarize the given text.

        Args:
            text: The input text to summarize.
            input_language: The language of the text (e.g., "eng" for English).
            summary_size: The desired size of the summary (in terms of the number of sentences or tokens).
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        self.validate_parameters(text=text, input_language=input_language, summary_size=summary_size, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "input_language": input_language,
            "summary_size": summary_size,
        }

        # Send the request to the summarization API
        return self._post(
            "/api/v1/languagelabs/summarization",
            body=maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizationResponse,
        )


class AsyncSummarizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummarizationResourceWithRawResponse:
        return AsyncSummarizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummarizationResourceWithStreamingResponse:
        return AsyncSummarizationResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        text: str,
        input_language: str,
        summary_size: int,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate input_language
        if not isinstance(input_language, str):
            raise TypeError("'input_language' must be a string.")
        if not input_language:
            raise ValueError("'input_language' cannot be empty.")

        # Validate summary_size
        if not isinstance(summary_size, int):
            raise TypeError("'summary_size' must be an integer.")
        if summary_size <= 0:
            raise ValueError("'summary_size' must be greater than 0.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
        self,
        *,
        text: str,
        input_language: str,
        summary_size: int,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizationResponse:
        """
        Summarize the given text asynchronously.

        Args:
            text: The input text to summarize.
            input_language: The language of the text (e.g., "eng" for English).
            summary_size: The desired size of the summary (in terms of the number of sentences or tokens).
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        await self.validate_parameters(text=text, input_language=input_language, summary_size=summary_size, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "input_language": input_language,
            "summary_size": summary_size,
        }

        # Send the request to the summarization API
        return await self._post(
            "/api/v1/languagelabs/summarization",
            body=await async_maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizationResponse,
        )



class SummarizationResourceWithRawResponse:
    def __init__(self, summarization: SummarizationResource) -> None:
        self._summarization = summarization
        self.summarization = to_raw_response_wrapper(summarization.run)


class SummarizationResourceWithStreamingResponse:
    def __init__(self, summarization: SummarizationResource) -> None:
        self._summarization = summarization
        self.summarization = to_streamed_response_wrapper(summarization.run)


class AsyncSummarizationResourceWithRawResponse:
    def __init__(self, summarization: AsyncSummarizationResource) -> None:
        self._summarization = summarization
        self.summarization = async_to_raw_response_wrapper(summarization.run)


class AsyncSummarizationResourceWithStreamingResponse:
    def __init__(self, summarization: AsyncSummarizationResource) -> None:
        self._summarization = summarization
        self.summarization = async_to_streamed_response_wrapper(summarization.run)

