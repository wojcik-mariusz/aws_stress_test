from fastapi.testclient import TestClient
from fastapi import status


def test_get_users_list(client_mock: TestClient):
    response = client_mock.get("/users/all")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "get_all_users"}