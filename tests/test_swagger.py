import pytest


@pytest.mark.parametrize("route", ["/api", "/api/docs", "/api/openapi.json"])
def test_swagger(client, route):
    """
    Test that the swagger ui, redoc and openapi json are available.
    """

    response = client.get(route)
    print(f"GET {route} {response}\n\n{response.content}")

    assert response.status_code == 200
