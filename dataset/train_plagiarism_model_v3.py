import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

df = pd.read_csv("metadata/training_pairs_v3.csv")

features = [
    # CODE FEATURES (UPGRADED IMPORTANCE)
    "token_similarity",
    "line_similarity",
    "length_similarity",
    "structure_similarity",
    "semantic_similarity",

    # TELEMETRY (rebalanced weight naturally)
    "typing_speed_gap",
    "idle_ratio_gap",
    "paste_ratio_gap",
    "tab_switch_gap",
    "suspicion_gap"
]

X = df[features]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=350,
    max_depth=16,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))

importances = pd.Series(model.feature_importances_, index=features)
print("\nFEATURE IMPORTANCE:")
print(importances.sort_values(ascending=False))

joblib.dump(model, "plagiarism_model_v3.pkl")

print("\nSaved: plagiarism_model_v3.pkl")
