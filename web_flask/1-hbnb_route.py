#!/usr/bin/python3
"""
A script that starts Flask web application
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    A function that returns "Hello HBNB!"
    """
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """
    A function that returns HBNB
    """
    return ('HBNB')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
