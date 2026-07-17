"""Shared model-loading errors for plagiarism detection."""

class ModelLoadError(RuntimeError):
    """Raised when a required ML model cannot be loaded or verified."""


class EmbeddingError(ModelLoadError):
    """Raised when semantic embeddings cannot be computed."""
