from tkinter import *
from PIL import Image, ImageTk
from all_pokemon_to_file import get_pokemons
from app import algemeen, list_of_pokemon

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
def p1_attack1():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 1'))
def p1_attack2():
    listbox.insert('0', str(pokemon_1_var.get().upper() + ' is using attack 2'))
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
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 1'))
def p2_attack2():
    listbox.insert('0', str(pokemon_2_var.get().upper() + ' is using attack 2'))
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
