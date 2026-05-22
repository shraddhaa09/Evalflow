import os
import pickle
import numpy as np
from pathlib import Path
from app.models.schemas import PlagiarismLabel

MODEL_PATH = Path(os.getenv("PKL_MODEL_PATH", "app/models/classifier.pkl"))

_model = None


def load_model():
    """
    Load ML model once. Fail fast if corrupted or incompatible.
    """
    global _model

    if _model is not None:
        return _model

    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at: {MODEL_PATH}")

    try:
        with open(MODEL_PATH, "rb") as f:
            _model = pickle.load(f)
    except Exception as e:
        raise RuntimeError(
            f"Failed to load ML model. Possible version mismatch or corrupted pickle. Error: {str(e)}"
        )

    return _model


# ─────────────────────────────────────────────
# FEATURE ENGINEERING (MATCHES YOUR TRAINING STYLE)
# ─────────────────────────────────────────────

def extract_features(code: str) -> np.ndarray:
    lines = code.splitlines()
    non_empty = [l for l in lines if l.strip()]

    total_lines = len(lines)

    avg_line_len = np.mean([len(l) for l in non_empty]) if non_empty else 0
    std_line_len = np.std([len(l) for l in non_empty]) if non_empty else 0

    indent = [len(l) - len(l.lstrip()) for l in non_empty]
    indent_std = np.std(indent) if indent else 0

    comment_lines = sum(1 for l in lines if l.strip().startswith("#"))
    comment_ratio = comment_lines / max(total_lines, 1)

    tokens = code.split()
    unique_ratio = len(set(tokens)) / max(len(tokens), 1)

    blank_ratio = sum(1 for l in lines if not l.strip()) / max(total_lines, 1)

    keywords = ["for", "while", "if", "else", "def", "return", "import", "class"]
    kw_density = sum(code.count(k) for k in keywords) / max(len(tokens), 1)

    features = np.array([
        total_lines,
        avg_line_len,
        std_line_len,
        indent_std,
        comment_ratio,
        unique_ratio,
        blank_ratio,
        kw_density,
    ], dtype=float).reshape(1, -1)

    return features


# ─────────────────────────────────────────────
# LABELING
# ─────────────────────────────────────────────

def get_label(prob: float) -> PlagiarismLabel:
    if prob >= 0.70:
        return PlagiarismLabel.likely_ai
    elif prob >= 0.45:
        return PlagiarismLabel.possibly_ai
    return PlagiarismLabel.likely_human


def build_signals(prob: float, code: str) -> list[str]:
    signals = []

    lines = code.splitlines()
    non_empty = [l for l in lines if l.strip()]

    if non_empty:
        indent = [len(l) - len(l.lstrip()) for l in non_empty]
        if np.std(indent) < 1.5:
            signals.append("Highly uniform indentation")

        avg_len = np.mean([len(l) for l in non_empty])
        if avg_len > 45:
            signals.append("Long consistent line structure")

    if "def " in code and "return" not in code:
        signals.append("Function structure incomplete (AI-like pattern)")

    if code.count("\n") > 20 and len(set(code.split())) < 15:
        signals.append("Low vocabulary diversity")

    if not signals:
        signals.append("No strong AI indicators detected")

    return signals


# ─────────────────────────────────────────────
# MAIN SCORING FUNCTION
# ─────────────────────────────────────────────

def score_code(code: str):
    model = load_model()
    features = extract_features(code)

    try:
        proba = model.predict_proba(features)[0]
        ai_prob = float(proba[1])
        confidence = float(max(proba))

    except Exception as e:
        raise RuntimeError(f"Model prediction failed: {str(e)}")

    label = get_label(ai_prob)
    signals = build_signals(ai_prob, code)

    return round(ai_prob, 4), label, round(confidence, 4), signals