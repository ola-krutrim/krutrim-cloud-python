# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations
import os
from typing import Mapping, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ...types.fine_tuning import dataset_copy_params, dataset_create_params, dataset_retrieve_params
from ...types.fine_tuning.dataset_copy_response import DatasetCopyResponse
from ...types.fine_tuning.dataset_list_response import DatasetListResponse
from ...types.fine_tuning.dataset_retrieve_response import DatasetRetrieveResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def _validate_retrieve_parameters(self, filename: str):
        # Validate engine
        if filename and not isinstance(filename, str):
            raise TypeError("'filename' must be of type string.")

    def _validate_delete_parameters(self, filename: str):
        # Validate engine
        if filename and not isinstance(filename, str):
            raise TypeError("'filename' must be of type string.")

    def _validate_copy_parameters(self, filename: str, path: str, s3_access_key: str, s3_endpoint: str, s3_region: str, s3_secret: str):
        # Validate 'filename'
        if filename is None or not isinstance(filename, str) or not filename.strip() or len(filename)==0:
            raise ValueError("Invalid 'filename': It must be a non-empty string and not None.")
        
        # Validate 'path'
        if path is None or not isinstance(path, str) or not path.strip() or len(path)==0:
            raise ValueError("Invalid 'path': It must be a non-empty string and not None.")

        # Validate 's3_access_key'
        if s3_access_key is None or not isinstance(s3_access_key, str) or not s3_access_key.strip() or len(s3_access_key)==0:
            raise ValueError("Invalid 's3_access_key': It must be a non-empty string and not None.")
        
        # Validate 's3_endpoint'
        if s3_endpoint is None or not isinstance(s3_endpoint, str) or not s3_endpoint.strip() or len(s3_endpoint)==0:
            raise ValueError("Invalid 's3_endpoint': It must be a non-empty string and not None.")
        
        # Validate 's3_region'
        if s3_region is None or not isinstance(s3_region, str) or not s3_region.strip() or len(s3_region)==0:
            raise ValueError("Invalid 's3_region': It must be a non-empty string and not None.")
        
        # Validate 's3_secret'
        if s3_secret is None or not isinstance(s3_secret, str) or not s3_secret.strip() or len(s3_secret)==0:
            raise ValueError("Invalid 's3_secret': It must be a non-empty string and not None.")


    def create(
        self,
        *,
        file: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create datasets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        # extra_headers.update({"K-Customer-ID": k_customer_id})
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return self._post(
            "/api/v1/fine_tuning/datasets",
            body=maybe_transform(body, dataset_create_params.DatasetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
    

    def retrieve(
        self,
        filename: str,
        *,
        line: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveResponse:
        """
        Read the dataset

        Args:
          line: Number of line to read

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_retrieve_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/fine_tuning/datasets/{filename}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"line": line}, dataset_retrieve_params.DatasetRetrieveParams),
            ),
            cast_to=DatasetRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        List all datasets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/v1/fine_tuning/datasets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    def copy(
        self,
        *,
        filename: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
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
    ) -> DatasetCopyResponse:
        """
        Copy dataset from own s3.

        Args:
          filename: Filename for the copied dataset

          path: s3 path

          s3_access_key: s3 access key

          s3_endpoint: s3 endpoint

          s3_region: s3 region

          s3_secret: s3 secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_copy_parameters(filename=filename, path=path, s3_access_key=s3_access_key, s3_endpoint=s3_endpoint, s3_region=s3_region, s3_secret=s3_secret)
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/v1/fine_tuning/datasets/copy",
            body=maybe_transform(
                {
                    "filename": filename,
                    "path": path,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret,
                },
                dataset_copy_params.DatasetCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCopyResponse,
        )


    def delete(
        self,
        filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete the dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        self._validate_delete_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/fine_tuning/datasets/{filename}/del",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/finetuning-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)
    async def _validate_retrieve_parameters(self, filename: str):
        # Validate engine
        if filename and not isinstance(filename, str):
            raise TypeError("'filename' must be of type string.")
            
    async def _validate_delete_parameters(self, filename: str):
        # Validate engine
        if filename and not isinstance(filename, str):
            raise TypeError("'filename' must be of type string.")

    async def _validate_copy_parameters(self, filename: str, path: str, s3_access_key: str, s3_endpoint: str, s3_region: str):
        # Validate 'filename'
        if filename is None or not isinstance(filename, str) or not filename.strip() or len(filename)==0:
            raise ValueError("Invalid 'filename': It must be a non-empty string and not None.")
        
        # Validate 'path'
        if path is None or not isinstance(path, str) or not path.strip() or len(path)==0:
            raise ValueError("Invalid 'path': It must be a non-empty string and not None.")

        # Validate 's3_access_key'
        if s3_access_key is None or not isinstance(s3_access_key, str) or not s3_access_key.strip() or len(s3_access_key)==0:
            raise ValueError("Invalid 's3_access_key': It must be a non-empty string and not None.")
        
        # Validate 's3_endpoint'
        if s3_endpoint is None or not isinstance(s3_endpoint, str) or not s3_endpoint.strip() or len(s3_endpoint)==0:
            raise ValueError("Invalid 's3_endpoint': It must be a non-empty string and not None.")
        
        # Validate 's3_region'
        if s3_region is None or not isinstance(s3_region, str) or not s3_region.strip() or len(s3_region)==0:
            raise ValueError("Invalid 's3_region': It must be a non-empty string and not None.")
        
        # Validate 's3_secret'
        if s3_secret is None or not isinstance(s3_secret, str) or not s3_secret.strip() or len(s3_secret)==0:
            raise ValueError("Invalid 's3_secret': It must be a non-empty string and not None.")
    

    async def create(
        self,
        *,
        # k_customer_id: str,
        file: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create datasets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers["Content-Type"] = "multipart/form-data"
        return await self._post(
            "/api/v1/fine_tuning/datasets",
            body=await async_maybe_transform(body, dataset_create_params.DatasetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
    

    async def retrieve(
        self,
        filename: str,
        *,
        # k_customer_id: str,
        line: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetRetrieveResponse:
        """
        Read the dataset

        Args:
          line: Number of line to read

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_retrieve_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            f"/api/v1/fine_tuning/datasets/{filename}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"line": line}, dataset_retrieve_params.DatasetRetrieveParams),
            ),
            cast_to=DatasetRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatasetListResponse:
        """
        List all datasets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._get(
            "/api/v1/fine_tuning/datasets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetListResponse,
        )

    async def copy(
        self,
        *,
        filename: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
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
    ) -> DatasetCopyResponse:
        """
        Copy dataset from own s3.

        Args:
          filename: Filename for the copied dataset

          path: s3 path

          s3_access_key: s3 access key

          s3_endpoint: s3 endpoint

          s3_region: s3 region

          s3_secret: s3 secret

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_copy_parameters(filename=filename, path=path, s3_access_key=s3_access_key, s3_endpoint=s3_endpoint, s3_region=s3_region, s3_secret=s3_secret)
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        return await self._post(
            "/api/v1/fine_tuning/datasets/copy",
            body=await async_maybe_transform(
                {
                    "filename": filename,
                    "path": path,
                    "s3_access_key": s3_access_key,
                    "s3_endpoint": s3_endpoint,
                    "s3_region": s3_region,
                    "s3_secret": s3_secret,
                },
                dataset_copy_params.DatasetCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DatasetCopyResponse,
        )

    async def delete(
        self,
        filename: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete the dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        await self._validate_delete_parameters(filename=filename)
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        if os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"):
            extra_headers = {"K-Customer-ID": os.environ.get("KRUTRIM_CLOUD_K_CUSTOMER_ID"), **(extra_headers or {})}
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"K-Customer-ID": k_customer_id})
        return await self._get(
            f"/api/v1/fine_tuning/datasets/{filename}/del",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.copy = to_raw_response_wrapper(
            datasets.copy,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.copy = async_to_raw_response_wrapper(
            datasets.copy,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.copy = to_streamed_response_wrapper(
            datasets.copy,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.copy = async_to_streamed_response_wrapper(
            datasets.copy,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )
