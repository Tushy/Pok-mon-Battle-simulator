import threading
import requests
from tkinter import *
from PIL import Image, ImageTk
import json
import csv
import os
from random import randint
from all_pokemon_to_file import get_pokemons
from app import list_of_pokemon, gotta_catch_em_all
from read_stats import get_stats
from ping import ping



class pokemonThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        self.move_lijst = gotta_catch_em_all(self.name)
        self.hp = get_stats(self.name, 'EffHp') * 10
        self.speed = get_stats(self.name, 'speed')
        self.EffAtt = get_stats(self.name,'EffAtt')
        self.attack_power1 = self.move_lijst[0]["attack_power"]
        self.attack_power2 = self.move_lijst[1]["attack_power"]
        self.attack_power3 = self.move_lijst[2]["attack_power"]
        self.attack_power4 = self.move_lijst[3]["attack_power"]
        self.attack_name1 = self.move_lijst[0]["attack_name"]
        self.attack_name2 = self.move_lijst[1]["attack_name"]
        self.attack_name3 = self.move_lijst[2]["attack_name"]
        self.attack_name4 = self.move_lijst[3]["attack_name"]
    '''
    def load_moves(self):
        self.attack_power1 = self.move_lijst[0]["attack_power"]
        self.attack_power2 = self.move_lijst[1]["attack_power"]
        self.attack_power3 = self.move_lijst[2]["attack_power"]
        self.attack_power4 = self.move_lijst[3]["attack_power"]
        self.attack_name1 = self.move_lijst[0]["attack_name"]
        self.attack_name2 = self.move_lijst[1]["attack_name"]
        self.attack_name3 = self.move_lijst[2]["attack_name"]
        self.attack_name4 = self.move_lijst[3]["attack_name"]
'''
    def change_hp(self, damage):
        self.hp = self.hp - damage * int(self.EffAtt)
        listbox.insert('0', str('{0} health: {1}'.format(self.name, self.hp)))
        check_game_winner()
        return ()


def lock():
    pokemon_2_move_1.configure(state='disabled')
    pokemon_2_move_2.configure(state='disabled')
    pokemon_2_move_3.configure(state='disabled')
    pokemon_2_move_4.configure(state='disabled')
    pokemon_1_move_1.configure(state='disabled')
    pokemon_1_move_2.configure(state='disabled')
    pokemon_1_move_3.configure(state='disabled')
    pokemon_1_move_4.configure(state='disabled')


def check_game_winner():
    if thread1.hp <= 0:
        lock()
    elif thread2.hp <= 0:
        lock()
    else:
        #neiamd heeft nog verloren
        return()


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

'''
def read_moves(pokemon, soort):
    with open('./pokemon/%s/moves.csv' % pokemon, 'r') as file:
        r = csv.DictReader(file, delimiter=';')
        lijst_moves = algemeen()
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
'''
global threadLock
global thread
threadLock = threading.Lock()
threads = []
def create_threads(pokemon1, pokemon2):
    global threadLock
    #threadLock = threading.Lock()
    #threads = []
    # Create new threads
    # pokemon1 = input('choose pokemon 1')
    # pokemon2 = input('choose pokemon 2')
    global thread1
    global thread2
    thread1 = pokemonThread(1, pokemon1.lower(), 1)
    thread2 = pokemonThread(2, pokemon2.lower(), 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    print(threading.enumerate())

    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)

    thread1.join()
    thread2.join()
    print(thread1.attack_power1)
    print(threading.enumerate())




list_of_pokemon()

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
def OptionMenu_pokemon_1(event):
    listbox.insert('0','RED HEEFT ' +pokemon_1_var.get().upper()+ ' GEKOZEN!')
    pokemon_1_type.config(text='MOVES POKÉMON ' +pokemon_1_var.get().upper())
def OptionMenu_pokemon_2(event):
    listbox.insert('0',"BLUE HEEFT " +pokemon_2_var.get().upper() +' GEKOZEN!')

pokemon_1 = OptionMenu(left, pokemon_1_var, *get_pokemons(), command= OptionMenu_pokemon_1) #get_pokemons komt vanaf bestand all_pokemon_to_file.py
pokemon_2 = OptionMenu(right, pokemon_2_var, *get_pokemons(), command= OptionMenu_pokemon_2)
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

# Stats
pokemon_1_stats = ('HP', 'Attack Power')
pokemon_2_stats = ('HP', 'Attack Power')
pokemon_1_stats = Label(left, text='\n\n'.join(pokemon_1_stats))
pokemon_2_stats = Label(right, text='\n\n'.join(pokemon_2_stats))
pokemon_1_stats.grid(row=1, column=1, sticky='w')
pokemon_2_stats.grid(row=1, column=1, sticky='w')

#tekst onder plaatje
pokemon_1_type = Label(left, text='MOVES POKÉMON ')
pokemon_2_type = Label(right, text='MOVES POKÉMON ')
pokemon_1_type.grid(row=2, column=0, sticky=NW)
pokemon_2_type.grid(row=2, column=0, sticky=NW)


#buttons moves pokémon 1
#buttons moves pokémon 1
def p1_attack1():
    if check_turn(1) == True:
        try:
            listbox.insert('0', str('Pokemon 1 used {0}'.format(thread1.attack_name1)))
            thread2.change_hp(int(thread1.attack_power1))
        except:
            listbox.insert('0', str('no damage was done'))
def p1_attack2():
    if check_turn(1) == True:
        listbox.insert('0', str('Pokemon 1 did ' ), thread1.attack_name1)
        try:
            thread2.change_hp(int(thread1.attack_power2))
        except:
            pass
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
        listbox.insert('0', str('Pokemon 2 used: {0}').format(thread2.attack_name1))
        try:
            thread1.change_hp(int(thread2.attack_power1))
        except:
            listbox.insert('0',str('No damage is done'))

def p2_attack2():
    if check_turn(2) == True:
        listbox.insert('0', str('Pokemon 2 used: {0}').format(thread2.attack_name2))
        try:
            thread1.change_hp(int(thread2.attack_power2))
        except:
            pass
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
    create_threads(pokemon_1_var.get().upper(), pokemon_2_var.get().upper())
    pokemon_1.configure(state="disabled")
    pokemon_2.configure(state="disabled")
    start.destroy()
    listbox.insert('0', str('Speler Red  kiest: ' + pokemon_1_var.get().upper() + '!'))
    listbox.insert('0', str('Speler Blue kiest: ' + pokemon_2_var.get().upper() + '!'))



#scroll text box
scrollbar = Scrollbar(bottom)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(bottom, yscrollcommand=scrollbar.set, width=width)
listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=listbox.yview)
#kijkt voor internet
listbox.insert('0', ping())


start = Button(text='Fight!', command=callback)
start.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
