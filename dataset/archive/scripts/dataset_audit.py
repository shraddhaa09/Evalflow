import joblib

for name in ["plagiarism_model.pkl", "plagiarism_model_v2.pkl", "plagiarism_model_v3.pkl"]:
    model = joblib.load(f"dataset/{name}")
    print(name)
    print("  n_features_in_:", getattr(model, "n_features_in_", "unknown"))
    print("  feature_names_in_:", getattr(model, "feature_names_in_", "not stored"))
    print("  type:", type(model))