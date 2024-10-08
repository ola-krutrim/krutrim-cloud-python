# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._exceptions import KrutrimCloudError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "KrutrimCloud",
    "AsyncKrutrimCloud",
    "Client",
    "AsyncClient",
]


class KrutrimCloud(SyncAPIClient):
    images: resources.ImagesResource
    multimodal: resources.MultimodalResource
    audio: resources.AudioResource
    chat: resources.ChatResource
    registry: resources.RegistryResource
    deploy: resources.DeployResource
    videos: resources.VideosResource
    fine_tuning: resources.FineTuningResource
    inference: resources.InferenceResource
    with_raw_response: KrutrimCloudWithRawResponse
    with_streaming_response: KrutrimCloudWithStreamedResponse


    # client options

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous krutrim-cloud client instance.

        This automatically infers the `api_key` argument from the `KRUTRIM_CLOUD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KRUTRIM_CLOUD_API_KEY")
        if api_key is None:
            raise KrutrimCloudError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KRUTRIM_CLOUD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("KRUTRIM_CLOUD_BASE_URL")
        if base_url is None:
            base_url = f"https://cloud.olakrutrim.com"

        default_headers = {"user-agent": f"Krutrim-Cloud-Python-SDK/{__version__}"}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )
        self.images = resources.ImagesResource(self)
        self.multimodal = resources.MultimodalResource(self)
        self.audio = resources.AudioResource(self)
        self.chat = resources.ChatResource(self)
        self.registry = resources.RegistryResource(self)
        self.deploy = resources.DeployResource(self)
        self.videos = resources.VideosResource(self)
        self.fine_tuning = resources.FineTuningResource(self)
        self.inference = resources.InferenceResource(self)
        self.with_raw_response = KrutrimCloudWithRawResponse(self)
        self.with_streaming_response = KrutrimCloudWithStreamedResponse(self)


    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Krutrim-Cloud-Async": "false",
            **self._custom_headers,
        }

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncKrutrimCloud(AsyncAPIClient):
    images: resources.AsyncImagesResource
    multimodal: resources.AsyncMultimodalResource
    audio: resources.AsyncAudioResource
    chat: resources.AsyncChatResource
    deploy: resources.AsyncDeployResource
    videos: resources.AsyncVideosResource
    fine_tuning: resources.AsyncFineTuningResource
    inference: resources.AsyncInferenceResource
    with_raw_response: resources.AsyncKrutrimCloudWithRawResponse
    with_streaming_response: resources.AsyncKrutrimCloudWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async krutrim-cloud client instance.

        This automatically infers the `api_key` argument from the `KRUTRIM_CLOUD_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("KRUTRIM_CLOUD_API_KEY")
        if api_key is None:
            raise KrutrimCloudError(
                "The api_key client option must be set either by passing api_key to the client or by setting the KRUTRIM_CLOUD_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("KRUTRIM_CLOUD_BASE_URL")
        if base_url is None:
            base_url = f"https://cloud.olakrutrim.com"

        default_headers = {"user-agent": f"Krutrim-Cloud-Python-SDK/{__version__}"}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.images = resources.AsyncImagesResource(self)
        self.multimodal = resources.AsyncMultimodalResource(self)
        self.audio = resources.AsyncAudioResource(self)
        self.chat = resources.AsyncChatResource(self)
        self.deploy = resources.AsyncDeployResource(self)
        self.videos = resources.AsyncVideosResource(self)
        self.fine_tuning = resources.AsyncFineTuningResource(self)
        self.inference = resources.AsyncInferenceResource(self)
        self.with_raw_response = resources.AsyncKrutrimCloudWithRawResponse(self)
        self.with_streaming_response =resources. AsyncKrutrimCloudWithStreamedResponse(self)


    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Krutrim-Cloud-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class KrutrimCloudWithRawResponse:
    def __init__(self, client: KrutrimCloud) -> None:
        self.images = resources.ImagesResourceWithRawResponse(client.images)
        self.multimodal = resources.MultimodalResourceWithRawResponse(client.multimodal)
        self.audio = resources.AudioResourceWithRawResponse(client.audio)
        self.chat = resources.ChatResourceWithRawResponse(client.chat)
        self.fine_tuning = resources.FineTuningResourceWithRawResponse(client.fine_tuning)
        self.inference = resources.InferenceResourceWithRawResponse(client.inference)


class AsyncKrutrimCloudWithRawResponse:
    def __init__(self, client: AsyncKrutrimCloud) -> None:
        self.images = resources.AsyncImagesResourceWithRawResponse(client.images)
        self.multimodal = resources.AsyncMultimodalResourceWithRawResponse(client.multimodal)
        self.audio = resources.AsyncAudioResourceWithRawResponse(client.audio)
        self.chat = resources.AsyncChatResourceWithRawResponse(client.chat)
        self.fine_tuning = resources.AsyncFineTuningResourceWithRawResponse(client.fine_tuning)
        self.inference = resources.AsyncInferenceResourceWithRawResponse(client.inference)


class KrutrimCloudWithStreamedResponse:
    def __init__(self, client: KrutrimCloud) -> None:
        self.images = resources.ImagesResourceWithStreamingResponse(client.images)
        self.multimodal = resources.MultimodalResourceWithStreamingResponse(client.multimodal)
        self.audio = resources.AudioResourceWithStreamingResponse(client.audio)
        self.chat = resources.ChatResourceWithStreamingResponse(client.chat)
        self.fine_tuning = resources.FineTuningResourceWithStreamingResponse(client.fine_tuning)
        self.inference = resources.InferenceResourceWithStreamingResponse(client.inference)


class AsyncKrutrimCloudWithStreamedResponse:
    def __init__(self, client: AsyncKrutrimCloud) -> None:
        self.images = resources.AsyncImagesResourceWithStreamingResponse(client.images)
        self.multimodal = resources.AsyncMultimodalResourceWithStreamingResponse(client.multimodal)
        self.audio = resources.AsyncAudioResourceWithStreamingResponse(client.audio)
        self.chat = resources.AsyncChatResourceWithStreamingResponse(client.chat)
        self.fine_tuning = resources.AsyncFineTuningResourceWithStreamingResponse(client.fine_tuning)
        self.inference = resources.AsyncInferenceResourceWithStreamingResponse(client.inference)


Client = KrutrimCloud

AsyncClient = AsyncKrutrimCloud
