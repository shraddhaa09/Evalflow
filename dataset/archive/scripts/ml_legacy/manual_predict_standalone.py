import re
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# =========================
# LOAD MODEL
# =========================

model = joblib.load("plagiarism_model_v3.pkl")

# =========================
# LOAD SEMANTIC MODEL
# =========================

semantic_model = SentenceTransformer("microsoft/codebert-base")

# =========================
# READ FILES
# =========================

with open("manual_test/code_a3.py", "r", encoding="utf-8") as f:
    code_a = f.read()

with open("manual_test/code_b3.py", "r", encoding="utf-8") as f:
    code_b = f.read()

# =========================
# TOKENIZATION
# =========================

def tokenize(code):
    return re.findall(r'\b\w+\b', code.lower())

# =========================
# BASIC FEATURES
# =========================

def jaccard(a, b):
    A, B = set(tokenize(a)), set(tokenize(b))
    return len(A & B) / len(A | B)

def line_similarity(a, b):
    A = set([x.strip() for x in a.splitlines() if x.strip()])
    B = set([x.strip() for x in b.splitlines() if x.strip()])
    return len(A & B) / len(A | B)

def length_similarity(a, b):
    return min(len(a), len(b)) / max(len(a), len(b))

# =========================
# STRUCTURE SIMILARITY
# =========================

def structure_features(code):
    return {
        "for": len(re.findall(r'\bfor\b', code)),
        "while": len(re.findall(r'\bwhile\b', code)),
        "if": len(re.findall(r'\bif\b', code)),
        "def": len(re.findall(r'\bdef\b', code)),
    }

def structure_similarity(a, b):
    A, B = structure_features(a), structure_features(b)

    score = 0
    total = 0

    for k in A:
        score += min(A[k], B[k])
        total += max(A[k], B[k]) + 1e-5

    return score / total

# =========================
# SEMANTIC SIMILARITY
# =========================

emb_a = semantic_model.encode(code_a)
emb_b = semantic_model.encode(code_b)

semantic_similarity = cosine_similarity(
    [emb_a],
    [emb_b]
)[0][0]

# =========================
# TELEMETRY PLACEHOLDERS
# =========================
# Real system will fetch these from DB

typing_speed_gap = 0.2
idle_ratio_gap = 0.1
paste_ratio_gap = 0.8
tab_switch_gap = 2
suspicion_gap = 0.7

# =========================
# BUILD FEATURE VECTOR
# =========================

features = np.array([[
    jaccard(code_a, code_b),
    line_similarity(code_a, code_b),
    length_similarity(code_a, code_b),
    structure_similarity(code_a, code_b),
    semantic_similarity,
    typing_speed_gap,
    idle_ratio_gap,
    paste_ratio_gap,
    tab_switch_gap,
    suspicion_gap
]])

# =========================
# PREDICT
# =========================

ml_probability = model.predict_proba(features)[0][1]

# --------------------------------
# PRECOMPUTED SCORES
# --------------------------------

token_sim = jaccard(code_a, code_b)
line_sim = line_similarity(code_a, code_b)
length_sim = length_similarity(code_a, code_b)
structure_sim = structure_similarity(code_a, code_b)

# --------------------------------
# STRONG PLAGIARISM SIGNAL
# --------------------------------

strong_code_match = (
    semantic_similarity > 0.97 and
    (
        token_sim > 0.45 or
        structure_sim > 0.85 or
        line_sim > 0.30
    )
)

# --------------------------------
# BEHAVIORAL SUSPICION
# --------------------------------

behavior_match = (
    paste_ratio_gap > 0.6 or
    suspicion_gap > 0.6
)

# --------------------------------
# FINAL DECISION ENGINE
# --------------------------------

if strong_code_match and behavior_match:
    prediction = 1
    plag_prob = max(ml_probability, 0.95)

elif strong_code_match:
    prediction = 1
    plag_prob = max(ml_probability, 0.80)

elif ml_probability > 0.60:
    prediction = 1
    plag_prob = ml_probability

else:
    prediction = 0
    plag_prob = ml_probability

# =========================
# RISK ENGINE
# =========================

if plag_prob >= 0.85:
    risk = "HIGH"
elif plag_prob >= 0.60:
    risk = "MEDIUM"
else:
    risk = "LOW"

# =========================
# OUTPUT
# =========================

print("\n" + "="*60)

print("PLAGIARISM ANALYSIS RESULT")

print("="*60)

print(f"\nPrediction       : {'PLAGIARIZED' if prediction == 1 else 'CLEAN'}")
print(f"Probability      : {plag_prob:.4f}")
print(f"Risk Level       : {risk}")

print("\nFEATURE BREAKDOWN")
print("-"*60)

print(f"Token Similarity     : {jaccard(code_a, code_b):.4f}")
print(f"Line Similarity      : {line_similarity(code_a, code_b):.4f}")
print(f"Length Similarity    : {length_similarity(code_a, code_b):.4f}")
print(f"Structure Similarity : {structure_similarity(code_a, code_b):.4f}")
print(f"Semantic Similarity  : {semantic_similarity:.4f}")

print("\n" + "="*60)