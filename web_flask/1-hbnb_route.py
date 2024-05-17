#!/usr/bin/python3
"""
A script that starts Flask web application
"""
from flask import Flask

app = Flask(__name__)
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    A function that returns HBNB
    """
    return ('HBNB')


if __name__ == "__main__":
    app.run(debug=True)
