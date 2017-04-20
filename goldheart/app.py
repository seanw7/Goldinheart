from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

from goldheart.views.pages import page


def create_app():
    """
    Create a Flask application

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    #app.config.from_object('config.settings')
    #app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)

    return app
