# Plagiarism Training Pipeline

Single source of truth for building `plagiarism_model_v3.pkl`.

Run from this directory:

```bash
cd dataset/pipeline
python 01_generate_pairs.py
python 02_extract_semantics.py
python 03_train_model.py
python 04_evaluate_model.py
```

## Steps

| Script | Input | Output |
|--------|-------|--------|
| `01_generate_pairs.py` | `data/raw/{submissions,telemetry,labels}.csv` | `data/processed/training_pairs_v2.csv` |
| `02_extract_semantics.py` | `training_pairs_v2.csv` | `data/processed/training_pairs_v3.csv` |
| `03_train_model.py` | `training_pairs_v3.csv` | `models/plagiarism_model_v3.pkl`, `models/plagiarism_model_v3.manifest.json` |
| `04_evaluate_model.py` | trained model + `training_pairs_v3.csv` | `models/evaluation/*` |

## Shared constants

All paths, feature order, split parameters, and model IDs live in `_paths.py`. Inference in `backend/app/services/` must stay aligned with these constants.

## Dependencies

```bash
pip install pandas scikit-learn joblib sentence-transformers
```

Legacy duplicate scripts were moved to `dataset/archive/scripts/ml_legacy/`.
