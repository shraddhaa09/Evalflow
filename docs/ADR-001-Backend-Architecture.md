# ADR-001: Backend Architecture for Modular Pluggable Inference

**Date**: 2026-07-17  
**Status**: Accepted  
**Context**: The EvalFlow plagiarism detection backend originally featured a monolithic inference pipeline where API endpoints, data fetching, feature extraction, and ML prediction were tightly coupled. As the project transitions from a research prototype to a stable, production-ready system suitable for future algorithmic experimentation and scalable deployment, a more robust architectural foundation is required.

## 1. Why this architecture was chosen

We adopted a **Domain-Driven Design (DDD)** approach with strict adherence to **Dependency Inversion** and **SOLID principles**.

- **Separation of Concerns**: By splitting responsibilities into `CandidateRetriever`, `FeatureExtractor`, `Predictor`, and `ExplanationEngine`, we ensure that each component only handles a single axis of change.
- **Pluggability**: Concrete infrastructure implementations (e.g., `RandomForestPredictor`, `CSVSubmissionRepository`) implement domain interfaces. This means we can hot-swap storage engines or ML models without touching the core orchestration logic.
- **Top-K Retrieval Strategy**: The architecture explicitly limits `O(N)` scaling issues by retrieving a small subset of candidate submissions prior to heavy feature extraction and prediction, paving the way for optimized vector search engines like FAISS.
- **Reusability of Expensive Compute**: The `EmbeddingProvider` computes the CodeBERT embedding immediately upon receiving the submission. This vector is shared downstream with both the Candidate Retriever and the Feature Extractor, preventing redundant GPU/CPU cycles.
- **Explainability**: The response explicitly models an explanation layer, keeping black-box prediction isolated from human-readable UI interpretation.

## 2. Alternatives considered

1. **Tight Coupling (Legacy approach)**
   - *Pros*: Faster to initially write, less boilerplate.
   - *Cons*: Impossible to test components in isolation. Any change to the model architecture forces changes to the API endpoints and feature engineering code. Poor scalability.

2. **Microservices (RPC/gRPC between Extraction, Retrieval, and Inference)**
   - *Pros*: Independent scaling of heavy ML inference nodes vs lightweight API nodes.
   - *Cons*: Significant operational overhead for a system of this current scale. Introduces network latency and complex deployment topologies.
   
*Decision*: A modular monolith provides the internal decoupling needed for clean code while avoiding the operational tax of microservices.

## 3. Trade-offs

- **Increased Boilerplate**: Introducing interfaces and distinct domain/infrastructure folders means more files and structural code compared to a simple procedural script.
- **Dependency Injection Overhead**: The API router must instantiate multiple infrastructure services and wire them manually (or via FastAPI's `Depends`), which adds slight initialization complexity.

## 4. Component Responsibilities

- **`InferenceOrchestrator` (Service)**: Coordinates the flow of execution. Ignorant of HTTP or specific algorithms.
- **`IEmbeddingProvider`**: Generates high-dimensional vector representations of code.
- **`ICandidateRetriever`**: Given an assignment and an embedding, identifies the most suspicious `K` submissions to compare against.
- **`IFeatureExtractor`**: Compares the target submission against retrieved candidates to build the pairwise feature matrix.
- **`IPredictor`**: Wraps the ML model to predict probabilities based on the feature matrix.
- **`IExplanationEngine`**: Translates probabilities and raw feature importance into actionable, human-readable risk signals.
- **`ISubmissionRepository`**: Abstracts the underlying storage for submissions (e.g., CSV, Postgres).

## 5. Dependency Graph

```text
                API (Router)
                 │ (Dependency Injection)
                 ▼
      Inference Orchestrator
                 │
     ┌───────────┼────────────┐
     │           │            │
     ▼           ▼            ▼
Embedding    Candidate    Submission
Provider     Retriever    Repository
     │            │            │
     └──────┬─────┘            │
            ▼                  │
      Feature Extractor ◄──────┘
            │
            ▼
        Predictor
            │
            ▼
     Explanation Engine
            │
            ▼
        API Response
```

## 6. Future Extensibility

- **Vector Search**: The `ICandidateRetriever` can be swapped from a simple `O(N)` loop to a `FAISS` or `Pinecone` implementation.
- **Ensemble Models**: The `IPredictor` can be easily substituted with a `VotingPredictor` combining Random Forest, XGBoost, and LightGBM.
- **Advanced Explainability**: The `IExplanationEngine` interface allows integration with SHAP or LIME libraries in the future without disrupting API contracts.
- **Database Migration**: The `CSVSubmissionRepository` can be replaced with a `PostgresSubmissionRepository` transparently.
