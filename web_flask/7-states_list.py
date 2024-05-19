#!/usr/bin/python3
"""
A script that starts Flask web application
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes the storage on teardown
    """
    storage.close()


@app.route('/states_list')
def states_list():
    """
    display a HTML page with the states listed in alphabetical order
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
