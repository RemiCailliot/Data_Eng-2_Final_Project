from flask import Flask, request, render_template
import pandas as pd
from detoxify import Detoxify

def create_app(test_config=None):
    app = Flask(__name__)
    predictor = Detoxify('original')
    @app.route('/main')
    def my_form():
        return render_template('my-form.html')
    @app.route('/main', methods=['POST'])
    def my_form_post():
        text = request.form['text']
        processed_text = text.lower()
        results = predictor.predict(processed_text)
        return '%.7f'%float(str(results['toxicity']))
    if __name__ =='__main__':
        app.run(host='0.0.0.0',port=5000)
    return app
create_app()

