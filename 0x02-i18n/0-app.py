#!/usr/bin/env python3
"""
0-app Module

This module contains the basic Flask app setup.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
