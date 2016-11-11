import threading
from tkinter import *

from app import list_of_pokemon, gotta_catch_em_all, read_stats
from damage_calc import damage_type_calculator
from ping import ping
from type_chart import get_types

# haalt de lijst van pokemons op
list_of_pokemon()
get_types()
global thread
global turn_player


class pokemonThread(threading.Thread):
    '''
    elke tread die word gecreert staat voor een pokemon
    '''

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name  # de pokemon naam

    def run(self):
        '''
        in deze functie word alle statusen en moves geladen en toegewezen
        '''
        self.move_lijst = gotta_catch_em_all(self.name)  # laad allen aanvallen op en wijst het toe aan een variabel
        self.statsDict = read_stats(self.name)[0]  # de dictonary met alle statusen van de pokemon woorden ingeladen
        self.hp = int(self.statsDict['hp']) * (int(self.statsDict['special_defense']) + int(self.statsDict['defense'])) #hp staat voor healt
        self.speed = int(self.statsDict['speed']) #de speed word geladen



        #voor alle 4 de moves worden de gevens van de dictonarie toegewezen aan variabel

        #attack power word toegewezen uit de dictonary
        self.attack_power1 = self.move_lijst[0]["attack_power"]
        self.attack_power2 = self.move_lijst[1]["attack_power"]
        self.attack_power3 = self.move_lijst[2]["attack_power"]
        self.attack_power4 = self.move_lijst[3]["attack_power"]

        #de naam van de aanval word toegewezen vanuit de dictonarie
        self.attack_name1 = self.move_lijst[0]["attack_name"]
        self.attack_name2 = self.move_lijst[1]["attack_name"]
        self.attack_name3 = self.move_lijst[2]["attack_name"]
        self.attack_name4 = self.move_lijst[3]["attack_name"]

        #de soort aanval word toegewezen vanuit de dictonarie
        self.attack_type1 = self.move_lijst[0]["attack_type"]
        self.attack_type2 = self.move_lijst[1]["attack_type"]
        self.attack_type3 = self.move_lijst[2]["attack_type"]
        self.attack_type4 = self.move_lijst[3]["attack_type"]

    def change_hp(self, naam, power, typeAanval):
        #hier word de health  van de pokemon veranderd en laat de zien hoeveel damage er is gedaan
        self.hp = self.hp - damage_type_calculator(naam, power, typeAanval)     #de damage word van de health afgehaald
        listbox.insert('0', str('{0} health: {1}'.format(self.name, self.hp))) #laat zien hoeveel damage er is gedaan
        check_game_winner()#kijkt als er een winaar is#
        displayHp(self.threadID, self.hp)#de hp word bijgewerkt in de interface


def lock():
    #de knoppen woorden geblockeerd
    pokemon_2_move_1.configure(state='disabled')
    pokemon_2_move_2.configure(state='disabled')
    pokemon_2_move_3.configure(state='disabled')
    pokemon_2_move_4.configure(state='disabled')
    pokemon_1_move_1.configure(state='disabled')
    pokemon_1_move_2.configure(state='disabled')
    pokemon_1_move_3.configure(state='disabled')
    pokemon_1_move_4.configure(state='disabled')


def check_game_winner():
    #deze functie bebaald als er verder mag gespeeld of als een pokemon heeft gewonnen
    if thread1.hp <= 0:         #kijkt als pokemon 1 dood is
        lock()
        listbox.insert('0', str('pokemon {} heeft gewonnen!'.format(thread2.name)))
        print('we hebben een winnaar')
    elif thread2.hp <= 0: #kijt als pokemon 2 dood is
        lock()
        listbox.insert('0', str('pokemon {} heeft gewonnen!'.format(thread1.name)))
        print('we hebben een winnaar')
    else:
        # neiamd heeft nog verloren
        return ()


def check_turn(x):
    #er word geken welke payer aan de buurt is
    global turn_player
    if x == turn_player: #kijt als de speler aan de buurt is en de volgende speler krijgt de buurt
        if x == 2:
            turn_player = 1
            print(turn_player)
        else:
            turn_player = 2
            print(turn_player)
        return (True)
    else: #de speler is niet aan de buurt
        return (False)


def create_threads(pokemon1, pokemon2):
    #de threads woorden in deze functie aan gemaakt
    global threadLock
    threads = []
    # Create new threads
    # pokemon1 = input('choose pokemon 1')
    # pokemon2 = input('choose pokemon 2')
    global thread1
    global thread2 #de threats woorden global gemaakt om het te kunnen aanroepen
    #threads woorden gemaakt en krijgen naam plus id
    thread1 = pokemonThread(1, pokemon1.lower())
    thread2 = pokemonThread(2, pokemon2.lower())

    # Start new Threads
    thread1.start()#de start functie word aangeroepen in de funcite
    thread2.start()
    thread1.join()
    thread2.join()#wacht tot het laden van de pokemon klaar is
    if thread2.speed >= thread1.speed:
        # er word naar de stats speed gekeken en bebaald wie mag starten
        global turn_player
        turn_player = 2
    else:
        turn_player = 1
    listbox.insert('0', str('player {} starts'.format(turn_player)))
    # Add threads to thread list
    threads.append(thread1)
    threads.append(thread2)


def image_ophalen1():
    # image vervangen
    image_1 = PhotoImage(file='./pokemon/' + pokemon_1_var.get() + '/' + pokemon_1_var.get() + '.png')
    image_1.image = image_1
    image_1_label.config(image=image_1)


def image_ophalen2():
    # image vervangen
    image_2 = PhotoImage(file='./pokemon/' + pokemon_2_var.get() + '/' + pokemon_2_var.get() + '.png')
    image_2.image = image_2
    image_2_label.config(image=image_2)


if __name__ == "__main__":
    root = Tk()
    root.wm_title('PBS - Pokémon Battle Station')
    root.state('zoomed')

    root.grid_columnconfigure(0, weight=1, uniform='HALF')
    root.grid_columnconfigure(1, weight=1, uniform='HALF')
    root.grid_rowconfigure(0, weight=1)

    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()

    # frames/ grid links en rechts
    left = Frame(root, height=height * 0.75, bd=5, relief=SUNKEN, background='red')
    right = Frame(root, height=height * 0.75, bd=5, relief=SUNKEN, background='blue')
    bottom = Frame(root, height=height * 0.25, bd=5, relief=SUNKEN, background='green')
    left.grid(row=0, column=0, sticky='nesw', padx=40, pady=(40, 20))
    right.grid(row=0, column=1, sticky='nesw', padx=40, pady=(40, 20))
    bottom.grid(row=1, columnspan=2, sticky='nesw', padx=40, pady=(20, 40))

    # background
    root.configure(background='yellow')

    # Label content
    pokemon_1_var = StringVar(root)
    pokemon_2_var = StringVar(root)
    pokemon_1_var.set('Kies Pokémon 1')
    pokemon_2_var.set('Kies Pokémon 2')


    # pokemon ophalen uit app.py


    # events
    def OptionMenu_pokemon_1(event):
        listbox.insert('0',
                       'RED HEEFT ' + pokemon_1_var.get().upper() + ' GEKOZEN!')  # laat zien welke pokemon er is gekozen
        #pokemon_1_type.config(text='MOVES POKÉMON ' + pokemon_1_var.get().upper())  # laat zien welke move er gebruikt word
        gotta_catch_em_all(pokemon_1_var.get())  # Controleerd of er al een stats bestand is aangemaakt en maakt deze aan als deze er niet is. voor info zie app.py
        pokemon_1_hp_number.config(
            text='HP: ' + read_stats(pokemon_1_var.get())[0]['hp'])  # haalt HP van pokemon op van database
        pokemon_1_stats.config(text='Speed: ' + read_stats(pokemon_1_var.get())[0]['speed'] +
                                    '\n Attack: ' + read_stats(pokemon_1_var.get())[0]['attack'] +
                                    '\n Special Attack: ' + read_stats(pokemon_1_var.get())[0]['special_attack'] +
                                    '\n Defense: ' + read_stats(pokemon_1_var.get())[0]['defense'] +
                                    '\n Special Defense: ' + read_stats(pokemon_1_var.get())[0]['special_defense'])


    def OptionMenu_pokemon_2(event):
        listbox.insert('0',
                       'BlUE HEEFT ' + pokemon_2_var.get().upper() + ' GEKOZEN!')  # laat zien welke pokemon er is gekozen
        #pokemon_2_type.config(
          # text='MOVES POKÉMON ' + pokemon_2_var.get().upper())  # laat zien welke move er gebruikt word
        gotta_catch_em_all(
            pokemon_2_var.get())  # Controleerd of er al een stats bestand is aangemaakt en maakt deze aan als deze er niet is. voor info zie app.py
        pokemon_2_hp_number.config(
            text='HP: ' + read_stats(pokemon_2_var.get())[0]['hp'])  # haalt HP van pokemon op van database
        pokemon_2_stats.config(text='Speed: ' + read_stats(pokemon_2_var.get())[0]['speed'] +
                                    '\n Attack: ' + read_stats(pokemon_2_var.get())[0]['attack'] +
                                    '\n Special Attack: ' + read_stats(pokemon_2_var.get())[0]['special_attack'] +
                                    '\n Defense: ' + read_stats(pokemon_2_var.get())[0]['defense'] +
                                    '\n Special Defense: ' + read_stats(pokemon_2_var.get())[0]['special_defense'])


    pokemon_1 = OptionMenu(left, pokemon_1_var, *list_of_pokemon()[1],
                           command=OptionMenu_pokemon_1)  # get_pokemons komt vanaf bestand all_pokemon_to_file.py
    pokemon_2 = OptionMenu(right, pokemon_2_var, *list_of_pokemon()[1], command=OptionMenu_pokemon_2)
    pokemon_1.grid(row=0, column=0, sticky=NW)
    pokemon_2.grid(row=0, column=0, sticky=NW)

    # plaatjes pokeballs en pokemons
    image_1 = PhotoImage(file='pokeball.gif')
    image_1_label = Label(left, image=image_1, bg='red')
    image_1_label.grid(row=1, column=0, sticky='W', padx=10, pady=20)
    image_1_label.image = image_1

    image_2 = PhotoImage(file='pokeball.gif')
    image_2_label = Label(right, image=image_2, bg='blue')
    image_2_label.grid(row=1, column=0, sticky='W', padx=10, pady=20)
    image_2_label.image = image_2


    def OptionMenu_pokemon_2(event):
        listbox.insert('0',
                       'BlUE HEEFT ' + pokemon_2_var.get().upper() + ' GEKOZEN!')  # laat zien welke pokemon er is gekozen
        pokemon_1_type.config(
            text='MOVES POKÉMON ' + pokemon_2_var.get().upper())  # laat zien welke move er gebruikt word
        gotta_catch_em_all(
            pokemon_2_var.get())  # Controleerd of er al een stats bestand is aangemaakt en maakt deze aan als deze er niet is. voor info zie app.py
        pokemon_2_hp_number.config(
            text='HP: ' + read_stats(pokemon_2_var.get())[0]['hp'])  # haalt HP van pokemon op van database
        pokemon_2_stats.config(text='Speed: ' + read_stats(pokemon_2_var.get())[0]['speed'] +
                                    '\n Attack: ' + read_stats(pokemon_2_var.get())[0]['attack'] +
                                    '\n Special Attack: ' + read_stats(pokemon_2_var.get())[0]['special_attack'] +
                                    '\n Defense: ' + read_stats(pokemon_2_var.get())[0]['defense'] +
                                    '\n Special Defense: ' + read_stats(pokemon_2_var.get())[0]['special_defense'])


    pokemon_1 = OptionMenu(left, pokemon_1_var, *list_of_pokemon()[1],
                           command=OptionMenu_pokemon_1)  # get_pokemons komt vanaf bestand all_pokemon_to_file.py
    pokemon_2 = OptionMenu(right, pokemon_2_var, *list_of_pokemon()[1], command=OptionMenu_pokemon_2)
    pokemon_1.grid(row=0, column=0, sticky=NW)
    pokemon_2.grid(row=0, column=0, sticky=NW)

    # HP Positie
    pokemon_1_hp_number = ('')
    pokemon_1_hp_number = Label(left, text=''.join(pokemon_1_hp_number), bg='red')
    pokemon_1_hp_number.grid(row=0, column=1, sticky='nw')
    pokemon_2_hp_number = ('')
    pokemon_2_hp_number = Label(right, text=''.join(pokemon_2_hp_number), bg='blue')
    pokemon_2_hp_number.grid(row=0, column=1, sticky='nw')


    def displayHp(id, hp):
        if id == 1:
            pokemon_1_hp_number.configure(text=hp)
        else:
            pokemon_2_hp_number.configure(text=hp)


    # Stats positie
    pokemon_1_stats = ('')
    pokemon_2_stats = ('')
    pokemon_1_stats = Label(left, text='\n'.join(pokemon_1_stats), bg='red')
    pokemon_2_stats = Label(right, text='\n'.join(pokemon_2_stats), bg='blue')
    pokemon_1_stats.grid(row=1, column=1, sticky='w')
    pokemon_2_stats.grid(row=1, column=1, sticky='w')

    # tekst onder plaatje
    pokemon_1_type = Label(left, text='MOVES POKÉMON ', bg='red')
    pokemon_2_type = Label(right, text='MOVES POKÉMON ', bg='blue')
    pokemon_1_type.grid(row=2, column=0, sticky=NW)
    pokemon_2_type.grid(row=2, column=0, sticky=NW)


    # buttons moves pokémon 1
    def p1_attack1():
        if check_turn(1) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 1 used {0}'.format(thread1.attack_name1)))
                thread2.change_hp(thread2.name, int(thread1.attack_power1), thread1.attack_type1)#de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                #de aanval heeft geen damage
                listbox.insert('0', str('no damage was done'))


    def p1_attack2():
        if check_turn(1) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 1 used {0}'.format(thread1.attack_name2)))
                thread2.change_hp(thread2.name, int(thread1.attack_power2), thread1.attack_type2) #de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                #de aanval heeft geen damage
                listbox.insert('0', str('no damage was done'))


    def p1_attack3():
        if check_turn(1) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 1 used {0}'.format(thread1.attack_name3)))
                thread2.change_hp(thread2.name, int(thread1.attack_power3), thread1.attack_type3) #de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                #de aanval heeft geen damage
                listbox.insert('0', str('no damage was done'))


    def p1_attack4():
        if check_turn(1) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 1 used {0}'.format(thread1.attack_name4)))
                thread2.change_hp(thread2.name, int(thread1.attack_power4), thread1.attack_type4) #de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                #de aanval heeft geen damage
                listbox.insert('0', str('no damage was done'))


    pokemon_1_move_1 = Button(left, padx=100, pady=1, text='attack 1', command=p1_attack1, bg='red')
    pokemon_1_move_1.grid(row=3, column=0, sticky=W)

    pokemon_1_move_2 = Button(left, padx=100, pady=1, text='attack 2', command=p1_attack2, bg='red')
    pokemon_1_move_2.grid(row=3, column=1, sticky=W)

    pokemon_1_move_3 = Button(left, padx=100, pady=1, text='attack 3', command=p1_attack3, bg='red')
    pokemon_1_move_3.grid(row=4, column=0, sticky=W)

    pokemon_1_move_4 = Button(left, padx=100, pady=1, text='attack 4', command=p1_attack4, bg='red')
    pokemon_1_move_4.grid(row=4, column=1, sticky=W)


    # buttons moves pokémon 2
    def p2_attack1():
        if check_turn(2) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 1 used {0}'.format(thread1.attack_name1)))
                thread1.change_hp(thread1.name, int(thread2.attack_power1), thread2.attack_type1) #de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                listbox.insert('0', str('no damage was done')) #de aanval heeft geen damage


    def p2_attack2():
        if check_turn(2) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 1 used {0}'.format(thread1.attack_name2)))
                thread1.change_hp(thread1.name, int(thread2.attack_power2), thread2.attack_type2) #de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                listbox.insert('0', str('no damage was done')) #de aanval heeft geen damage


    def p2_attack3():
        if check_turn(2) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 2 used {0}'.format(thread1.attack_name3)))
                thread1.change_hp(thread1.name, int(thread2.attack_power3), thread2.attack_type3) #de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                #de aanval heeft geen damage
                listbox.insert('0', str('no damage was done'))


    def p2_attack4():
        if check_turn(2) == True: #kijkt als het zijn buurt is
            try:
                listbox.insert('0', str('Pokemon 2 used {0}'.format(thread1.attack_name4)))
                thread1.change_hp(thread1.name, int(thread2.attack_power4), thread2.attack_type4) #de change_hp() funcite word geroepen met als parameters alle gevens van de aanval
            except:
                #de aanval heeft geen damage
                listbox.insert('0', str('no damage was done'))


    pokemon_2_move_1 = Button(right, padx=100, pady=1, text='attack 1', command=p2_attack1, bg='blue')
    pokemon_2_move_1.grid(row=3, column=0, sticky=W)

    pokemon_2_move_2 = Button(right, padx=100, pady=1, text='attack 2', command=p2_attack2, bg='blue')
    pokemon_2_move_2.grid(row=3, column=1, sticky=W)

    pokemon_2_move_3 = Button(right, padx=100, pady=1, text='attack 3', command=p2_attack3, bg='blue')
    pokemon_2_move_3.grid(row=7, column=0, sticky=W)

    pokemon_2_move_4 = Button(right, padx=100, pady=1, text='attack 4', command=p2_attack4, bg='blue')
    pokemon_2_move_4.grid(row=7, column=1, sticky=W)


    # Start functie
    def callback():
        create_threads(pokemon_1_var.get().upper(), pokemon_2_var.get().upper())
        pokemon_1.configure(state="disabled") #zorgt dat je niet meer een pokemon kan weizigen
        pokemon_2.configure(state="disabled")#zorgt dat je niet meer een pokemon kan weizigen
        start.destroy() #de fight button word wegehaald
        #images woorden geladen
        image_ophalen1()
        image_ophalen2()
        #text word in interface geprint
        listbox.insert('0', str('Speler Red  kiest: ' + pokemon_1_var.get().upper() + '!'))
        listbox.insert('0', str('Speler Blue kiest: ' + pokemon_2_var.get().upper() + '!'))
        #de buttons van pokemon 1 krijgen de naam van de aanval
        pokemon_1_move_1.configure(text=thread1.attack_name1)
        pokemon_1_move_2.configure(text=thread1.attack_name2)
        pokemon_1_move_3.configure(text=thread1.attack_name3)
        pokemon_1_move_4.configure(text=thread1.attack_name4)

        #de buttons van pokemon 2 krijgen de naam van de aanval
        pokemon_2_move_1.configure(text=thread2.attack_name1)
        pokemon_2_move_2.configure(text=thread2.attack_name2)
        pokemon_2_move_3.configure(text=thread2.attack_name3)
        pokemon_2_move_4.configure(text=thread2.attack_name4)


    # scroll text box
    scrollbar = Scrollbar(bottom)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(bottom, yscrollcommand=scrollbar.set, width=width)
    listbox.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=listbox.yview)

    # kijk voor internet
    listbox.insert('0', ping())

    start = Button(text='Fight!', command=callback)
    start.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()

mainloop()
