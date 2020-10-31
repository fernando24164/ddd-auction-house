from flask import Flask

from .api.config import config_by_name
from .api.v1.views import api_v1


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(api_v1)

    return app
