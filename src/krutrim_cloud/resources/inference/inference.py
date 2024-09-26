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
from .checkpoints import (
    CheckpointsResource,
    AsyncCheckpointsResource,
    CheckpointsResourceWithRawResponse,
    AsyncCheckpointsResourceWithRawResponse,
    CheckpointsResourceWithStreamingResponse,
    AsyncCheckpointsResourceWithStreamingResponse,
)

__all__ = ["InferenceResource", "AsyncInferenceResource"]


class InferenceResource(SyncAPIResource):
    @cached_property
    def checkpoints(self) -> CheckpointsResource:
        return CheckpointsResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> InferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return InferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return InferenceResourceWithStreamingResponse(self)


class AsyncInferenceResource(AsyncAPIResource):
    @cached_property
    def checkpoints(self) -> AsyncCheckpointsResource:
        return AsyncCheckpointsResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inferencing-python#with_streaming_response
        """
        return AsyncInferenceResourceWithStreamingResponse(self)


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

    @cached_property
    def checkpoints(self) -> CheckpointsResourceWithRawResponse:
        return CheckpointsResourceWithRawResponse(self._inference.checkpoints)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._inference.tasks)


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

    @cached_property
    def checkpoints(self) -> AsyncCheckpointsResourceWithRawResponse:
        return AsyncCheckpointsResourceWithRawResponse(self._inference.checkpoints)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._inference.tasks)


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

    @cached_property
    def checkpoints(self) -> CheckpointsResourceWithStreamingResponse:
        return CheckpointsResourceWithStreamingResponse(self._inference.checkpoints)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._inference.tasks)


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

    @cached_property
    def checkpoints(self) -> AsyncCheckpointsResourceWithStreamingResponse:
        return AsyncCheckpointsResourceWithStreamingResponse(self._inference.checkpoints)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._inference.tasks)
