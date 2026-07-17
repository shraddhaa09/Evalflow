import pandas as pd

df = pd.read_csv("metadata/training_pairs.csv")

print("\nTOTAL ROWS:", len(df))

print("\nLABEL DISTRIBUTION:")
print(df["label"].value_counts(normalize=True))

print("\nRISK DISTRIBUTION:")
print(df["risk_level"].value_counts(normalize=True))

print("\nSIMILARITY STATS:")
print(df["token_similarity"].describe())

print("\nHIGH SIMILARITY BUT LABEL=0 CHECK:")
print(
    df[(df["token_similarity"] > 0.8) & (df["label"] == 0)].shape
)

print("\nLOW SIMILARITY BUT LABEL=1 CHECK:")
print(
    df[(df["token_similarity"] < 0.3) & (df["label"] == 1)].shape
)