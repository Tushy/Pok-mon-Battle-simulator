import csv
import requests
import json
import os

POKE_TYPES = requests.get('http://pokeapi.co/api/v2/type')  # Vraagt de data aan.
POKE_TYPES_JSON = json.loads(POKE_TYPES.text)  # Decode de JSON data.


def get_types():
    """Een functie voor het ophalen van de data voor de types pokemon, en de types aanvallen. Dit om te controleren of
     een aanval super-effectief, niet effectief, of iets daar tussen in is"""
    type_list = ['steel', 'shadow', 'unknown', 'fairy',
                 'dark']  # Maakt een lijst aan met types die niet in de originele pokémon voor komen
    type_folder = './pokemon/types/'  # Definieert de folder waar de data in moet worden opgeslagen

    for i in POKE_TYPES_JSON['results']:
        type_name = i['name']
        if type_name not in type_list:
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)

            POKE_TYPE = requests.get(i['url'])  # Vraagt de data aan.
            POKE_TYPE_JSON = json.loads(POKE_TYPE.text)  # Decode de JSON data.

            damage_types = {}  # Maakt een lege dict aan om de verschillende effectiviteiten van de aanvallen in op te slaan

            for t in POKE_TYPE_JSON['damage_relations']:
                for i in POKE_TYPE_JSON['damage_relations'][t]:
                    if t == 'half_damage_from' or t == 'double_damage_from' or t == 'no_damage_from':
                        if i['name'] not in type_list:
                            if not t in damage_types:
                                damage_types[t] = [(i['name'])]
                            else:
                                damage_types[t].append(i['name'])

            with open(type_folder + type_name + '.csv',
                      'w') as file:  # Schrijft de data weg naar de verschillende bestanden die corresponderen met de types
                fieldnames = ['double_damage_from', 'half_damage_from', 'no_damage_from']
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()
                writer.writerow(damage_types)


get_types()
