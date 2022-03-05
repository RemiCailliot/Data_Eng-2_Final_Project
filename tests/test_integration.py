from tests.conftest import client

def test_requests_per_minute(client):
    rv = client.post('/main', data={'text' : "I\'m really bad at this"})
    response = client.get('/main')
    assert response.status_code ==200
    assert '%.7f'%float(rv.data.decode()) == "0.0020556"