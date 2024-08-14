# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from demo_project import DemoProject, AsyncDemoProject
from demo_project.types.shared import WhisperResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DemoProject) -> None:
        transcription = client.audio.transcriptions.create()
        assert_matches_type(WhisperResponse, transcription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DemoProject) -> None:
        transcription = client.audio.transcriptions.create(
            chunk_type="chunkType",
            file="file",
            language="language",
            model_name="modelName",
            response_format="responseFormat",
            task="task",
            temperature=0,
        )
        assert_matches_type(WhisperResponse, transcription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DemoProject) -> None:
        response = client.audio.transcriptions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        transcription = response.parse()
        assert_matches_type(WhisperResponse, transcription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DemoProject) -> None:
        with client.audio.transcriptions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            transcription = response.parse()
            assert_matches_type(WhisperResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDemoProject) -> None:
        transcription = await async_client.audio.transcriptions.create()
        assert_matches_type(WhisperResponse, transcription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDemoProject) -> None:
        transcription = await async_client.audio.transcriptions.create(
            chunk_type="chunkType",
            file="file",
            language="language",
            model_name="modelName",
            response_format="responseFormat",
            task="task",
            temperature=0,
        )
        assert_matches_type(WhisperResponse, transcription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDemoProject) -> None:
        response = await async_client.audio.transcriptions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        transcription = await response.parse()
        assert_matches_type(WhisperResponse, transcription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDemoProject) -> None:
        async with async_client.audio.transcriptions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            transcription = await response.parse()
            assert_matches_type(WhisperResponse, transcription, path=["response"])

        assert cast(Any, response.is_closed) is True
