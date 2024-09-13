from __future__ import annotations

from ..._resource import SyncAPIResource
from .model_registry import ModelRegistryResource
from ..._compat import cached_property

__all__ = ["RegistryResource"]


class RegistryResource(SyncAPIResource):
    @cached_property
    def model_registry(self) -> ModelRegistryResource:
        return ModelRegistryResource(self._client)
