"""Step 3: Train plagiarism_model_v3.pkl on processed pairwise features."""
import json
from datetime import datetime, timezone

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

from _paths import (
    FEATURE_COLUMNS,
    MODEL_MANIFEST,
    MODEL_V3,
    MODEL_VERSION,
    RF_PARAMS,
    SEMANTIC_MODEL_ID,
    TRAIN_TEST_SPLIT,
    TRAINING_PAIRS_V3,
)


def main() -> None:
    df = pd.read_csv(TRAINING_PAIRS_V3)
    x = df[FEATURE_COLUMNS]
    y = df["label"]

    split_kwargs = {
        "test_size": TRAIN_TEST_SPLIT["test_size"],
        "random_state": TRAIN_TEST_SPLIT["random_state"],
    }
    if TRAIN_TEST_SPLIT["stratify"]:
        split_kwargs["stratify"] = y

    x_train, x_test, y_train, y_test = train_test_split(x, y, **split_kwargs)

    model = RandomForestClassifier(**RF_PARAMS)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    MODEL_V3.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_V3)

    manifest = {
        "model_version": MODEL_VERSION,
        "model_file": MODEL_V3.name,
        "trained_at": datetime.now(timezone.utc).isoformat(),
        "dataset_file": TRAINING_PAIRS_V3.name,
        "dataset_rows": len(df),
        "feature_columns": FEATURE_COLUMNS,
        "semantic_model": SEMANTIC_MODEL_ID,
        "train_test_split": TRAIN_TEST_SPLIT,
        "classifier": {"type": "RandomForestClassifier", **RF_PARAMS},
        "train_rows": len(x_train),
        "test_rows": len(x_test),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
        "classification_report": classification_report(y_test, y_pred, output_dict=True),
    }
    MODEL_MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print("\nCONFUSION MATRIX:")
    print(confusion_matrix(y_test, y_pred))
    print("\nCLASSIFICATION REPORT:")
    print(classification_report(y_test, y_pred))
    print(f"\nSaved: {MODEL_V3}")
    print(f"Saved: {MODEL_MANIFEST}")


if __name__ == "__main__":
    main()
