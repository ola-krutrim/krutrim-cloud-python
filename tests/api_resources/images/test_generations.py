# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from demo_project import DemoProject, AsyncDemoProject
from demo_project.types.images import StableDiffusionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_diffusion(self, client: DemoProject) -> None:
        generation = client.images.generations.diffusion(
            model_name="diffusion1XL",
        )
        assert_matches_type(StableDiffusionResponse, generation, path=["response"])

    @parametrize
    def test_method_diffusion_with_all_params(self, client: DemoProject) -> None:
        generation = client.images.generations.diffusion(
            model_name="diffusion1XL",
            guidance_scale=0,
            image_height=0,
            image_width=0,
            negative_prompt="string",
            negative_prompt2="string",
            num_inference_steps=0,
            num_output_images=0,
            output_img_type="outputImgType",
            prompt="string",
            prompt2="string",
            seed=42,
        )
        assert_matches_type(StableDiffusionResponse, generation, path=["response"])

    @parametrize
    def test_raw_response_diffusion(self, client: DemoProject) -> None:
        response = client.images.generations.with_raw_response.diffusion(
            model_name="diffusion1XL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        generation = response.parse()
        assert_matches_type(StableDiffusionResponse, generation, path=["response"])

    @parametrize
    def test_streaming_response_diffusion(self, client: DemoProject) -> None:
        with client.images.generations.with_streaming_response.diffusion(
            model_name="diffusion1XL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            generation = response.parse()
            assert_matches_type(StableDiffusionResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_diffusion(self, async_client: AsyncDemoProject) -> None:
        generation = await async_client.images.generations.diffusion(
            model_name="diffusion1XL",
        )
        assert_matches_type(StableDiffusionResponse, generation, path=["response"])

    @parametrize
    async def test_method_diffusion_with_all_params(self, async_client: AsyncDemoProject) -> None:
        generation = await async_client.images.generations.diffusion(
            model_name="diffusion1XL",
            guidance_scale=0,
            image_height=0,
            image_width=0,
            negative_prompt="string",
            negative_prompt2="string",
            num_inference_steps=0,
            num_output_images=0,
            output_img_type="outputImgType",
            prompt="string",
            prompt2="string",
            seed=42,
        )
        assert_matches_type(StableDiffusionResponse, generation, path=["response"])

    @parametrize
    async def test_raw_response_diffusion(self, async_client: AsyncDemoProject) -> None:
        response = await async_client.images.generations.with_raw_response.diffusion(
            model_name="diffusion1XL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(StableDiffusionResponse, generation, path=["response"])

    @parametrize
    async def test_streaming_response_diffusion(self, async_client: AsyncDemoProject) -> None:
        async with async_client.images.generations.with_streaming_response.diffusion(
            model_name="diffusion1XL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Krutrim-Cloud-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(StableDiffusionResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True
