from flask import Flask
from flask_jwt_extended import JWTManager

from flasgger import Swagger


template = {
    "swagger": "2.0",
    "info": {
        "title": "Title",
        "description": "Pokemon API v1",
        "version": "1.0.0"
    },
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        }
    },
}

swagger = Swagger(template=template)
jwt = JWTManager()


def create_app(config_filename=None):
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Pokemon API v1',
    }
    app.config["JWT_SECRET_KEY"] = "super-secret"

    swagger.init_app(app)
    jwt.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.pokemon.routes import pokemons_blueprint
    app.register_blueprint(pokemons_blueprint, url_prefix='/api/v1')
    from app.auth.routes import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1')
