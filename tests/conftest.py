import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """
    Returns a fastapi.testclient.TestClient.
    """
    return TestClient(app)
