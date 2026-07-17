"""Step 4: Evaluate plagiarism_model_v3.pkl on the held-out test split."""
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

from _paths import (
    EVAL_DIR,
    FEATURE_COLUMNS,
    MODEL_MANIFEST,
    MODEL_V3,
    MODEL_VERSION,
    TRAIN_TEST_SPLIT,
    TRAINING_PAIRS_V3,
)


def save_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    if not MODEL_V3.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_V3}. Run 03_train_model.py first.")

    df = pd.read_csv(TRAINING_PAIRS_V3)
    x = df[FEATURE_COLUMNS]
    y = df["label"]

    split_kwargs = {
        "test_size": TRAIN_TEST_SPLIT["test_size"],
        "random_state": TRAIN_TEST_SPLIT["random_state"],
    }
    if TRAIN_TEST_SPLIT["stratify"]:
        split_kwargs["stratify"] = y

    _, x_test, _, y_test = train_test_split(x, y, **split_kwargs)
    model = joblib.load(MODEL_V3)
    y_pred = model.predict(x_test)
    y_prob = model.predict_proba(x_test)[:, 1]

    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    report_dict = classification_report(y_test, y_pred, output_dict=True)

    EVAL_DIR.mkdir(parents=True, exist_ok=True)
    save_text(EVAL_DIR / "confusion_matrix.txt", np.array2string(cm))
    save_text(EVAL_DIR / "classification_report.txt", report)

    metadata = {
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "model_version": MODEL_VERSION,
        "model_file": str(MODEL_V3),
        "dataset_file": str(TRAINING_PAIRS_V3),
        "dataset_rows": len(df),
        "held_out_test_rows": len(x_test),
        "train_test_split": TRAIN_TEST_SPLIT,
        "feature_columns": FEATURE_COLUMNS,
        "confusion_matrix": cm.tolist(),
        "classification_report": report_dict,
        "positive_class_rate_test": float(y_test.mean()),
        "mean_predicted_probability": float(y_prob.mean()),
    }

    if MODEL_MANIFEST.exists():
        metadata["training_manifest"] = json.loads(MODEL_MANIFEST.read_text(encoding="utf-8"))

    (EVAL_DIR / "evaluation_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print("Evaluation complete.")
    print(f"Confusion matrix saved to {EVAL_DIR / 'confusion_matrix.txt'}")
    print(f"Classification report saved to {EVAL_DIR / 'classification_report.txt'}")
    print(f"Metadata saved to {EVAL_DIR / 'evaluation_metadata.json'}")
    print("\nCONFUSION MATRIX:")
    print(cm)
    print("\nCLASSIFICATION REPORT:")
    print(report)


if __name__ == "__main__":
    main()
