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

def pokemon():
    'Functie voor de eerste pokémon. Als deze al bestaat wordt de database gebruikt, anders wordt er een nieuwe entry gemaakt'
    inputerino = input('Stats van pokemon één: ').lower()
    if not os.path.exists('./pokemon/%s.csv' % inputerino):  # kijkt of de input al bestaat in de map ./pokemon/
        with open('./pokemon/%s.csv' % inputerino, encoding='utf-8', mode='w') as file:  # Als deze niet bestaat wordt dit aangemaakt
            for i in pokemon_json['results']:
                if inputerino == i['name']:
                    naam = (i['name'])  # Zet de naam van de pokémon om in een variabele
                    fieldnames = ['naam', 'type', 'speed', 'special-defense', 'special-attack', 'defense', 'attack', 'hp']  # definieert de veldnamen voor het .csv bestand
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
                    STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
                    STATS_JSON = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
                    t = []  # Maakt een lijst aan voor de types
                    stats = {}  # Maakt een dictionary aan voor de stats
                    for i in STATS_JSON['types']:  # Voegt de verschillende types toe aan de lijst t
                        t.append(i['type']['name'])
                    for i in STATS_JSON['stats']:  # Voegt de verschillende stats met bijbehorende naam toe aan de dict met key=naam value=waarde van stat
                        stats.update({(i['stat']['name']): (i['base_stat'])})
                    for i in pokemon_json['results']:
                        MOVES = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
                        MOVES_JSON = json.loads(MOVES.text)  # Decode de data in de nieuwe URL.
                        t = 0
                        lst = []
                        while t < 4:
                            r = randint(0,len(MOVES_JSON['moves']))
                            if r not in lst:
                                lst.append(r)
                                t += 1
                            else:
                                pass
                        c = 0
                        while c < 4:
                            m = MOVES_JSON['moves'][lst[c]]
                            MOVE = requests.get(m['move']['url'])  # Vraagt een nieuwe URL aan.
                            MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.


                            print(m['move']['name'])
                            print('type is: ' +MOVE_JSON['type']['name'])
                            print('accuracy is: ' +str(MOVE_JSON['accuracy']))
                            print('power is: ' +str(MOVE_JSON['power'] ))
                            print('')
                            c += 1
                    writer.writerow({'naam': naam, 'type': t, 'speed': stats['speed'], 'special-defense': stats['special-defense'], 'special-attack': stats['special-attack'], 'defense': stats['defense'], 'attack': stats['attack'], 'hp': stats['hp']}) # schrijft de waardes naar het bestand
    else:
        with open('./pokemon/%s.csv' % inputerino, encoding='utf-8', mode='r') as file:
            file = csv.reader(file, delimiter=';')
            for row in file:
                naam = row[0]  # Zet de naam in een variabele voor de return functie
                type = row[1].replace('[', '').replace(']', '').replace("'", "")  # Stript de string van alle extra karakters
                speed = row[2]
                special_defense = row[3]
                special_attack = row[4]
                defense = row[5]
                attack = row[6]
                hp = row[7]
            print('{}\n{}\nSpeed: {}\nSpDef: {}\nSpAtt: {}\nDef: {}\nAttack: {}\nHP: {}\n'.format(naam, 'Type is: '+type, speed, special_defense, special_attack, defense, attack, hp))
            return naam, type, speed, special_defense, special_attack, defense, attack, hp


print(pokemon())
print(30*'*' + '\n' + 12*'-' + 'Fight!' + 12*'-' + '\n' + 30*'*')

