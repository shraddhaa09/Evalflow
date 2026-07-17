# EvalCode Backend

FastAPI backend powering EvalCode — code execution, EVEE hint engine, and ML-based plagiarism detection.

---

## Project Structure

```
backend/
├── app/
│   ├── main.py                     # FastAPI app, startup model checks, /health
│   ├── models/
│   │   └── schemas.py              # Pydantic request/response models
│   ├── routers/
│   │   ├── execute.py              # POST /execute
│   │   ├── hint.py                 # POST /hint
│   │   ├── plagiarism.py           # POST /plagiarism
│   │   └── session.py              # POST /session
│   └── services/
│       ├── evee_service.py         # Gemini hint engine
│       ├── model_loader.py         # Loads RF + CodeBERT; verifies at startup
│       ├── model_errors.py         # Explicit model/embedding errors
│       ├── repository.py           # Submission corpus + embedding cache
│       ├── plagiarism_features.py  # Pairwise feature vector (must match training)
│       └── plagiarism_service.py   # Pairwise comparison orchestration
├── run.py
├── requirements.txt
└── test_plagiarism.py              # Manual inference smoke test
```

Model artifact (not in this directory):

```
../dataset/models/plagiarism_model_v3.pkl
```

---

## Architecture layers

### Training pipeline (offline)

Scripts in `../dataset/pipeline/` build labeled pairwise features and train the classifier. See [../dataset/pipeline/README.md](../dataset/pipeline/README.md).

### Inference pipeline (runtime)

When `/plagiarism` is called:

1. `repository.get_embedding()` encodes code with CodeBERT (`microsoft/codebert-base`).
2. `plagiarism_features.compute_pairwise_features()` builds the 10-feature vector.
3. `model_loader.get_rf_model().predict_proba()` scores each peer pair.
4. The highest probability and explanatory signals are returned.

### Backend service

- **Startup:** `model_loader.verify_models()` loads the RF model and runs a CodeBERT probe embedding. Failures are recorded in app state; `/health` reports degraded status.
- **No silent fallbacks:** Missing models raise `ModelLoadError` (HTTP 503), not zero vectors or heuristic scores.
- **Corpus:** Peer submissions load from `../dataset/data/raw/` at startup.

Full design: [../docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md)

---

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS

pip install -r requirements.txt

cp .env.example .env         # add GEMINI_API_KEY

python run.py
# → http://localhost:8000
# → http://localhost:8000/docs
# → http://localhost:8000/health
```

Ensure `../dataset/models/plagiarism_model_v3.pkl` exists (run `dataset/pipeline/03_train_model.py` if missing).

---

## API Endpoints

### `GET /health`

Returns plagiarism model and corpus readiness.

### `POST /plagiarism`

Pairwise plagiarism score for submitted code against peers in the same assignment.

Returns HTTP 503 if models failed startup verification.

### `POST /execute`, `POST /hint`, `POST /session`

See inline docstrings and `/docs`.

---

## Plagiarism feature vector

Your `.pkl` model expects a `(1, 10)` array in this order (same as `dataset/pipeline/_paths.py`):

| Index | Feature |
|-------|---------|
| 0 | `token_similarity` |
| 1 | `line_similarity` |
| 2 | `length_similarity` |
| 3 | `structure_similarity` |
| 4 | `semantic_similarity` |
| 5 | `typing_speed_gap` |
| 6 | `idle_ratio_gap` |
| 7 | `paste_ratio_gap` |
| 8 | `tab_switch_gap` |
| 9 | `suspicion_gap` |

If features change, update both `dataset/pipeline/` and `app/services/plagiarism_features.py`.

---

## Manual test

```bash
cd backend
python test_plagiarism.py
```
