# Dataset Layout

EvalFlow plagiarism detection data and training artifacts.

```
dataset/
├── data/
│   ├── raw/                  # submissions.csv, telemetry.csv, labels.csv
│   └── processed/            # training_pairs_v2.csv, training_pairs_v3.csv
├── models/
│   ├── plagiarism_model_v3.pkl
│   ├── plagiarism_model_v3.manifest.json
│   └── evaluation/           # held-out test metrics
├── pipeline/                 # canonical training scripts (run in order 01→04)
├── original/                 # original student submissions
├── plagiarized/              # plagiarized submission variants
└── archive/                  # superseded scripts and older model versions
```

## Training

Use `pipeline/` only. See [pipeline/README.md](pipeline/README.md).

## Inference

Production inference runs in the FastAPI backend (`backend/app/services/`). It loads `models/plagiarism_model_v3.pkl` and computes the same feature vector defined in `pipeline/_paths.py`.

## Legacy paths

- `ML/dataset/` — archived; do not use for new work.
- `data/processed/training_pairs_final.csv` — legacy alias of `training_pairs_v3.csv`.
