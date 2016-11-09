import requests
import json
import csv
import os

POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

base += '?limit=20'  # Limit van 20 pokemon (dit is een extensie van de website URL)

pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.


def list_of_pokemon():
    while 1:
        if os.path.isfile('pokemon_list.csv'):
            with open('pokemon_list.csv', 'r') as f:
                r = csv.DictReader(f, delimiter=';')
                lst_of_pokemon = []
                for i in r:
                    lst_of_pokemon.append((i['number'] + ' ' + i['name'].capitalize()))
            break

        else:
            with open('pokemon_list.csv', 'w') as f:
                fieldnames = ['number', 'name']
                w = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';', lineterminator='\n')

                w.writeheader()
                number = 1
                for i in pokemon_json['results']:
                    w.writerow({'number': '{0:03}'.format(number), 'name': i['name']})
                    number += 1

    return lst_of_pokemon

print(list_of_pokemon())
