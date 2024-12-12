from __future__ import annotations
from typing import  Mapping, cast
import httpx
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (maybe_transform,
                       async_maybe_transform,
                       deepcopy_minimal,
                       extract_files, )
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.languagelabs.sts_trans_upload_params import StsTransUploadParams as StsTransUploadParams
from ...types.languagelabs.sts_trans_upload_response import StsTransUploadResponse as StsTransUploadResponse

__all__ = ["StsTransResource", "AsyncStsTransResource"]

class StsTransResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StsTransResourceWithRawResponse:
        return StsTransResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StsTransResourceWithStreamingResponse:
        return StsTransResourceWithStreamingResponse(self)

    def validate_parameters(
            self,
            file: FileTypes,
            src_lang_code: str,
            tgt_lang_code: str,
            input_speaker: str,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        """
        Validates the 'file', 'src_lang_code', 'tgt_lang_code', and 'input_speaker' parameters for speech-to-speech translation.
        """
        # Validate 'src_lang_code' and 'tgt_lang_code'
        if not isinstance(src_lang_code, str):
            raise TypeError("'src_lang_code' must be a string.")
        if not src_lang_code:
            raise ValueError("'src_lang_code' cannot be empty.")

        if not isinstance(tgt_lang_code, str):
            raise TypeError("'tgt_lang_code' must be a string.")
        if not tgt_lang_code:
            raise ValueError("'tgt_lang_code' cannot be empty.")

        # Validate 'input_speaker'
        if not isinstance(input_speaker, str):
            raise TypeError("'input_speaker' must be a string.")
        if input_speaker not in ["male", "female"]:
            raise ValueError("'input_speaker' must be either 'male' or 'female'.")

        # Validate timeout
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
            input_speaker: str,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StsTransUploadResponse:
        """
        Convert Speech to Speech with translation (Translates speech from one language to another and preserves speaker's gender)

        Args:
            file: The path to the audio file to be processed.
            src_lang_code: The source language code for transcription (e.g., "eng").
            tgt_lang_code: The target language code for translation (e.g., "hin").
            input_speaker: The gender of the speaker (e.g., "male").
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        self.validate_parameters(file=file, src_lang_code=src_lang_code, tgt_lang_code=tgt_lang_code,input_speaker=input_speaker, timeout=timeout)

        body = deepcopy_minimal(
            {
                "file": file,
                "src_lang_code": src_lang_code,
                "tgt_lang_code": tgt_lang_code,
                "input_speaker": input_speaker,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return self._post(  # type: ignore[return-value]
            "/api/v1/languagelabs/sts_trans/upload",
            body=maybe_transform(body, StsTransUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StsTransUploadResponse,
        )

class AsyncStsTransResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStsTransResourceWithRawResponse:
        return AsyncStsTransResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStsTransResourceWithStreamingResponse:
        return AsyncStsTransResourceWithStreamingResponse(self)

    async def validate_parameters(
            self,
            file: FileTypes,
            src_lang_code: str,
            tgt_lang_code: str,
            input_speaker: str,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        """
        Validates the 'file', 'src_lang_code', 'tgt_lang_code', and 'input_speaker' parameters for speech-to-speech translation.
        """

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

        # Validate 'src_lang_code' and 'tgt_lang_code'
        if not isinstance(src_lang_code, str):
            raise TypeError("'src_lang_code' must be a string.")
        if not src_lang_code:
            raise ValueError("'src_lang_code' cannot be empty.")

        if not isinstance(tgt_lang_code, str):
            raise TypeError("'tgt_lang_code' must be a string.")
        if not tgt_lang_code:
            raise ValueError("'tgt_lang_code' cannot be empty.")

        # Validate 'input_speaker'
        if not isinstance(input_speaker, str):
            raise TypeError("'input_speaker' must be a string.")
        if input_speaker not in ["male", "female"]:
            raise ValueError("'input_speaker' must be either 'male' or 'female'.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def upload(
            self,
            *,
            file: FileTypes,
            src_lang_code: str,
            tgt_lang_code: str,
            input_speaker: str,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StsTransUploadResponse:
        """
        Convert Speech to Speech with translation (Translates speech from one language to another and preserves speaker's gender)

        Args:
            file: The path to the audio file to be processed.
            src_lang_code: The source language code for transcription (e.g., "eng").
            tgt_lang_code: The target language code for translation (e.g., "hin").
            input_speaker: The gender of the speaker (e.g., "male").
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        await self.validate_parameters(file=file, src_lang_code=src_lang_code, tgt_lang_code=tgt_lang_code,input_speaker=input_speaker, timeout=timeout)
        body = deepcopy_minimal(
            {
                "file": file,
                "src_lang_code": src_lang_code,
                "tgt_lang_code": tgt_lang_code,
                "input_speaker": input_speaker,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])

        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return await self._post(  # type: ignore[return-value]
            "/api/v1/languagelabs/sts_trans/upload",
            body=async_maybe_transform(body, StsTransUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StsTransUploadResponse,
        )


class StsTransResourceWithRawResponse:
    def __init__(self, sts_trans: StsTransResource) -> None:
        self._sts_trans = sts_trans
        self.speech_to_speech_translation = to_raw_response_wrapper(sts_trans.upload)


class StsTransResourceWithStreamingResponse:
    def __init__(self, sts_trans: StsTransResource) -> None:
        self._sts_trans = sts_trans
        self.speech_to_speech_translation = to_streamed_response_wrapper(sts_trans.upload)


class AsyncStsTransResourceWithRawResponse:
    def __init__(self, sts_trans: AsyncStsTransResource) -> None:
        self._sts_trans = sts_trans
        self.speech_to_speech_translation = async_to_raw_response_wrapper(sts_trans.upload)


class AsyncStsTransResourceWithStreamingResponse:
    def __init__(self, sts_trans: AsyncStsTransResource) -> None:
        self._sts_trans = sts_trans
        self.speech_to_speech_translation = async_to_streamed_response_wrapper(sts_trans.upload)

