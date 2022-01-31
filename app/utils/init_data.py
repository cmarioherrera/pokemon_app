import logging
import csv

from app.models import Pokemon


def load_data():
    """Load data to database"""
    with open('pokemon.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file,  delimiter=',')
        for row in csv_reader:
            legendary = row['Legendary']
            Pokemon(
                name=row['Name'],
                type_1=row['Type 1'],
                type_2=row['Type 2'],
                total=int(row['Total']),
                hp=int(row['HP']),
                attack=int(row['Attack']),
                defense=int(row['Defense']),
                sp_atk=int(row['Sp. Atk']),
                sp_def=int(row['Sp. Def']),
                speed=int(row['Speed']),
                generation=int(row['Generation']),
                legendary=1 if legendary == 'True' else 0
            ).save()
