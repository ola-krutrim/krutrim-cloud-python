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
from ...types.languagelabs.language_detection_response import LanguageDetectionResponse as LanguageDetectionResponse

__all__ = ["LanguageDetectionResource", "AsyncLanguageDetectionResource"]

class LanguageDetectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LanguageDetectionResourceWithRawResponse:
        return LanguageDetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguageDetectionResourceWithStreamingResponse:
        return LanguageDetectionResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        query: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate query
        if not isinstance(query, str):
            raise TypeError("'query' must be a string.")
        if not query:
            raise ValueError("'query' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
        self,
        *,
        query: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageDetectionResponse:
        """
        Detect the language of the input text.

        Args:
            query: The text whose language needs to be detected.
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        self.validate_parameters(query=query, timeout=timeout)

        # Prepare the request payload
        payload = {
            "query": query
        }

        # Send the request to the language detection API
        return self._post(
            "/api/v1/languagelabs/language-detection",
            body=maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageDetectionResponse,
        )


class AsyncLanguageDetectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLanguageDetectionResourceWithRawResponse:
        return AsyncLanguageDetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguageDetectionResourceWithStreamingResponse:
        return AsyncLanguageDetectionResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        query: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate query
        if not isinstance(query, str):
            raise TypeError("'query' must be a string.")
        if not query:
            raise ValueError("'query' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
        self,
        *,
        query: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageDetectionResponse:
        """
        Detect the language of the input text (Asynchronous)

        Args:
            query: The text whose language needs to be detected.
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        await self.validate_parameters(query=query, timeout=timeout)

        # Prepare the request payload
        payload = {
            "query": query
        }

        # Send the request to the language detection API
        return await self._post(
            "/api/v1/languagelabs/language-detection",
            body=await async_maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageDetectionResponse,
        )



class LanguageDetectionResourceWithRawResponse:
    def __init__(self, language_detection: LanguageDetectionResource) -> None:
        self._language_detection = language_detection
        self.language_detection = to_raw_response_wrapper(language_detection.run)


class LanguageDetectionResourceWithStreamingResponse:
    def __init__(self, language_detection: LanguageDetectionResource) -> None:
        self._language_detection = language_detection
        self.language_detection = to_streamed_response_wrapper(language_detection.run)



class AsyncLanguageDetectionResourceWithRawResponse:
    def __init__(self, language_detection: AsyncLanguageDetectionResource) -> None:
        self._language_detection = language_detection
        self.language_detection = async_to_raw_response_wrapper(language_detection.run)


class AsyncLanguageDetectionResourceWithStreamingResponse:
    def __init__(self, language_detection: AsyncLanguageDetectionResource) -> None:
        self._language_detection = language_detection
        self.language_detection = async_to_streamed_response_wrapper(language_detection.run)