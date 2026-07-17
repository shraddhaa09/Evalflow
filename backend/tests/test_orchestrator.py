import pytest
from typing import List, Dict, Any, Tuple
from app.domain.models.plagiarism import Submission
from app.models.schemas import PlagiarismRequest
from app.domain.services.orchestrator import InferenceOrchestrator
from app.domain.exceptions import CandidateNotFoundException, ModelUnavailableException

class MockRepository:
    def get_by_assignment(self, assignment_id: str):
        return []

class MockEmbedder:
    def get_embedding(self, code: str):
        return [0.1, 0.2, 0.3]

class MockRetriever:
    def retrieve(self, assignment_id: str, emb: Any, top_k: int):
        if assignment_id == "empty":
            return []
        sub = Submission(
            submission_id="sub_test", 
            assignment_id=assignment_id, 
            code="def foo(): pass"
        )
        return [sub]

class MockExtractor:
    def extract(self, code: str, telem: Dict, emb: Any, candidate: Submission, cand_emb: Any):
        return {"semantic_similarity": 0.95}, [0.1, 0.2]

class MockPredictor:
    def predict_proba(self, features: Any) -> float:
        return 0.88

class MockExplainer:
    def explain(self, prob: float, features: Dict):
        return "High Plagiarism Risk", ["High semantic similarity"]

class MockCache:
    def get_embedding(self, assignment_id: str, submission_id: str, code: str):
        return [0.1, 0.2, 0.3]

class MockConfig:
    plagiarism_top_k = 5

def test_orchestrator_insufficient_data():
    orch = InferenceOrchestrator(
        MockRepository(), MockEmbedder(), MockCache(), MockRetriever(),
        MockExtractor(), MockPredictor(), MockExplainer(), MockConfig()
    )
    req = PlagiarismRequest(assignment_id="empty", code="print(1)")
    res = orch.score_code(req)
    assert res.probability == 0.0
    assert res.risk_level == "Insufficient Data"

def test_orchestrator_success():
    orch = InferenceOrchestrator(
        MockRepository(), MockEmbedder(), MockCache(), MockRetriever(),
        MockExtractor(), MockPredictor(), MockExplainer(), MockConfig()
    )
    req = PlagiarismRequest(assignment_id="hw1", code="print(1)")
    res = orch.score_code(req)
    assert res.probability == 0.88
    assert res.risk_level == "High Plagiarism Risk"
    assert res.matched_submission == "sub_test"
    assert "semantic_similarity" in res.feature_contributions
