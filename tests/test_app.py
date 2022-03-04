from tests.conftest import client


def test_should_status_code_ok(client):
    response = client.get('/main')
    assert response.status_code == 200
    assert b'Hello' in response.data

def test_should_return_a_correct_answer(client):
    rv = client.post('/main', data={'text' : "I\'m really bad at this"})
    data = rv.data.decode()
    response = client.get('/main')
    assert response.status_code == 200
    assert '%.7f'%float(data) == '0.0020556'
