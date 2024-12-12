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
from ...types.languagelabs.stt_trans_lf_upload_response import SttTransLfUploadResponse as SttTransLfUploadResponse
from ...types.languagelabs.stt_trans_upload_params import SttTransUploadParams as SttTransUploadParams

__all__ = ["SttTransLfResource", "AsyncSttTransLfResource"]

class SttTransLfResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SttTransLfResourceWithRawResponse:
        return SttTransLfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SttTransLfResourceWithStreamingResponse:
        return SttTransLfResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        file: FileTypes,
        src_lang_code: str,
        tgt_lang_code: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):

        if not isinstance(src_lang_code, str):
            raise TypeError("'src_lang_code' must be a string.")
        if not src_lang_code:
            raise ValueError("'src_lang_code' cannot be empty.")

        if not isinstance(tgt_lang_code, str):
            raise TypeError("'tgt_lang_code' must be a string.")
        if not tgt_lang_code:
            raise ValueError("'tgt_lang_code' cannot be empty.")

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
        src_lang_code: str,
        tgt_lang_code: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SttTransLfUploadResponse:

        """
                Convert Speech to Text with Translation for large files

                Args:
                    file: The path to the audio file to be transcribed and translated.
                    src_lang_code: The source language code for transcription (e.g., "eng").
                    tgt_lang_code: The target language code for translation (e.g., "hin").
                    extra_headers: Optional headers to send with the request.
                    extra_query: Optional query parameters to send with the request.
                    extra_body: Optional body content to send with the request.
                    timeout: Optional timeout override for the request.
                """

        self.validate_parameters(file=file, src_lang_code=src_lang_code, tgt_lang_code=tgt_lang_code,timeout=timeout)

        body = deepcopy_minimal(
            {
                'file': file,  # Open the audio file in binary mode
                'src_lang_code': src_lang_code,
                'tgt_lang_code': tgt_lang_code
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}


        # Send the request to the speech-to-text translation long duration API
        return self._post(
            "/api/v1/languagelabs/stt_trans/lf/upload",
            body=maybe_transform(body, SttTransUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SttTransLfUploadResponse,
        )



class AsyncSttTransLfResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSttTransLfResourceWithRawResponse:
        return AsyncSttTransLfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSttTransLfResourceWithStreamingResponse:
        return AsyncSttTransLfResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        file: FileTypes,
        src_lang_code: str,
        tgt_lang_code: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):

        if not isinstance(src_lang_code, str):
            raise TypeError("'src_lang_code' must be a string.")
        if not src_lang_code:
            raise ValueError("'src_lang_code' cannot be empty.")

        if not isinstance(tgt_lang_code, str):
            raise TypeError("'tgt_lang_code' must be a string.")
        if not tgt_lang_code:
            raise ValueError("'tgt_lang_code' cannot be empty.")

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


    async def upload(
        self,
        *,
        file: FileTypes,
        src_lang_code: str,
        tgt_lang_code: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SttTransLfUploadResponse:

        """
                Convert Speech to Text with Translation for large files

                Args:
                    file: The path to the audio file to be transcribed and translated.
                    src_lang_code: The source language code for transcription (e.g., "eng").
                    tgt_lang_code: The target language code for translation (e.g., "hin").
                    extra_headers: Optional headers to send with the request.
                    extra_query: Optional query parameters to send with the request.
                    extra_body: Optional body content to send with the request.
                    timeout: Optional timeout override for the request.
                """

        await self.validate_parameters(file=file, src_lang_code=src_lang_code, tgt_lang_code=tgt_lang_code, timeout=timeout)

        body = deepcopy_minimal(
            {
                'file': file,  # Open the audio file in binary mode
                'src_lang_code': src_lang_code,
                'tgt_lang_code': tgt_lang_code
            }
        )

        # Prepare the request body with the file
        files = {
            'file': file,  # Open the audio file in binary mode
            'src_lang_code': src_lang_code,
            'tgt_lang_code': tgt_lang_code
        }
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        # Send the request to the speech-to-text translation long duration API
        return await self._post(
            "/api/v1/languagelabs/stt_trans/lf/upload",
            body=async_maybe_transform(body, SttTransUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SttTransLfUploadResponse,
        )


# Response Wrappers for Raw and Streaming Responses

class SttTransLfResourceWithRawResponse:
    def __init__(self, stt_trans_long_duration: SttTransLfResource) -> None:
        self._stt_trans_long_duration = stt_trans_long_duration
        self.speech_to_text_translation_long_duration = to_raw_response_wrapper(stt_trans_long_duration.upload)


class AsyncSttTransLfResourceWithRawResponse:
    def __init__(self, stt_trans_long_duration: AsyncSttTransLfResource) -> None:
        self._stt_trans_long_duration = stt_trans_long_duration
        self.speech_to_text_translation_long_duration = async_to_raw_response_wrapper(stt_trans_long_duration.upload)


class SttTransLfResourceWithStreamingResponse:
    def __init__(self, stt_trans_long_duration: SttTransLfResource) -> None:
        self._stt_trans_long_duration = stt_trans_long_duration
        self.speech_to_text_translation_long_duration = to_streamed_response_wrapper(stt_trans_long_duration.upload)


class AsyncSttTransLfResourceWithStreamingResponse:
    def __init__(self, stt_trans_long_duration: AsyncSttTransLfResource) -> None:
        self._stt_trans_long_duration = stt_trans_long_duration
        self.speech_to_text_translation_long_duration = async_to_streamed_response_wrapper(stt_trans_long_duration.upload)
