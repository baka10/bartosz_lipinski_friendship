def test_users_api(mocker, app_client):

    resp = app_client.get("/api/users")
    assert resp.status_code == 200
    assert resp.json == {"results": "Endpoint: /api/user GET"}
