from fastapi.testclient import TestClient
from app.app import app

def test_health_endpoint_returns_ok():
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"ok": True}