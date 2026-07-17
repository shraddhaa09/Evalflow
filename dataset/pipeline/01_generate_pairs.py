"""Step 1: Build pairwise training features from raw submissions."""
import re
from itertools import combinations

import pandas as pd

from _paths import (
    DATASET_ROOT,
    LABELS_CSV,
    PROCESSED_DIR,
    SUBMISSIONS_CSV,
    TELEMETRY_CSV,
    TRAINING_PAIRS_V2,
)


def read_code(path: str) -> str:
    code_path = DATASET_ROOT / path
    with open(code_path, "r", encoding="utf-8") as f:
        return f.read()


def tokenize(code: str):
    return re.findall(r"\b\w+\b", code.lower())


def jaccard(a: str, b: str) -> float:
    a_tokens, b_tokens = set(tokenize(a)), set(tokenize(b))
    if not a_tokens and not b_tokens:
        return 1.0
    return len(a_tokens & b_tokens) / len(a_tokens | b_tokens)


def line_sim(a: str, b: str) -> float:
    a_lines = {line.strip() for line in a.splitlines() if line.strip()}
    b_lines = {line.strip() for line in b.splitlines() if line.strip()}
    if not a_lines and not b_lines:
        return 1.0
    return len(a_lines & b_lines) / len(a_lines | b_lines)


def length_sim(a: str, b: str) -> float:
    len_a, len_b = len(a), len(b)
    return min(len_a, len_b) / max(len_a, len_b) if max(len_a, len_b) > 0 else 1.0


def structure_features(code: str):
    return {
        "for": len(re.findall(r"\bfor\b", code)),
        "while": len(re.findall(r"\bwhile\b", code)),
        "if": len(re.findall(r"\bif\b", code)),
        "def": len(re.findall(r"\bdef\b", code)),
    }


def structure_sim(a: str, b: str) -> float:
    a_features, b_features = structure_features(a), structure_features(b)
    score, total = 0.0, 0.0
    for key in a_features:
        score += max(0, min(a_features[key], b_features[key]))
        total += max(a_features[key], b_features[key]) + 1e-5
    return score / total


def main() -> None:
    submissions = pd.read_csv(SUBMISSIONS_CSV)
    telemetry = pd.read_csv(TELEMETRY_CSV)
    labels = pd.read_csv(LABELS_CSV)

    df = (
        submissions.merge(telemetry, on="submission_id")
        .merge(labels, on="submission_id")
    )

    rows = []
    for assignment_id, group in df.groupby("assignment_id"):
        records = group.to_dict("records")
        for left, right in combinations(records, 2):
            code_a = read_code(left["file_path"])
            code_b = read_code(right["file_path"])
            rows.append(
                {
                    "submission_a": left["submission_id"],
                    "submission_b": right["submission_id"],
                    "assignment_id": assignment_id,
                    "code_a": code_a,
                    "code_b": code_b,
                    "token_similarity": jaccard(code_a, code_b),
                    "line_similarity": line_sim(code_a, code_b),
                    "length_similarity": length_sim(code_a, code_b),
                    "structure_similarity": structure_sim(code_a, code_b),
                    "typing_speed_gap": abs(left["typing_speed_wpm"] - right["typing_speed_wpm"]),
                    "idle_ratio_gap": abs(left["idle_ratio"] - right["idle_ratio"]),
                    "paste_ratio_gap": abs(left["paste_ratio"] - right["paste_ratio"]),
                    "tab_switch_gap": abs(left["tab_switches"] - right["tab_switches"]),
                    "suspicion_gap": abs(left["suspicion_score"] - right["suspicion_score"]),
                    "label": 1 if (left["label"] == 1 and right["label"] == 1) else 0,
                }
            )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    output = pd.DataFrame(rows)
    output.to_csv(TRAINING_PAIRS_V2, index=False)
    print(f"Saved {TRAINING_PAIRS_V2}")
    print(f"Rows: {len(output)}")


if __name__ == "__main__":
    main()
