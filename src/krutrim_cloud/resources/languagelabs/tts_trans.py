from __future__ import annotations
from typing import Optional
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
from ...types.languagelabs.tts_trans_run_response import TtsTransRunResponse as TtsTransRunResponse

__all__ = ["TtsTransResource", "AsyncTtsTransResource"]


class TtsTransResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TtsTransResourceWithRawResponse:
        return TtsTransResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TtsTransResourceWithStreamingResponse:
        return TtsTransResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        input_text: str,
        src_lang_code: str,
        tgt_lang_code: str,
        input_speaker: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate input_text
        if not isinstance(input_text, str):
            raise TypeError("'input_text' must be a string.")
        if not input_text:
            raise ValueError("'input_text' cannot be empty.")

        # Validate src_lang_code
        if not isinstance(src_lang_code, str):
            raise TypeError("'src_lang_code' must be a string.")
        if not src_lang_code:
            raise ValueError("'src_lang_code' cannot be empty.")

        # Validate tgt_lang_code
        if not isinstance(tgt_lang_code, str):
            raise TypeError("'tgt_lang_code' must be a string.")
        if not tgt_lang_code:
            raise ValueError("'tgt_lang_code' cannot be empty.")

        # Validate input_speaker
        if not isinstance(input_speaker, str):
            raise TypeError("'input_speaker' must be a string.")
        if not input_speaker:
            raise ValueError("'input_speaker' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
        self,
        *,
        input_text: str,
        src_lang_code: str,
        tgt_lang_code: str,
        input_speaker: str,
        # Optional additional parameters for extra headers, query, or body
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TtsTransRunResponse:
        """
        Convert Text to Speech with Translation (Synchronous)

        Args:
            input_text: The text to be translated and converted to speech.

            src_lang_code: The source language code (e.g., "eng" for English).

            tgt_lang_code: The target language code (e.g., "hin" for Hindi).

            input_speaker: The speaker type (e.g., "male").

            extra_headers: Optional headers to send with the request.

            extra_query: Optional query parameters to send with the request.

            extra_body: Optional body content to send with the request.

            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        self.validate_parameters(input_text=input_text, src_lang_code=src_lang_code, tgt_lang_code=tgt_lang_code, input_speaker=input_speaker, timeout=timeout)

        # Prepare the request body
        body = {
            "input_text": input_text,
            "src_lang_code": src_lang_code,
            "tgt_lang_code": tgt_lang_code,
            "input_speaker": input_speaker,
        }

        # Send the request to the text-to-speech translation API
        return self._post(
            "/api/v1/languagelabs/tts_trans",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TtsTransRunResponse,
        )



class AsyncTtsTransResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTtsTransResourceWithRawResponse:
        return AsyncTtsTransResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTtsTransResourceWithStreamingResponse:
        return AsyncTtsTransResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        input_text: str,
        src_lang_code: str,
        tgt_lang_code: str,
        input_speaker: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate input_text
        if not isinstance(input_text, str):
            raise TypeError("'input_text' must be a string.")
        if not input_text:
            raise ValueError("'input_text' cannot be empty.")

        # Validate src_lang_code
        if not isinstance(src_lang_code, str):
            raise TypeError("'src_lang_code' must be a string.")
        if not src_lang_code:
            raise ValueError("'src_lang_code' cannot be empty.")

        # Validate tgt_lang_code
        if not isinstance(tgt_lang_code, str):
            raise TypeError("'tgt_lang_code' must be a string.")
        if not tgt_lang_code:
            raise ValueError("'tgt_lang_code' cannot be empty.")

        # Validate input_speaker
        if not isinstance(input_speaker, str):
            raise TypeError("'input_speaker' must be a string.")
        if not input_speaker:
            raise ValueError("'input_speaker' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
        self,
        *,
        input_text: str,
        src_lang_code: str,
        tgt_lang_code: str,
        input_speaker: str,
        # Optional additional parameters for extra headers, query, or body
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TtsTransRunResponse:
        """
        Convert Text to Speech with Translation (Asynchronous)

        Args:
            input_text: The text to be translated and converted to speech.

            src_lang_code: The source language code (e.g., "eng" for English).

            tgt_lang_code: The target language code (e.g., "hin" for Hindi).

            input_speaker: The speaker type (e.g., "male").

            extra_headers: Optional headers to send with the request.

            extra_query: Optional query parameters to send with the request.

            extra_body: Optional body content to send with the request.

            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        await self.validate_parameters(input_text=input_text, src_lang_code=src_lang_code, tgt_lang_code=tgt_lang_code, input_speaker=input_speaker, timeout=timeout)

        # Prepare the request body
        body = {
            "input_text": input_text,
            "src_lang_code": src_lang_code,
            "tgt_lang_code": tgt_lang_code,
            "input_speaker": input_speaker,
        }

        # Send the request to the text-to-speech translation API
        return await self._post(
            "/api/v1/languagelabs/tts_trans",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TtsTransRunResponse,
        )

class TtsTransResourceWithRawResponse:
    def __init__(self, tts_trans: TtsTransResource) -> None:
        self._tts_trans = tts_trans
        self.text_to_speech_translation = to_raw_response_wrapper(tts_trans.run)


class AsyncTtsTransResourceWithRawResponse:
    def __init__(self, tts_trans: AsyncTtsTransResource) -> None:
        self._tts_trans = tts_trans
        self.text_to_speech_translation = async_to_raw_response_wrapper(tts_trans.run)


class TtsTransResourceWithStreamingResponse:
    def __init__(self, tts_trans: TtsTransResource) -> None:
        self._tts_trans = tts_trans
        self.text_to_speech_translation = to_streamed_response_wrapper(tts_trans.run)


class AsyncTtsTransResourceWithStreamingResponse:
    def __init__(self, tts_trans: AsyncTtsTransResource) -> None:
        self._tts_trans = tts_trans
        self.text_to_speech_translation = async_to_streamed_response_wrapper(tts_trans.run)
