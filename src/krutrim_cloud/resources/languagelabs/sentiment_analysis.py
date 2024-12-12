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
from ...types.languagelabs.sentiment_analysis_response import SentimentAnalysisResponse as SentimentAnalysisResponse

__all__ = ["SentimentAnalysisResource", "AsyncSentimentAnalysisResource"]

class SentimentAnalysisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SentimentAnalysisResourceWithRawResponse:
        return SentimentAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SentimentAnalysisResourceWithStreamingResponse:
        return SentimentAnalysisResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        text: str,
        lang_from: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate lang_from
        if not isinstance(lang_from, str):
            raise TypeError("'lang_from' must be a string.")
        if not lang_from:
            raise ValueError("'lang_from' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
        self,
        *,
        text: str,
        lang_from: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SentimentAnalysisResponse:
        """
        Perform sentiment analysis on the given text.

        Args:
            text: The input text to analyze.
            lang_from: The language code (e.g., "eng").
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        self.validate_parameters(text=text, lang_from=lang_from, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "lang_from": lang_from,
        }

        # Send the request to the sentiment analysis API
        return self._post(
            "/api/v1/languagelabs/sentiment-analysis",
            body=maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SentimentAnalysisResponse,
        )



class AsyncSentimentAnalysisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSentimentAnalysisResourceWithRawResponse:
        return AsyncSentimentAnalysisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSentimentAnalysisResourceWithStreamingResponse:
        return AsyncSentimentAnalysisResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        text: str,
        lang_from: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate lang_from
        if not isinstance(lang_from, str):
            raise TypeError("'lang_from' must be a string.")
        if not lang_from:
            raise ValueError("'lang_from' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
        self,
        *,
        text: str,
        lang_from: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SentimentAnalysisResponse:
        """
        Perform sentiment analysis on the given text asynchronously.

        Args:
            text: The input text to analyze.
            lang_from: The language code (e.g., "eng").
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        await self.validate_parameters(text=text, lang_from=lang_from, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "lang_from": lang_from,
        }

        # Send the request to the sentiment analysis API
        return self._post(
            "/api/v1/languagelabs/sentiment-analysis",
            body=await async_maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SentimentAnalysisResponse,
        )


class SentimentAnalysisResourceWithRawResponse:
    def __init__(self, sentiment_analysis: SentimentAnalysisResource) -> None:
        self._sentiment_analysis = sentiment_analysis
        self.sentiment_analysis = to_raw_response_wrapper(sentiment_analysis.run)


class SentimentAnalysisResourceWithStreamingResponse:
    def __init__(self, sentiment_analysis: SentimentAnalysisResource) -> None:
        self._sentiment_analysis = sentiment_analysis
        self.sentiment_analysis = to_streamed_response_wrapper(sentiment_analysis.run)


class AsyncSentimentAnalysisResourceWithRawResponse:
    def __init__(self, sentiment_analysis: AsyncSentimentAnalysisResource) -> None:
        self._sentiment_analysis = sentiment_analysis
        self.sentiment_analysis = async_to_raw_response_wrapper(sentiment_analysis.run)


class AsyncSentimentAnalysisResourceWithStreamingResponse:
    def __init__(self, sentiment_analysis: AsyncSentimentAnalysisResource) -> None:
        self._sentiment_analysis = sentiment_analysis
        self.sentiment_analysis = async_to_streamed_response_wrapper(sentiment_analysis.run)

