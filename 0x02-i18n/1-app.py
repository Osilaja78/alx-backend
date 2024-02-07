#!/usr/bin/env python3
"""0-app.py module, a simple Flask app"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """babel config class"""

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns the hello world template"""

    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
