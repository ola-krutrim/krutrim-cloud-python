# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import boto3
import os
from botocore.exceptions import ClientError, NoCredentialsError  # type: ignore
from .modes import (
    ModesResource,
    AsyncModesResource,
    ModesResourceWithRawResponse,
    AsyncModesResourceWithRawResponse,
    ModesResourceWithStreamingResponse,
    AsyncModesResourceWithStreamingResponse,
)
from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .models import (
    ModelsResource,
    AsyncModelsResource,
    ModelsResourceWithRawResponse,
    AsyncModelsResourceWithRawResponse,
    ModelsResourceWithStreamingResponse,
    AsyncModelsResourceWithStreamingResponse,
)
from .engines import (
    EnginesResource,
    AsyncEnginesResource,
    EnginesResourceWithRawResponse,
    AsyncEnginesResourceWithRawResponse,
    EnginesResourceWithStreamingResponse,
    AsyncEnginesResourceWithStreamingResponse,
)
from .datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .modes.modes import ModesResource, AsyncModesResource
from .models.models import ModelsResource, AsyncModelsResource
from .engines.engines import EnginesResource, AsyncEnginesResource
__all__ = ["FineTuningResource", "AsyncFineTuningResource"]


class FineTuningResource(SyncAPIResource):
    def __init__(self, client: object) -> None:

        self._S3_public_key = os.getenv("KRUTRIM_CLOUD_S3_PUBLIC_KEY")
        self._S3_secret_key = os.getenv("KRUTRIM_CLOUD_S3_SECRET_KEY")
        self._S3_endpoint_url = os.getenv("KRUTRIM_CLOUD_S3_BUCKET_ENDPOINT")
        self._session = None
        self.krutrim_s3_client = None
        self._client = client  # type: ignore
    

    def __create_session(self):
        """
        Initializes a new Krutrim S3 session using the provided Krutrim S3 credentials.

        This method attempts to create a new Krutrim S3 session using the Krutrim S3 access key and secret key stored in the instance variables
        `_S3_public_key` and `_S3_secret_key`. If successful, the session is assigned to the instance variable `_session`.
        If Krutrim S3 credentials are not available or an error occurs during session creation, appropriate exceptions are raised.

        Raises:
            Exception: If Krutrim S3 credentials are not found or an error occurs during session creation.

                - NoCredentialsError: Raised when Krutrim S3 credentials (`KRUTRIM_CLOUD_S3_PUBLIC_KEY` or `KRUTRIM_CLOUD_S3_SECRET_KEY`) are not set in env or invalid.
                - Exception: Raised for any other errors that occur during session creation.

        """
        try:
            self._session = boto3.Session(
                aws_access_key_id=self._S3_public_key,
                aws_secret_access_key=self._S3_secret_key,
            )
        except NoCredentialsError as nce:
            raise Exception(f"No Credentials found in Krutrim S3: {nce}") from nce
        except Exception as exc:
            raise Exception(f"Exception occurred while creating session: {exc}") from exc

    def __init_client(self):
        """
        Initializes the S3 client for interacting with the Krutrim S3 service.

        This method creates an S3 client using the Krutrim S3 session stored in the instance variable `_session`.
        The client is configured to interact with a custom S3-compatible service defined by the endpoint URL stored in `_S3_endpoint_url`.
        The initialized client is assigned to the instance variable `krutrim_s3_client`.
        If Krutrim S3 credentials are not available or an error occurs during client initialization, appropriate exceptions are raised.

        Raises:
            Exception: If there are issues with the provided Krutrim S3 credentials or if an error occurs while initializing the S3 client.

                - NoCredentialsError: Raised when Krutrim S3 credentials (`s3_access_key_id` or `s3_secret_access_key`) are missing or invalid.
                - ClientError: Raised when there is an error response from the S3 service.
                - Exception: Raised for any other errors that occur during client initialization.
        """
        try:
            self.krutrim_s3_client = self._session.client(endpoint_url=self._S3_endpoint_url, service_name="s3")  # type: ignore
        except NoCredentialsError as nce:
            raise Exception(f"No Credentials found in Krutrim S3: {nce}") from nce
        except (ClientError, Exception) as exc:
            raise Exception("Exception occurred while initializing Krutrim S3 client.") from exc


    def __upload_file_to_s3(
        self, local_dir_path: str, bucket_name: str
    ):
        """
        Uploads all files from a local directory to an S3 bucket while maintaining the directory structure.

        Args:
            local_dir_path (str): The local directory path.
            bucket_name (str): The name of the S3 bucket.

        Raises:
            NoCredentialsError: If credentials are not available.
            ClientError: If an error occurs while uploading a file.
        """
        try:
            if self._session is None:
                self.__create_session()

            if self.krutrim_s3_client is None:
                self.__init_client()
            
            model_s3_key = f"{os.path.basename(local_dir_path)}"

            try:
                # Upload the file to S3
                self.krutrim_s3_client.upload_file(local_dir_path, bucket_name, model_s3_key)  # type: ignore
                print(f"Uploaded {local_dir_path} to s3://{bucket_name}/{model_s3_key}")
            except ClientError as e:
                raise ClientError(
                    error_response=f"Failed to upload {local_dir_path} to s3://{bucket_name}/{model_s3_key}: {e}",
                    operation_name="Upload",
                )
            response = {"s3-path": f"s3://{bucket_name}/{model_s3_key}", "filename":model_s3_key}

            return  response

        except NoCredentialsError:
            raise Exception("Credentials not available for Krutrim S3.")
            # raise NoCredentialsError("Credentials not available for Krutrim S3.")
        except Exception as e:
            raise Exception(e)

    def __validate_upload_files_params(
        self,
        local_dir_path: str,
        bucket_name: str,
    ):
        # Validate local_dir_path
        if local_dir_path and not isinstance(local_dir_path, str):
            raise TypeError("'local_dir_path' must be of type string.")

        # Validate bucket_name
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("'bucket_name' must be of type string.")

    def upload_files_to_s3(
        self,
        local_dir_path: str,
        bucket_name: str,
    ):
        self.__validate_upload_files_params(
            local_dir_path=local_dir_path,
            bucket_name=bucket_name
        )
        try:
            # Enable validation of the config file provided by user
            # config_filepath = os.path.join(os.path.abspath(local_dir_path), config_filename)
            # is_config_valid = self.__validate_config_file(config_filepath)

            return self.__upload_file_to_s3(local_dir_path, bucket_name)

        except Exception as exc:
            raise Exception(f"Exception : {exc}")

    @cached_property
    def models(self) -> ModelsResource:
        return ModelsResource(self._client)

    @cached_property
    def modes(self) -> ModesResource:
        return ModesResource(self._client)

    @cached_property
    def engines(self) -> EnginesResource:
        return EnginesResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> FineTuningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return FineTuningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FineTuningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return FineTuningResourceWithStreamingResponse(self)


class AsyncFineTuningResource(AsyncAPIResource):
    @cached_property
    def models(self) -> AsyncModelsResource:
        return AsyncModelsResource(self._client)

    @cached_property
    def modes(self) -> AsyncModesResource:
        return AsyncModesResource(self._client)

    @cached_property
    def engines(self) -> AsyncEnginesResource:
        return AsyncEnginesResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFineTuningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFineTuningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFineTuningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncFineTuningResourceWithStreamingResponse(self)


class FineTuningResourceWithRawResponse:
    def __init__(self, fine_tuning: FineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def models(self) -> ModelsResourceWithRawResponse:
        return ModelsResourceWithRawResponse(self._fine_tuning.models)

    @cached_property
    def modes(self) -> ModesResourceWithRawResponse:
        return ModesResourceWithRawResponse(self._fine_tuning.modes)

    @cached_property
    def engines(self) -> EnginesResourceWithRawResponse:
        return EnginesResourceWithRawResponse(self._fine_tuning.engines)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._fine_tuning.datasets)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._fine_tuning.tasks)


class AsyncFineTuningResourceWithRawResponse:
    def __init__(self, fine_tuning: AsyncFineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def models(self) -> AsyncModelsResourceWithRawResponse:
        return AsyncModelsResourceWithRawResponse(self._fine_tuning.models)

    @cached_property
    def modes(self) -> AsyncModesResourceWithRawResponse:
        return AsyncModesResourceWithRawResponse(self._fine_tuning.modes)

    @cached_property
    def engines(self) -> AsyncEnginesResourceWithRawResponse:
        return AsyncEnginesResourceWithRawResponse(self._fine_tuning.engines)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._fine_tuning.datasets)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._fine_tuning.tasks)


class FineTuningResourceWithStreamingResponse:
    def __init__(self, fine_tuning: FineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def models(self) -> ModelsResourceWithStreamingResponse:
        return ModelsResourceWithStreamingResponse(self._fine_tuning.models)

    @cached_property
    def modes(self) -> ModesResourceWithStreamingResponse:
        return ModesResourceWithStreamingResponse(self._fine_tuning.modes)

    @cached_property
    def engines(self) -> EnginesResourceWithStreamingResponse:
        return EnginesResourceWithStreamingResponse(self._fine_tuning.engines)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._fine_tuning.datasets)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._fine_tuning.tasks)


class AsyncFineTuningResourceWithStreamingResponse:
    def __init__(self, fine_tuning: AsyncFineTuningResource) -> None:
        self._fine_tuning = fine_tuning

    @cached_property
    def models(self) -> AsyncModelsResourceWithStreamingResponse:
        return AsyncModelsResourceWithStreamingResponse(self._fine_tuning.models)

    @cached_property
    def modes(self) -> AsyncModesResourceWithStreamingResponse:
        return AsyncModesResourceWithStreamingResponse(self._fine_tuning.modes)

    @cached_property
    def engines(self) -> AsyncEnginesResourceWithStreamingResponse:
        return AsyncEnginesResourceWithStreamingResponse(self._fine_tuning.engines)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._fine_tuning.datasets)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._fine_tuning.tasks)
