from flask import Flask
from flasgger import Swagger

swagger = Swagger()


def create_app(config_filename=None):
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Pokemon API v1',
        'uiversion': 3
    }

    swagger.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.pokemon.routes import pokemons_blueprint
    app.register_blueprint(pokemons_blueprint, url_prefix='/api/v1')
