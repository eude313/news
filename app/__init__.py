# from .request import configure_request
from flask import Flask
from config import config_options
#creating app configuration

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #registering the blueprint
    from .main import main as blue_print
    app.register_blueprint(blue_print)

    #Setting up configuration
    from .request import configure_request
    configure_request(app)


    return app