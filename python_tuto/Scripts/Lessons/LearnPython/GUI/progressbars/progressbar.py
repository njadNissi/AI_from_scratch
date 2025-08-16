from tkinter import *
from tkinter import ttk
from turtle import color


root = Tk()
root.title("Python")
root.geometry("250x200")

val = IntVar(value=50)


ttk.Scale(orient=HORIZONTAL, length=200,
          from_=1.0, to=100.0, variable=val).pack(anchor=NW)

ttk.Progressbar(orient="vertical", length=100, value=40).pack(pady=5)

ttk.Progressbar(orient="horizontal", length=150, value=val).pack(pady=5)


root.mainloop()
