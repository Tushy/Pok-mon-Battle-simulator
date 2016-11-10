import csv
import requests
import json
import os

POKE_TYPES = requests.get('http://pokeapi.co/api/v2/type')  # Vraagt de data aan.
POKE_TYPES_JSON = json.loads(POKE_TYPES.text)  # Decode de JSON data.


def get_types():
    lst = ['steel', 'shadow', 'unknown', 'fairy', 'dark']
    type_folder = './pokemon/types/'

    for i in POKE_TYPES_JSON['results']:
        type_name = i['name']
        if type_name not in lst:
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)

            POKE_TYPE = requests.get(i['url'])  # Vraagt de data aan.
            POKE_TYPE_JSON = json.loads(POKE_TYPE.text)  # Decode de JSON data.

            damage_types = {}

            for t in POKE_TYPE_JSON['damage_relations']:
                for i in POKE_TYPE_JSON['damage_relations'][t]:
                    if t == 'half_damage_from' or t == 'double_damage_from' or t == 'no_damage_from':
                        if i['name'] not in lst:
                            if not t in damage_types:
                                damage_types[t] = [(i['name'])]
                            else:
                                damage_types[t].append(i['name'])

            with open(type_folder + type_name + '.csv', 'w') as f:
                fieldnames = ['double_damage_from', 'half_damage_from', 'no_damage_from']
                w = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
                w.writeheader()
                w.writerow(damage_types)
