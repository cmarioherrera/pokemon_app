from flask import Blueprint
pokemons_blueprint = Blueprint('pokemons', __name__)

from . import routes
