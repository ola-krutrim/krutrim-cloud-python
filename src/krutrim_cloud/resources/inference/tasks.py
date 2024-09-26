# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import os
import httpx

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
from ...types.inference import task_list_params, task_create_params
from ...types.inference.task_list_response import TaskListResponse
from ...types.inference.task_create_response import TaskCreateResponse
from ...types.inference.task_retrieve_response import TaskRetrieveResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def _validate_create_parameters(self,
        argument: str,
        checkpoint: str,
        environ: str,
        max_batch_size: int,
        max_replicas: int,
        min_replicas: int,
        model: str,
        namespace: str,
        ngpu: int,
        path: str,
        priority: int,
        s3_access_key: str,
        s3_endpoint: str,
        s3_region: str,
        s3_secret: str,
        ):
        # Validate 'checkpoint'
        if checkpoint is None or not isinstance(checkpoint, str) or not checkpoint.strip() or len(checkpoint) == 0:
            raise ValueError("Invalid'checkpoint': It must be a non-empty string and not None.")
        
        # Validate 'model'
        if model is None or not isinstance(model, str) or not model.strip() or len(model) == 0:
            raise ValueError("Invalid 'model': It must be a non-empty string and not None.")
        
        # Validate 'namespace'
        if namespace is None or not isinstance(namespace, str) or not namespace.strip() or len(namespace) == 0:
            raise ValueError("Invalid 'namespace': It must be a non-empty string and not None.")
        
        # Validate 'max_batch_size'
        if max_batch_size is None or not isinstance(max_batch_size, int) or max_batch_size <= 0:
            raise ValueError("Invalid 'max_batch_size': It must be a positive integer and not None, max_batch_size is 256")
        
        # Validate 'max_replicas'
        if max_replicas is None or not isinstance(max_replicas, int) or max_replicas <= 0:
            raise ValueError("Invalid 'max_replicas': It must be a positive integer and not None, default value is 1")
        
        # Validate 'min_replicas'
        if min_replicas is None or not isinstance(min_replicas, int) or min_replicas <= 0:
            raise ValueError("Invalid 'min_replicas': It must be a positive integer and not None, default value is 1")
        
        # Validate 'ngpu'
        if ngpu is None or not isinstance(ngpu, int) or ngpu <= 0:
            raise ValueError("Invalid 'ngpu': It must be a positive integer and not None, default value is 1")
        
        # Validate 'priority'
        if priority is None or not isinstance(priority, int) or priority <= 0:
            raise ValueError("Invalid 'priority': It must be a positive integer and not None, default value is 1")
        
        # Validate 'argument'
        if argument and not isinstance(argument, str):
            raise ValueError("Invalid 'argument': It must be a string.")

        # Validate 'environ'
        if environ and not isinstance(environ, str):
            raise ValueError("Invalid 'environ': It must be a string.")
        
        # Validate 'path'
        if path and not isinstance(path, str):
            raise ValueError("Invalid 'path': It must be a string.")

        # Validate 's3_access_key'
        if s3_access_key and  not isinstance(s3_access_key, str):
            raise ValueError("Invalid 's3_access_key': It must be a string.")

        # Validate 's3_endpoint'
        if s3_endpoint and not isinstance(s3_endpoint, str):
            raise ValueError("Invalid 's3_endpoint': It must be a string.")

        # Validate 's3_region'
        if s3_region and not isinstance(s3_region, str):
            raise ValueError("Invalid 's3_region': It must be a string.")
        
        # Validate 's3_secret'
        if s3_secret and not isinstance(s3_secret, str):
            raise ValueError("Invalid 's3_secret': It must be a string.")

    def _validate_cancel_parameters(self, id):
        # Validate 'id'
        if id is None or not isinstance(id, str) or not id.strip() or len(id) == 0:
            raise ValueError("Invalid 'id': It must be a non-empty string and not None.")

    def _validate_retrieve_parameters(self, id):
        # Validate 'id'
        if id is None or not isinstance(id, str) or not id.strip() or len(id) == 0:
            raise ValueError("Invalid 'id': It must be a non-empty string and not None.")


    def create(
        self,
        *,
        argument: str | NotGiven = NOT_GIVEN,
        checkpoint: str | NotGiven = NOT_GIVEN,
        environ: str | NotGiven = NOT_GIVEN,
        max_batch_size: int | NotGiven = NOT_GIVEN,
        max_replicas: int | NotGiven = NOT_GIVEN,
        min_replicas: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        namespace: str | NotGiven = NOT_GIVEN,
        ngpu: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        s3_access_key: str | NotGiven = NOT_GIVEN,
        s3_endpoint: str | NotGiven = NOT_GIVEN,
        s3_region: str | NotGiven = NOT_GIVEN,
        s3_secret: str | NotGiven = NOT_GIVEN,
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

          checkpoint: Checkpoint name.

          environ: environment variable to parse to inference engine

          max_batch_size: max batch size

          max_replicas: Max number of replicas

          min_replicas: Min number of replicas

          model: Model name.

          namespace: Task Name.

          ngpu: Number of GPU to be used by the inference task.

          path: Checkpoint path.

          priority: Task priority.

          s3_access_key: S3 access key

          s3_endpoint: S3 endpoint

          s3_region: S3 region

          s3_secret: S3 secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_create_parameters(
            checkpoint=checkpoint,
            max_batch_size=max_batch_size,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            model=model,
            namespace=namespace,
            ngpu=ngpu,
            priority=priority,
            path=path,
            s3_endpoint=s3_endpoint,
            s3_region=s3_region,
            s3_access_key=s3_access_key,
            s3_secret=s3_secret,
            argument=argument,
            environ=environ
            )
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        response =  self._post(
            "/api/v1/inference/tasks",
            body=maybe_transform(
                {
                    "argument": argument,
                    "checkpoint": checkpoint,
                    "environ": environ,
                    "max_batch_size": max_batch_size,
                    "max_replicas": max_replicas,
                    "min_replicas": min_replicas,
                    "model": model,
                    "namespace": namespace,
                    "ngpu": ngpu,
                    "path": path,
                    "priority": priority,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )
        model_id = self._client.registry.model_registry.fetch_model_id(model_name=model)
        response.name = self._client.registry.model_registry.fetch_model_name(model_id)
        
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/inference/tasks/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

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
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_cancel_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
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
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)
    async def _validate_create_parameters(self,
        checkpoint: str,
        max_batch_size: int,
        max_replicas: int,
        min_replicas: int,
        model: str,
        namespace: str,
        ngpu: int,
        priority: int,
        path: str,
        s3_endpoint: str,
        s3_region: str,
        s3_access_key: str,
        s3_secret: str,
        argument: str,
        environ: str
        ):
        # Validate 'checkpoint'
        if checkpoint is None or not isinstance(checkpoint, str) or not checkpoint.strip() or len(checkpoint) == 0:
            raise ValueError("Invalid'checkpoint': It must be a non-empty string and not None.")
        
        # Validate 'model'
        if model is None or not isinstance(model, str) or not model.strip() or len(model) == 0:
            raise ValueError("Invalid 'model': It must be a non-empty string and not None.")
        
        # Validate 'namespace'
        if namespace is None or not isinstance(namespace, str) or not namespace.strip() or len(namespace) == 0:
            raise ValueError("Invalid 'namespace': It must be a non-empty string and not None.")
        
        # Validate 'max_batch_size'
        if max_batch_size is None or not isinstance(max_batch_size, int) or max_batch_size <= 0:
            raise ValueError("Invalid 'max_batch_size': It must be a positive integer and not None, max_batch_size is 256")
        
        # Validate 'max_replicas'
        if max_replicas is None or not isinstance(max_replicas, int) or max_replicas <= 0:
            raise ValueError("Invalid 'max_replicas': It must be a positive integer and not None, default value is 1")
        
        # Validate 'min_replicas'
        if min_replicas is None or not isinstance(min_replicas, int) or min_replicas <= 0:
            raise ValueError("Invalid 'min_replicas': It must be a positive integer and not None, default value is 1")
        
        # Validate 'ngpu'
        if ngpu is None or not isinstance(ngpu, int) or ngpu <= 0:
            raise ValueError("Invalid 'ngpu': It must be a positive integer and not None, default value is 1")
        
        # Validate 'priority'
        if priority is None or not isinstance(priority, int) or priority <= 0:
            raise ValueError("Invalid 'priority': It must be a positive integer and not None, default value is 1")
        
        # Validate 'argument'
        if argument and not isinstance(argument, str):
            raise ValueError("Invalid 'argument': It must be a string.")

        # Validate 'environ'
        if environ and not isinstance(environ, str):
            raise ValueError("Invalid 'environ': It must be a string.")
        
        # Validate 'path'
        if path and not isinstance(path, str):
            raise ValueError("Invalid 'path': It must be a string.")

        # Validate 's3_access_key'
        if s3_access_key and  not isinstance(s3_access_key, str):
            raise ValueError("Invalid 's3_access_key': It must be a string.")

        # Validate 's3_endpoint'
        if s3_endpoint and not isinstance(s3_endpoint, str):
            raise ValueError("Invalid 's3_endpoint': It must be a string.")

        # Validate 's3_region'
        if s3_region and not isinstance(s3_region, str):
            raise ValueError("Invalid 's3_region': It must be a string.")
        
        # Validate 's3_secret'
        if s3_secret and not isinstance(s3_secret, str):
            raise ValueError("Invalid 's3_secret': It must be a string.")


    async def _validate_cancel_parameters(self, id):
        # Validate 'id'
        if id is None or not isinstance(id, str) or not id.strip() or len(id) == 0:
            raise ValueError("Invalid 'id': It must be a non-empty string and not None.")

    async def _validate_retrieve_parameters(self, id):
        # Validate 'id'
        if id is None or not isinstance(id, str) or not id.strip() or len(id) == 0:
            raise ValueError("Invalid 'id': It must be a non-empty string and not None.")


    async def create(
        self,
        *,
        argument: str | NotGiven = NOT_GIVEN,
        checkpoint: str | NotGiven = NOT_GIVEN,
        environ: str | NotGiven = NOT_GIVEN,
        max_batch_size: int | NotGiven = NOT_GIVEN,
        max_replicas: int | NotGiven = NOT_GIVEN,
        min_replicas: int | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        namespace: str | NotGiven = NOT_GIVEN,
        ngpu: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        s3_access_key: str | NotGiven = NOT_GIVEN,
        s3_endpoint: str | NotGiven = NOT_GIVEN,
        s3_region: str | NotGiven = NOT_GIVEN,
        s3_secret: str | NotGiven = NOT_GIVEN,
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

          checkpoint: Checkpoint name.

          environ: environment variable to parse to inference engine

          max_batch_size: max batch size

          max_replicas: Max number of replicas

          min_replicas: Min number of replicas

          model: Model name.

          namespace: Task Name.

          ngpu: Number of GPU to be used by the inference task.

          path: Checkpoint path.

          priority: Task priority.

          s3_access_key: S3 access key

          s3_endpoint: S3 endpoint

          s3_region: S3 region

          s3_secret: S3 secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_create_parameters(
            checkpoint=checkpoint,
            max_batch_size=max_batch_size,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            model=model,
            namespace=namespace,
            ngpu=ngpu,
            priority=priority,
            path=path,
            s3_endpoint=s3_endpoint,
            s3_region=s3_region,
            s3_access_key=s3_access_key,
            s3_secret=s3_secret,
            argument=argument,
            environ=environ,
            )
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/v1/inference/tasks",
            body=await async_maybe_transform(
                {
                    "argument": argument,
                    "checkpoint": checkpoint,
                    "environ": environ,
                    "max_batch_size": max_batch_size,
                    "max_replicas": max_replicas,
                    "min_replicas": min_replicas,
                    "model": model,
                    "namespace": namespace,
                    "ngpu": ngpu,
                    "path": path,
                    "priority": priority,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
