from fastapi import APIRouter, HTTPException
from app.models.schemas import HintRequest, HintResponse
from app.services.evee_service import get_evee_hint

router = APIRouter()


@router.post("", response_model=HintResponse)
async def request_hint(payload: HintRequest):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    if not payload.current_code.strip():
        raise HTTPException(status_code=400, detail="No code found in editor")

    try:
        hint, tokens = await get_evee_hint(
            question=payload.question,
            current_code=payload.current_code,
            language=payload.language,
            problem_statement=payload.problem_statement,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"EVEE service error: {str(e)}")

    return HintResponse(hint=hint, tokens_used=tokens)
