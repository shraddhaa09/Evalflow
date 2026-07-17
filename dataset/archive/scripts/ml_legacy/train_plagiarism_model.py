import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import joblib

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("metadata/training_pairs_clean.csv")

# =========================
# FEATURES (IMPORTANT)
# =========================

feature_cols = [
    "token_similarity",
    "line_similarity",
    "length_similarity",
    "typing_speed_gap",
    "idle_ratio_gap",
    "paste_ratio_gap",
    "tab_switch_gap",
    "suspicion_gap"
]

X = df[feature_cols]
y = df["label"]

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# MODEL (START SIMPLE)
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# =========================
# EVALUATION
# =========================

y_pred = model.predict(X_test)

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))

# =========================
# FEATURE IMPORTANCE
# =========================

importances = pd.Series(
    model.feature_importances_,
    index=feature_cols
).sort_values(ascending=False)

print("\nFEATURE IMPORTANCE:")
print(importances)

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "plagiarism_model.pkl")

print("\nModel saved as plagiarism_model.pkl")