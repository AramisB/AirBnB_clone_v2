#!/usr/bin/python3
"""
A script that starts Flask web application
"""
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    """
    A function that returns "Hello HBNB!"
    """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    A function that returns HBNB
    """
    return ('HBNB')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
