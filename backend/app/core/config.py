from pydantic_settings import BaseSettings
import os
from pathlib import Path

class Settings(BaseSettings):
    plagiarism_top_k: int = 5
    plagiarism_high_risk_threshold: float = 0.85
    plagiarism_medium_risk_threshold: float = 0.60
    
    # Path to models and data relative to backend/
    base_dir: Path = Path(__file__).resolve().parent.parent.parent
    dataset_dir: Path = base_dir.parent / "dataset"
    
    model_path: str = str(dataset_dir / "models" / "plagiarism_model_v3.pkl")
    submissions_csv_path: str = str(dataset_dir / "data" / "raw" / "submissions.csv")
    telemetry_csv_path: str = str(dataset_dir / "data" / "raw" / "telemetry.csv")
    semantic_model_id: str = "microsoft/codebert-base"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
