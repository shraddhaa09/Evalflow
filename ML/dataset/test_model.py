import joblib
import pandas as pd

# =========================
# LOAD MODEL
# =========================

model = joblib.load("plagiarism_model_v3.pkl")

# =========================
# LOAD SAMPLE DATA
# =========================

df = pd.read_csv("metadata/training_pairs_v3.csv")

# Pick random unseen samples
sample = df.sample(10, random_state=42)

# =========================
# FEATURES
# =========================

features = [
    "token_similarity",
    "line_similarity",
    "length_similarity",
    "structure_similarity",
    "semantic_similarity",
    "typing_speed_gap",
    "idle_ratio_gap",
    "paste_ratio_gap",
    "tab_switch_gap",
    "suspicion_gap"
]

X = sample[features]

# =========================
# PREDICTIONS
# =========================

predictions = model.predict(X)
probabilities = model.predict_proba(X)

# =========================
# SHOW RESULTS
# =========================

for i, (_, row) in enumerate(sample.iterrows()):

    actual = row["label"]
    predicted = predictions[i]
    confidence = round(max(probabilities[i]), 4)

    print("=" * 60)

    print(f"PAIR: {row['submission_a']} vs {row['submission_b']}")

    print(f"ACTUAL LABEL: {actual}")
    print(f"PREDICTED:    {predicted}")
    print(f"CONFIDENCE:   {confidence}")

    # Risk mapping
    if confidence >= 0.85:
        risk = "HIGH"
    elif confidence >= 0.60:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    print(f"RISK LEVEL:   {risk}")

    print("\nTOP FEATURES:")

    print(f"semantic_similarity : {row['semantic_similarity']:.4f}")
    print(f"token_similarity    : {row['token_similarity']:.4f}")
    print(f"paste_ratio_gap     : {row['paste_ratio_gap']:.4f}")
    print(f"suspicion_gap       : {row['suspicion_gap']:.4f}")

    print("=" * 60)