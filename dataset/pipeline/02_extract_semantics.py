"""Step 2: Add CodeBERT semantic similarity to pairwise training data."""
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from _paths import (
    SEMANTIC_MODEL_ID,
    TRAINING_PAIRS_V2,
    TRAINING_PAIRS_V3,
)


def embed(model: SentenceTransformer, code: str):
    return model.encode(str(code))


def main() -> None:
    model = SentenceTransformer(SEMANTIC_MODEL_ID)
    df = pd.read_csv(TRAINING_PAIRS_V2)

    semantic_scores = []
    for _, row in df.iterrows():
        emb_a = embed(model, row["code_a"])
        emb_b = embed(model, row["code_b"])
        semantic_scores.append(cosine_similarity([emb_a], [emb_b])[0][0])

    df["semantic_similarity"] = semantic_scores
    df.to_csv(TRAINING_PAIRS_V3, index=False)
    print(f"Saved {TRAINING_PAIRS_V3} with semantic similarity")


if __name__ == "__main__":
    main()
