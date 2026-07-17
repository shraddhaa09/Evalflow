import pandas as pd
import re

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("metadata/training_pairs_clean.csv")

# =========================
# BASIC TOKENIZER
# =========================

def tokenize(code):
    return re.findall(r'\b\w+\b', str(code).lower())

# =========================
# N-GRAM SIMILARITY (NEW)
# =========================

def ngram_similarity(a, b, n=3):
    a_tokens = tokenize(a)
    b_tokens = tokenize(b)

    a_ngrams = set(zip(*[a_tokens[i:] for i in range(n)])) if len(a_tokens) >= n else set()
    b_ngrams = set(zip(*[b_tokens[i:] for i in range(n)])) if len(b_tokens) >= n else set()

    if not a_ngrams and not b_ngrams:
        return 1.0

    return len(a_ngrams & b_ngrams) / len(a_ngrams | b_ngrams)

# =========================
# AST-LIKE STRUCTURE SIMULATION (FAST V1)
# =========================

def pseudo_ast_signature(code):
    """
    Lightweight structural signature:
    - loop patterns
    - condition patterns
    - function usage
    """
    code = str(code)

    features = {
        "for_loops": len(re.findall(r'\bfor\b', code)),
        "while_loops": len(re.findall(r'\bwhile\b', code)),
        "ifs": len(re.findall(r'\bif\b', code)),
        "functions": len(re.findall(r'\bdef\b', code)),
    }

    return features

# =========================
# STRUCTURE SIMILARITY
# =========================

def structure_similarity(a, b):
    fa = pseudo_ast_signature(a)
    fb = pseudo_ast_signature(b)

    score = 0
    total = 0

    for k in fa:
        maxv = max(fa[k], fb[k])
        diff = abs(fa[k] - fb[k])
        score += (maxv - diff)
        total += maxv + 1e-5

    return round(score / total, 4)

# =========================
# FEATURE ENGINEERING
# =========================

print("Enhancing dataset...")

df["ngram_similarity"] = df.apply(
    lambda r: ngram_similarity(r.get("code_a", ""), r.get("code_b", "")),
    axis=1
)

df["structure_similarity"] = df.apply(
    lambda r: structure_similarity(r.get("code_a", ""), r.get("code_b", "")),
    axis=1
)

# fallback if code not present in dataset
df["ngram_similarity"] = df["ngram_similarity"].fillna(0)
df["structure_similarity"] = df["structure_similarity"].fillna(0)

# =========================
# SAVE UPDATED DATASET
# =========================

df.to_csv("metadata/training_pairs_enhanced.csv", index=False)

print("Saved: training_pairs_enhanced.csv")