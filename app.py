import requests
import json
import csv
import os
from random import randint
from urllib import request


def list_of_pokemon():
    "Haal alle pokemon namen en url's op."
    while 1:
        if os.path.isfile('pokemon_list.csv'):
            with open('pokemon_list.csv', 'r') as f:
                r = csv.DictReader(f, delimiter=';')
                lst_of_pokemon = []
                for i in r:
                    lst_of_pokemon.append({'number': i['number'], 'name': i['name'], 'url': i['url']})
            break

        else:
            POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
            POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
            base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

            base += '?limit=151'  # Limit van 151 pokemon (dit is een extensie van de website URL)

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

    return lst_of_pokemon


def gotta_catch_em_all(x):
    "Algemene functie voor alles wat met de pokémon te maken heeft. Stats en moves."
    for i in list_of_pokemon():
        if x == i['name']:
            STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
            pokemon_stats = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
    print(pokemon_stats['sprites']['front_default'])
    # Functie voor de eerste pokémon. Als deze al bestaat wordt de database gebruikt, anders wordt er een nieuwe entry gemaakt
    bestandsnaam = './pokemon/%s/'
    if not os.path.exists(bestandsnaam % x):  # kijkt of de input al bestaat in de map ./pokemon/
        os.makedirs('./pokemon/%s/' % x)
        with open('./pokemon/%s/stats.csv' % x, encoding='utf-8',
                  mode='w') as file:  # Als deze niet bestaat wordt dit aangemaakt
            for i in list_of_pokemon():
                if x == i['name']:
                    naam = (i['name'])  # Zet de naam van de pokémon om in een variabele
                    fieldnames = ['name', 'type', 'speed', 'special_defense', 'special_attack', 'defense', 'attack',
                                  'hp']  # definieert de veldnamen voor het .csv bestand
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
                    writer.writeheader()

                    t = []  # Maakt een lijst aan voor de types
                    stats = {}  # Maakt een dictionary aan voor de stats
                    for i in pokemon_stats['types']:  # Voegt de verschillende types toe aan de lijst t
                        t.append(i['type']['name'])

                    for i in pokemon_stats[
                        'stats']:  # Voegt de verschillende stats met bijbehorende naam toe aan de dict met key=naam value=waarde van stat
                        stats.update({(i['stat']['name']): (i['base_stat'])})
                    writer.writerow(
                        {'name': naam, 'type': t, 'speed': stats['speed'],
                         'special_defense': stats['special-defense'],
                         'special_attack': stats['special-attack'], 'defense': stats['defense'],
                         'attack': stats['attack'], 'hp': stats['hp']})  # schrijft de waardes naar het bestand
                    #  request.urlretrieve(pokemon_stats['sprites']['front_default'], './pokemon/%s/' + x + '.jpg')
    # Haalt de moves op uit het JSON bestand en maakt een lijst met 4 dicts voor de moves
    for i in list_of_pokemon():
        if x == i['name']:
            h = 0
            lst = []
            while h < 4:
                r = randint(0, len(pokemon_stats['moves']) - 1)
                if r not in lst:
                    lst.append(r)
                    h += 1
                else:
                    pass
            c = 0
            moves_list = []
            while c < 4:
                m = pokemon_stats['moves'][lst[c]]
                MOVE = requests.get(m['move']['url'])  # Vraagt een nieuwe URL aan.
                MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.
                move_name1 = m['move']['name']
                move_type1 = MOVE_JSON['type']['name']
                move_accuracy1 = MOVE_JSON['accuracy']
                move_power1 = MOVE_JSON['power']
                c += 1
                moves_list.append(
                    {'attack_name': move_name1, 'attack_type': move_type1, 'attack_accuracy': move_accuracy1,
                     'attack_power': move_power1})
    return moves_list


print(gotta_catch_em_all('magikarp'))
