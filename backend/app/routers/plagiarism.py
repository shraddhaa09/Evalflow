from fastapi import APIRouter, HTTPException
from app.models.schemas import PlagiarismRequest, PlagiarismResponse
from app.services.plagiarism_service import score_code

router = APIRouter()


@router.post("", response_model=PlagiarismResponse)
def check_plagiarism(payload: PlagiarismRequest):

    if not payload.code or not payload.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")

    if len(payload.code.strip()) < 20:
        raise HTTPException(
            status_code=400,
            detail="Code too short for analysis (min 20 chars)"
        )

    try:
        ai_prob, label, confidence, signals = score_code(payload.code)

        return PlagiarismResponse(
            ai_probability=ai_prob,
            label=label,
            confidence=confidence,
            signals=signals,
        )

    except FileNotFoundError as e:
        raise HTTPException(status_code=503, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ML inference error: {str(e)}")