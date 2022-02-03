
from flask import request
from . import pokemons_blueprint
from flask_jwt_extended import jwt_required

from app.response import response, not_found
from app.pokemon import services as pokemon_services


@pokemons_blueprint.route('/pokemons')
@jwt_required()
def pokemons():
    """Return list of pokemons and filter and sort pokemon.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: Bulbasaur
        description: Get a pokemon for a given name

      - name: sort_by
        in: query
        type: string
        required: false
        enum: ['attack']
        default: all
        description: sort a pokemon by attack
      - name: order_by
        in: query
        type: string
        enum: ['desc', 'asc', '']
        required: false
        default: all
        description: Order by
    definitions:
      Pokemon:
        type: object
        properties:
          data:
            type: array
            items:
              $ref: '#/definitions/Pokemon'
    security:
      - Bearer: []
    responses:
      200:
        description: A list of pokemons (may be filtered by name)
        schema:
          $ref: '#/definitions/Pokemon'
    """
    name = request.args.get('name', None)
    sort_by = request.args.get('sort_by', None)
    order_by = request.args.get('order_by', None)

    # filtered
    if name:
        query = pokemon_services.GetPokemonByNameQuery(name)
        pokemons = query.execute()
        if pokemons is None:
            return not_found()
        return response(pokemons.to_dict())
    # sorted
    elif sort_by and order_by:
        if sort_by == 'attack' and order_by == 'desc':
            query = pokemon_services.OrderDescPokemonByAttackQuery()
            pokemons = [record.to_dict() for record in query.execute()]
        elif sort_by == 'attack' and order_by == 'asc':
            query = pokemon_services.OrderAscPokemonByAttackQuery()
            pokemons = [record.to_dict() for record in query.execute()]
        else:
            return not_found()
    else:
        query = pokemon_services.ListPokemonsQuery()
        pokemons = [record.to_dict() for record in query.execute()]

    return response(pokemons)
