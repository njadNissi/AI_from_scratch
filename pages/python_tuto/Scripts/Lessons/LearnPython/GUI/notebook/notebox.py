from cgitb import text
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Menu")
root.geometry("250x200")

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)


frame1 = ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
notebook.add(frame1, text="Python")

frame2 = ttk.Frame(notebook)
frame2.pack(fill=BOTH, expand=True)
notebook.add(frame2, text="Java")


root.mainloop()
