#!/usr/bin/python3
"""
A script that starts Flask web application
"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes the storage on teardown
    """
    storage.close()

@app.route('/hbnb_filters')
def hbnb_filters():
    """
    Display a HTML page with States, Cities, and Amenities
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
