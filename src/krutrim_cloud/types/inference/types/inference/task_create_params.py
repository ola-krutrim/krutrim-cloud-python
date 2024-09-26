# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    k_customer_id: Required[Annotated[str, PropertyInfo(alias="K-Customer-ID")]]

    argument: str
    """additional argument to parse to inference engine"""

    checkpoint: str
    """Checkpoint name."""

    environ: str
    """environment variable to parse to inference engine"""

    max_batch_size: int
    """max batch size"""

    max_replicas: int
    """Max number of replicas"""

    min_replicas: int
    """Min number of replicas"""

    model: str
    """Model name."""

    namespace: str
    """Task Name."""

    ngpu: int
    """Number of GPU to be used by the inference task."""

    path: str
    """Checkpoint path."""

    priority: int
    """Task priority."""

    s3_access_key: str
    """S3 access key"""

    s3_endpoint: str
    """S3 endpoint"""

    s3_region: str
    """S3 region"""

    s3_secret: str
    """S3 secret"""
