def test_static_root(client):
    response = client.get("/")
    assert response.status_code == 200
