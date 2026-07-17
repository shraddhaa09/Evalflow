import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Lightweight model (fast + good enough for v1)
model = SentenceTransformer("microsoft/codebert-base")

df = pd.read_csv("metadata/training_pairs_v2.csv")

# -------------------------
# EMBEDDING FUNCTION
# -------------------------

def embed(code):
    return model.encode(str(code))

# -------------------------
# COMPUTE SEMANTIC SIMILARITY
# -------------------------

semantic_scores = []

for _, row in df.iterrows():
    emb_a = embed(row["code_a"])
    emb_b = embed(row["code_b"])

    score = cosine_similarity([emb_a], [emb_b])[0][0]
    semantic_scores.append(score)

df["semantic_similarity"] = semantic_scores

# -------------------------
# SAVE UPDATED DATASET
# -------------------------

df.to_csv("metadata/training_pairs_v3.csv", index=False)

print("Saved training_pairs_v3.csv with semantic similarity")