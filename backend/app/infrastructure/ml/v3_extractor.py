import re
import numpy as np
from typing import Dict, Any, Tuple
from sklearn.metrics.pairwise import cosine_similarity
from app.domain.interfaces.extractor import IFeatureExtractor
from app.domain.models.plagiarism import Submission

def tokenize(code):
    return re.findall(r'\b\w+\b', str(code).lower())

def jaccard(a, b):
    A, B = set(tokenize(a)), set(tokenize(b))
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)

def line_sim(a, b):
    A = set([l.strip() for l in str(a).splitlines() if l.strip()])
    B = set([l.strip() for l in str(b).splitlines() if l.strip()])
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)

def length_sim(a, b):
    len_a, len_b = len(str(a)), len(str(b))
    return min(len_a, len_b) / max(len_a, len_b) if max(len_a, len_b) > 0 else 1.0

def structure_features(code):
    c = str(code)
    return {
        "for": len(re.findall(r'\bfor\b', c)),
        "while": len(re.findall(r'\bwhile\b', c)),
        "if": len(re.findall(r'\bif\b', c)),
        "def": len(re.findall(r'\bdef\b', c)),
    }

def structure_sim(a, b):
    A, B = structure_features(a), structure_features(b)
    score, total = 0, 0
    for k in A:
        score += max(0, min(A[k], B[k]))
        total += max(A[k], B[k]) + 1e-5
    return score / total

class V3FeatureExtractor(IFeatureExtractor):
    def extract(
        self,
        current_code: str,
        current_telem: Dict[str, float],
        current_emb: Any,
        candidate: Submission,
        candidate_emb: Any
    ) -> Tuple[Dict[str, float], Any]:
        
        semantic_sim = cosine_similarity([current_emb], [candidate_emb])[0][0]
        code_b = candidate.code or ""
        
        features = {
            "token_similarity": jaccard(current_code, code_b),
            "line_similarity": line_sim(current_code, code_b),
            "length_similarity": length_sim(current_code, code_b),
            "structure_similarity": structure_sim(current_code, code_b),
            "semantic_similarity": float(semantic_sim),
            "typing_speed_gap": abs(current_telem.get("typing_speed_wpm", 0) - candidate.typing_speed_wpm),
            "idle_ratio_gap": abs(current_telem.get("idle_ratio", 0) - candidate.idle_ratio),
            "paste_ratio_gap": abs(current_telem.get("paste_ratio", 0) - candidate.paste_ratio),
            "tab_switch_gap": abs(current_telem.get("tab_switches", 0) - candidate.tab_switches),
            "suspicion_gap": abs(current_telem.get("suspicion_score", 0) - candidate.suspicion_score)
        }
        
        vector = np.array([[
            features["token_similarity"],
            features["line_similarity"],
            features["length_similarity"],
            features["structure_similarity"],
            features["semantic_similarity"],
            features["typing_speed_gap"],
            features["idle_ratio_gap"],
            features["paste_ratio_gap"],
            features["tab_switch_gap"],
            features["suspicion_gap"]
        ]])
        
        return features, vector
