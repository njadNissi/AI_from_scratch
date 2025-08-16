from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Python")
root.geometry("250x200")


def change(newVal):
    label["text"] = newVal


label = ttk.Label()
label.pack(anchor="center")

vScale = ttk.Scale(orient=HORIZONTAL, length=200,
                   from_=1.0, to=100.0, command=change)
vScale.pack(anchor=NW)


root.mainloop()
