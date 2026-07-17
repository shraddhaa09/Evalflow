from fastapi import APIRouter, HTTPException, Depends, Request
from app.models.schemas import PlagiarismRequest, PlagiarismResponse
from app.core.config import settings
from app.core.logger import logger
from app.domain.exceptions import (
    ModelUnavailableException, 
    CorpusUnavailableException, 
    CandidateNotFoundException, 
    InferenceError
)

from app.domain.services.orchestrator import InferenceOrchestrator
from app.infrastructure.repositories.csv_repository import CSVSubmissionRepository
from app.infrastructure.ml.codebert_embedder import CodeBertEmbeddingProvider
from app.infrastructure.ml.topk_retriever import TopKCandidateRetriever
from app.infrastructure.ml.v3_extractor import V3FeatureExtractor
from app.infrastructure.ml.rf_predictor import RandomForestPredictor
from app.infrastructure.explainers.rule_explainer import RuleBasedExplainer
from app.infrastructure.ml.embedding_cache import EmbeddingCache

router = APIRouter()

# Singletons for dependencies that hold state
_repository = CSVSubmissionRepository()
_embedder = CodeBertEmbeddingProvider()
_predictor = RandomForestPredictor()
_embedding_cache = EmbeddingCache(_repository, _embedder)

def get_repository():
    return _repository

def get_embedder():
    return _embedder

def get_cache(repo=Depends(get_repository), emb=Depends(get_embedder)):
    return _embedding_cache

def get_retriever(repo=Depends(get_repository), cache=Depends(get_cache)):
    return TopKCandidateRetriever(repo, cache)

def get_extractor():
    return V3FeatureExtractor()

def get_predictor():
    return _predictor

def get_explainer():
    return RuleBasedExplainer()

def get_orchestrator(
    repo=Depends(get_repository),
    emb=Depends(get_embedder),
    cache=Depends(get_cache),
    ret=Depends(get_retriever),
    ext=Depends(get_extractor),
    pred=Depends(get_predictor),
    expl=Depends(get_explainer)
):
    return InferenceOrchestrator(repo, emb, cache, ret, ext, pred, expl, settings)

@router.post("", response_model=PlagiarismResponse)
def check_plagiarism(
    payload: PlagiarismRequest, 
    request: Request,
    orchestrator: InferenceOrchestrator = Depends(get_orchestrator)
):
    if not payload.code.strip():
        logger.warning("Received empty code payload.")
        raise HTTPException(
            400,
            "Code empty"
        )
        
    try:
        logger.info(f"Processing plagiarism check for assignment: {payload.assignment_id}")
        return orchestrator.score_code(payload)
    except ModelUnavailableException as e:
        logger.error(f"Model unavailable: {str(e)}")
        raise HTTPException(503, str(e))
    except CorpusUnavailableException as e:
        logger.error(f"Corpus unavailable: {str(e)}")
        raise HTTPException(503, str(e))
    except CandidateNotFoundException as e:
        logger.warning(f"No candidates found: {str(e)}")
        # If no candidates, we can still return a valid 200 response with Insufficient Data
        return PlagiarismResponse(
            probability=0.0,
            risk_level="Insufficient Data",
            explanation=[str(e)]
        )
    except InferenceError as e:
        logger.error(f"Inference error: {str(e)}")
        raise HTTPException(500, str(e))
    except Exception as e:
        logger.exception("Unhandled error processing plagiarism check")
        raise HTTPException(500, f"Internal Server Error: {str(e)}")