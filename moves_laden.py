import time
from tkinter import *
from threading import Thread

root = Tk()
root.wm_title('PBS - Pokémon Battle Station')
root.state('zoomed')

# Label aanmaken
kek_label = Label(text='kek')
kek_label.pack()

def kek():
    # Functie aanmaken voor threading
    c = 0
    while 1:
        if c != 4:
            kek_label.config(text='De pokemon moves ophalen' + c * '.')
            c += 1
            time.sleep(1)
        else:
            c = 0

# Start de thread
thread = Thread(target=kek)
thread.start()

root.mainloop()
