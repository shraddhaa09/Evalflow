import time
import numpy as np
from app.routers.plagiarism import get_orchestrator, get_repository, get_embedder, get_cache, get_retriever, get_extractor, get_predictor, get_explainer
from app.models.schemas import PlagiarismRequest

def run_benchmark(num_requests=50):
    print("Initializing components for benchmark...")
    
    repo = get_repository()
    emb = get_embedder()
    cache = get_cache(repo, emb)
    ret = get_retriever(repo, cache)
    ext = get_extractor()
    pred = get_predictor()
    expl = get_explainer()
    
    from app.core.config import settings
    orch = get_orchestrator(repo, emb, cache, ret, ext, pred, expl)
    
    print("Warming up models...")
    pred._get_model()
    emb._get_model()
    cache.load_cache()
    
    print(f"Running {num_requests} inference passes...")
    
    latencies = []
    
    payload = PlagiarismRequest(
        assignment_id="assignment_001",
        code="def hello():\n    print('world')",
        typing_speed_wpm=45.0,
        idle_ratio=0.1,
        paste_ratio=0.0,
        tab_switches=2,
        suspicion_score=0.0
    )
    
    for _ in range(num_requests):
        start_t = time.perf_counter()
        res = orch.score_code(payload)
        end_t = time.perf_counter()
        latencies.append((end_t - start_t) * 1000.0)
        
    latencies = np.array(latencies)
    avg_latency = np.mean(latencies)
    p95 = np.percentile(latencies, 95)
    p99 = np.percentile(latencies, 99)
    
    print("\n--- Benchmark Results ---")
    print(f"Requests: {num_requests}")
    print(f"Average Latency: {avg_latency:.2f} ms")
    print(f"P95 Latency:     {p95:.2f} ms")
    print(f"P99 Latency:     {p99:.2f} ms")
    print("-------------------------")

if __name__ == "__main__":
    run_benchmark(50)
