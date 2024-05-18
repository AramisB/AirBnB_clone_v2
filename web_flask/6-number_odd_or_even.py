#!/usr/bin/python3
"""
A script that starts Flask web application
"""
from flask import Flask, abort, render_template, redirect

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.route('/')
def hello():
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


@app.route('/c/<text>')
def c(text):
    """
    A function that displays C followed by text input
    """
    text_with_spaces = text.replace('_', ' ')
    return f"C {text_with_spaces}"


@app.route('/python/', defaults={'text': 'is_cool'},)
@app.route('/python/<text>')
def python(text):
    """
    A function that displays Python followed by text input
    default text input is "is fun"
    """
    text_with_spaces = text.replace('_', ' ')
    return f"Python {text_with_spaces}"


@app.route('/number/<int:n>')
def number(n):
    """
    A function that displays a number only if it's an integer
    """
    return redirect(f"/number_template/{n}")


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    A function that displays a HTML page only n is an integer
    """
    return render_template('5-number.html', n=n)
    

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    A function that displays a HTML page only n is an integer
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
