import numpy as np
from typing import Any
from sentence_transformers import SentenceTransformer
from app.domain.interfaces.embedder import IEmbeddingProvider
from app.core.config import settings
from app.core.logger import logger
from app.domain.exceptions import ModelUnavailableException

class CodeBertEmbeddingProvider(IEmbeddingProvider):
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CodeBertEmbeddingProvider, cls).__new__(cls)
        return cls._instance

    def _get_model(self):
        if self._model is None:
            logger.info(f"Loading {settings.semantic_model_id}...")
            try:
                self._model = SentenceTransformer(settings.semantic_model_id)
            except Exception as e:
                logger.error(f"Failed to load semantic model: {e}")
                raise ModelUnavailableException(f"Semantic model unavailable: {e}")
        return self._model

    def get_embedding(self, code: str) -> Any:
        model = self._get_model()
        return model.encode(str(code))
