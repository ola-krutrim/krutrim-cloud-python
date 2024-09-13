# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource


__all__ = ["DeployResource", "AsyncDeployResource"]


class DeployResource(SyncAPIResource):
    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> DeployResourceWithRawResponse:
        return DeployResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeployResourceWithStreamingResponse:
        return DeployResourceWithStreamingResponse(self)


class AsyncDeployResource(AsyncAPIResource):
    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeployResourceWithRawResponse:
        return AsyncDeployResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeployResourceWithStreamingResponse:
        return AsyncDeployResourceWithStreamingResponse(self)


class DeployResourceWithRawResponse:
    def __init__(self, inference: DeployResource) -> None:
        self._inference = inference

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._inference.tasks)


class AsyncDeployResourceWithRawResponse:
    def __init__(self, inference: AsyncDeployResource) -> None:
        self._inference = inference

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._inference.tasks)


class DeployResourceWithStreamingResponse:
    def __init__(self, inference: DeployResource) -> None:
        self._inference = inference

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._inference.tasks)


class AsyncDeployResourceWithStreamingResponse:
    def __init__(self, inference: AsyncDeployResource) -> None:
        self._inference = inference

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._inference.tasks)
