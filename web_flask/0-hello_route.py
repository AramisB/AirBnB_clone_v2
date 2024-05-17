#!/usr/bin/python3
"""
A script that starts Flask web application
"""
from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    """
    A function that returns Hello HBNB
    """
    return ('Hello HBNB!')


if __name__ == "__main__":
    app.run(debug=True)
