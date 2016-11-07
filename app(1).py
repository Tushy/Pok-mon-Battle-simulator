import requests
import json
import csv

POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

base += '?limit=151'  # Limit van 151 pokemon (dit is een extensie van de website URL)

pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.

inputerino1 = input('Stats van welke pokemon: ').lower()
inputerino2 = input('Stats van welke pokemon: ').lower()
with open('pokemon1.csv', encoding='utf-8', mode='w') as file1:
    for i in pokemon_json['results']:
        if inputerino1 == i['name']:
            naam = (i['name'])
            print(i['name'])
            fieldnames = ['naam', 'type', 'speed', 'special-defence', 'special-attack', 'defense', 'attack', 'hp']
            writer = csv.DictWriter(file1, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
            STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
            STATS_JSON = json.loads(STATS.text)  # Decode de data in de nieuwe URL.

            t = []
            stats = {}
            for i in STATS_JSON['types']:
                t.append(i['type']['name'])
            print('Type is: ' + ', '.join(t))
            for i in STATS_JSON['stats']:
                print('{:<15} : {:<10}'.format(i['stat']['name'], i['base_stat']))
                stats.update({(i['stat']['name']): (i['base_stat'])})
            writer.writerow({'naam': naam, 'type': t, 'speed': stats['speed']})
        elif inputerino1 == 'quit':
            check = False


for i in pokemon_json['results']:
    if inputerino2 == i['name']:
        print(i['name'])

        STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
        STATS_JSON = json.loads(STATS.text)  # Decode de data in de nieuwe URL.

        t = []
        for i in STATS_JSON['types']:
            t.append(i['type']['name'])
        print('Type is: ' + ', '.join(t))
        for i in STATS_JSON['stats']:
            print('{:<15} : {:<10}'.format(i['stat']['name'], i['base_stat']))
        break
    elif inputerino2 == 'quit':
        check = False

print(30*'*' + '\n' + 12*'-' + 'Fight!' + 12*'-' + '\n' + 30*'*')
