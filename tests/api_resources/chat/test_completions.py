# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from demo_project import DemoProject, AsyncDemoProject
from demo_project.types.chat import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: DemoProject) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: DemoProject) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            response_format={"type": "type"},
            stop="stop",
            stream=True,
            temperature=0,
            top_logprobs=0,
            top_p=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: DemoProject) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: DemoProject) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncDemoProject) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDemoProject) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
            frequency_penalty=0,
            logit_bias={"foo": 0},
            logprobs=True,
            max_tokens=0,
            n=0,
            presence_penalty=0,
            response_format={"type": "type"},
            stop="stop",
            stream=True,
            temperature=0,
            top_logprobs=0,
            top_p=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDemoProject) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDemoProject) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
                {
                    "role": "role",
                    "content": "content",
                },
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
