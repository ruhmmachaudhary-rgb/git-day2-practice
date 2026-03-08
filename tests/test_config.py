def test_config_does_not_expose_api_key(client):
    r = client.get("/config")
    assert r.status_code == 200
    data = r.json()
    assert "app_name" in data
    assert "environment" in data
    assert "api_key" not in data