import helpers
from flask import Flask
from flask import json

app = Flask(__name__)


@app.route('/')
def hello():
    out = helpers.RandomNumberGenerator(0, 30)
    result = out.generate_sequence(15)
    output = tuple(result)
    response = app.response_class(response=json.dumps(output), status=200, mimetype='application/json')
    return response

