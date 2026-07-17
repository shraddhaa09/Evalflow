from abc import ABC, abstractmethod
from typing import List, Any
from app.domain.models.plagiarism import Submission

class ICandidateRetriever(ABC):
    @abstractmethod
    def retrieve(self, assignment_id: str, code_embedding: Any, top_k: int) -> List[Submission]:
        """Retrieve the top_k candidate submissions to compare against."""
        pass
