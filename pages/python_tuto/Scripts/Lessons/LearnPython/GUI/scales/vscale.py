from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Python")
root.geometry("250x200")

val = IntVar(value=50)

ttk.Label(textvariable=val).pack(anchor="center")

vScale = ttk.Scale(orient=VERTICAL, length=200,
                   from_=1.0, to=100.0, variable=val)
vScale.pack(anchor="center")

root.mainloop()
