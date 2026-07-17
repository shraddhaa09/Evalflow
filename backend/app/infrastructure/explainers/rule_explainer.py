from typing import Dict, List, Tuple
from app.domain.interfaces.explainer import IExplanationEngine
from app.core.config import settings

class RuleBasedExplainer(IExplanationEngine):
    def explain(self, probability: float, features: Dict[str, float]) -> Tuple[str, List[str]]:
        if probability >= settings.plagiarism_high_risk_threshold:
            risk_level = "High Plagiarism Risk"
        elif probability >= settings.plagiarism_medium_risk_threshold:
            risk_level = "Medium Plagiarism Risk"
        else:
            risk_level = "Clean/Low Risk"
            
        signals = []
        if features:
            if features.get("semantic_similarity", 0) > 0.9:
                signals.append("Very high semantic similarity")
            if features.get("token_similarity", 0) > 0.7:
                signals.append("High token overlap")
            if features.get("structure_similarity", 0) > 0.9:
                signals.append("Nearly identical code structure")
            if features.get("paste_ratio_gap", 0) > 0.5:
                signals.append("Suspicious paste behavior gap")
                
        if not signals:
            signals.append("No strong plagiarism indicators")
            
        return risk_level, signals
