from pydantic import BaseModel
from typing import Dict, Any, Optional

class Submission(BaseModel):
    submission_id: str
    assignment_id: str
    file_path: Optional[str] = None
    code: Optional[str] = None
    label: Optional[int] = 0
    # Telemetry
    typing_speed_wpm: float = 0.0
    idle_ratio: float = 0.0
    paste_ratio: float = 0.0
    tab_switches: int = 0
    suspicion_score: float = 0.0
