from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Python")
root.geometry("250x200")

val = IntVar(value=50)

ttk.Label(textvariable=val).pack(anchor="center")

hScale = ttk.Scale(orient=HORIZONTAL, length=200,
                   from_=1.0, to=100.0, variable=val)
hScale.pack(anchor=NW)

root.mainloop()
