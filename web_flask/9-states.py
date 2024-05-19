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


@app.route('/states')
@app.route('/states/<state_id>')
def states(state_id=None):
    """
    display the states and cities listed in alphabetical order
    """
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
