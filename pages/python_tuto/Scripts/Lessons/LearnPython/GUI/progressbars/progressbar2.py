from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Python")
root.geometry("250x200")

val = IntVar(value=50)

ttk.Progressbar(orient="horizontal", variable=val).pack(fill=X, padx=6, pady=6)


root.mainloop()
