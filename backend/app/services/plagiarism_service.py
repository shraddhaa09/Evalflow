import os
import re
import pickle
import numpy as np
from pathlib import Path
from app.models.schemas import PlagiarismLabel

# ── Load model once at startup ──────────────────────────────
MODEL_PATH = Path(os.getenv("PKL_MODEL_PATH", "model/classifier.pkl"))

_model = None

def load_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"PKL model not found at {MODEL_PATH}. "
                "Set PKL_MODEL_PATH env var or place file at model/classifier.pkl"
            )
        with open(MODEL_PATH, "rb") as f:
            _model = pickle.load(f)
    return _model


# ── Feature extraction ──────────────────────────────────────
def extract_features(code: str) -> np.ndarray:
    """
    Extract a feature vector from raw source code.
    Adjust these to match the features your .pkl model was trained on.
    """
    lines = code.splitlines()
    non_empty = [l for l in lines if l.strip()]

    # Basic structural features
    total_lines       = len(lines)
    avg_line_length   = np.mean([len(l) for l in non_empty]) if non_empty else 0
    std_line_length   = np.std([len(l) for l in non_empty]) if non_empty else 0

    # Indentation regularity (AI code tends to be very uniform)
    indent_levels     = [len(l) - len(l.lstrip()) for l in non_empty]
    indent_std        = np.std(indent_levels) if indent_levels else 0

    # Comment density
    comment_lines     = sum(1 for l in lines if l.strip().startswith("#"))
    comment_ratio     = comment_lines / max(total_lines, 1)

    # Docstring presence
    has_docstring     = int('"""' in code or "'''" in code)

    # Token-level features
    tokens            = re.findall(r'\w+', code)
    unique_ratio      = len(set(tokens)) / max(len(tokens), 1)
    avg_token_length  = np.mean([len(t) for t in tokens]) if tokens else 0

    # Blank line ratio (AI often spaces neatly)
    blank_lines       = sum(1 for l in lines if not l.strip())
    blank_ratio       = blank_lines / max(total_lines, 1)

    # Keyword density
    keywords = ['def', 'class', 'return', 'import', 'for', 'while', 'if', 'else', 'try', 'except']
    kw_count  = sum(code.count(kw) for kw in keywords)
    kw_density = kw_count / max(len(tokens), 1)

    features = np.array([
        total_lines,
        avg_line_length,
        std_line_length,
        indent_std,
        comment_ratio,
        has_docstring,
        unique_ratio,
        avg_token_length,
        blank_ratio,
        kw_density,
    ], dtype=float).reshape(1, -1)

    return features


def build_signals(ai_probability: float, code: str) -> list[str]:
    """Return human-readable explanation flags for the UI."""
    signals = []
    lines   = code.splitlines()
    non_empty = [l for l in lines if l.strip()]

    indent_levels = [len(l) - len(l.lstrip()) for l in non_empty]
    if np.std(indent_levels) < 1.5:
        signals.append("High indentation regularity")

    avg_len = np.mean([len(l) for l in non_empty]) if non_empty else 0
    if avg_len > 45:
        signals.append("Consistently long line lengths")

    blank_ratio = sum(1 for l in lines if not l.strip()) / max(len(lines), 1)
    if blank_ratio > 0.25:
        signals.append("Excessive blank line spacing")

    if '"""' in code or "'''" in code:
        signals.append("Auto-generated docstrings detected")

    tokens      = re.findall(r'\w+', code)
    unique_ratio = len(set(tokens)) / max(len(tokens), 1)
    if unique_ratio < 0.4:
        signals.append("Low vocabulary diversity")

    if not signals:
        signals.append("No strong AI patterns detected")

    return signals


# ── Main scoring function ───────────────────────────────────
def score_code(code: str) -> tuple[float, PlagiarismLabel, float, list[str]]:
    """Returns (ai_probability, label, confidence, signals)."""
    model    = load_model()
    features = extract_features(code)

    # Probability of class 1 (AI-generated)
    proba       = model.predict_proba(features)[0]
    ai_prob     = float(proba[1])
    confidence  = float(max(proba))

    if ai_prob >= 0.70:
        label = PlagiarismLabel.likely_ai
    elif ai_prob >= 0.45:
        label = PlagiarismLabel.possibly_ai
    else:
        label = PlagiarismLabel.likely_human

    signals = build_signals(ai_prob, code)
    return round(ai_prob, 4), label, round(confidence, 4), signals
