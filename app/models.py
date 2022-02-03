import os
import sqlite3

from typing import List, Tuple
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
        return cls._get_by_query("SELECT * FROM pokemons")

    @classmethod
    def get_pokemon_by_id(cls, pokemon_id: int):
        return cls._get_by_attribute(
            "SELECT * FROM pokemons WHERE id = ?",
            (pokemon_id,)
        )

    @classmethod
    def get_pokemon_by_name(cls, name: str):
        return cls._get_by_attribute(
            "SELECT * FROM pokemons WHERE name = ?",
            (name,)
        )

    @classmethod
    def order_asc_pokemons_by_attack(cls):
        return cls._get_by_query("SELECT * FROM pokemons ORDER BY attack ASC;")

    @classmethod
    def order_desc_pokemons_by_attack(cls):
        return cls._get_by_query("SELECT * FROM pokemons ORDER BY attack DESC;")

    @classmethod
    def _get_by_attribute(cls, sql_query: str, query_values: Tuple):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db'))
        con.row_factory = sqlite3.Row

        cursor = con.cursor()
        cursor.execute(sql_query, query_values)

        record = cursor.fetchone()

        if record is None:
            return None

        data = cls(** record)
        con.close()

        return data

    @classmethod
    def _get_by_query(cls, sql_query: str):
        con = sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db'))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute(sql_query)

        records = cur.fetchall()
        data = [cls(**record) for record in records]
        con.close()

        return data


@dataclass
class User:
    id: str
    username: str
    password: str

    def __str__(self) -> str:
        return self.id
