from flask import Flask


def create_app(config_filename=None):
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.pokemon.routes import pokemons_blueprint
    app.register_blueprint(pokemons_blueprint, url_prefix='/api/v1')
