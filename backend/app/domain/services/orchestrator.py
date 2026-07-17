from typing import Optional
from app.domain.interfaces.repository import ISubmissionRepository
from app.domain.interfaces.embedder import IEmbeddingProvider, IEmbeddingCache
from app.domain.interfaces.retriever import ICandidateRetriever
from app.domain.interfaces.extractor import IFeatureExtractor
from app.domain.interfaces.predictor import IPredictor
from app.domain.interfaces.explainer import IExplanationEngine
from app.core.config import Settings
from app.models.schemas import PlagiarismRequest, PlagiarismResponse

class InferenceOrchestrator:
    def __init__(
        self,
        repository: ISubmissionRepository,
        embedder: IEmbeddingProvider,
        embedding_cache: IEmbeddingCache,
        retriever: ICandidateRetriever,
        extractor: IFeatureExtractor,
        predictor: IPredictor,
        explainer: IExplanationEngine,
        config: Settings
    ):
        self.repository = repository
        self.embedder = embedder
        self.embedding_cache = embedding_cache
        self.retriever = retriever
        self.extractor = extractor
        self.predictor = predictor
        self.explainer = explainer
        self.config = config

    def score_code(self, request: PlagiarismRequest) -> PlagiarismResponse:
        # Step 1: Compute embedding for the incoming request
        current_emb = self.embedder.get_embedding(request.code)
        
        # Step 2: Retrieve top K candidate submissions
        candidates = self.retriever.retrieve(request.assignment_id, current_emb, self.config.plagiarism_top_k)
        
        if not candidates:
            return PlagiarismResponse(
                probability=0.0,
                risk_level="Insufficient Data",
                explanation=["No other submissions found for this assignment to compare against."]
            )
            
        current_telem = {
            "typing_speed_wpm": request.typing_speed_wpm,
            "idle_ratio": request.idle_ratio,
            "paste_ratio": request.paste_ratio,
            "tab_switches": request.tab_switches,
            "suspicion_score": request.suspicion_score
        }

        best_prob = -1.0
        best_candidate = None
        best_features_dict = None
        
        # Step 3 & 4: Extract features and Predict for each candidate
        for candidate in candidates:
            # Fetch from embedding cache to prevent duplicate transformer operations
            candidate_emb = self.embedding_cache.get_embedding(
                candidate.assignment_id, candidate.submission_id, candidate.code
            )
            
            features_dict, features_vec = self.extractor.extract(
                request.code, current_telem, current_emb,
                candidate, candidate_emb
            )
            
            prob = self.predictor.predict_proba(features_vec)
            
            if prob > best_prob:
                best_prob = prob
                best_candidate = candidate
                best_features_dict = features_dict
                
        if best_prob < 0:
             return PlagiarismResponse(
                probability=0.0,
                risk_level="Insufficient Data",
                explanation=["Failed to process comparisons."]
            )

        # Step 5: Explain the prediction
        risk_level, signals = self.explainer.explain(best_prob, best_features_dict)
        
        return PlagiarismResponse(
            probability=round(best_prob, 4),
            risk_level=risk_level,
            matched_submission=best_candidate.submission_id if best_candidate else None,
            feature_contributions=best_features_dict,
            explanation=signals
        )
