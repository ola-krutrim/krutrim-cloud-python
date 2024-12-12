from __future__ import annotations
from typing import Optional
import httpx
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.languagelabs.tts_run_response import TtsRunResponse as TtsRunResponse

__all__ = ["TtsResource", "AsyncTtsResource"]


class TtsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TtsResourceWithRawResponse:
        return TtsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TtsResourceWithStreamingResponse:
        return TtsResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        input_text: str,
        input_language: str,
        input_speaker: Optional[str] = "male",
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate input_text
        if not isinstance(input_text, str):
            raise TypeError("'input_text' must be a string.")
        if not input_text:
            raise ValueError("'input_text' cannot be empty.")

        # Validate input_language
        if not isinstance(input_language, str):
            raise TypeError("'input_language' must be a string.")
        if not input_language:
            raise ValueError("'input_language' cannot be empty.")

        # Validate input_speaker
        if input_speaker is not None and input_speaker not in ["male", "female"]:
            raise ValueError("'input_speaker' must be either 'male' or 'female'.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
        self,
        *,
        input_text: str,
        input_language: str,
        input_speaker: Optional[str] = "male",
        # Optional additional parameters for extra headers, query, or body
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TtsRunResponse:
        """
        Convert Text to Speech

        Args:
            input_text: The text that will be converted to speech.

            input_language: The language of the text (e.g., "eng").

            input_speaker: The speaker's gender (either "male" or "female").

            extra_headers: Optional headers to send with the request.

            extra_query: Optional query parameters to send with the request.

            extra_body: Optional body content to send with the request.

            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        self.validate_parameters(input_text=input_text, input_language=input_language, input_speaker=input_speaker, timeout=timeout)

        # Prepare the request payload
        payload = {
            "input_text": input_text,
            "input_language": input_language,
            "input_speaker": input_speaker,
        }

        # Send the request to the TTS API
        return self._post(
            "/api/v1/languagelabs/tts",
            body=maybe_transform(payload, dict),  # Ensures the payload is properly transformed if needed
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TtsRunResponse,
        )



class AsyncTtsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTtsResourceWithRawResponse:
        return AsyncTtsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTtsResourceWithStreamingResponse:
        return AsyncTtsResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        input_text: str,
        input_language: str,
        input_speaker: Optional[str] = "male",
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate input_text
        if not isinstance(input_text, str):
            raise TypeError("'input_text' must be a string.")
        if not input_text:
            raise ValueError("'input_text' cannot be empty.")

        # Validate input_language
        if not isinstance(input_language, str):
            raise TypeError("'input_language' must be a string.")
        if not input_language:
            raise ValueError("'input_language' cannot be empty.")

        # Validate input_speaker
        if input_speaker is not None and input_speaker not in ["male", "female"]:
            raise ValueError("'input_speaker' must be either 'male' or 'female'.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
        self,
        *,
        input_text: str,
        input_language: str,
        input_speaker: Optional[str] = "male",
        # Optional additional parameters for extra headers, query, or body
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TtsRunResponse:
        """
        Convert Text to Speech (Asynchronous)

        Args:
            input_text: The text that will be converted to speech.

            input_language: The language of the text (e.g., "eng").

            input_speaker: The speaker's gender (either "male" or "female").

            extra_headers: Optional headers to send with the request.

            extra_query: Optional query parameters to send with the request.

            extra_body: Optional body content to send with the request.

            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        await self.validate_parameters(input_text=input_text, input_language=input_language, input_speaker=input_speaker, timeout=timeout)

        # Prepare the request payload
        payload = {
            "input_text": input_text,
            "input_language": input_language,
            "input_speaker": input_speaker,
        }

        # Send the request to the TTS API
        return await self._post(
            "/api/v1/languagelabs/tts",
            body=await async_maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TtsRunResponse,
        )


class TtsResourceWithRawResponse:
    def __init__(self, tts: TtsResource) -> None:
        self._tts = tts
        self.text_to_speech = to_raw_response_wrapper(tts.run)


class AsyncTtsResourceWithRawResponse:
    def __init__(self, tts: AsyncTtsResource) -> None:
        self._tts = tts
        self.text_to_speech = async_to_raw_response_wrapper(tts.run)


class TtsResourceWithStreamingResponse:
    def __init__(self, tts: TtsResource) -> None:
        self._tts = tts
        self.text_to_speech = to_streamed_response_wrapper(tts.run)


class AsyncTtsResourceWithStreamingResponse:
    def __init__(self, tts: AsyncTtsResource) -> None:
        self._tts = tts
        self.text_to_speech = async_to_streamed_response_wrapper(tts.run)
