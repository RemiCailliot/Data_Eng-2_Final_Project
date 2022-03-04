from tests.conftest import client
from detoxify import Detoxify

def test_function_toxicity(client):
    predictor = Detoxify('original')
    text = "I\'m really bad at this"
    processed_text = text.lower()
    results = predictor.predict(processed_text)
    assert '%.7f'%float(str(results['toxicity'])) == '0.0020556'
