from tkinter import *
from tkinter import ttk


root = Tk()
root.tile('Spinbox')
root.geometry("250x200")


def change():
    label['text'] = spinbox.get()


label = ttk.Label()
label.pack(anchor=NW)

spinbox = ttk.Spinbox(from_=1.0, to=100.0)
spinbox.pack(anchor=NW)

root.mainloop()
