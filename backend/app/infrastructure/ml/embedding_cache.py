from typing import Any, Dict
from app.domain.interfaces.repository import ISubmissionRepository
from app.domain.interfaces.embedder import IEmbeddingProvider, IEmbeddingCache
from app.core.logger import logger
from app.domain.exceptions import CorpusUnavailableException

class EmbeddingCache(IEmbeddingCache):
    _instance = None
    _embeddings: Dict[str, Dict[str, Any]] = {}
    _loaded: bool = False

    def __new__(cls, repository: ISubmissionRepository, embedder: IEmbeddingProvider):
        if cls._instance is None:
            cls._instance = super(EmbeddingCache, cls).__new__(cls)
            cls._instance.repository = repository
            cls._instance.embedder = embedder
        return cls._instance

    def load_cache(self):
        if self._loaded:
            return
            
        logger.info("Initializing embedding cache for historical submissions...")
        
        try:
            submissions = self.repository.get_all_submissions()
        except Exception as e:
            logger.error(f"Failed to load corpus for embedding cache: {e}")
            raise CorpusUnavailableException(f"Repository corpus could not be loaded: {e}")
            
        total_cached = 0
        for sub in submissions:
            if sub.code:
                if sub.assignment_id not in self._embeddings:
                    self._embeddings[sub.assignment_id] = {}
                emb = self.embedder.get_embedding(sub.code)
                self._embeddings[sub.assignment_id][sub.submission_id] = emb
                total_cached += 1
                    
        self._loaded = True
        logger.info(f"Embedding cache ready. Cached {total_cached} code embeddings.")

    def get_embedding(self, assignment_id: str, submission_id: str, code: str) -> Any:
        # Lazy load if needed
        if not self._loaded:
            self.load_cache()
            
        # Fast path
        if assignment_id in self._embeddings and submission_id in self._embeddings[assignment_id]:
            return self._embeddings[assignment_id][submission_id]
            
        # Fallback if not found in cache (e.g., new submission)
        emb = self.embedder.get_embedding(code)
        
        # Cache it for future
        if assignment_id not in self._embeddings:
            self._embeddings[assignment_id] = {}
        self._embeddings[assignment_id][submission_id] = emb
        return emb
