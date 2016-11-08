import threading
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


class pokemonThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
         pokemon(self.name)
    def load_moves(self):
        self.attack_power1 = read_moves(self.name, 'p')[0]
        self.attack_power2 = read_moves(self.name, 'p')[1]
        self.attack_power3 = read_moves(self.name, 'p')[2]
        self.attack_power4 = read_moves(self.name, 'p')[3]
    def load_hp(self):
        self.hp = get_hp()
    def change_hp(self, damage):
        self.hp = self.hp - damage
        return (self.hp)

def get_hp():
    return (125)
def pokemon(x):
    'Functie voor de eerste pokémon. Als deze al bestaat wordt de database gebruikt, anders wordt er een nieuwe entry gemaakt'
    inputerino = x
    if not os.path.exists('./pokemon/%s/stats.csv' % inputerino):  # kijkt of de input al bestaat in de map ./pokemon/
        os.makedirs('./pokemon/%s/' % inputerino)
        with open('./pokemon/%s/stats.csv' % inputerino, encoding='utf-8', mode='w') as file:  # Als deze niet bestaat wordt dit aangemaakt
            for i in pokemon_json['results']:
                if inputerino == i['name']:
                    naam = (i['name'])  # Zet de naam van de pokémon om in een variabele
                    fieldnames = ['name', 'type', 'speed', 'special_defense', 'special_attack', 'defense', 'attack', 'hp']  # definieert de veldnamen voor het .csv bestand
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';', lineterminator='\n')
                    writer.writeheader()
                    STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
                    STATS_JSON = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
                    t = []  # Maakt een lijst aan voor de types
                    stats = {}  # Maakt een dictionary aan voor de stats
                    for i in STATS_JSON['types']:  # Voegt de verschillende types toe aan de lijst t
                        t.append(i['type']['name'])
                    for i in STATS_JSON['stats']:  # Voegt de verschillende stats met bijbehorende naam toe aan de dict met key=naam value=waarde van stat
                        stats.update({(i['stat']['name']): (i['base_stat'])})
                    writer.writerow({'name': naam, 'type': t, 'speed': stats['speed'], 'special_defense': stats['special-defense'], 'special_attack': stats['special-attack'], 'defense': stats['defense'], 'attack': stats['attack'], 'hp': stats['hp']})  # schrijft de waardes naar het bestand
                    moves(inputerino)
    else:
        moves(inputerino)
def moves(x):
    inputerino = x
    for i in pokemon_json['results']:
        if inputerino == i['name']:
            STATS = requests.get(i['url'])  # Vraagt een nieuwe URL aan.
            STATS_JSON = json.loads(STATS.text)  # Decode de data in de nieuwe URL.
            with open('./pokemon/%s/moves.csv' % inputerino, encoding ='utf-8', mode='w') as file2:
                veldnamen = ['attack_name', 'attack_type', 'attack_accuracy', 'attack_power']
                schrijver = csv.DictWriter(file2, fieldnames=veldnamen, delimiter=';', lineterminator='\n')
                schrijver.writeheader()
                h = 0
                lst = []
                while h < 4:
                    r = randint(0,len(STATS_JSON['moves']))
                    if r not in lst:
                        lst.append(r)
                        h += 1
                    else:
                        pass
                c = 0
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
                    schrijver.writerow({'attack_name': move_name1, 'attack_type': move_type1, 'attack_accuracy': move_accuracy1, 'attack_power': move_power1})
def read_moves(pokemon, soort):
    with open('./pokemon/%s/moves.csv' % pokemon, 'r') as file:
        r = csv.DictReader(file, delimiter=';')
        lijst_moves = []
        for moves in r:
            attack_name = moves['attack_name']
            attack_type = moves['attack_type']
            attack_accuracy = moves['attack_accuracy']
            attack_power = moves['attack_power']
            if soort == 'n':
                lijst_moves.append(attack_name)
            elif soort == 'p':
                lijst_moves.append(attack_power)
            elif soort == 'a':
                lijst_moves.append(attack_accuracy)
            elif soort == 't':
                lijst_moves.append(attack_type)

        return (lijst_moves)


threadLock = threading.Lock()
threads = []

# Create new threads
pokemon1 = input('choose pokemon 1')
pokemon2 = input('choose pokemon 2')
thread1 = pokemonThread(1, pokemon1, 1)
thread2 = pokemonThread(2, pokemon2, 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

thread1.join()
thread2.join()
thread1.load_hp()
thread2.load_hp()
thread1.load_moves()
thread2.load_moves()
thread1.change_hp(thread2.attack_power2)
thread2.change_hp(25)


thread1.join()
thread2.join()
print(' hp of %s is:' % thread1.name, thread1.hp)
print(' hp of %s is:' % thread2.name, thread2.hp)
