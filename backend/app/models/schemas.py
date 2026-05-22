from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


# ── Execution ──────────────────────────────────────────────
class ExecuteRequest(BaseModel):
    code: str = Field(..., description="Source code to run")
    language: str = Field(default="python", description="Programming language")
    version: str = Field(default="3.10.0", description="Language version")
    stdin: Optional[str] = Field(default=None, description="Standard input for the program")

class ExecuteResponse(BaseModel):
    stdout: str
    stderr: str
    exit_code: int
    execution_time: float   # seconds
    memory_used: Optional[str] = None
    status: str             # "success" | "error" | "timeout"


# ── EVEE Hint ──────────────────────────────────────────────
class HintRequest(BaseModel):
    question: str = Field(..., description="What the user is asking")
    current_code: str = Field(..., description="Current code in the editor")
    language: str = Field(default="python")
    problem_statement: Optional[str] = Field(default=None, description="Original problem/task description")

class HintResponse(BaseModel):
    hint: str
    tokens_used: Optional[int] = None


# ── Plagiarism ─────────────────────────────────────────────
class PlagiarismLabel(str, Enum):
    likely_ai       = "Likely AI Generated"
    possibly_ai     = "Possibly AI Assisted"
    likely_human    = "Likely Human Written"

class PlagiarismRequest(BaseModel):
    code: str = Field(..., description="Code to analyse")
    language: str = Field(default="python")

class PlagiarismResponse(BaseModel):
    ai_probability: float           # 0.0 – 1.0
    label: PlagiarismLabel
    confidence: float               # model confidence
    signals: List[str]              # explanatory flags shown in UI


# ── Session ────────────────────────────────────────────────
class EventType(str, Enum):
    tab_switch    = "TAB_SWITCH"
    copy_attempt  = "COPY_ATTEMPT"
    paste_attempt = "PASTE_ATTEMPT"
    run           = "RUN"
    hint_request  = "HINT_REQUEST"
    plag_check    = "PLAG_CHECK"

class SessionEvent(BaseModel):
    event_type: EventType
    timestamp: float    # Unix epoch ms
    metadata: Optional[dict] = None

class SessionRequest(BaseModel):
    session_id: str
    events: List[SessionEvent]

class SessionResponse(BaseModel):
    session_id: str
    events_logged: int
    summary: dict