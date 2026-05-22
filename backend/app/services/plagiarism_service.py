from pathlib import Path
import joblib
import numpy as np

from app.models.feature_extractor import extract_features
from app.models.schemas import PlagiarismLabel


# ===============================
# LOAD MODEL
# ===============================

MODEL_PATH = Path(
    "app/models/binary_classifier.pkl"
)

model = None


def load_model():
    global model

    if model is None:
        model = joblib.load(MODEL_PATH)

    return model


# ===============================
# SIGNAL GENERATOR
# ===============================

def build_signals(features):

    signals = []

    if features[0][6] > 6:
        signals.append("Deep nesting detected")

    if features[0][7] > 3:
        signals.append("High token regularity")

    if features[0][5] > 0.6:
        signals.append("Structured naming style")

    if not signals:
        signals.append("No strong AI indicators")

    return signals


# ===============================
# MAIN SCORING
# ===============================

def score_code(code):

    clf = load_model()

    features = extract_features(code)

    proba = clf.predict_proba(features)[0]

    ai_probability = float(proba[1])

    confidence = float(max(proba))

    if ai_probability >= 0.75:
        label = PlagiarismLabel.likely_ai

    elif ai_probability >= 0.45:
        label = PlagiarismLabel.possibly_ai

    else:
        label = PlagiarismLabel.likely_human

    signals = build_signals(features)

    return (
        round(ai_probability, 4),
        label,
        round(confidence, 4),
        signals
    )