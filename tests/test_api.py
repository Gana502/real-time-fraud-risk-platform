from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_score_transaction():

    transaction = {
        "transaction_id": "TXN001",
        "customer_id": "CUST001",
        "amount": 1500,
        "merchant": "Amazon",
        "country": "US",
        "transaction_time": "2026-06-17T10:00:00Z",
        "channel": "mobile",
        "device_id": "DEV001",
        "is_new_device": True
    }

    response = client.post(
        "/score-transaction",
        json=transaction
    )

    assert response.status_code == 200
    assert response.json()["risk_band"] == "HIGH"