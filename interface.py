from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.wm_title('PBS - Pokémon Battle Station')
root.state('zoomed')

root.grid_columnconfigure(0, weight=1, uniform='HALF')
root.grid_columnconfigure(1, weight=1, uniform='HALF')
root.grid_rowconfigure(0, weight=1)

height = root.winfo_screenheight()
width = root.winfo_screenwidth()

left = Frame(root, height=height * 0.75, bd=5, relief=SUNKEN)
right = Frame(root, height=height * 0.75, bd=5, relief=SUNKEN)
bottom = Frame(root, height=height * 0.25, bd=5, relief=SUNKEN)
left.grid(row=0, column=0, sticky='nesw', padx=40, pady=(40, 20))
right.grid(row=0, column=1, sticky='nesw', padx=40, pady=(40, 20))
bottom.grid(row=1, columnspan=2, sticky='nesw', padx=40, pady=(20, 40))

#background


image_background = Image.open('t.jpeg')


# Label content
pokemon_1_var = StringVar(root)
pokemon_2_var = StringVar(root)
pokemon_1_var.set('Kies Pokémon 1')
pokemon_2_var.set('Kies Pokémon 2')

pokemon_1 = OptionMenu(left, pokemon_1_var, 'Hillary Clintcunt', 'Hillary', 'Hillary_1')
pokemon_2 = OptionMenu(right, pokemon_2_var, 'Donald Trumpcunt', 'Trump', 'Trump_1', 'kut pokemon')
pokemon_1.grid(row=0, column=0, sticky=NW)
pokemon_2.grid(row=0, column=0, sticky=NW)

image_1 = Image.open('h.jpg')
image_2 = Image.open('t.jpeg')
image_1 = image_1.resize((int(width * 0.1), int(height * 0.1)), Image.ANTIALIAS)
image_2 = image_2.resize((int(width * 0.1), int(height * 0.1)), Image.ANTIALIAS)
pokemon_1_img_load = ImageTk.PhotoImage(image_1)
pokemon_2_img_load = ImageTk.PhotoImage(image_2)
pokemon_1_img = Label(left, image=pokemon_1_img_load)
pokemon_2_img = Label(right, image=pokemon_2_img_load)
pokemon_1_img.grid(row=1, column=0, sticky='nesw')
pokemon_2_img.grid(row=1, column=0, sticky='nesw')

pokemon_1_type = Label(left, text='Corrupted cunt')
pokemon_2_type = Label(right, text='Cretin')
pokemon_1_type.grid(row=2, column=0, sticky=NW)
pokemon_2_type.grid(row=2, column=0, sticky=NW)

# Stats kek







pokemon_1_stats = ('HP', 'Attack Power')
pokemon_2_stats = ('HP', 'Attack Power')
pokemon_1_stats = Label(left, text='\n\n'.join(pokemon_1_stats))
pokemon_2_stats = Label(right, text='\n\n'.join(pokemon_2_stats))
pokemon_1_stats.grid(row=1, column=1, sticky=NW)
pokemon_2_stats.grid(row=1, column=1, sticky=NW)


def p1_attack1():
    text_box.config(text='Pokemon 1 uses attack 1', justify=LEFT)
def p1_attack2():
    text_box.config(text='Pokemon 1 uses attack 2', justify=LEFT)
def p1_attack3():
    text_box.config(text='Pokemon 1 uses attack 3', justify=LEFT)
def p1_attack4():
    text_box.config(text='Pokemon 1 uses attack 4', justify=LEFT)

pokemon_1_move_1 = Button(left, padx=110, pady= 20, text='attack 1', command=p1_attack1)
pokemon_1_move_1.grid(row=3, column=0,sticky=W )

pokemon_1_move_2 = Button(left, padx=110, pady= 20, text='attack 2', command=p1_attack2)
pokemon_1_move_2.grid(row=3, column=1,sticky=W)

pokemon_1_move_3 = Button(left, padx=110, pady= 20, text='attack 3', command=p1_attack3)
pokemon_1_move_3.grid(row=4, column=0, sticky=W)

pokemon_1_move_4 = Button(left, padx=110, pady= 20, text='attack 4', command=p1_attack4)
pokemon_1_move_4.grid(row=4, column=1, sticky=W)


def p2_attack1():
    text_box.config(text='Pokemon 2 uses attack 1', justify=LEFT)
def p2_attack2():
    text_box.config(text='Pokemon 2 uses attack 2', justify=LEFT)
def p2_attack3():
    text_box.config(text='Pokemon 2 uses attack 3', justify=LEFT)
def p2_attack4():
    text_box.config(text='Pokemon 2 uses attack 4', justify=LEFT)

pokemon_2_move_1 = Button(right, padx=100, pady= 20, text='attack 1', command=p2_attack1)
pokemon_2_move_1.grid(row=3, column=0,sticky=W )

pokemon_2_move_2 = Button(right, padx=100, pady= 20, text='attack 2', command=p2_attack2)
pokemon_2_move_2.grid(row=3, column=1,sticky=W)

pokemon_2_move_3 = Button(right, padx=100, pady= 20, text='attack 3', command=p2_attack3)
pokemon_2_move_3.grid(row=4, column=0, sticky=W)

pokemon_2_move_4 = Button(right, padx=100, pady= 20, text='attack 4', command=p2_attack4)
pokemon_2_move_4.grid(row=4, column=1, sticky=W)

# Start functie
def callback():
    text_box.config(
        text='THE FIRST POKEMON IS: ' + pokemon_1_var.get().upper() + '!\nTHE SECOND POKEMON IS: ' + pokemon_2_var.get().upper() + '!',
        justify=LEFT)


start = Button(text='Start', command=callback)
start.place(relx=0.5, rely=0.5, anchor=CENTER)

text_box = Label(bottom, text='TEXT BOX KEK', height=5)
text_box.grid(padx=20, pady=20, sticky=NW)

root.mainloop()
