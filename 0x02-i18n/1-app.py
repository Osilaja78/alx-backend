#!/usr/bin/env python3
"""0-app.py module, a simple Flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

LANGUAGES = ['en', 'fr']


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns the hello world template"""

    return render_template('0-index.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
