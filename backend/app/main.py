from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import execute, hint, plagiarism, session

app = FastAPI(
    title="EvalCode API",
    description="Backend for EvalCode — guided coding environment",
    version="1.0.0",
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
app.include_router(plagiarism.router, prefix="/plagiarism", tags=["Plagiarism"])
app.include_router(session.router, prefix="/session", tags=["Session"])


@app.get("/")
def root():
    return {
        "message": "EvalCode Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "EvalCode API"
    }