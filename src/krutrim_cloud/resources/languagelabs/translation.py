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
from ...types.languagelabs.translation_response import TranslationResponse as TranslationResponse

__all__ = ["TranslationResource", "AsyncTranslationResource"]

class TranslationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranslationResourceWithRawResponse:
        return TranslationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranslationResourceWithStreamingResponse:
        return TranslationResourceWithStreamingResponse(self)

    def validate_parameters(
        self,
        text: str,
        src_language: str,
        tgt_language: str,
        model: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate src_language
        if not isinstance(src_language, str):
            raise TypeError("'src_language' must be a string.")
        if not src_language:
            raise ValueError("'src_language' cannot be empty.")

        # Validate tgt_language
        if not isinstance(tgt_language, str):
            raise TypeError("'tgt_language' must be a string.")
        if not tgt_language:
            raise ValueError("'tgt_language' cannot be empty.")

        # Validate model
        if not isinstance(model, str):
            raise TypeError("'model' must be a string.")
        if not model:
            raise ValueError("'model' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
        self,
        *,
        text: str,
        src_language: str,
        tgt_language: str,
        model: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TranslationResponse:
        """
        Translate the given text.

        Args:
            text: The input text to translate.
            src_language: The source language (e.g., "eng_Latn").
            tgt_language: The target language (e.g., "hin_Deva").
            model: The model to use for translation.
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        self.validate_parameters(text=text, src_language=src_language, tgt_language=tgt_language, model=model, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "src_language": src_language,
            "tgt_language": tgt_language,
            "model": model,
        }

        # Send the request to the translation API
        return self._post(
            "/api/v1/languagelabs/translation",
            body=maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranslationResponse,
        )


class AsyncTranslationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranslationResourceWithRawResponse:
        return AsyncTranslationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranslationResourceWithStreamingResponse:
        return AsyncTranslationResourceWithStreamingResponse(self)

    async def validate_parameters(
        self,
        text: str,
        src_language: str,
        tgt_language: str,
        model: str,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate src_language
        if not isinstance(src_language, str):
            raise TypeError("'src_language' must be a string.")
        if not src_language:
            raise ValueError("'src_language' cannot be empty.")

        # Validate tgt_language
        if not isinstance(tgt_language, str):
            raise TypeError("'tgt_language' must be a string.")
        if not tgt_language:
            raise ValueError("'tgt_language' cannot be empty.")

        # Validate model
        if not isinstance(model, str):
            raise TypeError("'model' must be a string.")
        if not model:
            raise ValueError("'model' cannot be empty.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
        self,
        *,
        text: str,
        src_language: str,
        tgt_language: str,
        model: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TranslationResponse:
        """
        Translate the given text asynchronously.

        Args:
            text: The input text to translate.
            src_language: The source language (e.g., "eng_Latn").
            tgt_language: The target language (e.g., "hin_Deva").
            model: The model to use for translation.
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        await self.validate_parameters(text=text, src_language=src_language, tgt_language=tgt_language, model=model, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "src_language": src_language,
            "tgt_language": tgt_language,
            "model": model,
        }

        # Send the request to the translation API
        return await self._post(
            "/api/v1/languagelabs/translation",
            body=await async_maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranslationResponse,
        )



class TranslationResourceWithRawResponse:
    def __init__(self, translation: TranslationResource) -> None:
        self._translation = translation
        self.translation = to_raw_response_wrapper(translation.run)


class TranslationResourceWithStreamingResponse:
    def __init__(self, translation: TranslationResource) -> None:
        self._translation = translation
        self.translation = to_streamed_response_wrapper(translation.run)


class AsyncTranslationResourceWithRawResponse:
    def __init__(self, translation: AsyncTranslationResource) -> None:
        self._translation = translation
        self.translation = async_to_raw_response_wrapper(translation.run)


class AsyncTranslationResourceWithStreamingResponse:
    def __init__(self, translation: AsyncTranslationResource) -> None:
        self._translation = translation
        self.translation = async_to_streamed_response_wrapper(translation.run)

