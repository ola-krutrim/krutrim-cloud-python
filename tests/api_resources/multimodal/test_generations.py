# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from demo_project import DemoProject, AsyncDemoProject
from demo_project.types.multimodal import IdeficsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_idefics(self, client: DemoProject) -> None:
        generation = client.multimodal.generations.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
        )
        assert_matches_type(IdeficsResponse, generation, path=["response"])

    @parametrize
    def test_method_idefics_with_all_params(self, client: DemoProject) -> None:
        generation = client.multimodal.generations.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
            images=[["string", "string", "string"], ["string", "string", "string"], ["string", "string", "string"]],
            max_tokens=0,
        )
        assert_matches_type(IdeficsResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_idefics(self, client: DemoProject) -> None:
        response = client.multimodal.generations.with_raw_response.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        generation = response.parse()
        assert_matches_type(IdeficsResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_idefics(self, client: DemoProject) -> None:
        with client.multimodal.generations.with_streaming_response.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            generation = response.parse()
            assert_matches_type(IdeficsResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_idefics(self, async_client: AsyncDemoProject) -> None:
        generation = await async_client.multimodal.generations.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
        )
        assert_matches_type(IdeficsResponse, generation, path=["response"])

    @parametrize
    async def test_method_idefics_with_all_params(self, async_client: AsyncDemoProject) -> None:
        generation = await async_client.multimodal.generations.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
            images=[["string", "string", "string"], ["string", "string", "string"], ["string", "string", "string"]],
            max_tokens=0,
        )
        assert_matches_type(IdeficsResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_idefics(self, async_client: AsyncDemoProject) -> None:
        response = await async_client.multimodal.generations.with_raw_response.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(IdeficsResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_idefics(self, async_client: AsyncDemoProject) -> None:
        async with async_client.multimodal.generations.with_streaming_response.idefics(
            model_name="modelName",
            prompts=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(IdeficsResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True
