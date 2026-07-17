# EvalFlow - AI-Assisted Python Coding Platform

EvalFlow is an AI-assisted coding platform designed to help learners improve programming skills through interactive coding, AI-generated hints, and personalized programming assistance.

The platform combines a web-based coding environment with AI capabilities to provide contextual programming guidance, coding workflows, and learning support.

---

## Features

- Interactive Python coding environment
- AI-powered programming hints using Google Gemini API
- Real-time code execution workflow
- Session-based learning experience
- AI-authorship analysis support
- REST API-based backend architecture
- Modular frontend and backend structure

---

## Tech Stack

### Frontend
- React
- TypeScript
- CSS

### Backend
- Python
- FastAPI
- Pydantic
- REST APIs

### AI Integration
- Google Gemini API

### Development Tools
- Git
- GitHub
- VS Code

---

# System Architecture

```
                    User
                      |
                      v
              React Frontend
                      |
                      v
              FastAPI Backend
                      |
          +-----------+-----------+
          |                       |
          v                       v
 Code Execution Workflow     Gemini API
          |
          v
 Learning Session Data
```

---

# My Contributions

I contributed to the backend development and AI integration workflows of EvalFlow.

## Backend Development

- Developed and modified FastAPI backend components for platform functionality.
- Implemented REST API workflows for communication between frontend and backend services.
- Added Pydantic-based request validation to improve API reliability.
- Improved backend organization using modular service components.

## AI Integration

- Integrated Google Gemini API workflows for contextual programming assistance.
- Worked on AI-generated programming hints to improve the learning experience.

## Debugging and Collaboration

- Debugged backend issues and improved application reliability.
- Collaborated with team members using Git-based development workflows.
- Participated in feature discussions and code improvements.

---

# Project Structure

```
EvalFlow/
│
├── backend/
│   ├── API endpoints
│   ├── Backend services
│   ├── Models
│   └── Configuration
│
├── frontend/
│   ├── React components
│   ├── UI logic
│   └── Client-side workflows
│
├── dataset/
│   ├── pipeline/              # canonical plagiarism training scripts
│   ├── data/raw/              # submissions, telemetry, labels
│   ├── data/processed/        # training pair CSVs
│   └── models/                # plagiarism_model_v3.pkl + evaluation
├── docs/
│   ├── ARCHITECTURE.md        # system design (training / inference / backend)
│   └── PAPER.md               # technical summary for reporting
├── ML/                        # deprecated — see ML/README.md
│
├── package.json
├── package-lock.json
└── README.md
```

---

# Plagiarism Detection (ML)

EvalFlow includes a pairwise plagiarism classifier trained on code similarity and telemetry features.

## Pipelines

| Layer | Location | Purpose |
|-------|----------|---------|
| **Training** | `dataset/pipeline/` | Offline scripts `01`→`04` to build features, train, and evaluate |
| **Inference** | `backend/app/services/` | Runtime feature extraction + `predict_proba()` |
| **Backend API** | `POST /plagiarism`, `GET /health` | Serves scores; fails explicitly if models are unavailable |

Full diagrams and component tables: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)  
Reporting summary: [docs/PAPER.md](docs/PAPER.md)

## Train or re-evaluate the model

```bash
cd dataset/pipeline
pip install pandas scikit-learn joblib sentence-transformers
python 01_generate_pairs.py
python 02_extract_semantics.py
python 03_train_model.py
python 04_evaluate_model.py
```

Metrics are saved under `dataset/models/evaluation/`. Model version and split metadata are in `dataset/models/plagiarism_model_v3.manifest.json`.

---

# Installation and Setup

## 1. Clone Repository

```bash
git clone https://github.com/shraddhaa09/Evalflow.git

cd Evalflow
```

---

# Backend Setup

Navigate to backend directory:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Backend will run at:

```
http://localhost:8000
```

API documentation:

```
http://localhost:8000/docs
```

---

# Frontend Setup

Open a new terminal.

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

# Environment Variables

Create a `.env` file according to your project configuration.

Example:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit API keys or sensitive credentials to GitHub.

---

# API Overview

EvalFlow uses REST APIs for communication between frontend and backend.

Major backend responsibilities:

- User interaction workflows
- Code processing
- AI hint generation
- Session management
- Request validation

---

# Development Practices

The project follows software engineering practices including:

- Modular backend architecture
- REST API design
- Version control using Git
- Code debugging and validation
- Collaborative development workflow

---

# Future Improvements

- Add automated testing coverage
- Improve learning analytics dashboard
- Expand AI feedback capabilities
- Support additional programming languages
- Improve deployment workflow

---

# Acknowledgements

This project was developed as a collaborative software engineering project.

Original repository:

https://github.com/SharwillKhisti/EvalCode

---

# License

This project is developed for educational and learning purposes.
