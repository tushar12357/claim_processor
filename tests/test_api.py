import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_process_endpoint():
    # Create a fake PDF file in memory
    fake_pdf = io.BytesIO(b"%PDF-1.4 fake pdf content")

    response = client.post(
        "/api/process",
        data={"claim_id": "test123"},
        files={"file": ("test.pdf", fake_pdf, "application/pdf")},
    )

    assert response.status_code == 200
    data = response.json()

    assert "claim_id" in data
    assert data["claim_id"] == "test123"
    assert "data" in data