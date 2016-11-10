import requests
import json
import csv
import os
from random import randint
from urllib import request


def list_of_pokemon():
    "Haal alle pokemon namen en url's op."
    while 1:
        if os.path.isfile(
                './pokemon/pokemon_list.csv'):  # Controlleer of er al een bestand bestaat dat pokemon_list.csv heet
            with open('./pokemon/pokemon_list.csv',
                      'r') as f:  # Als het bestand al bestaat, voeg de data dan toe aan een lijst.
                r = csv.DictReader(f, delimiter=';')
                lst_of_pokemon = []
                pokemon_names = []
                for i in r:
                    lst_of_pokemon.append({'number': i['number'], 'name': i['name'], 'url': i['url']})
                    pokemon_names.append(i['name'])
            break

        else:
            POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
            POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
            base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

            base += '?limit=151'  # Limit van 151 pokemon (dit is een extensie van de website URL)

            pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
            pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.

            with open('./pokemon/pokemon_list.csv',
                      'w') as f:  # Als het bestand nog niet bestaat, maak deze dan aan en vul het met data
                fieldnames = ['number', 'name', 'url']
                w = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')

                w.writeheader()  # Schrijf de headers boven de rows
                number = 1  # Pokémon beginnen met tellen op nummer 1
                for i in pokemon_json['results']:  # Voeg de data toe aan het bestand met de volgende format
                    w.writerow({'number': '{0:03}'.format(number), 'name': i['name'], 'url': i['url']})
                    number += 1

    return lst_of_pokemon, pokemon_names  # Zodat de data gebruikt kan worden in verdere functies en programma's


def gotta_catch_em_all(x):  # x is hier de input van het dropdown menu in het interface
    "Algemene functie voor bijna alles wat met de pokémon te maken heeft. Stats en moves voornamelijk."
    for pokemon in list_of_pokemon()[0]:  # refereerd terug naar de bovenstaande functie
        if x == pokemon['name']:
            STATS = requests.get(pokemon['url'])  # Vraagt een nieuwe URL aan.
            pokemon_stats = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
    # Functie voor de pokémon. Als deze al een map heeft wordt de database gebruikt, anders wordt er een nieuwe map...
    # gemaakt, en de data toegevoegd in een .csv bestand met de naam van de betreffende pokémon. Hier wordt ook de
    # sprite van de pokémon opgehaald (en omgezet van .png(want dat werkt niet op mac) naar .jpg)

    bestandsnaam = './pokemon/%s/' % x  # Variabele om sneller de locatie van de mappen te vinden en aan te maken...
    #  mocht dit nodig zijn

    if not os.path.exists(bestandsnaam):  # controlleert of er al een map is voor de pokémon
        os.makedirs(bestandsnaam)  # Zo niet wordt er een map aangemaakt
        with open(bestandsnaam + 'stats.csv', encoding='utf-8',
                  mode='w') as file:  # Hier wordt er een nieuw .csv bestand aangemaakt voor de stats van de pokémon
            for pokemon in list_of_pokemon()[
                0]:  # gebruikt de vorige functie's return om door de lijst met pokémon te lopen
                if x == pokemon['name']:
                    naam = (pokemon['name'])  # Zet de naam van de pokémon om in een variabele voor later gebruik
                    fieldnames = ['name', 'type', 'speed', 'special_defense', 'special_attack', 'defense', 'attack',
                                  'hp']  # definieert de keys voor het .csv bestand, het is immers een dict :-)
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
                    writer.writeheader()  # maak de keys ook zichtbaar in het bestand

                    t = []  # Maakt een lijst aan voor de types
                    stats = {}  # Maakt een dictionary aan voor de stats
                    for pokemon in pokemon_stats['types']:  # Voegt de verschillende types toe aan de lijst 't' ...
                        # voor later gebruik?
                        t.append(pokemon['type']['name'])

                    for pokemon in pokemon_stats[
                        'stats']:  # Voegt de verschillende stats met bijbehorende naam toe aan de dict...
                        # met key=naam value=waarde van stat
                        stats.update({(pokemon['stat']['name']): (pokemon['base_stat'])})
                    writer.writerow(
                        {'name': naam, 'type': t, 'speed': stats['speed'],
                         'special_defense': stats['special-defense'],
                         'special_attack': stats['special-attack'], 'defense': stats['defense'],
                         'attack': stats['attack'], 'hp': stats['hp']})  # schrijft de waardes naar het bestand
                    request.urlretrieve(pokemon_stats['sprites']['front_default'],
                                        bestandsnaam + x + '.png')  # Haalt een sprite op van de pokémon

    # Haalt de moves op uit het JSON bestand en maakt een lijst met 4 dicts voor de moves
    for pokemon in list_of_pokemon()[
        0]:  # Gebruikt de return van de functie voor het uitlezen van de lijst met namen van de pokémon
        if x == pokemon['name']:
            teller = 0  # lege variabele met type int (gebruikt als counter)
            move_list_number = []  # lege lijst.. duh. Deze wordt gebruikt om de nummers van de move (ID's) op te slaan die hierna
            #  worden gebruikt om de moves op te halen
            while teller < 4:  # Zolang de teller een waarde heeft van minder dan 4, doe dit
                random_number = randint(0, len(
                    pokemon_stats['moves']) - 1)  # genereert een random getal zodat de moves die een
                #  pokémon krijgt random uit zijn beschikbare   lijst met moves wordt gekozen. Het random getal mag niet
                #  hoger zijn dan lengte van de lijst met moves, anders komt er een IndexError terug. Op deze
                #  manier zijn bijna alle gevechten uniek, ook als de zelfde pokémon steeds opnieuw wordt gekozen.
                if random_number not in move_list_number:  # Controlleerd of het random gegenereerde getal al in de lijst voorkomt. ALs dit zo is
                    #  moet er een nieuw getal worden gemaakt. We kunnen geen pokémon hebben die vier keer hypper beam heeft :-)
                    move_list_number.append(random_number)  # Voeg het random getal toe aan de lijst
                    teller += 1  # Teller eentje hoger maken zodat de pokémon niet al zijn moves krijgt die hij zou KUNNEN
                    # leren, maar een limiet heeft van 4 moves
                else:
                    pass  # Als het getal wel in de lijst voorkomt moet er een nieuw getal worden gemaakt, dus pass
                    #  en doe de functie maar weer opnieuw
            counter = 0  # Nogmaals een teller, dit keer een c, want waarom ook niet.
            moves_list = []  # Lijst aanmaken voor het opslaan van de moves die de pokémon uiteindelijk krijgt wanneer
            #  er op 'Fight!' wordt geklikt in het interface
            while counter < 4:  # Teller check, net als hierboven
                m = pokemon_stats['moves'][
                    move_list_number[counter]]  # Haal de moves uit de dict die bovenaan deze functie is aangevraagd
                #  en kijk naar het random getal dat in 'move_list_number' opgeslagen is met indexnummer 'c'.
                #  Dit nummer correspondeerd met een nummer van een move. Sla de data die terug komt op in 'm'
                MOVE = requests.get(m['move']['url'])  # Vraagt een nieuwe URL aan.
                MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.
                move_name1 = m['move']['name']  # Gebruik de data van de opgehaalde URL voor deze variabele
                move_type1 = MOVE_JSON['type']['name']
                move_accuracy1 = MOVE_JSON['accuracy']
                move_power1 = MOVE_JSON['power']
                counter += 1
                moves_list.append(
                    {'attack_name': move_name1, 'attack_type': move_type1, 'attack_accuracy': move_accuracy1,
                     'attack_power': move_power1})  # Alle zojuist aangemaakte variabele worden in een dict gezet, en deze worden toegevoegd aan de lijst 'move_list'
    return moves_list  # returned de lijst met moves zodat het gebruik van de functie


def read_stats(x):
    with open('./pokemon/%s/stats.csv' % x, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')

        stats_dict = []
        for row in reader:
            stats_dict.append(row)

    return stats_dict
