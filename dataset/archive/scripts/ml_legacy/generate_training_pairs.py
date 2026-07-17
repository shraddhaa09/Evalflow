import os
import re
import pandas as pd
from itertools import combinations

# =========================
# LOAD CSV FILES
# =========================

BASE_PATH = "metadata"

submissions = pd.read_csv(os.path.join(BASE_PATH, "submissions.csv"))
telemetry = pd.read_csv(os.path.join(BASE_PATH, "telemetry.csv"))
labels = pd.read_csv(os.path.join(BASE_PATH, "labels.csv"))

# =========================
# MERGE DATA
# =========================

df = submissions.merge(telemetry, on="submission_id")
df = df.merge(labels, on="submission_id")

# =========================
# SIMPLE TOKENIZER
# =========================

def tokenize_code(code):
    tokens = re.findall(r'\b\w+\b', code.lower())
    return set(tokens)

# =========================
# TOKEN SIMILARITY
# =========================

def jaccard_similarity(code1, code2):
    tokens1 = tokenize_code(code1)
    tokens2 = tokenize_code(code2)

    if not tokens1 and not tokens2:
        return 1.0

    intersection = len(tokens1.intersection(tokens2))
    union = len(tokens1.union(tokens2))

    return round(intersection / union, 4)

# =========================
# LINE SIMILARITY
# =========================

def line_similarity(code1, code2):
    lines1 = set([
        line.strip()
        for line in code1.splitlines()
        if line.strip()
    ])

    lines2 = set([
        line.strip()
        for line in code2.splitlines()
        if line.strip()
    ])

    if not lines1 and not lines2:
        return 1.0

    intersection = len(lines1.intersection(lines2))
    union = len(lines1.union(lines2))

    return round(intersection / union, 4)

# =========================
# LENGTH SIMILARITY
# =========================

def length_similarity(code1, code2):
    len1 = len(code1)
    len2 = len(code2)

    if max(len1, len2) == 0:
        return 1.0

    return round(min(len1, len2) / max(len1, len2), 4)

# =========================
# LOAD CODE CONTENT
# =========================

def read_code_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# =========================
# GENERATE PAIRS
# =========================

training_rows = []

grouped = df.groupby("assignment_id")

for assignment_id, group in grouped:

    records = group.to_dict("records")

    for a, b in combinations(records, 2):

        code_a = read_code_file(a["file_path"])
        code_b = read_code_file(b["file_path"])

        token_sim = jaccard_similarity(code_a, code_b)
        line_sim = line_similarity(code_a, code_b)
        length_sim = length_similarity(code_a, code_b)

        typing_gap = round(
            abs(a["typing_speed_wpm"] - b["typing_speed_wpm"]), 4
        )

        idle_gap = round(
            abs(a["idle_ratio"] - b["idle_ratio"]), 4
        )

        paste_gap = round(
            abs(a["paste_ratio"] - b["paste_ratio"]), 4
        )

        tab_gap = abs(a["tab_switches"] - b["tab_switches"])

        suspicion_gap = round(
            abs(a["suspicion_score"] - b["suspicion_score"]), 4
        )

        # =========================
        # LABEL LOGIC
        # =========================

        plag_pair = (
            a["label"] == 1 and
            b["label"] == 1
        )

        label = 1 if plag_pair else 0

        # =========================
        # RISK LOGIC
        # =========================

        if token_sim >= 0.85:
            risk = "high"
        elif token_sim >= 0.60:
            risk = "medium"
        else:
            risk = "low"

        training_rows.append({
            "submission_a": a["submission_id"],
            "submission_b": b["submission_id"],
            "assignment_id": assignment_id,

            "token_similarity": token_sim,
            "line_similarity": line_sim,
            "length_similarity": length_sim,

            "typing_speed_gap": typing_gap,
            "idle_ratio_gap": idle_gap,
            "paste_ratio_gap": paste_gap,
            "tab_switch_gap": tab_gap,
            "suspicion_gap": suspicion_gap,

            "label": label,
            "risk_level": risk
        })

# =========================
# SAVE CSV
# =========================

training_df = pd.DataFrame(training_rows)

output_path = os.path.join(BASE_PATH, "training_pairs.csv")

training_df.to_csv(output_path, index=False)

print(f"Generated training_pairs.csv with {len(training_df)} rows.")