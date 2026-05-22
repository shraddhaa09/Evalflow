import time
import httpx
from fastapi import APIRouter, HTTPException
from app.models.schemas import ExecuteRequest, ExecuteResponse

router = APIRouter()

PISTON_URL = "https://emkc.org/api/v2/piston/execute"

# Map friendly language names to Piston runtime identifiers
LANGUAGE_MAP = {
    "python":     {"language": "python",     "version": "3.10.0"},
    "javascript": {"language": "javascript", "version": "18.15.0"},
    "java":       {"language": "java",       "version": "15.0.2"},
    "c":          {"language": "c",          "version": "10.2.0"},
    "cpp":        {"language": "c++",        "version": "10.2.0"},
}


@router.post("", response_model=ExecuteResponse)
async def execute_code(payload: ExecuteRequest):
    lang_cfg = LANGUAGE_MAP.get(payload.language.lower())
    if not lang_cfg:
        raise HTTPException(status_code=400, detail=f"Unsupported language: {payload.language}")

    piston_payload = {
        "language": lang_cfg["language"],
        "version":  lang_cfg["version"],
        "files": [
            {"name": "main", "content": payload.code}
        ],
        "stdin":    payload.stdin or "",
        "args":     [],
        "compile_timeout": 10000,
        "run_timeout":     10000,
        "compile_memory_limit": -1,
        "run_memory_limit":     -1,
    }

    start = time.perf_counter()
    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.post(PISTON_URL, json=piston_payload)
            resp.raise_for_status()
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Piston execution timed out")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=502, detail=f"Piston error: {e.response.text}")

    elapsed = round(time.perf_counter() - start, 3)
    data    = resp.json()
    run     = data.get("run", {})

    stdout    = run.get("stdout", "") or ""
    stderr    = run.get("stderr", "") or ""
    exit_code = run.get("code", 0)

    status = "success"
    if exit_code != 0:
        status = "error"
    if "timed out" in stderr.lower():
        status = "timeout"

    return ExecuteResponse(
        stdout=stdout,
        stderr=stderr,
        exit_code=exit_code,
        execution_time=elapsed,
        memory_used=None,   # Piston free tier doesn't expose memory
        status=status,
    )
