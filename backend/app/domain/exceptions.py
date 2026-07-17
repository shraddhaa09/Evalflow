class ModelUnavailableException(Exception):
    """Raised when an ML model fails to load or is unavailable."""
    pass

class CorpusUnavailableException(Exception):
    """Raised when the repository corpus cannot be loaded."""
    pass

class CandidateNotFoundException(Exception):
    """Raised when no suitable candidates are found for comparison."""
    pass

class InferenceError(Exception):
    """Raised when feature extraction or model prediction fails during inference."""
    pass
