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
    high_plagiarism = "High Plagiarism Risk"
    medium_plagiarism = "Medium Plagiarism Risk"
    low_plagiarism = "Low Plagiarism Risk"
    clean = "Clean"
    insufficient_data = "Insufficient Data"

class PlagiarismRequest(BaseModel):
    code: str = Field(..., description="Code to analyse")
    language: str = Field(default="python")
    assignment_id: str = Field(..., description="Assignment ID for pairwise matching")
    typing_speed_wpm: float = 0.0
    idle_ratio: float = 0.0
    paste_ratio: float = 0.0
    tab_switches: int = 0
    suspicion_score: float = 0.0

class PlagiarismResponse(BaseModel):
    probability: float           # 0.0 – 1.0
    risk_level: str
    matched_submission: Optional[str] = None
    feature_contributions: Optional[dict] = None
    explanation: List[str]


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