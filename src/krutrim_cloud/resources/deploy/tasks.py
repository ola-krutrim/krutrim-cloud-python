# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx
import os
from typing import Optional

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..._base_client import make_request_options
from ...types.deploy import task_list_params, task_create_params
from ...types.deploy.task_list_response import TaskListResponse
from ...types.deploy.task_create_response import TaskCreateResponse
from ...types.deploy.task_retrieve_response import TaskRetrieveResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self)

    def _validate_create_parameters(
        self,
        bucket_name: str,
        model: str,
        version: str,
        s3_access_key: str,
        s3_endpoint: str,
        s3_region: str,
        s3_secret: str,
        argument: str | NotGiven = NOT_GIVEN,
        max_batch_size: Optional[int] = 256,
        max_replicas: Optional[int] = 1,
        min_replicas: Optional[int] = 1,
        environ: Optional[str] = "",
    ):
        # Validate bucket_name
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("'bucket_name' must be of type string.")

        # Validate model
        if model and not isinstance(model, str):
            raise TypeError("'model' must be of type string.")

        # Validate version
        if version and not isinstance(version, str):
            raise TypeError("'version' must be of type string.")

        # Validate argument
        if argument and not isinstance(argument, str):
            raise TypeError("'argument' must be of type string.")

        # Validate max_batch_size
        if max_batch_size and not isinstance(max_batch_size, int):
            raise TypeError("'max_batch_size' must be of type integer.")

        # Validate max_replicas
        if max_replicas and not isinstance(max_replicas, int):
            raise TypeError("'max_replicas' must be of type integer.")

        # Validate min_replicas
        if min_replicas and not isinstance(min_replicas, int):
            raise TypeError("'min_replicas' must be of type integer.")

        # Validate s3_access_key
        if s3_access_key and not isinstance(s3_access_key, str):
            raise TypeError("'s3_access_key' must be of type string.")

        # Validate s3_endpoint
        if s3_endpoint and not isinstance(s3_endpoint, str):
            raise TypeError("'s3_endpoint' must be of type string.")

        # Validate s3_region
        if s3_region and not isinstance(s3_region, str):
            raise TypeError("'s3_region' must be of type string.")

        # Validate s3_secret
        if s3_secret and not isinstance(s3_secret, str):
            raise TypeError("'s3_secret' must be of type string.")

        # Validate environ
        if environ and not isinstance(environ, str):
            raise TypeError("'environ' must be of type string.")

    def _validate_retrieve_parameters(
        self,
        id: str,
    ):

        # Validate id
        if id and not isinstance(id, str):
            raise TypeError("'id' must be of type string.")

    def _validate_list_parameters(self, limit: int, offset: int):

        # Validate limit
        if limit and not isinstance(limit, int):
            raise TypeError("'limit' must be of type integer.")

        # Validate offset
        if offset and not isinstance(offset, int):
            raise TypeError("'offset' must be of type integer.")

    def _validate_cancel_parameters(
        self,
        id: str,
    ):

        # Validate id
        if id and not isinstance(id, str):
            raise TypeError("'id' must be of type string.")

    def create(
        self,
        *,
        bucket_name: str,
        version: str,
        argument: str | NotGiven = NOT_GIVEN,
        max_batch_size: int | NotGiven = NOT_GIVEN,
        max_replicas: int | NotGiven = NOT_GIVEN,
        min_replicas: int | NotGiven = NOT_GIVEN,
        model: str,
        s3_access_key: str,
        s3_endpoint: str,
        s3_region: str,
        s3_secret: str,
        environ: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create inference task

        Args:
            bucket_name: Bucket name where model files got uploaded

            version: Version of model given while uploading the model to S3 bucket

            argument: additional argument to parse to inference engine

            max_batch_size: max batch size

            max_replicas: Max number of replicas

            min_replicas: Min number of replicas

            model: Model name.

            s3_access_key: S3 access key

            s3_endpoint: S3 endpoint

            s3_region: S3 region

            s3_secret: S3 secret

            environ: additional environment variables as "key_1=value1,key_2=value2" to pass to inference engine

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_create_parameters(
            bucket_name=bucket_name,
            version=version,
            argument=argument,
            max_batch_size=max_batch_size,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            model=model,
            s3_access_key=s3_access_key,
            s3_endpoint=s3_endpoint,
            s3_region=s3_region,
            s3_secret=s3_secret,
            environ=environ,
        )
        # Fetch Model ID from Model Card by given model name
        model_id = self._client.registry.model_registry.fetch_model_id(model_name=model)
        s3_path = f"s3://{bucket_name}/{model}/{version}"

        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        response = self._post(
            "/api/v1/inference/tasks",
            body=maybe_transform(
                {
                    "argument": argument,
                    "max_batch_size": max_batch_size,
                    "max_replicas": max_replicas,
                    "min_replicas": min_replicas,
                    "model": model_id,
                    "path": s3_path,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret,
                    "environ": environ,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )
        response.name = self._client.registry.model_registry.fetch_model_name(response.name)

        self._client.registry.model_registry.add_model_deployment_version(
            model_name=response.name, model_id=model_id, deploy_id=response.id, base_model=""
        )
        return response

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Get inference task information.

        Args:
            id: Task ID

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_retrieve_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        response = self._get(
            f"/api/v1/inference/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )
        response.name = self._client.registry.model_registry.fetch_model_name(response.name)
        return response

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        List inference tasks

        Args:
            limit: Limit the max number of item to be return.

            offset: Offset index.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_list_parameters(limit=limit, offset=offset)

        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        response = self._get(
            "/api/v1/inference/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )
        for task_obj in response.task_list:
            task_obj["name"] = self._client.registry.model_registry.fetch_model_name(task_obj["name"])
        return response

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancel inference task.

        Args:

            id: Task ID

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_cancel_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/inference/tasks/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self)

    async def _validate_create_parameters(
        self,
        model: str,
        s3_access_key: str,
        s3_endpoint: str,
        s3_region: str,
        s3_secret: str,
        argument: str | NotGiven = NOT_GIVEN,
        max_batch_size: Optional[int] = 256,
        max_replicas: Optional[int] = 1,
        min_replicas: Optional[int] = 1,
        environ: Optional[str] = "",
    ):

        # Validate model
        if model and not isinstance(model, str):
            raise TypeError("'model' must be of type string.")

        # Validate path
        if path and not isinstance(path, str):
            raise TypeError("'path' must be of type string.")
        if path and not path.lower().startswith("s3://"):
            raise TypeError("'path' must start with S3:// or s3://")

        # Validate argument
        if argument and not isinstance(argument, str):
            raise TypeError("'argument' must be of type string.")

        # Validate checkpoint
        if checkpoint and not isinstance(checkpoint, str):
            raise TypeError("'checkpoint' must be of type string.")

        # Validate max_batch_size
        if max_batch_size and not isinstance(max_batch_size, int):
            raise TypeError("'max_batch_size' must be of type integer.")

        # Validate max_replicas
        if max_replicas and not isinstance(max_replicas, int):
            raise TypeError("'max_replicas' must be of type integer.")

        # Validate min_replicas
        if min_replicas and not isinstance(min_replicas, int):
            raise TypeError("'min_replicas' must be of type integer.")

        # Validate namespace
        if namespace and not isinstance(namespace, str):
            raise TypeError("'namespace' must be of type string.")

        # Validate priority
        if priority and not isinstance(priority, int):
            raise TypeError("'priority' must be of type integer.")

        # Validate region
        if region and not isinstance(region, str):
            raise TypeError("'region' must be of type string.")

        # Validate s3_access_key
        if s3_access_key and not isinstance(s3_access_key, str):
            raise TypeError("'s3_access_key' must be of type string.")

        # Validate s3_endpoint
        if s3_endpoint and not isinstance(s3_endpoint, str):
            raise TypeError("'s3_endpoint' must be of type string.")

        # Validate s3_region
        if s3_region and not isinstance(s3_region, str):
            raise TypeError("'s3_region' must be of type string.")

        # Validate s3_secret
        if s3_secret and not isinstance(s3_secret, str):
            raise TypeError("'s3_secret' must be of type string.")

        # Validate environ
        if environ and not isinstance(environ, str):
            raise TypeError("'environ' must be of type string.")

    async def _validate_retrieve_parameters(
        self,
        id: str,
    ):

        # Validate id
        if id and not isinstance(id, str):
            raise TypeError("'id' must be of type string.")

    async def _validate_list_parameters(self, limit: int, offset: int):

        # Validate limit
        if limit and not isinstance(limit, int):
            raise TypeError("'limit' must be of type integer.")

        # Validate offset
        if offset and not isinstance(offset, int):
            raise TypeError("'offset' must be of type integer.")

    async def _validate_cancel_parameters(
        self,
        id: str,
    ):

        # Validate id
        if id and not isinstance(id, str):
            raise TypeError("'id' must be of type string.")

    async def create(
        self,
        *,
        argument: str | NotGiven = NOT_GIVEN,
        max_batch_size: int | NotGiven = NOT_GIVEN,
        max_replicas: int | NotGiven = NOT_GIVEN,
        min_replicas: int | NotGiven = NOT_GIVEN,
        model: str,
        s3_access_key: str,
        s3_endpoint: str,
        s3_region: str,
        s3_secret: str,
        environ: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create inference task

        Args:
            argument: additional argument to parse to inference engine

            max_batch_size: max batch size

            max_replicas: Max number of replicas

            min_replicas: Min number of replicas

            model: Model name.

            s3_access_key: S3 access key

            s3_endpoint: S3 endpoint

            s3_region: S3 region

            s3_secret: S3 secret

            environ: additional environment variables as "key_1=value1,key_2=value2" to pass to inference engine

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_create_parameters(
            argument=argument,
            max_batch_size=max_batch_size,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            model=model,
            s3_access_key=s3_access_key,
            s3_endpoint=s3_endpoint,
            s3_region=s3_region,
            s3_secret=s3_secret,
            environ=environ,
        )

        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._post(
            "/api/v1/inference/tasks",
            body=await async_maybe_transform(
                {
                    "argument": argument,
                    "max_batch_size": max_batch_size,
                    "max_replicas": max_replicas,
                    "min_replicas": min_replicas,
                    "model": model,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret,
                    "environ": environ,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Get inference task information.

        Args:
            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_retrieve_parameters(id=id)

        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            f"/api/v1/inference/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskListResponse:
        """
        List inference tasks

        Args:
            limit: Limit the max number of item to be return.

            offset: Offset index.

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_list_parameters(limit=limit, offset=offset)

        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            "/api/v1/inference/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    task_list_params.TaskListParams,
                ),
            ),
            cast_to=TaskListResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancel inference task.

        Args:
            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

            timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_cancel_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/inference/tasks/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.cancel = to_raw_response_wrapper(
            tasks.cancel,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            tasks.cancel,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.cancel = to_streamed_response_wrapper(
            tasks.cancel,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            tasks.cancel,
        )
