
from flask import jsonify, request
from . import pokemons_blueprint

from app.pokemon import services as pokemon_services


@pokemons_blueprint.route('/pokemons')
def pokemons():
    name = request.args.get('name', None)
    sort_by = request.args.get('sort_by', None)
    order_by = request.args.get('order_by', None)
    # filtered
    if name:
        query = pokemon_services.GetPokemonByNameQuery(name)
        pokemons = query.execute().to_dict()
    # sorted and order
    elif sort_by and order_by:
        if sort_by == 'attack':
            query = pokemon_services.OrderPokemonByAttackQuery()
            pokemons = [record.to_dict() for record in query.execute()]
    else:
        query = pokemon_services.ListPokemonsQuery()
        pokemons = [record.to_dict() for record in query.execute()]

    return jsonify(pokemons)


@pokemons_blueprint.route('/pokemons/<pokemon_id>/', methods=['GET'])
def get_pokemon(pokemon_id: int):
    query = pokemon_services.GetPokemonByIdQuery(id=pokemon_id)
    pokemon = query.execute().to_dict()

    return jsonify(pokemon)
