import pandas as pd

INPUT_PATH = "metadata/training_pairs.csv"
OUTPUT_PATH = "metadata/training_pairs_clean.csv"

df = pd.read_csv(INPUT_PATH)

print("Original size:", len(df))

# -------------------------
# RULE 1:
# High similarity but labeled clean → REMOVE
# -------------------------
rule1 = (df["token_similarity"] > 0.85) & (df["label"] == 0)

# -------------------------
# RULE 2:
# Low similarity but labeled plagiarized → REMOVE
# -------------------------
rule2 = (df["token_similarity"] < 0.25) & (df["label"] == 1)

# -------------------------
# COMBINE FILTERS
# -------------------------
filtered_df = df[~(rule1 | rule2)].copy()

print("Removed rows:", len(df) - len(filtered_df))
print("Cleaned size:", len(filtered_df))

# -------------------------
# SAVE CLEAN DATASET
# -------------------------
filtered_df.to_csv(OUTPUT_PATH, index=False)

print("\nSaved cleaned dataset to:", OUTPUT_PATH)

# -------------------------
# NEW DISTRIBUTION CHECK
# -------------------------
print("\nLabel distribution after cleaning:")
print(filtered_df["label"].value_counts(normalize=True))

print("\nRisk distribution after cleaning:")
print(filtered_df["risk_level"].value_counts(normalize=True))