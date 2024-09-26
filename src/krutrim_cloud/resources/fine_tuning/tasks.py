# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import os
import httpx
import requests
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
from ...types.fine_tuning import task_list_params, task_logs_params, task_create_params
from ...types.fine_tuning.task_list_response import TaskListResponse
from ...types.fine_tuning.task_logs_response import TaskLogsResponse
from ...types.fine_tuning.task_create_response import TaskCreateResponse
from ...types.fine_tuning.task_retrieve_response import TaskRetrieveResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):

    def __init__(self, client: object) -> None:
        super().__init__(client)  # Initialize the parent class
        self._client = client  # type: ignore
        # Configure the model registry server URL
        self._model_registry_url: Union[str, URL] = ""
        if os.environ.get("KRUTRIM_CLOUD_MODEL_REGISTRY_URL"):
            self._model_registry_url = str(os.environ.get("KRUTRIM_CLOUD_MODEL_REGISTRY_URL"))
        else:
            self._model_registry_url = self._client.base_url

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def _validate_create_parameters(
        self,
        batch: int,
        dataset: str, 
        engine: str, 
        epoch: int, 
        lora_alpha: int,
        lora_rank: int,
        lr: int,
        mode: str,
        model: str,
        namespace: str,
        ngpu: int,
        priority: int,
        seed: int,
        task_name: str,
        test_dataset: str,
        total_checkpoint: int,
        version: str
         ):
        # Validate batch
        if batch is not None:
            if not isinstance(batch, int):
                raise TypeError("'batch' must be of type int.")
            if batch <= 0:
                raise ValueError("'batch' must be greater than 0, default value is 8")
        else:
            if batch is None:
                raise ValueError("'batch' must be a non-empty value, default value is 8")
 
        # Validate dataset
        if dataset is not None:
            if not isinstance(dataset, str):
                raise TypeError("'dataset' must be of type string.")
            if not dataset.strip():
                raise ValueError("'dataset' must be a non-empty string.")
        else:
            if dataset is None:
                raise ValueError("'dataset' must be a non-empty string.")

        # Validate engine
        if engine is not None:
            if not isinstance(engine, str):
                raise TypeError("'engine' must be of type string.")
            if not engine.strip():
                raise ValueError("'engine' must be a non-empty string.")
        else:
            if engine is None:
                raise ValueError("'engine' must be a non-empty string.")

        # Validate epoch
        if epoch is not None:
            if not isinstance(epoch, int):
                raise TypeError("'epoch' must be of type int.")
            if epoch <= 0:
                raise ValueError("'epoch' must be greater than 0.")
        else:
            if epoch is None:
                raise ValueError("'epoch' must be non-empty value, default value is 1")

        # Validate lora_alpha
        if lora_alpha is not None:
            if not isinstance(lora_alpha, int):
                raise TypeError("'lora_alpha' must be of type int.")
            if not (0 <= lora_alpha <= 128):
                raise ValueError("'lora_alpha' must be between 0 and 128, default value is 0")
        else:
            if lora_alpha is None:
                raise ValueError("'lora_alpha' must be non-empty value, default value is 0")

        # Validate lora_rank
        if lora_rank is not None:
            if not isinstance(lora_rank, int):
                raise TypeError("'lora_rank' must be of type int.")
            if not (0 <= lora_rank <= 64):
                raise ValueError("'lora_rank' must be between 0 and 64, default value is 0")
        else:
            if lora_rank is None:
                raise ValueError("'lora_rank' must be between 0 and 64, default valu is 0")

        # Validate lr
        if lr is not None:
            if lr <= 0:
                raise ValueError("'lr' must be greater than 0.")
            if not isinstance(lr, int):
                raise TypeError("'lr' must be of type int.")
        else:
            if lr is None or len(lr)==0:
                raise ValueError("'lr' must be non-empty value, default value is 1")
            
        # Validate mode
        if mode is not None:
            if not isinstance(mode, str):
                raise TypeError("'mode' must be of type string.")
            if not mode.strip():
                raise ValueError("'mode' must be a non-empty string.")
        else:
            if mode is None or len(mode)==0:
                raise ValueError("'mode' must be a non-empty string.")

        # Validate model
        if model is not None:
            if not isinstance(model, str):
                raise TypeError("'model' must be of type string.")
            if not model.strip():
                raise ValueError("'model' must be a non-empty string.")
        else:
            if model is None or len(model)==0:
                raise ValueError("'model' must be a non-empty string.")

        # Validate namespace
        if namespace is not None:
            if not isinstance(namespace, str):
                raise TypeError("'namespace' must be of type string.")
            if not namespace.strip():
                raise ValueError("'namespace' must be a non-empty string")
        else:
            if namespace is None or len(namespace)==0:
                raise ValueError("'namespace' must be a non-empty string, defaul value is 'gpu-scheduler'")

        # Validate ngpu
        if ngpu is not None:
            if not isinstance(ngpu, int):
                raise TypeError("'ngpu' must be of type integer.")
            if ngpu <=0:
                raise ValueError("'ngpu' must be greater than 0 or a positive integer.")
        else:
            if ngpu is None:
                raise ValueError("'ngpu' must be greater than 0 or a positive integer.")

        # Validate priority
        if priority is not None:
            if not isinstance(priority, int):
                raise TypeError("'priority' must be of type int.")
            if priority < 0:
                raise ValueError("'priority' must be >=0 or a positive integer, default value is 0")
        else:
            if priority is None or len(priority)==0:
                raise TypeError("'priority' must be of type int, default value is 0")

        # Validate seed
        if seed is not None:
            if not isinstance(seed, int):
                raise TypeError("'seed' must be of type int.")
            if seed < 0:
                raise ValueError("'seed' must be a non-negative integer.")
        else:
            if seed is None or len(seed)==0:
                raise ValueError("'seed' must be a non-negative integer, default value is 0")

        # Validate task_name
        if task_name is not None:
            if not isinstance(task_name, str):
                raise TypeError("'task_name' must be of type string.")
            if not task_name.strip():
                raise ValueError("'task_name' must be a non-empty string.")
        else:
            if task_name is None or len(task_name)==0:
                raise ValueError("'task_name' must be a non-empty string.")

        # Validate test_dataset (optional)
        if test_dataset is not None and len(test_dataset) != 0:
            if not isinstance(test_dataset, str):
                raise TypeError("'test_dataset' must be of type string if provided.")
            if not test_dataset.strip():
                raise ValueError("'test_dataset' must be a non-empty string if provided.")
        
        # Validate total_checkpoint
        if total_checkpoint is not None:
            if not isinstance(total_checkpoint, int):
                raise TypeError("'total_checkpoint' must be of type int.")
            if not (1 <= total_checkpoint <= 10):
                raise ValueError("'total_checkpoint' must be between 1 and 10.")
        else:
            if total_checkpoint is None:
                raise ValueError("'total_checkpoint' must be between 1 and 10, default value is 1")

        # Validate version
        if version is not None:
            if not isinstance(version, str):
                raise TypeError("'version' must be of type string.")
            if not version.strip():
                raise ValueError("'version' must be a non-empty string.")
        else:
            if version is None:
                raise ValueError("'version' must be a non-empty string.")

    def _validate_retrieve_parameters(self, id: str):
        if id is not None:
            if not isinstance(id, str):
                raise TypeError("'id' must be of type string.")
            if not id.strip():
                raise ValueError("'id' must be a non-empty string.")

    def _validate_cancel_parameters(self, id: str):
        if id is not None:
            if not isinstance(id, str):
                raise TypeError("'id' must be of type string.")
            if not id.strip():
                raise ValueError("'id' must be a non-empty string.")

    def _validate_logs_parameters(self, id: str):
        if id is not None:
            if not isinstance(id, str):
                raise TypeError("'id' must be of type string.")
            if not id.strip():
                raise ValueError("'id' must be a non-empty string.")

    def _validate_list_parameters(self, offset: int, limit: int):
        # Validate limit
        if not isinstance(limit, int) or limit <= 0:
            raise TypeError("'limit' must be a positive integer.")
        # Validate offset
        if not isinstance(offset, int) or offset < 0:
            raise TypeError("'offset' must be a non-negative integer.")


    def __make_post_request(
        self, url: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None, timeout: int = 30
        ) -> Union[Dict[str, Any], bool, None]:
        """
        Makes a POST request to a given URL with a payload and optional headers.

        :param url: str - The URL to send the POST request to.
        :param payload: dict - The data to be sent in the POST request.
        :param headers: dict, optional - Headers to include in the POST request.
        :param timeout: int, optional - Timeout for the request in seconds (default is 10).
        :return: dict - The response from the server in JSON format, or an error message.
        """
        try:
            # Ensure the payload is in JSON format
            if not isinstance(payload, dict):  # type: ignore
                raise ValueError("Payload must be a dictionary.")

            # Make the POST request
            if self._client.api_key:
                auth_headers = self._client.auth_headers
                default_headers = self._client.default_headers
                headers = {**auth_headers, **default_headers}

            k_customer_id = os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID")
            x_user = os.environ.get("KRUTRIM_CLOUD_X_USER")

            if k_customer_id:
                if headers:
                    headers["K-Customer-ID"] = k_customer_id
                else:
                    headers = {"K-Customer-ID": k_customer_id}
            if x_user:
                if headers:
                    headers["x-user"] = x_user
                else:
                    headers = {"x-user": x_user}

            response = requests.post(url, json=payload, headers=headers, timeout=timeout)
            tag_already_exist = False

            try:
                if response.status_code != 200 and "detail" in response.json():
                    if isinstance(response.json()["detail"], str):
                        if "Tag already exists".lower() in response.json()["detail"].lower():
                            tag_already_exist = True
                            return tag_already_exist
                        else:
                            print(f"ERROR DESCRIPTION: {response.json()['detail']}")
                            response.raise_for_status()
                    if isinstance(response.json()["detail"], list):
                        print(f"ERROR DESCRIPTION: {response.json()['detail'][0]['msg']}")
                        response.raise_for_status()

                else:
                    # Raise an exception for HTTP error responses (4xx or 5xx)
                    response.raise_for_status()
            except Exception as exc:
                raise Exception(f"{exc}")

            # Try to parse the response as JSON
            try:
                response_data = response.json()
            except json.JSONDecodeError:
                raise ValueError("Response content is not valid JSON.")

            # Return the parsed JSON response
            return response_data

        except requests.exceptions.Timeout as timeout_exc:
            raise TimeoutError(f"Request to {url} timed out after {timeout} seconds. : {timeout_exc}")
        except requests.exceptions.ConnectionError as conn_error:
            raise ConnectionError(f"Failed to connect to {url}. Please check your network connection.: {conn_error}")
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except ValueError as val_err:
            raise ValueError(f"Value error: {val_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def __create_model_registry_tag(
        self, model_id: str
        ):
        # Call Artifact Registry to update the model information
        payload = {
            "artifactName": model_id,
            "artifactInfo": {
                "task": "finetuning",
                "status": "active",
                "repoType": "private",
            },
            "artifactType": "model",
        }
        create_tag_endpoint_url = f"{self._model_registry_url}/artifact_registry/v1/create_tag"
        # import pdb
        # pdb.set_trace()
        try:
            response = self.__make_post_request(url=create_tag_endpoint_url, payload=payload)
        except Exception as exc:
            raise Exception(f"Exception occurred while registering the model details. : {exc}") from exc


    def create(
        self,
        *,
        batch: int | NotGiven = NOT_GIVEN,
        dataset: str | NotGiven = NOT_GIVEN,
        engine: str | NotGiven = NOT_GIVEN,
        epoch: int | NotGiven = NOT_GIVEN,
        lora_alpha: int | NotGiven = NOT_GIVEN,
        lora_rank: int | NotGiven = NOT_GIVEN,
        lr: int | NotGiven = NOT_GIVEN,
        mode: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        namespace: str | NotGiven = NOT_GIVEN,
        ngpu: int | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        task_name: str | NotGiven = NOT_GIVEN,
        test_dataset: str | NotGiven = NOT_GIVEN,
        total_checkpoint: int | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create finetuning task.

        Args:
          batch: Batch Size.

          dataset: Dataset Name.

          engine: Engine type.

          epoch: Epoch Number.

          lora_alpha: Lora alpha

          lora_rank: Lora rank

          lr: Learn Rate.

          mode: Mode Name.

          model: Model Name.

          namespace: Task Name.

          ngpu: Number of GPU.

          priority: Task priority.

          seed: Random Seed.

          task_name: Task Name.

          test_dataset: Test Dataset Name.

          total_checkpoint: total checkpoint saved

          version: Version String.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_create_parameters(
                    batch=batch,
                    dataset=dataset,
                    engine=engine,
                    epoch=epoch,
                    lora_alpha=lora_alpha,
                    lora_rank=lora_rank,
                    lr=lr,
                    mode=mode,
                    model=model,
                    namespace=namespace,
                    ngpu=ngpu,
                    priority=priority,
                    seed=seed,
                    task_name=task_name,
                    test_dataset=test_dataset,
                    total_checkpoint=total_checkpoint,
                    version=version
                    )

        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}

        self.__create_model_registry_tag(model_id=task_name)
        return self._post(
            "/api/v1/fine_tuning/tasks",
            body=maybe_transform(
                {
                    "batch": batch,
                    "dataset": dataset,
                    "engine": engine,
                    "epoch": epoch,
                    "lora_alpha": lora_alpha,
                    "lora_rank": lora_rank,
                    "lr": lr,
                    "mode": mode,
                    "model": model,
                    "namespace": namespace,
                    "ngpu": ngpu,
                    "priority": priority,
                    "seed": seed,
                    "task_name": task_name,
                    "test_dataset": test_dataset,
                    "total_checkpoint": total_checkpoint,
                    "version": version,

                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

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
        Get fine_tuning task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_retrieve_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        # extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return self._get(
            f"/api/v1/fine_tuning/tasks/{id}",
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
        List fine_tuning tasks

        Args:
          limit: Limit the max number of item to be return.

          offset: Offset index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # Assign default values if not provided
        limit = limit if limit is not NOT_GIVEN else 10
        offset = offset if offset is not NOT_GIVEN else 0

        self._validate_list_parameters(offset=offset, limit=limit)
        # extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return self._get(
            "/api/v1/fine_tuning/tasks",
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
        Cancel fine_tuning task

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
        # extra_headers.update({"K-Customer-ID": k_customer_id})
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return self._get(
            f"/api/v1/fine_tuning/tasks/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def logs(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskLogsResponse:
        """
        Get all logs from the fine_tuning task.

        Args:
          limit: Limit of the log

          offset: Offset Index of the log

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_logs_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        # extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return self._get(
            f"/api/v1/fine_tuning/tasks/{id}/logs",
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
                    task_logs_params.TaskLogsParams,
                ),
            ),
            cast_to=TaskLogsResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def _validate_create_parameters(
        self,
        batch: int,
        dataset: str, 
        engine: str, 
        epoch: int, 
        lora_alpha: int,
        lora_rank: int,
        lr: int,
        mode: str,
        model: str,
        namespace: str,
        ngpu: int,
        priority: int,
        seed: int,
        task_name: str,
        test_dataset: str,
        total_checkpoint: int,
        version: str
         ):

        # Validate batch
        if batch is not None:
            if not isinstance(batch, int):
                raise TypeError("'batch' must be of type int.")
            if batch <= 0:
                raise ValueError("'batch' must be greater than 0, default value is 8")
        else:
            if batch is None:
                raise ValueError("'batch' must be a non-empty value, default value is 8")
 
        # Validate dataset
        if dataset is not None:
            if not isinstance(dataset, str):
                raise TypeError("'dataset' must be of type string.")
            if not dataset.strip():
                raise ValueError("'dataset' must be a non-empty string.")
        else:
            if dataset is None:
                raise ValueError("'dataset' must be a non-empty string.")

        # Validate engine
        if engine is not None:
            if not isinstance(engine, str):
                raise TypeError("'engine' must be of type string.")
            if not engine.strip():
                raise ValueError("'engine' must be a non-empty string.")
        else:
            if engine is None:
                raise ValueError("'engine' must be a non-empty string.")

        # Validate epoch
        if epoch is not None:
            if not isinstance(epoch, int):
                raise TypeError("'epoch' must be of type int.")
            if epoch <= 0:
                raise ValueError("'epoch' must be greater than 0.")
        else:
            if epoch is None:
                raise ValueError("'epoch' must be non-empty value, default value is 1")

        # Validate lora_alpha
        if lora_alpha is not None:
            if not isinstance(lora_alpha, int):
                raise TypeError("'lora_alpha' must be of type int.")
            if not (0 <= lora_alpha <= 128):
                raise ValueError("'lora_alpha' must be between 0 and 128, default value is 0")
        else:
            if lora_alpha is None:
                raise ValueError("'lora_alpha' must be non-empty value, default value is 0")

        # Validate lora_rank
        if lora_rank is not None:
            if not isinstance(lora_rank, int):
                raise TypeError("'lora_rank' must be of type int.")
            if not (0 <= lora_rank <= 64):
                raise ValueError("'lora_rank' must be between 0 and 64, default value is 0")
        else:
            if lora_rank is None:
                raise ValueError("'lora_rank' must be between 0 and 64, default valu is 0")

        # Validate lr
        if lr is not None:
            if lr <= 0:
                raise ValueError("'lr' must be greater than 0.")
            if not isinstance(lr, int):
                raise TypeError("'lr' must be of type int.")
        else:
            if lr is None or len(lr)==0:
                raise ValueError("'lr' must be non-empty value, default value is 1")
            
        # Validate mode
        if mode is not None:
            if not isinstance(mode, str):
                raise TypeError("'mode' must be of type string.")
            if not mode.strip():
                raise ValueError("'mode' must be a non-empty string.")
        else:
            if mode is None or len(mode)==0:
                raise ValueError("'mode' must be a non-empty string.")

        # Validate model
        if model is not None:
            if not isinstance(model, str):
                raise TypeError("'model' must be of type string.")
            if not model.strip():
                raise ValueError("'model' must be a non-empty string.")
        else:
            if model is None or len(model)==0:
                raise ValueError("'model' must be a non-empty string.")

        # Validate namespace
        if namespace is not None:
            if not isinstance(namespace, str):
                raise TypeError("'namespace' must be of type string.")
            if not namespace.strip():
                raise ValueError("'namespace' must be a non-empty string")
        else:
            if namespace is None or len(namespace)==0:
                raise ValueError("'namespace' must be a non-empty string, defaul value is 'gpu-scheduler'")

        # Validate ngpu
        if ngpu is not None:
            if not isinstance(ngpu, int):
                raise TypeError("'ngpu' must be of type integer.")
            if ngpu <=0:
                raise ValueError("'ngpu' must be greater than 0 or a positive integer.")
        else:
            if ngpu is None:
                raise ValueError("'ngpu' must be greater than 0 or a positive integer.")

        # Validate priority
        if priority is not None:
            if not isinstance(priority, int):
                raise TypeError("'priority' must be of type int.")
            if priority < 0:
                raise ValueError("'priority' must be >=0 or a positive integer, default value is 0")
        else:
            if priority is None or len(priority)==0:
                raise TypeError("'priority' must be of type int, default value is 0")

        # Validate seed
        if seed is not None:
            if not isinstance(seed, int):
                raise TypeError("'seed' must be of type int.")
            if seed < 0:
                raise ValueError("'seed' must be a non-negative integer.")
        else:
            if seed is None or len(seed)==0:
                raise ValueError("'seed' must be a non-negative integer, default value is 0")

        # Validate task_name
        if task_name is not None:
            if not isinstance(task_name, str):
                raise TypeError("'task_name' must be of type string.")
            if not task_name.strip():
                raise ValueError("'task_name' must be a non-empty string.")
        else:
            if task_name is None or len(task_name)==0:
                raise ValueError("'task_name' must be a non-empty string.")

        # Validate test_dataset (optional)
        if test_dataset is not None and len(test_dataset) != 0:
            if not isinstance(test_dataset, str):
                raise TypeError("'test_dataset' must be of type string if provided.")
            if not test_dataset.strip():
                raise ValueError("'test_dataset' must be a non-empty string if provided.")
        
        # Validate total_checkpoint
        if total_checkpoint is not None:
            if not isinstance(total_checkpoint, int):
                raise TypeError("'total_checkpoint' must be of type int.")
            if not (1 <= total_checkpoint <= 10):
                raise ValueError("'total_checkpoint' must be between 1 and 10.")
        else:
            if total_checkpoint is None:
                raise ValueError("'total_checkpoint' must be between 1 and 10, default value is 1")

        # Validate version
        if version is not None:
            if not isinstance(version, str):
                raise TypeError("'version' must be of type string.")
            if not version.strip():
                raise ValueError("'version' must be a non-empty string.")
        else:
            if version is None:
                raise ValueError("'version' must be a non-empty string.")

    async def _validate_retrieve_parameters(self, id: str):
        if id is not None:
            if not isinstance(id, str):
                raise TypeError("'id' must be of type string.")
            if not id.strip():
                raise ValueError("'id' must be a non-empty string.")

    async def _validate_cancel_parameters(self, id: str):
        if id is not None:
            if not isinstance(id, str):
                raise TypeError("'id' must be of type string.")
            if not id.strip():
                raise ValueError("'id' must be a non-empty string.")

    async def _validate_logs_parameters(self, id: str):
        if id is not None:
            if not isinstance(id, str):
                raise TypeError("'id' must be of type string.")
            if not id.strip():
                raise ValueError("'id' must be a non-empty string.")
    
    async def _validate_list_parameters(self, offset: int, limit: int):
        # Validate limit
        if not isinstance(limit, int) or limit <= 0:
            raise TypeError("'limit' must be a positive integer.")
        # Validate offset
        if not isinstance(offset, int) or offset < 0:
            raise TypeError("'offset' must be a non-negative integer.")

    async def create(
        self,
        *,
        k_customer_id: str,
        batch: int | NotGiven = NOT_GIVEN,
        dataset: str | NotGiven = NOT_GIVEN,
        engine: str | NotGiven = NOT_GIVEN,
        epoch: int | NotGiven = NOT_GIVEN,
        lora_alpha: int | NotGiven = NOT_GIVEN,
        lora_rank: int | NotGiven = NOT_GIVEN,
        lr: int | NotGiven = NOT_GIVEN,
        mode: str | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        namespace: str | NotGiven = NOT_GIVEN,
        ngpu: int | NotGiven = NOT_GIVEN,
        priority: int | NotGiven = NOT_GIVEN,
        seed: int | NotGiven = NOT_GIVEN,
        task_name: str | NotGiven = NOT_GIVEN,
        test_dataset: str | NotGiven = NOT_GIVEN,
        total_checkpoint: int | NotGiven = NOT_GIVEN,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Create finetuning task.

        Args:
          batch: Batch Size.

          dataset: Dataset Name.

          engine: Engine type.

          epoch: Epoch Number.

          lora_alpha: Lora alpha

          lora_rank: Lora rank

          lr: Learn Rate.

          mode: Mode Name.

          model: Model Name.

          namespace: Task Name.

          ngpu: Number of GPU.

          priority: Task priority.

          seed: Random Seed.

          task_name: Task Name.

          test_dataset: Test Dataset Name.

          total_checkpoint: total checkpoint saved

          version: Version String.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_create_parameters(
                    batch=batch,
                    dataset=dataset,
                    engine=engine,
                    epoch=epoch,
                    lora_alpha=lora_alpha,
                    lora_rank=lora_rank,
                    lr=lr,
                    mode=mode,
                    model=model,
                    namespace=namespace,
                    ngpu=ngpu,
                    priority=priority,
                    seed=seed,
                    task_name=task_name,
                    test_dataset=test_dataset,
                    total_checkpoint=total_checkpoint,
                    version=version
                    )
        extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        return await self._post(
            "/api/v1/fine_tuning/tasks",
            body=await async_maybe_transform(
                {
                    "batch": batch,
                    "dataset": dataset,
                    "engine": engine,
                    "epoch": epoch,
                    "lora_alpha": lora_alpha,
                    "lora_rank": lora_rank,
                    "lr": lr,
                    "mode": mode,
                    "model": model,
                    "namespace": namespace,
                    "ngpu": ngpu,
                    "priority": priority,
                    "seed": seed,
                    "task_name": task_name,
                    "test_dataset": test_dataset,
                    "total_checkpoint": total_checkpoint,
                    "version": version,
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
        Get fine_tuning task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_retrieve_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
            
        # extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            f"/api/v1/fine_tuning/tasks/{id}",
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
        List fine_tuning tasks

        Args:
          limit: Limit the max number of item to be return.

          offset: Offset index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # Assign default values if not provided
        limit = limit if limit is not NOT_GIVEN else 10
        offset = offset if offset is not NOT_GIVEN else 0
        await self._validate_list_parameters(offset=offset, limit=limit)
        # extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            "/api/v1/fine_tuning/tasks",
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
        Cancel fine_tuning task

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_cancel_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # extra_headers.update({"K-Customer-ID": k_customer_id})
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            f"/api/v1/fine_tuning/tasks/{id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def logs(
        self,
        id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskLogsResponse:
        """
        Get all logs from the fine_tuning task.

        Args:
          limit: Limit of the log

          offset: Offset Index of the log

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_logs_parameters(id=id)
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        # extra_headers = {"K-Customer-ID": k_customer_id, **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            f"/api/v1/fine_tuning/tasks/{id}/logs",
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
                    task_logs_params.TaskLogsParams,
                ),
            ),
            cast_to=TaskLogsResponse,
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
        self.logs = to_raw_response_wrapper(
            tasks.logs,
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
        self.logs = async_to_raw_response_wrapper(
            tasks.logs,
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
        self.logs = to_streamed_response_wrapper(
            tasks.logs,
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
        self.logs = async_to_streamed_response_wrapper(
            tasks.logs,
        )
