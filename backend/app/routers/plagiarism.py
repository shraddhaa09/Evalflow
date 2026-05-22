from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    PlagiarismRequest,
    PlagiarismResponse
)

from app.services.plagiarism_service import score_code


router = APIRouter()


@router.post(
    "",
    response_model=PlagiarismResponse
)
def check_plagiarism(
    payload: PlagiarismRequest
):

    if not payload.code.strip():
        raise HTTPException(
            400,
            "Code empty"
        )

    try:

        (
            ai_probability,
            label,
            confidence,
            signals
        ) = score_code(
            payload.code
        )

        return PlagiarismResponse(
            ai_probability=ai_probability,
            label=label,
            confidence=confidence,
            signals=signals
        )

    except FileNotFoundError:
        raise HTTPException(
            500,
            "binary_classifier.pkl not found"
        )

    except Exception as e:
        raise HTTPException(
            500,
            str(e)
        )