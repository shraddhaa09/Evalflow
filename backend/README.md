# EvalCode Backend

FastAPI backend powering EvalCode — four endpoints, Piston code execution, EVEE hint engine, and ML-based plagiarism detection.

---

## Project Structure

```
evalcode-backend/
├── app/
│   ├── main.py                  # FastAPI app + CORS + routers
│   ├── models/
│   │   └── schemas.py           # Pydantic request/response models
│   ├── routers/
│   │   ├── execute.py           # POST /execute  — Piston code runner
│   │   ├── hint.py              # POST /hint     — EVEE hinter
│   │   ├── plagiarism.py        # POST /plagiarism — ML classifier
│   │   └── session.py           # POST /session  — anti-cheat event log
│   └── services/
│       ├── evee_service.py      # Claude API call with guardrail prompt
│       └── plagiarism_service.py # .pkl model loading + feature extraction
├── model/
│   └── classifier.pkl           # ← place YOUR trained model here
├── session_logs/                # auto-created, stores per-session JSON
├── .env.example
├── requirements.txt
└── run.py
```

---

## Setup

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env — add your ANTHROPIC_API_KEY

# 4. Place your trained classifier
mkdir model
cp /path/to/your/classifier.pkl model/classifier.pkl

# 5. Start the dev server
python run.py
# → http://localhost:8000
# → http://localhost:8000/docs  (auto-generated Swagger UI)
```

---

## API Endpoints

### `POST /execute`
Run code via Piston.
```json
// Request
{ "code": "print('hello')", "language": "python" }

// Response
{ "stdout": "hello\n", "stderr": "", "exit_code": 0, "execution_time": 0.14, "status": "success" }
```

### `POST /hint`
Get a conceptual hint from EVEE. Never returns full solutions.
```json
// Request
{ "question": "How do I optimise this loop?", "current_code": "for i in range(n):\n    ...", "language": "python" }

// Response
{ "hint": "Think about whether you need to visit every element...", "tokens_used": 142 }
```

### `POST /plagiarism`
Score code with your trained `.pkl` classifier.
```json
// Request
{ "code": "def binary_search(arr, target):\n    ..." }

// Response
{ "ai_probability": 0.81, "label": "Likely AI Generated", "confidence": 0.91, "signals": ["High indentation regularity", "Auto-generated docstrings detected"] }
```

### `POST /session`
Log anti-cheat events from the frontend.
```json
// Request
{ "session_id": "abc123", "events": [{ "event_type": "TAB_SWITCH", "timestamp": 1718000000000 }] }

// Response
{ "session_id": "abc123", "events_logged": 1, "summary": { "tab_switches": 1, ... } }
```

---

## Plagiarism Model — Feature Vector

Your `.pkl` model must accept a `(1, 10)` numpy array with these features in order:

| Index | Feature              |
|-------|----------------------|
| 0     | total_lines          |
| 1     | avg_line_length      |
| 2     | std_line_length      |
| 3     | indent_std           |
| 4     | comment_ratio        |
| 5     | has_docstring        |
| 6     | unique_token_ratio   |
| 7     | avg_token_length     |
| 8     | blank_line_ratio     |
| 9     | keyword_density      |

If your model uses different features, update `extract_features()` in `app/services/plagiarism_service.py`.

---

## CORS

By default, requests from `http://localhost:3000` (Next.js dev) are allowed.
Update `allow_origins` in `app/main.py` before deploying to production.
