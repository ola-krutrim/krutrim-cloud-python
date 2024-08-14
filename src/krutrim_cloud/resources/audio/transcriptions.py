# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, Union

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.audio import transcription_create_params
from ..._base_client import make_request_options
from ...types.shared.whisper_response import WhisperResponse

__all__ = ["TranscriptionsResource", "AsyncTranscriptionsResource"]


class TranscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranscriptionsResourceWithRawResponse:
        return TranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscriptionsResourceWithStreamingResponse:
        return TranscriptionsResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        chunk_type: Optional[str] | Union[object, None],
        file: str | Union[object, None],
        language: Optional[str] | Union[object, None],
        model_name: str | Union[object, None],
        response_format: Optional[str] | Union[object, None],
        task: str | Union[object, None],
        temperature: Optional[float] | Union[object, None],
        timeout: Union[float, httpx.Timeout, None, object],
    ):
        # Validate chunk_type
        if chunk_type is not NOT_GIVEN:
            if chunk_type not in (None, "sentence", "word"):
                raise ValueError("'chunk_type' must be 'sentence', 'word', or None.")

        # Validate file
        if file is not NOT_GIVEN:
            if not isinstance(file, str):
                raise ValueError("'file' must be a string.")
            if not file:
                raise ValueError("'file' cannot be empty.")

        # Validate language
        if language is not NOT_GIVEN:
            if not isinstance(language, str) and language is not None:
                raise ValueError("'language' must be a string or None.")
            if language:
                language = str(language).lower()
        else:
            language = "english"

        # Validate model_name
        if model_name is not NOT_GIVEN:
            if not isinstance(model_name, str):
                raise ValueError("'model_name' must be a string.")
            if not model_name:
                raise ValueError("'model_name' cannot be empty.")

        # Validate response_format
        if response_format is not NOT_GIVEN:
            if response_format not in (None, "json", "verbose_json"):
                raise ValueError("'response_format' must be 'json', 'verbose_json', or None.")

        # Validate task
        if task is not NOT_GIVEN:
            if not isinstance(task, str):
                raise ValueError("'task' must be a string.")
            if not task:
                raise ValueError("'task' cannot be empty.")

        # Validate temperature
        if temperature is not NOT_GIVEN:
            if not isinstance(temperature, (float, int)) and temperature is not None:
                raise ValueError("'temperature' must be a float or None.")
            if isinstance(temperature, float) and not (0.0 <= temperature <= 2.0):
                raise ValueError("'temperature' must be between 0.0 and 2.0.")
            if isinstance(temperature, int) and not (0 <= temperature <= 2):
                raise ValueError("'temperature' must be between 0.0 and 2.0.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

        return language

    def create(
        self,
        *,
        chunk_type: Optional[str] | NotGiven = NOT_GIVEN,
        file: str | NotGiven = NOT_GIVEN,
        language: Optional[str] | NotGiven = NOT_GIVEN,
        model_name: str | NotGiven = NOT_GIVEN,
        response_format: Optional[str] | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WhisperResponse:
        """
        Generate Audio Transcription

        Args:
            file:"<your encoded audio byte data here>", # Refer to fetch audio bytes from audio file section

            model_name: "openai/whisper-large-v3", # DO NOT CHANGE this

            task: "transcribe",

            language: "hindi", # Source language of the audio

            temperature: 0.0, # Optional, defaults to 0.0. Range - 0.0 to 2.0

            response_format: "json", # Optional, defaults to json. Values - verbose_json (or) json

            chunk_type: "word" # Optional, defaults to sentence. Values - sentence (or) word

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        language = str(
            self.validate_parameters(
                chunk_type=chunk_type,
                file=file,
                language=language,
                model_name=model_name,
                response_format=response_format,
                task=task,
                temperature=temperature,
                timeout=timeout,
            )
        )

        return self._post(
            "/v1/audio/transcriptions",
            body=maybe_transform(
                {
                    "chunk_type": chunk_type,
                    "file": file,
                    "language": language,
                    "model_name": model_name,
                    "response_format": response_format,
                    "task": task,
                    "temperature": temperature,
                },
                transcription_create_params.TranscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhisperResponse,
        )


class AsyncTranscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranscriptionsResourceWithRawResponse:
        return AsyncTranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscriptionsResourceWithStreamingResponse:
        return AsyncTranscriptionsResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        chunk_type: Optional[str] | Union[object, None],
        file: str | Union[object, None],
        language: Optional[str] | Union[object, None],
        model_name: str | Union[object, None],
        response_format: Optional[str] | Union[object, None],
        task: str | Union[object, None],
        temperature: Optional[float] | Union[object, None],
        timeout: Union[float, httpx.Timeout, None, object],
    ):
        # Validate chunk_type
        if chunk_type is not NOT_GIVEN:
            if chunk_type not in (None, "sentence", "word"):
                raise ValueError("'chunk_type' must be 'sentence', 'word', or None.")

        # Validate file
        if file is not NOT_GIVEN:
            if not isinstance(file, str):
                raise ValueError("'file' must be a string.")
            if not file:
                raise ValueError("'file' cannot be empty.")

        # Validate language
        if language is not NOT_GIVEN:
            if not isinstance(language, str) and language is not None:
                raise ValueError("'language' must be a string or None.")
            if language:
                language = str(language).lower()
        else:
            language = "english"

        # Validate model_name
        if model_name is not NOT_GIVEN:
            if not isinstance(model_name, str):
                raise ValueError("'model_name' must be a string.")
            if not model_name:
                raise ValueError("'model_name' cannot be empty.")

        # Validate response_format
        if response_format is not NOT_GIVEN:
            if response_format not in (None, "json", "verbose_json"):
                raise ValueError("'response_format' must be 'json', 'verbose_json', or None.")

        # Validate task
        if task is not NOT_GIVEN:
            if not isinstance(task, str):
                raise ValueError("'task' must be a string.")
            if not task:
                raise ValueError("'task' cannot be empty.")

        # Validate temperature
        if temperature is not NOT_GIVEN:
            if not isinstance(temperature, (float, int)) and temperature is not None:
                raise ValueError("'temperature' must be a float or None.")
            if isinstance(temperature, float) and not (0.0 <= temperature <= 2.0):
                raise ValueError("'temperature' must be between 0.0 and 2.0.")
            if isinstance(temperature, int) and not (0 <= temperature <= 2):
                raise ValueError("'temperature' must be between 0.0 and 2.0.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

        return language

    async def create(
        self,
        *,
        chunk_type: Optional[str] | NotGiven = NOT_GIVEN,
        file: str | NotGiven = NOT_GIVEN,
        language: Optional[str] | NotGiven = NOT_GIVEN,
        model_name: str | NotGiven = NOT_GIVEN,
        response_format: Optional[str] | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WhisperResponse:
        """
        Generate Audio Transcription

        Args:
            file:"<your encoded audio byte data here>", # Refer to fetch audio bytes from audio file section

            model_name: "openai/whisper-large-v3", # DO NOT CHANGE this

            task: "transcribe",

            language: "hindi", # Source language of the audio

            temperature: 0.0, # Optional, defaults to 0.0. Range - 0.0 to 2.0

            response_format: "json", # Optional, defaults to json. Values - verbose_json (or) json

            chunk_type: "word" # Optional, defaults to sentence. Values - sentence (or) word

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        language = str(
            await self.validate_parameters(
                chunk_type=chunk_type,
                file=file,
                language=language,
                model_name=model_name,
                response_format=response_format,
                task=task,
                temperature=temperature,
                timeout=timeout,
            )
        )
        return await self._post(
            "/v1/audio/transcriptions",
            body=await async_maybe_transform(
                {
                    "chunk_type": chunk_type,
                    "file": file,
                    "language": language,
                    "model_name": model_name,
                    "response_format": response_format,
                    "task": task,
                    "temperature": temperature,
                },
                transcription_create_params.TranscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhisperResponse,
        )


class TranscriptionsResourceWithRawResponse:
    def __init__(self, transcriptions: TranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = to_raw_response_wrapper(
            transcriptions.create,
        )


class AsyncTranscriptionsResourceWithRawResponse:
    def __init__(self, transcriptions: AsyncTranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = async_to_raw_response_wrapper(
            transcriptions.create,
        )


class TranscriptionsResourceWithStreamingResponse:
    def __init__(self, transcriptions: TranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = to_streamed_response_wrapper(
            transcriptions.create,
        )


class AsyncTranscriptionsResourceWithStreamingResponse:
    def __init__(self, transcriptions: AsyncTranscriptionsResource) -> None:
        self._transcriptions = transcriptions

        self.create = async_to_streamed_response_wrapper(
            transcriptions.create,
        )
