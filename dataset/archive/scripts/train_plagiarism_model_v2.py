import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import joblib

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("metadata/training_pairs_v2.csv")

# =========================
# FEATURES (HYBRID MODEL)
# =========================

features = [
    # code similarity
    "token_similarity",
    "line_similarity",
    "length_similarity",
    "structure_similarity",

    # telemetry
    "typing_speed_gap",
    "idle_ratio_gap",
    "paste_ratio_gap",
    "tab_switch_gap",
    "suspicion_gap"
]

X = df[features]
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
# MODEL (BETTER VERSION)
# =========================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    class_weight="balanced",
    random_state=42
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

importances = pd.Series(model.feature_importances_, index=features)
print("\nFEATURE IMPORTANCE:")
print(importances.sort_values(ascending=False))

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "plagiarism_model_v2.pkl")

print("\nSaved: plagiarism_model_v2.pkl")