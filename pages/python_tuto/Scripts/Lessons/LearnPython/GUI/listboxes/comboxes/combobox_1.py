from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.geometry("250x200")

languages = ["Python", "C#", "Java", "JS"]
combobox = ttk.Combobox(values=languages)
combobox.pack(anchor=NW, padx=6, pady=6)


root.mainloop()
