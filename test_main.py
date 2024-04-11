from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_response():
    response = client.post('/scrape', json={"name": "a", "organization_name": "abc"})
    assert response.status_code == 200

def test_get_response():
    response = client.get("/scrape_results/{job_id}", params={"job_id": "a"})
    assert response.status_code == 200
