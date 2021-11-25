from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_invalid():
    response = client.get("/invalid")
    assert response.status_code == 200