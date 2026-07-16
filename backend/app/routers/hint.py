import logging

from fastapi import APIRouter, HTTPException
from app.models.schemas import HintRequest, HintResponse
from app.services.evee_service import get_evee_hint

router = APIRouter()
logger = logging.getLogger(__name__)


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
    except Exception as exc:
        logger.exception("Unexpected EVEE hint failure; returning fallback hint: %s", exc)
        hint = (
            "Focus on the core control flow first: identify the condition that should stop the loop, "
            "and then decide how the search boundaries should shrink after each comparison."
        )
        tokens = 0

    return HintResponse(hint=hint, tokens_used=tokens)
