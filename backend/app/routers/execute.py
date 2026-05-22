import subprocess
import tempfile
import time
import os

from fastapi import APIRouter, HTTPException
from app.models.schemas import ExecuteRequest, ExecuteResponse

router = APIRouter()


@router.post("", response_model=ExecuteResponse)
async def execute_code(payload: ExecuteRequest):

    if payload.language.lower() != "python":
        raise HTTPException(
            status_code=400,
            detail="Only Python supported"
        )

    start = time.perf_counter()

    temp_path = None

    try:

        with tempfile.NamedTemporaryFile(
            suffix=".py",
            mode="w",
            delete=False,
            encoding="utf-8"
        ) as f:

            temp_path = f.name
            f.write(payload.code)

        result = subprocess.run(
            ["python", temp_path],
            input=payload.stdin or "",
            capture_output=True,
            text=True,
            timeout=10
        )

        elapsed = round(
            time.perf_counter() - start,
            3
        )

        return ExecuteResponse(
            stdout=result.stdout,
            stderr=result.stderr,
            exit_code=result.returncode,
            execution_time=elapsed,
            memory_used=None,
            status=(
                "success"
                if result.returncode == 0
                else "error"
            )
        )

    except subprocess.TimeoutExpired:

        return ExecuteResponse(
            stdout="",
            stderr="Execution timed out",
            exit_code=-1,
            execution_time=10,
            memory_used=None,
            status="timeout"
        )

    finally:

        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)