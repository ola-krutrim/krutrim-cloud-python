from __future__ import annotations
from typing import Optional
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
from ...types.languagelabs.entity_extraction_response import EntityExtractionResponse as EntityExtractionResponse

__all__ = ["EntityExtractionResource", "AsyncEntityExtractionResource"]


class EntityExtractionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntityExtractionResourceWithRawResponse:
        return EntityExtractionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntityExtractionResourceWithStreamingResponse:
        return EntityExtractionResourceWithStreamingResponse(self)

    def validate_parameters(
            self,
            text: str,
            param_list: Optional[list[str]] = None,
            lang_from: Optional[str] = "hin",
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate param_list
        if param_list is not None:
            if not isinstance(param_list, list):
                raise TypeError("'param_list' must be a list.")
            if not all(isinstance(i, str) for i in param_list):
                raise TypeError("Each item in 'param_list' must be a string.")

        # Validate lang_from
        if lang_from is not None and not isinstance(lang_from, str):
            raise TypeError("'lang_from' must be a string.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    def run(
            self,
            *,
            text: str,
            param_list: Optional[list[str]] = None,
            lang_from: Optional[str] = "hin",
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityExtractionResponse:
        """
        Extract entities from the provided text.

        Args:
            text: The text from which entities need to be extracted.
            param_list: A list of parameters like "ner" and "pii" to define the types of entities.
            lang_from: The source language of the text (e.g., "hin" for Hindi).
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        self.validate_parameters(text=text, param_list=param_list, lang_from=lang_from, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "param_list": param_list or ["ner", "pii"],  # Default to 'ner' and 'pii' if not provided
            "lang_from": lang_from,
        }

        # Send the request to the entity extraction API
        return self._post(
            "/api/v1/languagelabs/entity-extraction",
            body=maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityExtractionResponse,
        )


class AsyncEntityExtractionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntityExtractionResourceWithRawResponse:
        return AsyncEntityExtractionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntityExtractionResourceWithStreamingResponse:
        return AsyncEntityExtractionResourceWithStreamingResponse(self)

    async def validate_parameters(
            self,
            text: str,
            param_list: Optional[list[str]] = None,
            lang_from: Optional[str] = "hin",
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ):
        # Validate text
        if not isinstance(text, str):
            raise TypeError("'text' must be a string.")
        if not text:
            raise ValueError("'text' cannot be empty.")

        # Validate param_list
        if param_list is not None:
            if not isinstance(param_list, list):
                raise TypeError("'param_list' must be a list.")
            if not all(isinstance(i, str) for i in param_list):
                raise TypeError("Each item in 'param_list' must be a string.")

        # Validate lang_from
        if lang_from is not None and not isinstance(lang_from, str):
            raise TypeError("'lang_from' must be a string.")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

    async def run(
            self,
            *,
            text: str,
            param_list: Optional[list[str]] = None,
            lang_from: Optional[str] = "hin",
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityExtractionResponse:
        """
        Extract entities from the provided text (Asynchronous)

        Args:
            text: The text from which entities need to be extracted.
            param_list: A list of parameters like "ner" and "pii" to define the types of entities.
            lang_from: The source language of the text (e.g., "hin" for Hindi).
            extra_headers: Optional headers to send with the request.
            extra_query: Optional query parameters to send with the request.
            extra_body: Optional body content to send with the request.
            timeout: Optional timeout override for the request.
        """
        # Validate parameters before making the API call
        await self.validate_parameters(text=text, param_list=param_list, lang_from=lang_from, timeout=timeout)

        # Prepare the request payload
        payload = {
            "text": text,
            "param_list": param_list or ["ner", "pii"],  # Default to 'ner' and 'pii' if not provided
            "lang_from": lang_from,
        }

        # Send the request to the entity extraction API
        return await self._post(
            "/api/v1/languagelabs/entity-extraction",
            body=await async_maybe_transform(payload, dict),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityExtractionResponse,
        )


class EntityExtractionResourceWithRawResponse:
    def __init__(self, entity_extraction: EntityExtractionResource) -> None:
        self._entity_extraction = entity_extraction
        self.entity_extraction = to_raw_response_wrapper(entity_extraction.run)


class EntityExtractionResourceWithStreamingResponse:
    def __init__(self, entity_extraction: EntityExtractionResource) -> None:
        self._entity_extraction = entity_extraction
        self.entity_extraction = to_streamed_response_wrapper(entity_extraction.run)


class AsyncEntityExtractionResourceWithRawResponse:
    def __init__(self, entity_extraction: AsyncEntityExtractionResource) -> None:
        self._entity_extraction = entity_extraction
        self.entity_extraction = async_to_raw_response_wrapper(entity_extraction.run)


class AsyncEntityExtractionResourceWithStreamingResponse:
    def __init__(self, entity_extraction: AsyncEntityExtractionResource) -> None:
        self._entity_extraction = entity_extraction
        self.entity_extraction = async_to_streamed_response_wrapper(entity_extraction.run)
