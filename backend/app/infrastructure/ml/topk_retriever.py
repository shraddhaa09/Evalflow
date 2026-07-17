from typing import List, Any
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.domain.interfaces.retriever import ICandidateRetriever
from app.domain.interfaces.repository import ISubmissionRepository
from app.infrastructure.ml.embedding_cache import EmbeddingCache
from app.domain.models.plagiarism import Submission
from app.core.logger import logger

class TopKCandidateRetriever(ICandidateRetriever):
    def __init__(self, repository: ISubmissionRepository, embedding_cache: EmbeddingCache):
        self.repository = repository
        self.embedding_cache = embedding_cache

    def retrieve(self, assignment_id: str, code_embedding: Any, top_k: int) -> List[Submission]:
        all_subs = self.repository.get_by_assignment(assignment_id)
        if not all_subs:
            return []

        scored_subs = []
        for sub in all_subs:
            if sub.code:
                # O(1) fetch from cache instead of O(N) model runs
                sub_emb = self.embedding_cache.get_embedding(assignment_id, sub.submission_id, sub.code)
                sim = cosine_similarity([code_embedding], [sub_emb])[0][0]
                scored_subs.append((sim, sub))
                
        # Sort by similarity descending
        scored_subs.sort(key=lambda x: x[0], reverse=True)
        return [sub for sim, sub in scored_subs[:top_k]]
