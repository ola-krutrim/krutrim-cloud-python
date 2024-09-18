from ..._resource import SyncAPIResource
import os
import boto3  # type: ignore
from botocore.exceptions import ClientError, NoCredentialsError  # type: ignore
from typing import List, Union, Dict, Any, Optional
import requests
import json
from httpx import URL
import re

__all__ = ["ModelRegistryResource"]


class JSONValidationError(Exception):
    """Custom exception for JSON validation errors."""

    pass


class ModelRegistryResource(SyncAPIResource):

    def __init__(self, client: object) -> None:

        self._S3_public_key = os.environ.get("KRUTRIM_CLOUD_S3_PUBLIC_KEY")
        self._S3_secret_key = os.environ.get("KRUTRIM_CLOUD_S3_SECRET_KEY")
        self._S3_endpoint_url = os.environ.get("KRUTRIM_CLOUD_S3_BUCKET_ENDPOINT")
        self._session = None
        self.krutrim_s3_client = None
        self.__create_session()
        self.__init_client()
        self._client = client  # type: ignore

        # Configure the model registry server URL
        self._model_registry_url: Union[str, URL] = ""
        if os.environ.get("KRUTRIM_CLOUD_MODEL_REGISTRY_URL"):
            self._model_registry_url = str(os.environ.get("KRUTRIM_CLOUD_MODEL_REGISTRY_URL"))
        else:
            self._model_registry_url = self._client.base_url

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

    def __make_get_request(
        self, url: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None, timeout: int = 30
    ) -> Union[Dict[str, Any], bool, None]:
        """
        Makes a GET request to a given URL with a payload and optional headers.

        :param url: str - The URL to send the GET request to.
        :param payload: dict - The data to be sent in the GET request.
        :param headers: dict, optional - Headers to include in the GET request.
        :param timeout: int, optional - Timeout for the request in seconds (default is 10).
        :return: dict - The response from the server in JSON format, or an error message.
        """
        try:
            # Ensure the payload is in JSON format
            if not isinstance(payload, dict):  # type: ignore
                raise ValueError("Payload must be a dictionary.")

            # Make the GET request
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

            response = requests.get(url, params=payload, headers=headers, timeout=timeout)
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

    def __upload_directory_to_s3(
        self, local_dir_path: str, bucket_name: str, model_id: str, base_model: str, version: str
    ):
        """
        Uploads all files from a local directory to an S3 bucket while maintaining the directory structure.

        Args:
            local_dir_path (str): The local directory path.
            bucket_name (str): The name of the S3 bucket.
            model_id (str): Model id of the model
            base_model (str): Base model string
            version (str): Version of the model

        Raises:
            NoCredentialsError: If credentials are not available.
            ClientError: If an error occurs while uploading a file.
        """
        s3_dir_path = f"{model_id}/{version}"
        try:
            # Traverse the local directory
            abs_path = os.path.abspath(local_dir_path)
            for root, dirs, files in os.walk(abs_path):
                relative_dirpath = os.path.relpath(root, abs_path)
                for file_name in files:
                    local_file_path = os.path.join(root, file_name)
                    if relative_dirpath == ".":
                        file_path = file_name
                    else:
                        file_path = os.path.join(relative_dirpath, file_name)

                    model_s3_key = f"{model_id}/{version}/{file_path}"

                    try:
                        # Upload the file to S3
                        self.krutrim_s3_client.upload_file(local_file_path, bucket_name, model_s3_key)  # type: ignore
                        print(f"Uploaded {local_file_path} to s3://{bucket_name}/{model_s3_key}")
                    except ClientError as e:
                        raise ClientError(
                            error_response=f"Failed to upload {local_file_path} to s3://{bucket_name}/{model_s3_key}: {e}",
                            operation_name="Upload",
                        )

            return s3_dir_path

        except NoCredentialsError:
            raise Exception("Credentials not available for Krutrim S3.")
            # raise NoCredentialsError("Credentials not available for Krutrim S3.")
        except Exception as e:
            raise Exception(f"An error occurred while uploading the model files to S3: {e}")

    def __create_model_registry_tag(
        self, bucket_name: str, model_id: str, version: str, base_model: Optional[str] = ""
    ):
        # Call Artifact Registry to update the model information
        s3_dir_path = f"{model_id}/{version}"
        model_version_s3_path = f"s3://{bucket_name}/{s3_dir_path}"
        payload = {
            "artifactName": model_id,
            "artifactInfo": {
                "task": "byom",
                "status": "active",
                "modelRegistryVersionInfo": {
                    version: {
                        "bucketName": bucket_name,
                        "modelId": model_id,
                        "bucketDirPath": model_version_s3_path,
                        "region": "",
                        "basemodel": base_model,
                    }
                },
                "repoType": "private",
            },
            "artifactType": "model",
        }
        create_tag_endpoint_url = f"{self._model_registry_url}/artifact_registry/v1/create_tag"
        try:
            response = self.__make_post_request(url=create_tag_endpoint_url, payload=payload)
            if type(response) == bool and response == True:
                add_update_tag_version_endpoint_url = (
                    f"{self._model_registry_url}/artifact_registry/v1/add_update_model_registry_version"
                )
                payload = {
                    "artifactName": model_id,
                    "version": version,
                    "versionInfo": {
                        "bucketName": bucket_name,
                        "modelId": model_id,
                        "bucketDirPath": model_version_s3_path,
                        "region": "",
                        "basemodel": base_model,
                    },
                    "artifactType": "model",
                }
                response = self.__make_post_request(url=add_update_tag_version_endpoint_url, payload=payload)
        except Exception as exc:
            raise Exception(f"Exception occurred while registering the model details. : {exc}") from exc

    def __update_model_registry_tag(
        self,
        model_name: str,
        model_id: str,
        deploy_id: str,
        base_model: Optional[str] = "",
    ):
        # Call Artifact Registry to update the model version information
        payload = {
            "artifactName": model_name,
            "artifactInfo": {
                "task": "finetuning",
                "status": "active",
                "parentTags": ["text-generation"],
                "repoType": "private",
                "version": {
                    model_id: {
                        "endpointInfo": f"{self._client.base_url}/v1/chat/completions",
                        "uuid": deploy_id,
                        "modelParameterName": f"{model_id}:{deploy_id}",
                        "basemodel": base_model,
                    }
                },
            },
            "artifactType": "model",
        }
        create_tag_endpoint_url = f"{self._model_registry_url}/artifact_registry/v1/create_tag"
        try:
            self.__make_post_request(url=create_tag_endpoint_url, payload=payload)
        except Exception as exc:
            raise Exception(f"Exception occurred while registering the model details. : {exc}") from exc

    def __list_files_in_s3_bucket(self, bucket_name: str, s3_dir_path: Optional[str] = None) -> List[str]:
        """
        Lists all files in an S3 bucket.

        Args:
            bucket_name (str): The name of the S3 bucket.
            s3_dir_path: A S3 bucket files path within bucket.

        Returns:
            list: A list of file keys (paths) in the specified S3 bucket.
        """
        try:
            # List to hold all file keys
            file_keys: List[str] = []

            # Initialize the paginator to handle large result sets
            paginator = self.krutrim_s3_client.get_paginator("list_objects_v2")  # type: ignore
            if s3_dir_path:
                response_iterator = paginator.paginate(Bucket=bucket_name, Prefix=s3_dir_path)  # type: ignore
            else:
                response_iterator = paginator.paginate(Bucket=bucket_name)  # type: ignore

            # Iterate over each page of results
            for page in response_iterator:  # type: ignore
                # Check if the page contains any files
                if "Contents" in page:
                    for page_obj in page["Contents"]:  # type: ignore
                        file_keys.append(page_obj["Key"])  # type: ignore

            return file_keys

        except NoCredentialsError as nce:
            raise Exception("Credentials not available for Krutrim S3.") from nce
        except ClientError as client_exc:
            raise Exception(f"Failed to list files in s3://{bucket_name}: {client_exc}")
        except Exception as exc:
            raise Exception(f"An error occurred: {exc}")

    def __list_model_versions(self, bucket_name: str, model_id: str) -> List[str]:
        """
        Lists all available versions for a given model_id in the specified S3 bucket.

        Args:
            bucket_name (str): The name of the S3 bucket.
            model_id (str): The model_id to list versions for.

        Returns:
            List[str]: A list of version strings for the given model_id.

        Raises:
            Exception: If AWS credentials are not found or an error occurs while listing versions.

                - NoCredentialsError: Raised when AWS credentials (`aws_access_key_id` or `aws_secret_access_key`) are missing or invalid.
                - ClientError: Raised when there is an error response from the S3 service.
                - Exception: Raised for any other errors that occur during the process.

        """
        try:
            versions = set()  # type: ignore # Use a set to avoid duplicate versions

            # Prefix for the model_id to list versions
            prefix = f"{model_id}/"

            # Initialize the paginator to handle large result sets
            paginator = self.krutrim_s3_client.get_paginator("list_objects_v2")  # type: ignore
            response_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix, Delimiter="/")  # type: ignore

            for page in response_iterator:  # type: ignore
                # Check if the page contains any common prefixes (subdirectories)
                if "CommonPrefixes" in page:
                    for common_prefix in page["CommonPrefixes"]:  # type: ignore
                        version = common_prefix["Prefix"].split("/")[1]  # type: ignore
                        versions.add(version)  # type: ignore

            return list(versions)  # type: ignore

        except NoCredentialsError as nce:
            raise Exception(f"No credentials found for S3: {nce}") from nce
        except ClientError as cle:
            raise Exception(f"Failed to list model versions in s3://{bucket_name}/{model_id}: {cle}") from cle
        except Exception as exc:
            raise Exception(f"An error occurred while listing model versions: {exc}") from exc

    def __download_files_from_s3(self, bucket_name: str, s3_dir_path: str, download_dir_path: str):
        """
        Downloads all files from a specified S3 bucket's directory path (prefix) to a local directory.

        Args:
            bucket_name (str): The name of the S3 bucket.
            s3_dir_path (str): The prefix (path) in the S3 bucket to download files from.
            download_dir_path (str): The local directory to download files to.

        Raises:
            NoCredentialsError: If credentials are not available.
            ClientError: If an error occurs while downloading a file.
        """
        try:
            # Ensure local directory exists
            if not os.path.exists(download_dir_path):
                os.makedirs(download_dir_path, exist_ok=True)

            # Initialize the paginator to handle large result sets
            paginator = self.krutrim_s3_client.get_paginator("list_objects_v2")  # type: ignore
            response_iterator = paginator.paginate(Bucket=bucket_name, Prefix=s3_dir_path)  # type: ignore

            # Iterate over each page of results
            for page in response_iterator:  # type: ignore
                # Check if the page contains any files
                if "Contents" in page:
                    for page_obj in page["Contents"]:  # type: ignore
                        s3_key = page_obj["Key"]  # type: ignore
                        # Construct the local path to save the file
                        relative_path = os.path.relpath(s3_key, s3_dir_path)  # type: ignore
                        local_path = os.path.join(download_dir_path, s3_dir_path, relative_path)

                        # Create any necessary directories locally
                        local_dir = os.path.dirname(local_path)
                        if not os.path.exists(local_dir):
                            os.makedirs(local_dir, exist_ok=True)

                        try:
                            # Download the file from S3
                            self.krutrim_s3_client.download_file(bucket_name, s3_key, local_path)  # type: ignore
                            print(f"Downloaded {s3_key} to {local_path}")
                        except ClientError as e:
                            raise ClientError(
                                error_response=f"Failed to download {s3_key} from s3://{bucket_name}: {e}",
                                operation_name="Download",
                            )

        except NoCredentialsError:
            raise Exception("Credentials not available for Krutrim S3.")
        except Exception as e:
            raise Exception(f"An error occurred while downloading files : {e}")

    def __validate_json_architectures(self, json_data: Dict[str, Any], allowed_values: List[str] = []) -> bool:
        """
        Validates that the 'architectures' key in the JSON data contains only allowed values.

        :param json_data: The JSON data to validate (as a dictionary).
        :param allowed_values: A list of allowed values for the 'architectures' key.
        :return: True if the 'architectures' key contains only allowed values, False otherwise.
        :raises JSONValidationError: If the JSON data does not meet the validation criteria.
        """
        # Check if 'architectures' key exists and is a list
        if "architectures" not in json_data:
            raise JSONValidationError("Error: 'architectures' key not found in JSON data.")

        if not isinstance(json_data["architectures"], list):
            raise JSONValidationError("Error: 'architectures' must be a list.")

        # Validate each value in the 'architectures' list
        for arch_value in json_data["architectures"]:  # type: ignore
            if arch_value not in allowed_values:
                raise JSONValidationError(
                    f"Invalid architecture value found: '{arch_value}'. Allowed values are: {allowed_values}."
                )

        return True

    def __load_json_file(self, file_path: str) -> Dict[str, Any]:
        """
        Loads JSON data from a file.

        :param file_path: The path to the JSON file.
        :return: The loaded JSON data as a dictionary.
        :raises FileNotFoundError: If the file is not found.
        :raises json.JSONDecodeError: If the file is not a valid JSON format.
        :raises Exception: For any other unexpected exceptions.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File not found - {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Error: File is not a valid JSON - {file_path}")
        except Exception as exc:
            raise Exception(f"An unexpected error occurred while loading the JSON file: {exc}")

    def __validate_config_file(self, json_config_file_path: str) -> bool:
        try:
            config_json_data = self.__load_json_file(json_config_file_path)

            return self.__validate_json_architectures(config_json_data)
        except Exception as exc:
            raise Exception(f"Error in validation: {exc}")

    def __validate_upload_files_params(
        self,
        local_dir_path: str,
        bucket_name: str,
        model_id: str,
        base_model: Optional[str],
        version: str,
    ):
        # Validate local_dir_path
        if local_dir_path and not isinstance(local_dir_path, str):
            raise TypeError("'local_dir_path' must be of type string.")

        # Validate bucket_name
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("'bucket_name' must be of type string.")

        # Validate model_id
        if model_id and not isinstance(model_id, str):
            raise TypeError("'model_id' must be of type string.")
        if model_id:
            # Check if the string has min 3 and max 96 characters and only contains alphanumeric characters or '_', '-' and '.'
            if len(model_id) < 3 or len(model_id) > 96:
                raise ValueError("model_id must contain a minimum of 3 characters and a maximum of 96 characters")
            if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9_.-]*[a-zA-Z0-9])?$", model_id):
                ValueError("Invalid value. Only letters, numbers, '_', '-', and '.' are allowed")

        # Validate version
        if version and not isinstance(version, str):
            raise TypeError("'version' must be of type string.")

        # Validate base_model
        if base_model and not isinstance(base_model, str):
            raise TypeError("'base_model' must be of type string.")

    def upload_files_to_s3(
        self,
        local_dir_path: str,
        bucket_name: str,
        model_id: str,
        version: str,
        base_model: Optional[str] = "",
    ):
        self.__validate_upload_files_params(
            local_dir_path=local_dir_path,
            bucket_name=bucket_name,
            model_id=model_id,
            base_model=base_model,
            version=version,
        )
        try:
            # Enable validation of the config file provided by user
            # config_filepath = os.path.join(os.path.abspath(local_dir_path), config_filename)
            # is_config_valid = self.__validate_config_file(config_filepath)

            self.__upload_directory_to_s3(local_dir_path, bucket_name, model_id, base_model, version)
            self.__create_model_registry_tag(bucket_name, model_id, version, base_model)

        except Exception as exc:
            raise Exception(f"Exception : {exc}")

    def __validate_download_files_params(
        self,
        bucket_name: str,
        model_id: str,
        version: str,
        download_dir_path: str,
    ):
        # Validate download_dir_path
        if download_dir_path and not isinstance(download_dir_path, str):
            raise TypeError("'download_dir_path' must be of type string.")

        # Validate bucket_name
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("'bucket_name' must be of type string.")

        # Validate model_id
        if model_id and not isinstance(model_id, str):
            raise TypeError("'model_id' must be of type string.")
        if model_id:
            # Check if the string has min 3 and max 96 characters and only contains alphanumeric characters or '_', '-' and '.'
            if len(model_id) < 3 or len(model_id) > 96:
                raise ValueError("model_id must contain a minimum of 3 characters and a maximum of 96 characters")
            if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9_.-]*[a-zA-Z0-9])?$", model_id):
                ValueError("Invalid value. Only letters, numbers, '_', '-', and '.' are allowed")

        # Validate version
        if version and not isinstance(version, str):
            raise TypeError("'version' must be of type string.")

    def download_files(self, bucket_name: str, model_id: str, version: str, download_dir_path: str):
        self.__validate_download_files_params(
            bucket_name=bucket_name, model_id=model_id, version=version, download_dir_path=download_dir_path
        )
        try:

            self.__download_files_from_s3(
                bucket_name, s3_dir_path=f"{model_id}/{version}", download_dir_path=download_dir_path
            )
        except Exception as exc:
            raise Exception(f"Error in downloading files: {exc}")

    def __validate_list_files_params(self, bucket_name: str, model_id: str, version: str):
        # Validate bucket_name
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("'bucket_name' must be of type string.")

        # Validate model_id
        if model_id and not isinstance(model_id, str):
            raise TypeError("'model_id' must be of type string.")
        if model_id:
            # Check if the string has min 3 and max 96 characters and only contains alphanumeric characters or '_', '-' and '.'
            if len(model_id) < 3 or len(model_id) > 96:
                raise ValueError("model_id must contain a minimum of 3 characters and a maximum of 96 characters")
            if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9_.-]*[a-zA-Z0-9])?$", model_id):
                ValueError("Invalid value. Only letters, numbers, '_', '-', and '.' are allowed")
        # Validate version
        if version and not isinstance(version, str):
            raise TypeError("'version' must be of type string.")

    def list_model_files(self, bucket_name: str, model_id: str, version: str) -> List[str]:
        self.__validate_list_files_params(bucket_name=bucket_name, model_id=model_id, version=version)
        s3_dir_path = f"{model_id}/{version}"

        return self.__list_files_in_s3_bucket(bucket_name=bucket_name, s3_dir_path=s3_dir_path)

    def __validate_list_model_version_params(self, bucket_name: str, model_id: str):
        # Validate bucket_name
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("'bucket_name' must be of type string.")

        # Validate model_id
        if model_id and not isinstance(model_id, str):
            raise TypeError("'model_id' must be of type string.")
        if model_id:
            # Check if the string has min 3 and max 96 characters and only contains alphanumeric characters or '_', '-' and '.'
            if len(model_id) < 3 or len(model_id) > 96:
                raise ValueError("model_id must contain a minimum of 3 characters and a maximum of 96 characters")
            if not re.match(r"^[a-zA-Z0-9]([a-zA-Z0-9_.-]*[a-zA-Z0-9])?$", model_id):
                ValueError("Invalid value. Only letters, numbers, '_', '-', and '.' are allowed")

    def __fetch_model_id_from_registry(self, model_name: str) -> str:
        # Call Artifact Registry to fetch the model id

        payload = {
            "artifactName": model_name,
            "artifactType": "model",
        }
        get_model_card_endpoint_url = f"{self._model_registry_url}/artifact_registry/v1/get_model_card"
        try:
            response = self.__make_get_request(url=get_model_card_endpoint_url, payload=payload)
            return response["modelID"]

        except Exception as exc:
            raise Exception(f"Exception occurred while fetching the model ID. : {exc}") from exc

    def __fetch_model_name_from_registry(self, model_id: str) -> str:
        # Call Artifact Registry to fetch the model name

        payload = {
            "modelID": model_id,
        }
        get_model_name_endpoint_url = f"{self._model_registry_url}/artifact_registry/v1/get_model_name"
        try:
            response = self.__make_get_request(url=get_model_name_endpoint_url, payload=payload)
            return response["artifactName"]

        except Exception as exc:
            raise Exception(f"Exception occurred while fetching the model ID. : {exc}") from exc

    def fetch_model_id(self, model_name: str):
        return self.__fetch_model_id_from_registry(model_name)

    def fetch_model_name(self, model_id: str):
        return self.__fetch_model_name_from_registry(model_id)

    def add_model_deployment_version(self, model_name: str, model_id: str, deploy_id: str, base_model: str):
        self.__update_model_registry_tag(
            model_name=model_name, model_id=model_id, deploy_id=deploy_id, base_model=base_model
        )

    def list_model_version(self, bucket_name: str, model_id: str) -> List[str]:
        self.__validate_list_model_version_params(bucket_name=bucket_name, model_id=model_id)
        return self.__list_model_versions(bucket_name, model_id)
