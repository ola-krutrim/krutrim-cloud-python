# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CheckpointRetrieveResponse"]


class CheckpointRetrieveResponse(BaseModel):
    ctime: Optional[str] = None
    """Create time"""

    dataset: Optional[str] = None
    """dataset"""

    epoch: Optional[str] = None
    """Epoch"""

    mode: Optional[str] = None
    """mode"""

    model: Optional[str] = None
    """model"""

    mtime: Optional[str] = None
    """Last modified time"""

    name: Optional[str] = None
    """Check Points name"""

    status: Optional[str] = None
    """Check Points status"""

    steps: Optional[str] = None
    """steps"""

    test_dataset: Optional[str] = None
    """test-dataset"""
