import os
import sqlite3
from app.utils.init_data import load_data


def create_table():
    conn = sqlite3.connect(os.getenv('DATABASE_NAME', 'pokemon.db'))

    conn.execute(
        "CREATE TABLE IF NOT EXISTS pokemons (id INTEGER PRIMARY KEY AUTOINCREMENT, \
        name TEXT, type_1 TEXT, type_2 TEXT, total INTEGER, hp INTEGER, attack INTEGER, \
        defense INTEGER, sp_atk INTEGER, sp_def INTEGER, speed INTEGER, \
        generation INTEGER, legendary BOOLEAN CHECK (legendary IN (0, 1)))"
    )

    conn.close()


if __name__ == '__main__':
    create_table()
    load_data()
