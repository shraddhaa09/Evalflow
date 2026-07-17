from abc import ABC, abstractmethod
from typing import List, Dict
from app.domain.models.plagiarism import Submission

class ISubmissionRepository(ABC):
    @abstractmethod
    def get_by_assignment(self, assignment_id: str) -> List[Submission]:
        """Fetch all submissions for a given assignment."""
        pass

    @abstractmethod
    def get_all_submissions(self) -> List[Submission]:
        """Fetch all submissions across all assignments."""
        pass
