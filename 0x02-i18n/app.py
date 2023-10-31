#!/usr/bin/env python3
"""
8-app Module

This module contains the Flask app setup with
Babel configuration and displaying current time.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

import datetime

app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Config class with language configuration.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported
    languages based on request.accept_languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the index.html template with current time."""
    current_time = datetime.datetime.now().strftime(
        '%b %d, %Y, %I:%M:%S %p')
    return render_template(
        'index.html', current_time=_(
        'The current time is %(current_time)s.') % {
            'current_time': current_time})

if __name__ == '__main__':
    app.run()
