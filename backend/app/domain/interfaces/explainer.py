from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

class IExplanationEngine(ABC):
    @abstractmethod
    def explain(self, probability: float, features: Dict[str, float]) -> Tuple[str, List[str]]:
        """
        Translate the model probability and raw feature matrix into 
        a human-readable risk level and explanation signals.
        Returns: (risk_level, [list_of_signals])
        """
        pass
