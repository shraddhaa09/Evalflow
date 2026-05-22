from fastapi import APIRouter, HTTPException
from app.models.schemas import PlagiarismRequest, PlagiarismResponse
from app.services.plagiarism_service import score_code

router = APIRouter()


@router.post("", response_model=PlagiarismResponse)
def check_plagiarism(payload: PlagiarismRequest):
    if not payload.code.strip():
        raise HTTPException(status_code=400, detail="Code is empty")
    if len(payload.code) < 20:
        raise HTTPException(status_code=400, detail="Code too short to analyse (min 20 chars)")

    try:
        ai_prob, label, confidence, signals = score_code(payload.code)
    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ML inference error: {str(e)}")

    return PlagiarismResponse(
        ai_probability=ai_prob,
        label=label,
        confidence=confidence,
        signals=signals,
    )
