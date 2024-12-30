from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)


def test_read_main():
    # Test type spam
    response = client.get("/check?message=SIX chances to win CASH!")
    assert response.status_code == 200
    assert response.json() == {"message": "SIX chances to win CASH!", "classification": "spam"}

    # Test type ham
    response = client.get("/check?message=Hello, world, my name is Fred")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world, my name is Fred", "classification": "ham"}
