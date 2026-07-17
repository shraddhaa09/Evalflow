from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "models" in data
    assert "corpus" in data
    assert "embedding_cache" in data

def test_plagiarism_empty_code():
    payload = {
        "assignment_id": "test_assign",
        "code": "   "
    }
    response = client.post("/api/v1/plagiarism", json=payload)
    assert response.status_code == 400
    assert "Code empty" in response.text
