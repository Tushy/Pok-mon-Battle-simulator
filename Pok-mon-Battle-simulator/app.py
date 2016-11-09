import requests
import json
import csv
import os
from random import randint

POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

base += '?limit=151'  # Limit van 151 pokemon (dit is een extensie van de website URL)

pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.


def list_of_pokemon():
    'Haalt een lijst op met alle pokémon namen en bijbehorende IDs'
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


def pokemon(x):
    'Functie voor de eerste pokémon. Als deze al bestaat wordt de database gebruikt, anders wordt er een nieuwe entry gemaakt'
    inputerino = x
    if not os.path.exists('./pokemon/%s/stats.csv' % inputerino):  # kijkt of de input al bestaat in de map ./pokemon/
        os.makedirs('./pokemon/%s/' % inputerino)
        with open('./pokemon/%s/stats.csv' % inputerino, encoding='utf-8',
                  mode='w') as file:  # Als deze niet bestaat wordt dit aangemaakt
            for i in pokemon_json['results']:
                if inputerino == i['name']:
                    naam = (i['name'])  # Zet de naam van de pokémon om in een variabele
                    fieldnames = ['name', 'type', 'speed', 'special_defense', 'special_attack', 'defense', 'attack',
                                  'hp']  # definieert de veldnamen voor het .csv bestand
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
                    writer.writeheader()
                    STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
                    STATS_JSON = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
                    t = []  # Maakt een lijst aan voor de types
                    stats = {}  # Maakt een dictionary aan voor de stats
                    for i in STATS_JSON['types']:  # Voegt de verschillende types toe aan de lijst t
                        t.append(i['type']['name'])
                    for i in STATS_JSON[
                        'stats']:  # Voegt de verschillende stats met bijbehorende naam toe aan de dict met key=naam value=waarde van stat
                        stats.update({(i['stat']['name']): (i['base_stat'])})
                    writer.writerow(
                        {'name': naam, 'type': t, 'speed': stats['speed'], 'special_defense': stats['special-defense'],
                         'special_attack': stats['special-attack'], 'defense': stats['defense'],
                         'attack': stats['attack'], 'hp': stats['hp']})  # schrijft de waardes naar het bestand
                    moves(inputerino)
    else:
        moves(inputerino)


def moves(x):
    inputerino = x
    for i in pokemon_json['results']:
        if inputerino == i['name']:
            STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
            STATS_JSON = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
            with open('./pokemon/%s/moves.csv' % inputerino, encoding='utf-8', mode='w') as file2:
                veldnamen = ['attack_name', 'attack_type', 'attack_accuracy', 'attack_power']
                schrijver = csv.DictWriter(file2, fieldnames=veldnamen, delimiter=';', lineterminator='\n')
                schrijver.writeheader()
                h = 0
                lst = []
                while h < 4:
                    r = randint(0, len(STATS_JSON['moves']) - 1)
                    r = randint(0, len(STATS_JSON['moves']))
                    if r not in lst:
                        lst.append(r)
                        h += 1
                    else:
                        pass
                c = 0
                while c < 1:
                    m = STATS_JSON['moves'][c]
                    MOVE = requests.get(m['move']['url'])  # Vraagt een nieuwe URL aan.
                    MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.
                    move_name1 = m['move']['name']
                    move_type1 = MOVE_JSON['type']['name']
                    move_accuracy1 = MOVE_JSON['accuracy']
                    move_power1 = MOVE_JSON['power']
                    c += 1
                    schrijver.writerow(
                        {'attack_name': move_name1, 'attack_type': move_type1, 'attack_accuracy': move_accuracy1,
                         'attack_power': move_power1})
                print(lst)
                while c < 4:
                    m = STATS_JSON['moves'][lst[c]]
                    MOVE = requests.get(m['move']['url'])  # Vraagt een nieuwe URL aan.
                    MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.
                    move_name1 = m['move']['name']
                    move_type1 = MOVE_JSON['type']['name']
                    move_accuracy1 = MOVE_JSON['accuracy']
                    move_power1 = MOVE_JSON['power']
                    c += 1
                    schrijver.writerow(
                        {'attack_name': move_name1, 'attack_type': move_type1, 'attack_accuracy': move_accuracy1,
                         'attack_power': move_power1})


inputerino = input('Stats van pokemon één: ').lower()
list_of_pokemon()
print(pokemon(inputerino))
print(30 * '*' + '\n' + 12 * '-' + 'Fight!' + 12 * '-' + '\n' + 30 * '*')
