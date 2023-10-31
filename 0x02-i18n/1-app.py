#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)  # Config class for app.config
babel = Babel(app)  # Babel instance for babel


@babel.localeselector
def get_locale():
    """ Get locale language """
    return 'en'


@app.route('/')
def index():
    """ Index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
