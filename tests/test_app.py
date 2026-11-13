from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Cloud DevOps Dashboard" in response.data


def test_status():
    client = app.test_client()
    response = client.get("/api/status")
    assert response.status_code == 200
    assert response.json["status"] == "Running"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "Healthy"


def test_metrics():
    client = app.test_client()
    client.get("/health")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"http_requests_total" in response.data
    assert b"http_request_duration_seconds" in response.data
