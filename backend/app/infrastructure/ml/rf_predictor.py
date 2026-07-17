from typing import Any
import joblib
from app.domain.interfaces.predictor import IPredictor
from app.core.config import settings
from app.core.logger import logger
from app.domain.exceptions import ModelUnavailableException

class RandomForestPredictor(IPredictor):
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RandomForestPredictor, cls).__new__(cls)
        return cls._instance

    def _get_model(self):
        if self._model is None:
            try:
                self._model = joblib.load(settings.model_path)
                logger.info(f"Successfully loaded RF model from {settings.model_path}")
            except Exception as e:
                logger.error(f"Failed to load RF model from {settings.model_path}: {e}")
                raise ModelUnavailableException(f"RF model unavailable: {e}")
        return self._model

    def predict_proba(self, features: Any) -> float:
        model = self._get_model()
        return float(model.predict_proba(features)[0][1])
