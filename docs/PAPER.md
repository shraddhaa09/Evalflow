# EvalFlow Plagiarism Detection — Technical Summary

This document supports project reporting and distinguishes the three runtime layers of the plagiarism subsystem.

## Problem

Detect likely plagiarism between student code submissions within the same assignment using code similarity features and behavioral telemetry gaps.

## Model

- **Classifier:** `RandomForestClassifier` (350 trees, max depth 16, balanced class weights)
- **Version:** `v3` (`dataset/models/plagiarism_model_v3.pkl`)
- **Semantic encoder:** `microsoft/codebert-base` via SentenceTransformers
- **Similarity metric:** sklearn cosine similarity on CodeBERT embeddings

## Training pipeline (offline)

Scripts in `dataset/pipeline/` are the single source of truth:

1. Generate pairwise features from raw submissions.
2. Add semantic similarity with CodeBERT.
3. Train and serialize the classifier.
4. Evaluate on a held-out 20% stratified test split (`random_state=42`).

Evaluation artifacts are written to `dataset/models/evaluation/`.

## Inference pipeline (runtime)

At request time the backend:

1. Loads the trained `.pkl` model and CodeBERT once at startup.
2. Retrieves peer submissions for the assignment from the in-memory corpus.
3. Computes the same 10-feature vector as training for each pair.
4. Returns the maximum plagiarized-class probability and explanatory signals.

Feature logic lives in `backend/app/services/plagiarism_features.py` and must remain aligned with `dataset/pipeline/01_generate_pairs.py` and `02_extract_semantics.py`.

## Backend service architecture

FastAPI exposes `POST /plagiarism`. The router delegates to `plagiarism_service.py`, which uses:

- `model_loader.py` — model lifecycle and startup verification
- `repository.py` — corpus and embedding cache
- `plagiarism_features.py` — pairwise feature construction

`GET /health` reports whether models and corpus loaded successfully. The service fails explicitly (HTTP 503) when models are unavailable; it does not fall back to zero embeddings or heuristic scores.

## Reproducibility

| Item | Value |
|------|-------|
| Dataset | `dataset/data/processed/training_pairs_v3.csv` |
| Split | 80/20 stratified, `random_state=42` |
| Semantic model | `microsoft/codebert-base` |
| Model artifact | `dataset/models/plagiarism_model_v3.pkl` |
| Metrics | `dataset/models/evaluation/` |

Regenerate everything:

```bash
cd dataset/pipeline
python 01_generate_pairs.py
python 02_extract_semantics.py
python 03_train_model.py
python 04_evaluate_model.py
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for diagrams and component tables.
