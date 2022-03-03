from tests.conftest import client
import time
def test_requests_per_minute(client):
    start_time = time.time()
    for k in range (0,100):
        response = client.get('/main')
    assert (time.time() - start_time) <= 60