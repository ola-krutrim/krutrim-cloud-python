from __future__ import annotations
from typing import cast,Mapping
import httpx
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven,FileTypes
from ..._utils import (maybe_transform,
                       async_maybe_transform,
                       deepcopy_minimal,
                       extract_files,)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, to_streamed_response_wrapper, async_to_raw_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.languagelabs.transcribe_lf_upload_response import TranscribeLfUploadResponse as TranscribeLfUploadResponse
from ...types.languagelabs.transcribe_lf_upload_params import TranscribeLfUploadParams as TranscribeLfUploadParams

__all__ = ["TranscribeLfResource", "AsyncTranscribeLfResource"]

class TranscribeLfResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranscribeLfResourceWithRawResponse:
        return TranscribeLfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscribeLfResourceWithStreamingResponse:
        return TranscribeLfResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        file: FileTypes,
        lang_code: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):


        if not isinstance(lang_code, str):
            raise TypeError("'lang_code' must be a string.")
        if not lang_code:
            raise ValueError("'lang_code' cannot be empty.")

        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

        # Check if file is of type FileContent (bytes or file-like object)
        if isinstance(file, bytes):  # A simple file content (binary data)
            return  # Valid, as bytes represent valid file content
        elif hasattr(file, 'read'):  # Could be a file-like object
            return  # Valid, as file-like objects (e.g., io.BytesIO) are acceptable

        # Check if file is a tuple (filename, file content)
        if isinstance(file, tuple):
            if len(file) < 2:
                raise ValueError("'file' tuple must have at least two elements: (filename, file content).")

            filename, file_content = file[:2]

            # Validate the filename (it can be None or a string)
            if filename is not None and not isinstance(filename, str):
                raise TypeError("'filename' must be a string or None.")

            # Validate file_content (must be file content)
            if not isinstance(file_content, (bytes, bytearray)) and not hasattr(file_content, 'read'):
                raise TypeError("'file_content' must be bytes, bytearray, or a file-like object.")

            # If there are more elements, validate them
            if len(file) >= 3:
                content_type = file[2]
                if content_type is not None and not isinstance(content_type, str):
                    raise TypeError("'content_type' must be a string or None.")

            if len(file) == 4:
                headers = file[3]
                if headers is not None and not isinstance(headers, Mapping):
                    raise TypeError("'headers' must be a dictionary-like object (Mapping).")

        else:
            raise TypeError(
                "'file' must be a bytes object, a file-like object, or a tuple of the form (filename, file_content, ...).")


    def upload(
            self,
            *,
            file: FileTypes,
            lang_code: str,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TranscribeLfUploadResponse:

        self.validate_parameters(file=file,lang_code=lang_code,timeout=timeout)
        """
        Convert Speech to Text (Transcribe Audio File)

        Args:
            file: The path to the audio file to be transcribed.
            lang_code: The language code for transcription (e.g., "eng").
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """

        body = deepcopy_minimal(
            {
                "file": file,
                "lang_code": lang_code,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return self._post(  # type: ignore[return-value]
            "/api/v1/languagelabs/transcribe/lf/upload",
            body=maybe_transform(body, TranscribeLfUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranscribeLfUploadResponse,
        )


class AsyncTranscribeLfResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranscribeLfResourceWithRawResponse:
        return AsyncTranscribeLfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscribeLfResourceWithStreamingResponse:
        return AsyncTranscribeLfResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        file: FileTypes,
        lang_code: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):

        # Validate lang_code
        if not isinstance(lang_code, str):
            raise TypeError("'lang_code' must be a string.")
        if not lang_code:
            raise ValueError("'lang_code' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

        """
           Validates the 'file' parameter according to its type (FileTypes).
         """

        # Check if file is of type FileContent (bytes or file-like object)
        if isinstance(file, bytes):  # A simple file content (binary data)
            return  # Valid, as bytes represent valid file content
        elif hasattr(file, 'read'):  # Could be a file-like object
            return  # Valid, as file-like objects (e.g., io.BytesIO) are acceptable

        # Check if file is a tuple (filename, file content)
        if isinstance(file, tuple):
            if len(file) < 2:
                raise ValueError("'file' tuple must have at least two elements: (filename, file content).")

            filename, file_content = file[:2]

            # Validate the filename (it can be None or a string)
            if filename is not None and not isinstance(filename, str):
                raise TypeError("'filename' must be a string or None.")

            # Validate file_content (must be file content)
            if not isinstance(file_content, (bytes, bytearray)) and not hasattr(file_content, 'read'):
                raise TypeError("'file_content' must be bytes, bytearray, or a file-like object.")

            # If there are more elements, validate them
            if len(file) >= 3:
                content_type = file[2]
                if content_type is not None and not isinstance(content_type, str):
                    raise TypeError("'content_type' must be a string or None.")

            if len(file) == 4:
                headers = file[3]
                if headers is not None and not isinstance(headers, Mapping):
                    raise TypeError("'headers' must be a dictionary-like object (Mapping).")

        else:
            raise TypeError(
                "'file' must be a bytes object, a file-like object, or a tuple of the form (filename, file_content, ...).")



async def upload(
            self,
            *,
            file: FileTypes,
            lang_code: str,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TranscribeLfUploadResponse:
        """
        Convert Speech to Text (Transcribe Audio File)

        Args:
            file: The path to the audio file to be transcribed.
            lang_code: The language code for transcription (e.g., "eng").
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        await self.validate_parameters(file=file,lang_code=lang_code,timeout=timeout)
        body = deepcopy_minimal(
            {
                "file": file,
                "lang_code": lang_code,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return await self._post(  # type: ignore[return-value]
            "/api/v1/languagelabs/transcribe/lf/upload",
            body=async_maybe_transform(body, TranscribeLfUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranscribeLfUploadResponse,
        )


# Response Wrappers for Raw and Streaming Responses

class TranscribeLfResourceWithRawResponse:
    def __init__(self, stt_long_duration: TranscribeLfResource) -> None:
        self._stt_long_duration = stt_long_duration
        self.speech_to_text_long_duration = to_raw_response_wrapper(stt_long_duration.upload)


class AsyncTranscribeLfResourceWithRawResponse:
    def __init__(self, stt_long_duration: AsyncTranscribeLfResource) -> None:
        self._stt_long_duration = stt_long_duration
        self.speech_to_text_long_duration = async_to_raw_response_wrapper(stt_long_duration.upload)


class TranscribeLfResourceWithStreamingResponse:
    def __init__(self, stt_long_duration: TranscribeLfResource) -> None:
        self._stt_long_duration = stt_long_duration
        self.speech_to_text_long_duration = to_streamed_response_wrapper(stt_long_duration.upload)


class AsyncTranscribeLfResourceWithStreamingResponse:
    def __init__(self, stt_long_duration: AsyncTranscribeLfResource) -> None:
        self._stt_long_duration = stt_long_duration
        self.speech_to_text_long_duration = async_to_streamed_response_wrapper(stt_long_duration.upload)
