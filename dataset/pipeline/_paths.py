"""Canonical paths and constants for the EvalFlow plagiarism training pipeline."""
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
DATASET_ROOT = PIPELINE_DIR.parent
RAW_DIR = DATASET_ROOT / "data" / "raw"
PROCESSED_DIR = DATASET_ROOT / "data" / "processed"
MODELS_DIR = DATASET_ROOT / "models"
EVAL_DIR = MODELS_DIR / "evaluation"

SUBMISSIONS_CSV = RAW_DIR / "submissions.csv"
TELEMETRY_CSV = RAW_DIR / "telemetry.csv"
LABELS_CSV = RAW_DIR / "labels.csv"

TRAINING_PAIRS_V2 = PROCESSED_DIR / "training_pairs_v2.csv"
TRAINING_PAIRS_V3 = PROCESSED_DIR / "training_pairs_v3.csv"
MODEL_V3 = MODELS_DIR / "plagiarism_model_v3.pkl"
MODEL_MANIFEST = MODELS_DIR / "plagiarism_model_v3.manifest.json"

FEATURE_COLUMNS = [
    "token_similarity",
    "line_similarity",
    "length_similarity",
    "structure_similarity",
    "semantic_similarity",
    "typing_speed_gap",
    "idle_ratio_gap",
    "paste_ratio_gap",
    "tab_switch_gap",
    "suspicion_gap",
]

MODEL_VERSION = "v3"
SEMANTIC_MODEL_ID = "microsoft/codebert-base"
TRAIN_TEST_SPLIT = {
    "test_size": 0.2,
    "random_state": 42,
    "stratify": True,
}
RF_PARAMS = {
    "n_estimators": 350,
    "max_depth": 16,
    "class_weight": "balanced",
    "random_state": 42,
}
