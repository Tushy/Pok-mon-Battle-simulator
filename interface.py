from tkinter import *
from PIL import Image, ImageTk

import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

# Label content
pokemon_1_var = StringVar(root)
pokemon_2_var = StringVar(root)
pokemon_1_var.set('Pokemon 1')
pokemon_2_var.set('Pokemon 2')

pokemon_1 = OptionMenu(left, pokemon_1_var, 'Hillary Clintcunt', 'Hillary', 'Hillary_1')
pokemon_2 = OptionMenu(right, pokemon_2_var, 'Donald Trumpcunt', 'Trump', 'Trump_1')
pokemon_1.grid(row=0, column=0, sticky=NW)
pokemon_2.grid(row=0, column=0, sticky=NW)

image_1 = Image.open('h.jpg')
image_2 = Image.open('t.jpeg')
image_1 = image_1.resize((int(width * 0.25), int(height * 0.25)), Image.ANTIALIAS)
image_2 = image_2.resize((int(width * 0.25), int(height * 0.25)), Image.ANTIALIAS)
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

pokemon_1_stats = ('HP', 'Attack', 'Defense', 'Speed', 'SP Attack', 'SP Defense')[::-1]
y_pos = np.arange(len(pokemon_1_stats))
performance = [100, 53, 45, 23, 87, 94]

fig = plt.figure(1)
fig.patch.set_alpha(0)
fig.add_subplot(111).patch.set_alpha(0)
plt.barh(y_pos, performance, align='center', alpha=.5)
plt.yticks(y_pos, pokemon_1_stats)

canvas = FigureCanvasTkAgg(fig, master=left)
canvas.get_tk_widget().config(width=width * 0.25, height=height * 0.25)
canvas.get_tk_widget().grid(row=1, column=1, sticky=NW)

'''
pokemon_1_stats = ['1', '2', '3', '4']
pokemon_2_stats = ['1', '2', '3', '4']
pokemon_1_stats = Label(left, text='\n\n'.join(pokemon_1_stats))
pokemon_2_stats = Label(right, text='\n\n'.join(pokemon_2_stats))
pokemon_1_stats.grid(row=1, column=1, sticky=NW)
pokemon_2_stats.grid(row=1, column=1, sticky=NW)
'''

pokemon_1_moves = ['1', '2', '3', '4']
pokemon_2_moves = ['1', '2', '3', '4']

c = 3
for i in pokemon_1_moves:
    i = Label(left, text=i)
    i.grid(row=c, column=0, sticky=NW)
    c += 1

c = 3
for i in pokemon_2_moves:
    i = Label(right, text=i)
    i.grid(row=c, column=0, sticky=NW)
    c += 1


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
