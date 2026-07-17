from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import execute, hint, plagiarism, session
from app.core.logger import logger

# Import singletons from the router mapping
from app.routers.plagiarism import _repository, _embedder, _predictor, _embedding_cache

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    logger.info("Starting up EvalFlow Backend...")
    try:
        # Load Predictor
        _predictor._get_model()
        # Load Embedder
        _embedder._get_model()
        # Load Repository and build Embedding Cache
        _embedding_cache.load_cache()
        logger.info("All models and caches loaded successfully.")
    except Exception as e:
        logger.error(f"Startup initialization failed: {e}")
        # Note: We log the error but allow startup to finish, so the /health endpoint can report degradation
    
    yield
    
    # Shutdown actions
    logger.info("Shutting down EvalFlow Backend...")

app = FastAPI(
    title="EvalCode API",
    description="Backend for EvalCode — guided coding environment",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(execute.router, prefix="/execute", tags=["Execution"])
app.include_router(hint.router, prefix="/hint", tags=["EVEE Hinter"])
app.include_router(plagiarism.router, prefix="/api/v1/plagiarism", tags=["Plagiarism"])
app.include_router(session.router, prefix="/session", tags=["Session"])

@app.get("/")
def root():
    return {
        "message": "EvalCode Backend Running"
    }

@app.get("/health")
def health():
    # Check states
    rf_loaded = _predictor._model is not None
    codebert_loaded = _embedder._model is not None
    corpus_loaded = _repository.loaded
    cache_ready = _embedding_cache._loaded
    
    status = "healthy" if (rf_loaded and codebert_loaded and corpus_loaded and cache_ready) else "degraded"
    
    return {
        "status": status,
        "models": {
            "random_forest": "loaded" if rf_loaded else "unavailable",
            "codebert": "loaded" if codebert_loaded else "unavailable"
        },
        "corpus": "loaded" if corpus_loaded else "unavailable",
        "embedding_cache": "ready" if cache_ready else "unavailable"
    }
