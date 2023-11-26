import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client_mock():
    with TestClient(app) as client:
        yield client
