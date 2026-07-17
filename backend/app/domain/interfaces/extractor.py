from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple
from app.domain.models.plagiarism import Submission

class IFeatureExtractor(ABC):
    @abstractmethod
    def extract(
        self,
        current_code: str,
        current_telem: Dict[str, float],
        current_emb: Any,
        candidate: Submission,
        candidate_emb: Any
    ) -> Tuple[Dict[str, float], Any]:
        """
        Compare the incoming submission data against a retrieved candidate 
        to produce the pairwise features required by the Predictor.
        Returns (feature_dict, feature_vector).
        """
        pass
