from abc import ABC, abstractmethod
from typing import Any

class IPredictor(ABC):
    @abstractmethod
    def predict_proba(self, features: Any) -> float:
        """Predict the probability of plagiarism given a feature vector."""
        pass
