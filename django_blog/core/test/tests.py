def test_get(client):
    request = client.get('/')
    assert request.status_code == 200