import helpers
from flask import Flask
from flask import json

app = Flask(__name__)

# Enter parameters to generate a list of random numbers

min_value=0;
max_value=100;
length=30;

@app.route('/')
def hello():
    out = helpers.RandomNumberGenerator(min_value, max_value)
    result = out.generate_sequence(length)
    output = tuple(result)
    response = app.response_class(response=json.dumps(output), status=200, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run()
