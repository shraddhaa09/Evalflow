# Deprecated — use `dataset/pipeline/`

These scripts are archived copies of the old `ML/dataset/` training workflow.

| Legacy script | Replacement |
|---------------|-------------|
| `generate_training_pairs_v2.py` | `dataset/pipeline/01_generate_pairs.py` |
| `code_semantic_features.py` | `dataset/pipeline/02_extract_semantics.py` |
| `train_plagiarism_model_v3.py` | `dataset/pipeline/03_train_model.py` |
| `test_model.py` | `dataset/pipeline/04_evaluate_model.py` |
| `manual_predict.py` | `backend/test_plagiarism.py` or `/plagiarism` API |

Do not modify these files. Update `dataset/pipeline/` instead.
