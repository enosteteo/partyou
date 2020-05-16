from django.test import Client


def test_status_code(client: Client):
    resp = client.get('/store/')
    assert resp.status_code == 200
