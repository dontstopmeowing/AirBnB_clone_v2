#!/usr/bin/python3
"""This module contains functions that starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Route /states/stateID"""
    items = storage.all(State).values()
    if id is not None:
        items = storage.all(State).get("State.{}".format(id))
    return render_template('9-states.html', states=items, id=id)


@app.teardown_appcontext
def storage_close(self):
    """After each request is done,
        the current SQLAlchemy Session will be closed/removed.
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
