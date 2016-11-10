from tkinter import *
from PIL import Image, ImageTk
from app import gotta_catch_em_all, list_of_pokemon, read_stats
#from stats import read_stats

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

#events
def OptionMenu_pokemon_1(event):
    listbox.insert('0','RED HEEFT ' +pokemon_1_var.get().upper()+ ' GEKOZEN!') # laat zien welke pokemon er is gekozen
    pokemon_1_type.config(text='MOVES POKÉMON ' +pokemon_1_var.get().upper()) # laat zien welke move er gebruikt word
    gotta_catch_em_all(pokemon_1_var.get()) #Controleerd of er al een stats bestand is aangemaakt en maakt deze aan als deze er niet is. voor info zie app.py
    pokemon_1_hp_number.config(text='HP: '+read_stats(pokemon_1_var.get())[0]['hp']) # haalt HP van pokemon op van database
    pokemon_1_stats.config(text='Speed: '+read_stats(pokemon_1_var.get())[0]['speed']+
                            '\n Attack: '+read_stats(pokemon_1_var.get())[0]['attack']+
                            '\n Special Attack: '+read_stats(pokemon_1_var.get())[0]['special_attack']+
                            '\n Defense: '+read_stats(pokemon_1_var.get())[0]['defense']+
                            '\n Special Defense: '+read_stats(pokemon_1_var.get())[0]['special_defense'])
    image_1_place = PhotoImage(file='./pokemon/%s/%s.csv' % pokemon_1_var.get())
    image_1.config(image=image_1_place)


def OptionMenu_pokemon_2(event):
    listbox.insert('0',"BLUE HEEFT " +pokemon_2_var.get().upper() +' GEKOZEN!')

pokemon_1 = OptionMenu(left, pokemon_1_var, *list_of_pokemon()[1], command= OptionMenu_pokemon_1) #get_pokemons komt vanaf bestand all_pokemon_to_file.py
pokemon_2 = OptionMenu(right, pokemon_2_var, *list_of_pokemon()[1], command= OptionMenu_pokemon_2)
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

#HP Positie
pokemon_1_hp_number = ('')
pokemon_1_hp_number = Label(left, text=''.join(pokemon_1_hp_number))
pokemon_1_hp_number.grid(row=1, column=1, sticky='n')


# Stats positie
pokemon_1_stats = ('')
pokemon_2_stats = ('')
pokemon_1_stats = Label(left, text='\n'.join(pokemon_1_stats), bg='red')
pokemon_2_stats = Label(right,text='\n'.join(pokemon_2_stats), bg='blue')
pokemon_1_stats.grid(row=1, column=1, sticky='w')
pokemon_2_stats.grid(row=1, column=1, sticky='w')



#tekst onder plaatje
pokemon_1_type = Label(left, text='MOVES POKÉMON ', bg='red')
pokemon_2_type = Label(right, text='MOVES POKÉMON ', bg='blue')
pokemon_1_type.grid(row=2, column=0, sticky=NW)
pokemon_2_type.grid(row=2, column=0, sticky=NW)


#buttons moves pokémon 1
def p1_attack1():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 1'))
def p1_attack2():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 2'))
def p1_attack3():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 3'))
def p1_attack4():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 4'))

pokemon_1_move_1 = Button(left, padx=100, pady= 1, text='attack 1', command=p1_attack1, bg='red')
pokemon_1_move_1.grid(row=3, column=0,sticky=W )

pokemon_1_move_2 = Button(left, padx=100, pady= 1, text='attack 2', command=p1_attack2, bg='red')
pokemon_1_move_2.grid(row=3, column=1,sticky=W)

pokemon_1_move_3 = Button(left, padx=100, pady= 1, text='attack 3', command=p1_attack3, bg='red')
pokemon_1_move_3.grid(row=4, column=0, sticky=W)

pokemon_1_move_4 = Button(left, padx=100, pady= 1, text='attack 4', command=p1_attack4, bg='red')
pokemon_1_move_4.grid(row=4, column=1, sticky=W)

#buttons moves pokémon 2
def p2_attack1():
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 1'))
def p2_attack2():
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 2'))
def p2_attack3():
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 3'))
def p2_attack4():
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 4'))

pokemon_2_move_1 = Button(right, padx=100, pady= 1, text='attack 1', command=p2_attack1, bg='blue')
pokemon_2_move_1.grid(row=3, column=0,sticky=W )

pokemon_2_move_2 = Button(right, padx=100, pady= 1, text='attack 2', command=p2_attack2,  bg='blue')
pokemon_2_move_2.grid(row=3, column=1,sticky=W)

pokemon_2_move_3 = Button(right, padx=100, pady= 1, text='attack 3', command=p2_attack3, bg='blue')
pokemon_2_move_3.grid(row=7, column=0, sticky=W)

pokemon_2_move_4 = Button(right, padx=100, pady= 1, text='attack 4', command=p2_attack4, bg='blue')
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
