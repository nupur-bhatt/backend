import helpers
from flask import Flask
from flask import json

app = Flask(__name__)


@app.route('/')
def hello():
    out = helpers.RandomNumberGenerator(0, 100)
    result = out.generate_sequence(30)
    output = tuple(result)
    response = app.response_class(response=json.dumps(output), status=200, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run()
