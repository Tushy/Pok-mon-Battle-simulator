import requests
import json
import csv
import os
from random import randint
from urllib import request
from damage_calc import damage_type_calculator


def list_of_pokemon():
    "Haal alle pokemon namen en url's op."
    while 1:
        if os.path.isfile(
                './pokemon/pokemon_list.csv'):  # Controlleer of er al een bestand bestaat dat pokemon_list.csv heet
            with open('./pokemon/pokemon_list.csv',
                      'r') as f:  # Als het bestand al bestaat, voeg de data dan toe aan een lijst.
                reader = csv.DictReader(f, delimiter=';')
                lst_of_pokemon = []
                pokemon_names = []
                for item in reader:
                    lst_of_pokemon.append({'number': item['number'], 'name': item['name'], 'url': item['url']})
                    pokemon_names.append(item['name'])
            break

        else:
            POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
            POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
            base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

            base += '?limit=151'  # Limit van 151 pokemon (dit is een extensie van de website URL)

            pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
            pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.

            os.makedirs('./pokemon/')
            with open('./pokemon/pokemon_list.csv',
                      'w') as f:  # Als het bestand nog niet bestaat, maak deze dan aan en vul het met data
                fieldnames = ['number', 'name', 'url']
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')

                writer.writeheader()  # Schrijf de headers boven de rows
                number = 1  # Pokémon beginnen met tellen op nummer 1
                for item in pokemon_json['results']:  # Voeg de data toe aan het bestand met de volgende format
                    writer.writerow({'number': '{0:03}'.format(number), 'name': item['name'], 'url': item['url']})
                    number += 1

    return lst_of_pokemon, pokemon_names  # Zodat de data gebruikt kan worden in verdere functies en programma's


def gotta_catch_em_all(pokemon):
    "Algemene functie voor alles wat met de pokémon te maken heeft. Stats en moves."
    for item in list_of_pokemon()[0]:
        if pokemon == item['name']:
            STATS = requests.get(item['url'])  # Vraagt een nieuwe URL aan.
            pokemon_stats = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
    # Functie voor de pokémon. Als deze al bestaat wordt de database gebruikt, anders wordt er een nieuwe entry gemaakt
    bestandsnaam = './pokemon/%s/' % pokemon
    if not os.path.exists(bestandsnaam):  # kijkt of de input al bestaat in de map ./pokemon/
        os.makedirs(bestandsnaam)
        with open(bestandsnaam + 'stats.csv', encoding='utf-8',
                  mode='w') as file:  # Als deze niet bestaat wordt dit aangemaakt
            for item in list_of_pokemon()[0]:
                if pokemon == item['name']:
                    naam = (item['name'])  # Zet de naam van de pokémon om in een variabele
                    fieldnames = ['name', 'type', 'speed', 'special_defense', 'special_attack', 'defense', 'attack',
                                  'hp']  # definieert de veldnamen voor het .csv bestand
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
                    writer.writeheader()

                    type_list = []  # Maakt een lijst aan voor de types
                    stats = {}  # Maakt een dictionary aan voor de stats
                    for item in pokemon_stats['types']:  # Voegt de verschillende types toe aan de lijst t
                        type_list.append(item['type']['name'])

                    for item in pokemon_stats[
                        'stats']:  # Voegt de verschillende stats met bijbehorende naam toe aan de dict met key=naam value=waarde van stat
                        stats.update({(item['stat']['name']): (item['base_stat'])})
                    writer.writerow(
                        {'name': naam, 'type': type_list, 'speed': stats['speed'],
                         'special_defense': stats['special-defense'],
                         'special_attack': stats['special-attack'], 'defense': stats['defense'],
                         'attack': stats['attack'], 'hp': stats['hp']})  # schrijft de waardes naar het bestand
                    request.urlretrieve(pokemon_stats['sprites']['front_default'], bestandsnaam + pokemon + '.png')
    # Haalt de moves op uit het JSON bestand en maakt een lijst met 4 dicts voor de moves
    for item in list_of_pokemon()[0]:
        if pokemon == item['name']:
            counter = 0  # Teller
            teller = 0  # nieuwe teller
            random_lijst = []  # Lijst voor het opslaan van random gegenereerde getallen
            moves_list = []  # een lijst voor de moves
            while counter < 4:
                cijfer = randint(0, len(pokemon_stats['moves']) - 1)  # genereer een getal die tussen de 0 en de lengte
                #  van de lijst met moves voor de geselecteerde pokémon
                if cijfer not in random_lijst:  # controlleerd of het gegenereerde cijfer reeds is opgenomen in de lijst
                    random_lijst.append(cijfer)  # zo niet wordt het getal toegevoegd
                    counter += 1  # tel één bij de teller
                else:  # Als het getal al wel in de lijst voorkomt wordt het append gedeelte overgeslagen en wordt er opnieuw gegenereerd
                    pass

            while teller < 4:
                move = pokemon_stats['moves'][random_lijst[teller]]  # Kijkt in de lijst met moves en zoekt daar de
                #  entry van het random getal op de index plaats van de teller
                MOVE = requests.get(move['move']['url'])  # Vraagt een nieuwe URL aan.
                MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.
                move_name1 = move['move']['name']  # zet de naam van de move in een variabele
                move_type1 = MOVE_JSON['type']['name']  # zet het type van de move in een variabele
                move_accuracy1 = MOVE_JSON['accuracy']  # zet de accuracy van de move in een variabele
                move_power1 = MOVE_JSON['power']  # zet de power van de move in een variabele
                teller += 1  # tel één bij de teller
                moves_list.append(
                    {'attack_name': move_name1, 'attack_type': move_type1, 'attack_accuracy': move_accuracy1,
                     'attack_power': move_power1})  # Voeg alle zojuist gemaakte variabele toe aan een dictionary met de keys die hierbij staan
    return moves_list


def read_stats(pokemon):
    'Geeft een lijst terug met een dict daarin. Dit bevat alle stats uit het .csv bestand en returned deze voor berekeningen'
    with open('./pokemon/%s/stats.csv' % pokemon, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        stats_dict = []  # lege lijst voor de dict
        for row in reader:
            stats_dict.append(row)

    return stats_dict
