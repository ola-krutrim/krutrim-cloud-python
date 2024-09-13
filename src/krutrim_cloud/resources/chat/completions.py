# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional, Union, List

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
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.chat.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        return CompletionsResourceWithStreamingResponse(self)

    supported_models = [
        "Krutrim-spectre-v2",
        "Mistral-7B-Instruct",
        "Meta-Llama-3-8B-Instruct",
        "Gemma-2-27B-IT",
    ]

    context_8k_models: List[str] = [
        "Mistral-7B-Instruct",
        "Meta-Llama-3-8B-Instruct",
    ]

    context_4k_models: List[str] = [
        "Krutrim-spectre-v2",
        "Gemma-2-27B-IT",
    ]

    context_128k_models: List[str] = []

    def validate_parameters(
        self,
        messages: Iterable[completion_create_params.Message] | List[Dict[str, str]],
        model: str,
        frequency_penalty: float | Union[object, None],
        logit_bias: Dict[str, int] | Union[object, None],
        logprobs: bool | Union[object, None],
        max_tokens: int | Union[object, None],
        n: int | Union[object, None],
        presence_penalty: float | Union[object, None],
        response_format: Dict[str, str] | Union[object, None],
        stop: Optional[str] | Union[object, None],
        stream: bool | Union[object, None],
        temperature: float | Union[object, None],
        top_logprobs: int | Union[object, None],
        top_p: float | Union[object, None],
        timeout: Union[float, httpx.Timeout, None, object],
        skip_special_tokens: bool | Union[object, None],
    ):
        # Validate messages
        if not isinstance(messages, list):
            raise ValueError("'messages' must be a list of dictionaries.")

        for message in messages:
            if not isinstance(message, dict):  # type: ignore
                raise ValueError("Each message in 'messages' must be a dictionary.")

            # Validate 'role' key
            if "role" not in message:
                raise ValueError("Each message dictionary must contain a 'role' key.")
            if message["role"] not in ["system", "user", "assistant"]:
                raise ValueError("The 'role' key must be one of 'system', 'user', or 'assistant'.")

            # Validate 'content' key
            if "content" not in message:
                raise ValueError("Each message dictionary must contain a 'content' key.")
            if not isinstance(message["content"], str):  # type: ignore
                raise ValueError("The 'content' key must be a string.")
            if not message["content"]:
                raise ValueError("The 'content' key cannot be empty.")

        # Validate model
        if not isinstance(model, str):  # type: ignore
            raise ValueError("'model' must be a string.")

        # Validate frequency_penalty
        if frequency_penalty is not NOT_GIVEN:
            if not isinstance(frequency_penalty, (float, int)):
                raise ValueError("'frequency_penalty' must be a float or int.")
            if isinstance(frequency_penalty, float) and not (-2.0 <= frequency_penalty <= 2.0):
                raise ValueError("'frequency_penalty' must be between -2 and 2.")
            if isinstance(frequency_penalty, int) and not (-2 <= frequency_penalty <= 2):
                raise ValueError("'frequency_penalty' must be between -2 and 2.")

        # Validate logit_bias
        if logit_bias is not NOT_GIVEN:
            if not isinstance(logit_bias, dict):
                raise ValueError("'logit_bias' must be a dictionary.")
            for key, value in logit_bias.items():  # type: ignore
                if not isinstance(key, (str, int)) or not isinstance(value, int):
                    raise ValueError("'logit_bias' keys must be strings/int and values must be integers.")

        # Validate logprobs
        if logprobs is not NOT_GIVEN:
            if not isinstance(logprobs, bool):
                raise ValueError("'logprobs' must be a boolean.")

        # Validate max_tokens
        if max_tokens is not NOT_GIVEN:
            if not isinstance(max_tokens, int):
                raise ValueError("'max_tokens' must be an integer.")
            if max_tokens <= 0:
                raise ValueError("'max_tokens' must be greater than 0.")
            if model in self.context_4k_models and max_tokens > 4096:
                raise ValueError(f"'max_tokens' must be less than 4096 for {model}.")
            if model in self.context_8k_models and max_tokens > 8192:
                raise ValueError(f"'max_tokens' must be less than 8192 for {model}.")
            if model in self.context_128k_models and max_tokens > 128000:
                raise ValueError(f"'max_tokens' must be less than 128000 for {model}.")

        # Validate n
        if n is not NOT_GIVEN:
            if not isinstance(n, int):
                raise ValueError("'n' must be an integer.")
            if n <= 0:
                raise ValueError("'n' must be greater than 0.")

        # Validate presence_penalty
        if presence_penalty is not NOT_GIVEN:
            if not isinstance(presence_penalty, (float, int)):
                raise ValueError("'presence_penalty' must be a float or int.")
            if isinstance(presence_penalty, float) and not (-2.0 <= presence_penalty <= 2.0):
                raise ValueError("'presence_penalty' must be between -2 and 2.")
            if isinstance(presence_penalty, int) and not (-2 <= presence_penalty <= 2):
                raise ValueError("'presence_penalty' must be between -2 and 2.")

        # Validate response_format
        if response_format is not NOT_GIVEN:
            if not isinstance(response_format, dict):
                raise ValueError("'response_format' must be a dictionary.")
            if "type" not in response_format or response_format["type"] not in ["text"]:
                raise ValueError("'response_format' must be a dictionary with a 'type' key set to 'text'.")

        # Validate stop
        if stop is not NOT_GIVEN:
            if not (isinstance(stop, str) or stop is None):
                raise ValueError("'stop' must be a string or None.")

        # Validate stream
        if stream is not NOT_GIVEN:
            if not isinstance(stream, bool):
                raise ValueError("'stream' must be a boolean.")

        # Validate temperature
        if temperature is not NOT_GIVEN:
            if not isinstance(temperature, (float, int)):
                raise ValueError("'temperature' must be a float/int.")
            if isinstance(temperature, float) and not (0.0 <= temperature <= 2.0):
                raise ValueError("'temperature' must be between 0 and 2.")
            if isinstance(temperature, int) and not (0 <= temperature <= 2):
                raise ValueError("'temperature' must be between 0 and 2.")

        # Validate top_logprobs
        if top_logprobs is not NOT_GIVEN:
            if not isinstance(top_logprobs, int):
                raise ValueError("'top_logprobs' must be an integer.")
            if not (0 <= top_logprobs <= 50):
                raise ValueError("'top_logprobs' must be between 0 and 50.")

        # Validate top_p
        if top_p is not NOT_GIVEN:
            if not isinstance(top_p, float):
                raise ValueError("'top_p' must be a float.")
            if not (0 < top_p <= 1):
                raise ValueError("'top_p' must be greater than 0.0 and less than and 1.0")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

        # Validate skip_special_tokens
        if skip_special_tokens is not NOT_GIVEN:
            if not isinstance(skip_special_tokens, bool):
                raise ValueError("'skip_special_tokens' must be a boolean.")

    def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message] | List[Dict[str, str]],
        model: str,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, int] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Optional[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        skip_special_tokens: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Create a chat completion

        Args:
            model: "Krutrim-spectre-v2", Supported Values are:
            "Krutrim-spectre-v2",
            "Mistral-7B-Instruct",
            "Meta-Llama-3-8B-Instruct",
            "Gemma-2-27B-IT",

            messages: [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Hello!"
                }
            ]

            frequency_penalty: 0, # Optional, Defaults to 0. Range: -2 to 2

            logit_bias: {2435: -100, 640: -100}

            logprobs: true, # Optional, Defaults to false

            top_logprobs: 2, # Optional. Range: 0 to 50

            max_tokens: 256, # Optional

            n: 1, # Optional, Defaults to 1

            presence_penalty: 0, # Optional, Defaults to 0. Range: -2 to 2

            response_format: { "type": "text" }, # Optional, Defaults to text

            stop: null, # Optional, Defaults to null. Can take up to 4 sequences where the API will stop generating further tokens.

            stream: false, # Optional, Defaults to false

            temperature: 0, # Optional, Defaults to 1. Range: 0 to 2

            top_p: 1 # Optional, Defaults to 1. We generally recommend altering this or temperature but not both.

            skip_special_tokens: False # Optional, Defaults to False which allows special tokens like <reflection>, <thinking>, <output> in the output text.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """

        self.validate_parameters(
            messages=messages,
            model=model,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            presence_penalty=presence_penalty,
            response_format=response_format,
            stop=stop,
            stream=stream,
            temperature=temperature,
            top_logprobs=top_logprobs,
            top_p=top_p,
            timeout=timeout,
            skip_special_tokens=skip_special_tokens,
        )

        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "skip_special_tokens": skip_special_tokens,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        return AsyncCompletionsResourceWithStreamingResponse(self)

    supported_models = [
        "Krutrim-spectre-v2",
        "Mistral-7B-Instruct",
        "Meta-Llama-3-8B-Instruct",
        "Gemma-2-27B-IT",
    ]

    context_8k_models: List[str] = [
        "Mistral-7B-Instruct",
        "Meta-Llama-3-8B-Instruct",
    ]

    context_4k_models: List[str] = [
        "Krutrim-spectre-v2",
        "Gemma-2-27B-IT",
    ]

    context_128k_models: List[str] = []

    async def validate_parameters(
        self,
        messages: Iterable[completion_create_params.Message] | List[Dict[str, str]],
        model: str,
        frequency_penalty: float | Union[object, None],
        logit_bias: Dict[str, int] | Union[object, None],
        logprobs: bool | Union[object, None],
        max_tokens: int | Union[object, None],
        n: int | Union[object, None],
        presence_penalty: float | Union[object, None],
        response_format: Dict[str, str] | Union[object, None],
        stop: Optional[str] | Union[object, None],
        stream: bool | Union[object, None],
        temperature: float | Union[object, None],
        top_logprobs: int | Union[object, None],
        top_p: float | Union[object, None],
        timeout: Union[float, httpx.Timeout, None, object],
        skip_special_tokens: bool | Union[object, None],
    ):
        # Validate messages
        if not isinstance(messages, list):
            raise ValueError("'messages' must be a list of dictionaries.")

        for message in messages:
            if not isinstance(message, dict):  # type: ignore
                raise ValueError("Each message in 'messages' must be a dictionary.")

            # Validate 'role' key
            if "role" not in message:
                raise ValueError("Each message dictionary must contain a 'role' key.")
            if message["role"] not in ["system", "user", "assistant"]:
                raise ValueError("The 'role' key must be one of 'system', 'user', or 'assistant'.")

            # Validate 'content' key
            if "content" not in message:
                raise ValueError("Each message dictionary must contain a 'content' key.")
            if not isinstance(message["content"], str):  # type: ignore
                raise ValueError("The 'content' key must be a string.")
            if not message["content"]:
                raise ValueError("The 'content' key cannot be empty.")

        # Validate model
        if not isinstance(model, str):  # type: ignore
            raise ValueError("'model' must be a string.")

        # Validate frequency_penalty
        if frequency_penalty is not NOT_GIVEN:
            if not isinstance(frequency_penalty, (float, int)):
                raise ValueError("'frequency_penalty' must be a float or int.")
            if isinstance(frequency_penalty, float) and not (-2.0 <= frequency_penalty <= 2.0):
                raise ValueError("'frequency_penalty' must be between -2 and 2.")
            if isinstance(frequency_penalty, int) and not (-2 <= frequency_penalty <= 2):
                raise ValueError("'frequency_penalty' must be between -2 and 2.")

        # Validate logit_bias
        if logit_bias is not NOT_GIVEN:
            if not isinstance(logit_bias, dict):
                raise ValueError("'logit_bias' must be a dictionary.")
            for key, value in logit_bias.items():  # type: ignore
                if not isinstance(key, (str, int)) or not isinstance(value, int):
                    raise ValueError("'logit_bias' keys must be strings/int and values must be integers.")

        # Validate logprobs
        if logprobs is not NOT_GIVEN:
            if not isinstance(logprobs, bool):
                raise ValueError("'logprobs' must be a boolean.")

        # Validate max_tokens
        if max_tokens is not NOT_GIVEN:
            if not isinstance(max_tokens, int):
                raise ValueError("'max_tokens' must be an integer.")
            if max_tokens <= 0:
                raise ValueError("'max_tokens' must be greater than 0.")
            if model in self.context_4k_models and max_tokens > 4096:
                raise ValueError(f"'max_tokens' must be less than 4096 for {model}.")
            if model in self.context_8k_models and max_tokens > 8192:
                raise ValueError(f"'max_tokens' must be less than 8192 for {model}.")
            if model in self.context_128k_models and max_tokens > 128000:
                raise ValueError(f"'max_tokens' must be less than 128000 for {model}.")

        # Validate n
        if n is not NOT_GIVEN:
            if not isinstance(n, int):
                raise ValueError("'n' must be an integer.")
            if n <= 0:
                raise ValueError("'n' must be greater than 0.")

        # Validate presence_penalty
        if presence_penalty is not NOT_GIVEN:
            if not isinstance(presence_penalty, (float, int)):
                raise ValueError("'presence_penalty' must be a float or int.")
            if isinstance(presence_penalty, float) and not (-2.0 <= presence_penalty <= 2.0):
                raise ValueError("'presence_penalty' must be between -2 and 2.")
            if isinstance(presence_penalty, int) and not (-2 <= presence_penalty <= 2):
                raise ValueError("'presence_penalty' must be between -2 and 2.")

        # Validate response_format
        if response_format is not NOT_GIVEN:
            if not isinstance(response_format, dict):
                raise ValueError("'response_format' must be a dictionary.")
            if "type" not in response_format or response_format["type"] not in ["text"]:
                raise ValueError("'response_format' must be a dictionary with a 'type' key set to 'text'.")

        # Validate stop
        if stop is not NOT_GIVEN:
            if not (isinstance(stop, str) or stop is None):
                raise ValueError("'stop' must be a string or None.")

        # Validate stream
        if stream is not NOT_GIVEN:
            if not isinstance(stream, bool):
                raise ValueError("'stream' must be a boolean.")

        # Validate temperature
        if temperature is not NOT_GIVEN:
            if not isinstance(temperature, (float, int)):
                raise ValueError("'temperature' must be a float/int.")
            if isinstance(temperature, float) and not (0.0 <= temperature <= 2.0):
                raise ValueError("'temperature' must be between 0 and 2.")
            if isinstance(temperature, int) and not (0 <= temperature <= 2):
                raise ValueError("'temperature' must be between 0 and 2.")

        # Validate top_logprobs
        if top_logprobs is not NOT_GIVEN:
            if not isinstance(top_logprobs, int):
                raise ValueError("'top_logprobs' must be an integer.")
            if not (0 <= top_logprobs <= 50):
                raise ValueError("'top_logprobs' must be between 0 and 50.")

        # Validate top_p
        if top_p is not NOT_GIVEN:
            if not isinstance(top_p, float):
                raise ValueError("'top_p' must be a float.")
            if not (0 < top_p <= 1):
                raise ValueError("'top_p' must be greater than 0.0 and less than and 1.0")

        # Validate timeout
        if timeout is not NOT_GIVEN:
            if not isinstance(timeout, (float, int, httpx.Timeout, type(None))):
                raise ValueError("'timeout' must be a float, int, httpx.Timeout, or None.")

        # Validate skip_special_tokens
        if skip_special_tokens is not NOT_GIVEN:
            if not isinstance(skip_special_tokens, bool):
                raise ValueError("'skip_special_tokens' must be a boolean.")

    async def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: str,
        frequency_penalty: float | NotGiven = NOT_GIVEN,
        logit_bias: Dict[str, int] | NotGiven = NOT_GIVEN,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        presence_penalty: float | NotGiven = NOT_GIVEN,
        response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
        stop: Optional[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_logprobs: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        skip_special_tokens: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Create a chat completion

        Args:
            model: "Krutrim-spectre-v2", Supported Values are:
            "Krutrim-spectre-v2",
            "Mistral-7B-Instruct",
            "Meta-Llama-3-8B-Instruct",
            "Gemma-2-27B-IT",

            messages: [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Hello!"
                }
            ]

            frequency_penalty: 0, # Optional, Defaults to 0. Range: -2 to 2

            logit_bias: {2435: -100, 640: -100}

            logprobs: true, # Optional, Defaults to false

            top_logprobs: 2, # Optional. Range: 0 to 50

            max_tokens: 256, # Optional

            n: 1, # Optional, Defaults to 1

            presence_penalty: 0, # Optional, Defaults to 0. Range: -2 to 2

            response_format: { "type": "text" }, # Optional, Defaults to text

            stop: null, # Optional, Defaults to null. Can take up to 4 sequences where the API will stop generating further tokens.

            stream: false, # Optional, Defaults to false

            temperature: 0, # Optional, Defaults to 1. Range: 0 to 2

            top_p: 1 # Optional, Defaults to 1. We generally recommend altering this or temperature but not both.

            skip_special_tokens: False # Optional, Defaults to False which allows special tokens like <reflection>, <thinking>, <output> in the output text.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        await self.validate_parameters(
            messages=messages,
            model=model,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            presence_penalty=presence_penalty,
            response_format=response_format,
            stop=stop,
            stream=stream,
            temperature=temperature,
            top_logprobs=top_logprobs,
            top_p=top_p,
            skip_special_tokens=skip_special_tokens,
            timeout=timeout,
        )

        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "response_format": response_format,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "top_logprobs": top_logprobs,
                    "top_p": top_p,
                    "skip_special_tokens": skip_special_tokens,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
