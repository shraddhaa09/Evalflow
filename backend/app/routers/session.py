import json
import os
from datetime import datetime
from pathlib import Path
from fastapi import APIRouter
from app.models.schemas import SessionRequest, SessionResponse, EventType

router   = APIRouter()
LOG_DIR  = Path(os.getenv("SESSION_LOG_DIR", "session_logs"))
LOG_DIR.mkdir(exist_ok=True)


def summarise_events(events) -> dict:
    counts = {e.value: 0 for e in EventType}
    for ev in events:
        counts[ev.event_type.value] += 1
    return {
        "total_events":    len(events),
        "tab_switches":    counts[EventType.tab_switch.value],
        "paste_attempts":  counts[EventType.paste_attempt.value],
        "copy_attempts":   counts[EventType.copy_attempt.value],
        "runs":            counts[EventType.run.value],
        "hint_requests":   counts[EventType.hint_request.value],
        "plag_checks":     counts[EventType.plag_check.value],
    }


@router.post("", response_model=SessionResponse)
def log_session(payload: SessionRequest):
    summary = summarise_events(payload.events)

    log_entry = {
        "session_id": payload.session_id,
        "logged_at":  datetime.utcnow().isoformat(),
        "summary":    summary,
        "events":     [
            {
                "type":      e.event_type.value,
                "timestamp": e.timestamp,
                "metadata":  e.metadata,
            }
            for e in payload.events
        ],
    }

    log_file = LOG_DIR / f"{payload.session_id}.json"

    # Append to existing log or create new
    if log_file.exists():
        with open(log_file, "r") as f:
            existing = json.load(f)
        existing["events"].extend(log_entry["events"])
        existing["summary"] = summarise_events(
            [type("E", (), {"event_type": type("T", (), {"value": e["type"]})()})() 
             for e in existing["events"]]
        )
        existing["last_updated"] = log_entry["logged_at"]
        with open(log_file, "w") as f:
            json.dump(existing, f, indent=2)
    else:
        with open(log_file, "w") as f:
            json.dump(log_entry, f, indent=2)

    return SessionResponse(
        session_id=payload.session_id,
        events_logged=len(payload.events),
        summary=summary,
    )


@router.get("/{session_id}")
def get_session(session_id: str):
    log_file = LOG_DIR / f"{session_id}.json"
    if not log_file.exists():
        return {"error": "Session not found"}
    with open(log_file) as f:
        return json.load(f)
