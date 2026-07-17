from abc import ABC, abstractmethod
from typing import Any

class IEmbeddingProvider(ABC):
    @abstractmethod
    def get_embedding(self, code: str) -> Any:
        """Computes and returns the dense vector embedding for the given code."""
        pass

class IEmbeddingCache(ABC):
    @abstractmethod
    def load_cache(self) -> None:
        """Precompute and cache all embeddings."""
        pass

    @abstractmethod
    def get_embedding(self, assignment_id: str, submission_id: str, code: str) -> Any:
        """Retrieve embedding from cache or calculate if missing."""
        pass
