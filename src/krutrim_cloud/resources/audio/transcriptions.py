# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional, Union, Dict, Any, List

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
from ...lib.utils import convert_audio_file_to_base64
from pathlib import Path
from pydub import AudioSegment  # type: ignore
from pydub.exceptions import CouldntDecodeError  # type: ignore
from os import sep
import shutil

__all__ = ["TranscriptionsResource", "AsyncTranscriptionsResource"]


class TranscriptionsResource(SyncAPIResource):
    tmp_path = Path("./tmp_audio_store")
    tmp_filename_prefix = "audio-chunk"

    @cached_property
    def with_raw_response(self) -> TranscriptionsResourceWithRawResponse:
        return TranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscriptionsResourceWithStreamingResponse:
        return TranscriptionsResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        chunk_type: Optional[str] | Union[object, None],
        file: str | Path | AudioSegment | Union[object, None],
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
            if not isinstance(file, (str, Path, AudioSegment)):
                raise ValueError(
                    "'file' must be a string or Path object from pathlib or AudioSegment object from pydub."
                )
            if not file:
                raise ValueError("'file' cannot be empty or None.")

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

    def _send_post_request(self, payload: Dict[str, Any], extra_options: Dict[str, Any]):
        return self._post(
            "/v1/audio/transcriptions",
            body=maybe_transform(
                payload,
                transcription_create_params.TranscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_options["extra_headers"],
                extra_query=extra_options["extra_query"],
                extra_body=extra_options["extra_body"],
                timeout=extra_options["timeout"],
            ),
            cast_to=WhisperResponse,
        )

    def _merge_predictions(self, dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Merges a list of predictions that contain `text` and `chunks`(if present) keys.

        This function combines the `text` values from each prediction into a single string,
        separated by spaces. It also merges the `chunks` lists from each prediction into a
        single list, preserving the order of chunks as they appear in the input dictionaries.

        Parameters:
        -----------
        dicts : List[Dict[str, Any]]
            A list of predictions to be merged. Each prediction should contain the keys
            'text' (a string) and 'chunks' (a list of dictionaries with `timestamp` and `text`).

        Returns:
        --------
        Dict[str, Any]
            A single dictionary with the merged `text` and `chunks` values.

        Example:
        --------
        >>> dict_1 = {
        ...     "text": "Hello, this is the first text.",
        ...     "chunks": [
        ...         {"timestamp": [0.0, 3.0], "text": "Hello, this"},
        ...         {"timestamp": [3.0, 7.0], "text": "is the first text."}
        ...     ]
        ... }
        >>> dict_2 = {
        ...     "text": "And here is the second text.",
        ...     "chunks": [
        ...         {"timestamp": [0.0, 4.0], "text": "And here"},
        ...         {"timestamp": [4.0, 8.0], "text": "is the second text."}
        ...     ]
        ... }
        >>> _merge_predictions([dict_1, dict_2])
        {
            'text': 'Hello, this is the first text. And here is the second text.',
            'chunks': [
                {"timestamp": [0.0, 3.0], "text": "Hello, this"},
                {"timestamp": [3.0, 7.0], "text": "is the first text."},
                {"timestamp": [0.0, 4.0], "text": "And here"},
                {"timestamp": [4.0, 8.0], "text": "is the second text."}
            ]
        }
        """
        merged_dict: Dict[str, Any]

        if "chunks" in dicts[0]:
            merged_dict = {"text": "", "chunks": []}
        else:
            merged_dict = {"text": ""}

        for data_dict in dicts:
            # Ensure that the current dictionary has the expected keys
            if "text" in data_dict:
                merged_dict["text"] += data_dict.get("text", "") + " "
            if "chunks" in data_dict:
                merged_dict["chunks"].extend(data_dict.get("chunks", []))

        # Clean up the trailing space in the merged 'text'
        merged_dict["text"] = merged_dict["text"].strip()

        return merged_dict

    def create(
        self,
        *,
        chunk_type: Optional[str] | NotGiven = NOT_GIVEN,
        file: str | Path | NotGiven = NOT_GIVEN,
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
    ) -> WhisperResponse:  # type: ignore
        """
        Generate Audio Transcription

        Args:
            file:"<your base64 encoded audio byte data here>" OR "Path object of pathlib for the audio filepath"

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
        payload = {
            "chunk_type": chunk_type,
            "file": file,
            "language": language,
            "model_name": model_name,
            "response_format": response_format,
            "task": task,
            "temperature": temperature,
        }

        extra_options = {
            "extra_headers": extra_headers,
            "extra_query": extra_query,
            "extra_body": extra_body,
            "timeout": timeout,
        }
        tmp_filepath = None

        if isinstance(file, str):
            return self._send_post_request(payload, extra_options)
        elif isinstance(file, Path) or isinstance(file, AudioSegment):
            try:
                if isinstance(file, Path):
                    audio_data = AudioSegment.from_file(file)  # type: ignore
                else:
                    audio_data = file  # type: ignore
                audio_data_duration: float = audio_data.duration_seconds  # type: ignore

                Path.mkdir(self.tmp_path, exist_ok=True)
                tmp_filepath = f"{self.tmp_path.as_posix()}{sep}{self.tmp_filename_prefix}.mp3"
                if audio_data_duration <= 120.0:  # Less then or equal to 2 minutes audio
                    with open(tmp_filepath, "wb") as file_object:
                        audio_data.export(file_object, format="mp3")  # type: ignore

                    audio_b64_data = convert_audio_file_to_base64(tmp_filepath)
                    payload["file"] = audio_b64_data
                    shutil.rmtree(self.tmp_path.as_posix())
                    return self._send_post_request(payload, extra_options)
                else:
                    audio_data_chunks = audio_data[::120000]  # type: ignore # chunking with interval of 120 seconds
                    predictions: List[Dict[str, Any]] = []
                    for index, audio_data_chunk in enumerate(audio_data_chunks):  # type: ignore
                        tmp_filepath = f"{self.tmp_path.as_posix()}{sep}{self.tmp_filename_prefix}-{index}.mp3"
                        with open(tmp_filepath, "wb") as f:
                            audio_data_chunk.export(f, format="mp3")  # type: ignore

                        audio_b64_data = convert_audio_file_to_base64(tmp_filepath)
                        payload["file"] = audio_b64_data
                        predictions.append(self._send_post_request(payload, extra_options).predictions)  # type: ignore
                    shutil.rmtree(self.tmp_path.as_posix())
                    whisperResponse = WhisperResponse(predictions=None)
                    whisperResponse.predictions = self._merge_predictions(predictions)
                    return whisperResponse
            except CouldntDecodeError as decode_error:
                if isinstance(file, Path):
                    raise CouldntDecodeError(
                        f"The file '{file.as_posix()}' is not a valid or supported audio file format.\n{decode_error}"
                    )
                else:
                    raise CouldntDecodeError(f"The file is not a valid or supported audio file format.\n{decode_error}")
            except FileNotFoundError as fnf_error:
                raise FileNotFoundError(f"Error: The file '{tmp_filepath}' was not found. {fnf_error}")

            except ValueError as val_error:
                raise ValueError(f"{val_error}")

            except Exception as exc:
                raise Exception(exc)


class AsyncTranscriptionsResource(AsyncAPIResource):
    tmp_path = Path("./tmp_audio_store")
    tmp_filename_prefix = "audio-chunk"

    @cached_property
    def with_raw_response(self) -> AsyncTranscriptionsResourceWithRawResponse:
        return AsyncTranscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscriptionsResourceWithStreamingResponse:
        return AsyncTranscriptionsResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        chunk_type: Optional[str] | Union[object, None],
        file: str | Path | AudioSegment | Union[object, None],
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
            if not isinstance(file, (str, Path, AudioSegment)):
                raise ValueError(
                    "'file' must be a string or Path object from pathlib or AudioSegment object from pydub."
                )
            if not file:
                raise ValueError("'file' cannot be empty or None.")

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

    async def _send_post_request(self, payload: Dict[str, Any], extra_options: Dict[str, Any]):
        return await self._post(
            "/v1/audio/transcriptions",
            body=await async_maybe_transform(
                payload,
                transcription_create_params.TranscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_options["extra_headers"],
                extra_query=extra_options["extra_query"],
                extra_body=extra_options["extra_body"],
                timeout=extra_options["timeout"],
            ),
            cast_to=WhisperResponse,
        )

    async def _merge_predictions(self, dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Merges a list of dictionaries that contain `text` and `chunks`(if present) keys.

        This function combines the `text` values from each dictionary into a single string,
        separated by spaces. It also merges the `chunks` lists from each dictionary into a
        single list, preserving the order of chunks as they appear in the input dictionaries.

        Parameters:
        -----------
        dicts : List[Dict[str, Any]]
            A list of dictionaries to be merged. Each dictionary should contain the keys
            'text' (a string) and 'chunks' (a list of dictionaries with `timestamp` and `text`).

        Returns:
        --------
        Dict[str, Any]
            A single dictionary with the merged `text` and `chunks` values.

        Example:
        --------
        >>> dict_1 = {
        ...     "text": "Hello, this is the first text.",
        ...     "chunks": [
        ...         {"timestamp": [0.0, 3.0], "text": "Hello, this"},
        ...         {"timestamp": [3.0, 7.0], "text": "is the first text."}
        ...     ]
        ... }
        >>> dict_2 = {
        ...     "text": "And here is the second text.",
        ...     "chunks": [
        ...         {"timestamp": [0.0, 4.0], "text": "And here"},
        ...         {"timestamp": [4.0, 8.0], "text": "is the second text."}
        ...     ]
        ... }
        >>> _merge_predictions([dict_1, dict_2])
        {
            'text': 'Hello, this is the first text. And here is the second text.',
            'chunks': [
                {"timestamp": [0.0, 3.0], "text": "Hello, this"},
                {"timestamp": [3.0, 7.0], "text": "is the first text."},
                {"timestamp": [0.0, 4.0], "text": "And here"},
                {"timestamp": [4.0, 8.0], "text": "is the second text."}
            ]
        }
        """
        merged_dict: Dict[str, Any]

        if "chunks" in dicts[0]:
            merged_dict = {"text": "", "chunks": []}
        else:
            merged_dict = {"text": ""}

        for data_dict in dicts:
            # Ensure that the current dictionary has the expected keys
            if "text" in data_dict:
                merged_dict["text"] += data_dict.get("text", "") + " "
            if "chunks" in data_dict:
                merged_dict["chunks"].extend(data_dict.get("chunks", []))

        # Clean up the trailing space in the merged 'text'
        merged_dict["text"] = merged_dict["text"].strip()

        return merged_dict

    async def create(
        self,
        *,
        chunk_type: Optional[str] | NotGiven = NOT_GIVEN,
        file: str | Path | NotGiven = NOT_GIVEN,
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
    ) -> WhisperResponse:  # type: ignore
        """
        Generate Audio Transcription

        Args:
            file:"<your base64 encoded audio byte data here>" OR "Path object of pathlib for the audio filepath"

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
        payload = {
            "chunk_type": chunk_type,
            "file": file,
            "language": language,
            "model_name": model_name,
            "response_format": response_format,
            "task": task,
            "temperature": temperature,
        }

        extra_options = {
            "extra_headers": extra_headers,
            "extra_query": extra_query,
            "extra_body": extra_body,
            "timeout": timeout,
        }
        tmp_filepath = None

        if isinstance(file, str):
            return await self._send_post_request(payload, extra_options)
        elif isinstance(file, Path) or isinstance(file, AudioSegment):
            try:
                if isinstance(file, Path):
                    audio_data = AudioSegment.from_file(file)  # type: ignore
                else:
                    audio_data = file  # type: ignore
                audio_data_duration: float = audio_data.duration_seconds  # type: ignore

                Path.mkdir(self.tmp_path, exist_ok=True)
                tmp_filepath = f"{self.tmp_path.as_posix()}{sep}{self.tmp_filename_prefix}.mp3"
                if audio_data_duration <= 120.0:  # Less then or equal to 2 minutes audio
                    with open(tmp_filepath, "wb") as file_object:
                        audio_data.export(file_object, format="mp3")  # type: ignore

                    audio_b64_data = convert_audio_file_to_base64(tmp_filepath)
                    payload["file"] = audio_b64_data
                    shutil.rmtree(self.tmp_path.as_posix())
                    return await self._send_post_request(payload, extra_options)
                else:
                    audio_data_chunks = audio_data[::120000]  # type: ignore # chunking with interval of 120 seconds
                    predictions: List[Dict[str, Any]] = []
                    for index, audio_data_chunk in enumerate(audio_data_chunks):  # type: ignore
                        tmp_filepath = f"{self.tmp_path.as_posix()}{sep}{self.tmp_filename_prefix}-{index}.mp3"
                        with open(tmp_filepath, "wb") as f:
                            audio_data_chunk.export(f, format="mp3")  # type: ignore

                        audio_b64_data = convert_audio_file_to_base64(tmp_filepath)
                        payload["file"] = audio_b64_data
                        predictions.append(self._send_post_request(payload, extra_options).predictions)  # type: ignore
                    shutil.rmtree(self.tmp_path.as_posix())
                    whisperResponse = WhisperResponse(predictions=None)
                    whisperResponse.predictions = await self._merge_predictions(predictions)
                    return whisperResponse
            except CouldntDecodeError as decode_error:
                if isinstance(file, Path):
                    raise CouldntDecodeError(
                        f"The file '{file.as_posix()}' is not a valid or supported audio file format.\n{decode_error}"
                    )
                else:
                    raise CouldntDecodeError(f"The file is not a valid or supported audio file format.\n{decode_error}")
            except FileNotFoundError as fnf_error:
                raise FileNotFoundError(f"Error: The file '{tmp_filepath}' was not found. {fnf_error}")

            except ValueError as val_error:
                raise ValueError(f"{val_error}")

            except Exception as exc:
                raise Exception(exc)


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
