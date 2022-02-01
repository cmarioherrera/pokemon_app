import os
import sqlite3

from typing import List
from dataclasses import dataclass, field


@dataclass
class Pokemon:
    name: str
    type_1: str
    type_2: str
    total: int
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int
    generation: int
    legendary: int
    id: int = field(default=None)

    def to_dict(self):
        return self.__dict__

    def save(self) -> None:
        with sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db')) as con:
            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO pokemons (name, type_1, type_2, total, hp, \
                attack, defense, sp_atk, sp_def, speed, generation, \
                legendary) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (self.name, self.type_1, self.type_2, self.total,
                 self.hp, self.attack, self.defense, self.sp_atk,
                 self.sp_def, self.speed, self.generation, self.legendary)
            )
            con.commit()

        return self

    @classmethod
    def get_pokemons(cls) -> List:
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM pokemons")

        records = cur.fetchall()
        pokemons = [cls(**record) for record in records]
        con.close()

        return pokemons

    @classmethod
    def get_pokemon_by_id(cls, pokemon_id: int):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db'))
        con.row_factory = sqlite3.Row

        cursor = con.cursor()
        cursor.execute("SELECT * FROM pokemons WHERE id = ?", (pokemon_id,))

        record = cursor.fetchone()

        pokemon = cls(** record)
        con.close()

        return pokemon

    @classmethod
    def get_pokemon_by_name(cls, name: str):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db'))
        con.row_factory = sqlite3.Row

        cursor = con.cursor()
        cursor.execute("SELECT * FROM pokemons WHERE name = ?", (name,))

        record = cursor.fetchone()

        pokemon = cls(** record)
        con.close()

        return pokemon

    @classmethod
    def order_pokemon_by_attack(cls):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM pokemons ORDER BY attack ASC;")

        records = cur.fetchall()
        pokemons = [cls(**record) for record in records]
        con.close()

        return pokemons
