from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.state('zoomed')

root.grid_columnconfigure(0, weight=1, uniform="group1")
root.grid_columnconfigure(1, weight=1, uniform="group1")
root.grid_rowconfigure(0, weight=1)

left = Frame(root)
right = Frame(root)
left.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)
right.grid(row=0, column=1, sticky="nsew", padx=40, pady=40)

# Label content
pokemon_1_var = StringVar(root)
pokemon_1_var.set("Pokemon 1")
pokemon_2_var = StringVar(root)
pokemon_2_var.set("Pokemon 2")

pokemon_1 = OptionMenu(left, pokemon_1_var, 'Hillary Clintcunt', 'Hillary', 'Hillary_1')
pokemon_2 = OptionMenu(right, pokemon_2_var, 'Donald Trumpcunt', 'Trump', 'Trump_1')
pokemon_1.grid(row=0, column=0)
pokemon_2.grid(row=0, column=0)

image_1 = Image.open('h.jpg')
image_2 = Image.open('t.jpeg')
pokemon_1_img_load = ImageTk.PhotoImage(image_1)
pokemon_2_img_load = ImageTk.PhotoImage(image_2)
pokemon_1_img = Label(left, image=pokemon_1_img_load)
pokemon_2_img = Label(right, image=pokemon_2_img_load)
pokemon_1_img.grid(row=1, column=0)
pokemon_2_img.grid(row=1, column=0)

pokemon_1_type = Label(left, text='corrupted cunt')
pokemon_2_type = Label(right, text='cretin')
pokemon_1_type.grid(row=2, column=0)
pokemon_2_type.grid(row=2, column=0)

pokemon_1_moves = ['1', '2', '3', '4', '5', '6']
pokemon_2_moves = ['1', '2', '3', '4', '5', '6']

c = 3
for i in pokemon_1_moves:
    i = Label(left, text=i)
    i.grid(row=c, column=0)
    c += 1

c = 3
for i in pokemon_2_moves:
    i = Label(right, text=i)
    i.grid(row=c, column=0)
    c += 1


# Start functie
def callback():
    print('THE FIRST POKEMON IS: ' + pokemon_1_var.get().upper() + '!')
    print('THE SECOND POKEMON IS: ' + pokemon_2_var.get().upper() + '!')


start = Button(text="Start", command=callback)
start.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
