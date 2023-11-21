from fastapi.testclient import TestClient
from fastapi import status


def test_read_root(client_mock: TestClient):
    response = client_mock.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "server running"}
