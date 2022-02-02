from typing import List
from dataclasses import dataclass

from app.models import Pokemon


class ListPokemonsQuery():

    def execute(self) -> List[Pokemon]:
        pokemons = Pokemon.get_pokemons()

        return pokemons


@dataclass
class GetPokemonByNameQuery():
    name: str

    def execute(self) -> Pokemon:
        pokemon = Pokemon.get_pokemon_by_name(self.name)

        return pokemon


@dataclass
class GetPokemonByIdQuery():
    id: int

    def execute(self) -> Pokemon:
        pokemon = Pokemon.get_pokemon_by_id(self.id)

        return pokemon


class OrderAscPokemonByAttackQuery():

    def execute(self) -> List[Pokemon]:
        pokemons = Pokemon.order_asc_pokemons_by_attack()

        return pokemons


class OrderDescPokemonByAttackQuery():

    def execute(self) -> List[Pokemon]:
        pokemons = Pokemon.order_desc_pokemons_by_attack()

        return pokemons
