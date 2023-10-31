#!/usr/bin/env python3
""" Route module for the API - Basic Babel setup """


from flask import Flask, request, render_template
from flask_babel import Babel
from config import Config

app = Flask(__name__)
babel = Babel(app)
# set the above class object as the configuration for the app
app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)