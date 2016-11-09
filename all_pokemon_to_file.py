import requests
import json
import csv
import os




def list_of_pokemon():
    while 1:
        if not os.path.isfile('pokemon_list.csv'):
            POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
            POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
            base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie
            base += '?limit=151'  # Limit van aantal pokemon (dit is een extensie van de website URL)
            pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
            pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.

            with open('pokemon_list.csv', 'w') as f:
                fieldnames = ['number', 'name', 'url']
                w = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')

                w.writeheader()
                number = 1
                for i in pokemon_json['results']:
                    w.writerow({'number': '{0:03}'.format(number), 'name': i['name'], 'url': i['url']})
                    number += 1
def get_pokemons():
    get_pokemons_list = []
    with open('pokemon_list.csv', 'r') as f:
        r = csv.DictReader(f, delimiter=';')
        for i in r:
            get_pokemons_list.append(i['name'])
    return get_pokemons_list


