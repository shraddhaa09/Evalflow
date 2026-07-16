import os
import pandas as pd
import re
from itertools import combinations

BASE = "metadata"

submissions = pd.read_csv(os.path.join(BASE, "submissions.csv"))
telemetry = pd.read_csv(os.path.join(BASE, "telemetry.csv"))
labels = pd.read_csv(os.path.join(BASE, "labels.csv"))

df = submissions.merge(telemetry, on="submission_id").merge(labels, on="submission_id")

# =========================
# READ CODE
# =========================

def read_code(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# =========================
# TOKEN SIMILARITY
# =========================

def tokenize(code):
    return re.findall(r'\b\w+\b', code.lower())

def jaccard(a, b):
    A, B = set(tokenize(a)), set(tokenize(b))
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)

# =========================
# LINE SIMILARITY
# =========================

def line_sim(a, b):
    A = set([l.strip() for l in a.splitlines() if l.strip()])
    B = set([l.strip() for l in b.splitlines() if l.strip()])
    if not A and not B:
        return 1.0
    return len(A & B) / len(A | B)

# =========================
# LENGTH SIMILARITY
# =========================

def length_sim(a, b):
    return min(len(a), len(b)) / max(len(a), len(b)) if max(len(a), len(b)) > 0 else 1

# =========================
# STRUCTURE FEATURES
# =========================

def structure_features(code):
    return {
        "for": len(re.findall(r'\bfor\b', code)),
        "while": len(re.findall(r'\bwhile\b', code)),
        "if": len(re.findall(r'\bif\b', code)),
        "def": len(re.findall(r'\bdef\b', code)),
    }

def structure_sim(a, b):
    A, B = structure_features(a), structure_features(b)
    score, total = 0, 0

    for k in A:
        score += max(0, min(A[k], B[k]))
        total += max(A[k], B[k]) + 1e-5

    return score / total

# =========================
# BUILD PAIRS
# =========================

rows = []

for aid, group in df.groupby("assignment_id"):
    records = group.to_dict("records")

    for a, b in combinations(records, 2):

        code_a = read_code(a["file_path"])
        code_b = read_code(b["file_path"])

        row = {
            "submission_a": a["submission_id"],
            "submission_b": b["submission_id"],
            "assignment_id": aid,

            # CODE FEATURES (NEW CORE)
            "code_a": code_a,
            "code_b": code_b,

            "token_similarity": jaccard(code_a, code_b),
            "line_similarity": line_sim(code_a, code_b),
            "length_similarity": length_sim(code_a, code_b),
            "structure_similarity": structure_sim(code_a, code_b),

            # TELEMETRY
            "typing_speed_gap": abs(a["typing_speed_wpm"] - b["typing_speed_wpm"]),
            "idle_ratio_gap": abs(a["idle_ratio"] - b["idle_ratio"]),
            "paste_ratio_gap": abs(a["paste_ratio"] - b["paste_ratio"]),
            "tab_switch_gap": abs(a["tab_switches"] - b["tab_switches"]),
            "suspicion_gap": abs(a["suspicion_score"] - b["suspicion_score"]),

            # LABEL
            "label": 1 if (a["label"] == 1 and b["label"] == 1) else 0,
        }

        rows.append(row)

df_out = pd.DataFrame(rows)
df_out.to_csv("metadata/training_pairs_v2.csv", index=False)

print("Saved training_pairs_v2.csv")
print("Rows:", len(df_out))