import threading
import requests
from tkinter import *
from PIL import Image, ImageTk
import json
import csv
import os
from random import randint
from all_pokemon_to_file import get_pokemons


try:
    POKE_API = requests.get('http://pokeapi.co/api/v2')  # Vraagt de data aan.
    POKE_API_JSON = json.loads(POKE_API.text)  # Decode de JSON data.
    base = POKE_API_JSON['pokemon']  # Navigeert naar de basis van de informatie

    base += '?limit=151'  # Limit van 151 pokemon (dit is een extensie van de website URL)

    pokemon = requests.get(base)  # Vraagt de lijst met alle pokemon aan.
    pokemon_json = json.loads(pokemon.text)  # Decode de lijst met pokemon.
except:
    print('no internet')

print('1')


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
        self.attack_name1 = read_moves(self.name, 'n')[0]
        self.attack_name2 = read_moves(self.name, 'n')[1]
        self.attack_name3 = read_moves(self.name, 'n')[2]
        self.attack_name4 = read_moves(self.name, 'n')[3]

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
                    r = randint(0, len(STATS_JSON['moves']))
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
                    schrijver.writerow(
                        {'attack_name': move_name1, 'attack_type': move_type1, 'attack_accuracy': move_accuracy1,
                         'attack_power': move_power1})


global turn_player
turn_player = 1


def check_turn(x):
    global turn_player
    if x == turn_player:
        if x == 2:
            turn_player = 1
            print(turn_player)
        else:
            turn_player = 2
            print(turn_player)
        return (True)
    else:
        return (False)


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


def create_threads(pokemon1, pokemon2):
    threadLock = threading.Lock()
    threads = []
    # Create new threads
    # pokemon1 = input('choose pokemon 1')
    # pokemon2 = input('choose pokemon 2')
    global thread1
    global thread2
    thread1 = pokemonThread(1, pokemon1, 1)
    thread2 = pokemonThread(2, pokemon2, 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    print(threading.enumerate())

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)

    thread1.join()
    thread2.join()
    thread1.load_hp()
    thread2.load_hp()
    thread1.load_moves()
    thread2.load_moves()
    print(thread1.attack_power1)
    print(threading.enumerate())
'''
def p1_attack1():
    if check_turn(1) == True:
        listbox.insert('0', str('Pokemon 1 did ' ), thread1.attack_name1)
        try:
            thread2.change_hp(int(thread1.attack_power1))
        except:
            pass
        print(thread2.change_hp(0))
'''
create_threads('mew', 'muk')




root = Tk()
root.wm_title('PBS - Pokémon Battle Station')
root.state('zoomed')


root.grid_columnconfigure(0, weight=1, uniform='HALF')
root.grid_columnconfigure(1, weight=1, uniform='HALF')
root.grid_rowconfigure(0, weight=1)


height = root.winfo_screenheight()
width = root.winfo_screenwidth()

#frames/ grid links en rechts
left = Frame(root, height=height * 0.75, bd=5, relief=SUNKEN, background='red')
right = Frame(root, height=height * 0.75, bd=5, relief=SUNKEN, background='blue')
bottom = Frame(root, height=height * 0.25, bd=5, relief=SUNKEN, background='green')
left.grid(row=0, column=0, sticky='nesw', padx=40, pady=(40, 20))
right.grid(row=0, column=1, sticky='nesw', padx=40, pady=(40, 20))
bottom.grid(row=1, columnspan=2, sticky='nesw', padx=40, pady=(20, 40))

#background
root.configure(background='yellow')

# Label content
pokemon_1_var = StringVar(root)
pokemon_2_var = StringVar(root)
pokemon_1_var.set('Kies Pokémon 1')
pokemon_2_var.set('Kies Pokémon 2')


#drop down menu pokemon
pokemon_1 = OptionMenu(left, pokemon_1_var, *get_pokemons()) #get_pokemons komt vanaf bestand all_pokemon_to_file.py
pokemon_2 = OptionMenu(right, pokemon_2_var, *get_pokemons())
pokemon_1.grid(row=0, column=0, sticky=NW)
pokemon_2.grid(row=0, column=0, sticky=NW)


#plaatjes pokeballs en pokemons
image_1 = Image.open('pokeball.jpg')
image_2 = Image.open('pokeball.jpg')
image_1 = image_1.resize((200, 160), Image.ANTIALIAS)
image_2 = image_2.resize((200, 160), Image.ANTIALIAS)
pokemon_1_img_load = ImageTk.PhotoImage(image_1)
pokemon_2_img_load = ImageTk.PhotoImage(image_2)
pokemon_1_img = Label(left, image=pokemon_1_img_load)
pokemon_2_img = Label(right, image=pokemon_2_img_load)
pokemon_1_img.grid(row=1, column=0, sticky='nw')
pokemon_2_img.grid(row=1, column=0, sticky='nw')

#tekst onder plaatje
pokemon_1_type = Label(left, text='MOVES POKÉMON')
pokemon_2_type = Label(right, text='MOVES POKÉMON')
pokemon_1_type.grid(row=2, column=0, sticky=NW)
pokemon_2_type.grid(row=2, column=0, sticky=NW)

# Stats
pokemon_1_stats = ('HP', 'Attack Power')
pokemon_2_stats = ('HP', 'Attack Power')
pokemon_1_stats = Label(left, text='\n\n'.join(pokemon_1_stats))
pokemon_2_stats = Label(right, text='\n\n'.join(pokemon_2_stats))
pokemon_1_stats.grid(row=1, column=1, sticky='nw')
pokemon_2_stats.grid(row=1, column=1, sticky='nw')

#buttons moves pokémon 1
def p1_attack1():
    if check_turn(1) == True:
        listbox.insert('0', str('Pokemon 1 did ' ), thread1.attack_name1)
        try:
            thread2.change_hp(int(thread1.attack_power1))
        except:
            pass
        print(thread1.attack_power1)
        print(thread2.change_hp(0))
def p1_attack2():
    if check_turn(1) == True:
        listbox.insert('0', str('Pokemon 1 did ' ), thread1.attack_name1)
        try:
            thread2.change_hp(int(thread1.attack_power2))
        except:
            pass
        print('power is', thread1.attack_power2)
        print('power is', thread2.change_hp(0))
def p1_attack3():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 3'))
def p1_attack4():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 4'))

pokemon_1_move_1 = Button(left, padx=100, pady= 1, text='attack 1', command=p1_attack1)
pokemon_1_move_1.grid(row=3, column=0,sticky=W )

pokemon_1_move_2 = Button(left, padx=100, pady= 1, text='attack 2', command=p1_attack2)
pokemon_1_move_2.grid(row=3, column=1,sticky=W)

pokemon_1_move_3 = Button(left, padx=100, pady= 1, text='attack 3', command=p1_attack3)
pokemon_1_move_3.grid(row=4, column=0, sticky=W)

pokemon_1_move_4 = Button(left, padx=100, pady= 1, text='attack 4', command=p1_attack4)
pokemon_1_move_4.grid(row=4, column=1, sticky=W)

#buttons moves pokémon 2
def p2_attack1():
    if check_turn(2) == True:
        listbox.insert('0', str('Pokemon 2 did ' ), thread2.attack_name1)
    try:
        thread1.change_hp(int(thread2.attack_power1))
    except:
        pass
    print('power is',thread2.attack_power1)
    print('hp is', thread2.change_hp(0))
def p2_attack2():
    if check_turn(2) == True:
        listbox.insert('0', str('Pokemon 2 did ' ), thread2.attack_name1)
        try:
            thread1.change_hp(int(thread2.attack_power2))
        except:
            pass
        print('power is', thread2.attack_power2)
        print('hp is', thread2.change_hp(0))
def p2_attack3():
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 3'))
def p2_attack4():
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 4'))

pokemon_2_move_1 = Button(right, padx=100, pady= 1, text='attack 1', command=p2_attack1)
pokemon_2_move_1.grid(row=3, column=0,sticky=W )

pokemon_2_move_2 = Button(right, padx=100, pady= 1, text='attack 2', command=p2_attack2)
pokemon_2_move_2.grid(row=3, column=1,sticky=W)

pokemon_2_move_3 = Button(right, padx=100, pady= 1, text='attack 3', command=p2_attack3)
pokemon_2_move_3.grid(row=7, column=0, sticky=W)

pokemon_2_move_4 = Button(right, padx=100, pady= 1, text='attack 4', command=p2_attack4)
pokemon_2_move_4.grid(row=7, column=1, sticky=W)

# Start functie
def callback():
    listbox.insert('0', str('Speler Red  kiest: ' + pokemon_1_var.get().upper() + '!'))
    listbox.insert('0', str('Speler Blue kiest: ' + pokemon_2_var.get().upper() + '!'))


#scroll text box
scrollbar = Scrollbar(bottom)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(bottom, yscrollcommand=scrollbar.set, width=width)
listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=listbox.yview)



start = Button(text='Fight!', command=callback)
start.place(relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()
