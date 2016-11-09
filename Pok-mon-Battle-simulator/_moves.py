import requests
import json
from random import randint


POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

base += '?limit=1'  # Limit van 151 pokemon (dit is een extensie van de website URL)

pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.


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






