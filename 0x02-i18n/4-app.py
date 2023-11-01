#!/usr/bin/env python3
""" force a particular locale with locale=fr parameter
    in the URL
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Select a language translation to use """
    req = request.args.get('locale')
    if req in app.config['LANGUAGES']:
        return req
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ GET /
    Return: 4-index.html
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
