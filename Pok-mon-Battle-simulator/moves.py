import requests
import json
from random import randint

POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

base += '?limit=151'  # Limit van 151 pokemon (dit is een extensie van de website URL)

pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.


def pokemon_moves():
    for i in pokemon_json['results']:
        if i['name'] == 'magikarp':
            MOVES = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
            MOVES_JSON = json.loads(MOVES.text)  # Decode de data in de nieuwe URL.

            lst = []
            t = 0
            while t < 4:
                r = randint(0, len(MOVES_JSON['moves'])-1)
                if r not in lst:
                    lst.append(r)
                    t += 1
                else:
                    pass
            print(lst)
            c = 0
            attacks_list = []
            over = len(lst) - len(MOVES_JSON['moves'])
            if len(MOVES_JSON['moves']) >= len(lst):
                for i in lst:
                    if c < 4:
                        m = MOVES_JSON['moves'][i]
                        m = m['move']
                        MOVE = requests.get(m['url'])  # Vraagt een nieuwe URL aan.
                        MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.

                        attack_name = m['name']
                        attack_type = MOVE_JSON['type']['name']
                        accuracy = str(MOVE_JSON['accuracy'])
                        power = str(MOVE_JSON['power'])

                        attacks_list.append([attack_name, attack_type, accuracy, power])
                        c += 1
                    else:
                        break
            else:
                for i in MOVES_JSON['moves']:
                    m = i['move']
                    MOVE = requests.get(m['url'])  # Vraagt een nieuwe URL aan.
                    MOVE_JSON = json.loads(MOVE.text)  # Decode de data in de nieuwe URL.

                    attack_name = m['name']
                    attack_type = MOVE_JSON['type']['name']
                    accuracy = str(MOVE_JSON['accuracy'])
                    power = str(MOVE_JSON['power'])
                    attacks_list.append([attack_name, attack_type, accuracy, power])

                while over > 0:
                    attack_name = '---'
                    attack_type = '---'
                    accuracy = '---'
                    power = '---'
                    attacks_list.append([attack_name, attack_type, accuracy, power])
                    over -= 1

            return attacks_list

print(pokemon_moves())
