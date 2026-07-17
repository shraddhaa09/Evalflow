import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# ======================================
# LOAD DATA
# ======================================

df = pd.read_csv("features_binary.csv")

# ======================================
# FEATURES
# ======================================

FEATURE_COLUMNS = [

    "lines_of_code",
    "avg_line_length",
    "comment_ratio",
    "function_count",
    "loop_count",
    "variable_naming_score",
    "nesting_depth",

    "token_entropy",
    "import_count",
    "try_except_count",
    "comprehension_count",
    "unique_identifier_ratio",
    "ast_node_count"
]

X = df[FEATURE_COLUMNS]

y = df["binary_label"]

# ======================================
# SPLIT
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ======================================
# MODEL
# ======================================

model = RandomForestClassifier(
    n_estimators=500,
    max_depth=16,
    min_samples_split=3,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# ======================================
# PREDICTIONS
# ======================================

y_pred = model.predict(X_test)

# ======================================
# RESULTS
# ======================================

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.4f}")

# ======================================
# FEATURE IMPORTANCE
# ======================================

importance_df = pd.DataFrame({
    "Feature": FEATURE_COLUMNS,
    "Importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE:")
print(importance_df)

# ======================================
# SAVE MODEL
# ======================================

joblib.dump(model, "binary_classifier.pkl")

print("\nbinary_classifier.pkl saved successfully")