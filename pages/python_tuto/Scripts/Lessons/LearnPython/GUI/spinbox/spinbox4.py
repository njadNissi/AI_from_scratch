from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Spinbox')
root.geometry("250x200")

spinbox_var = StringVar()

languages = ["Python", "JS", "C#", "Java", "C++"]

label = ttk.Label(textvariable=spinbox_var)
label.pack(anchor=NW)

spinbox = ttk.Spinbox(from_=1.0, to=100.0)
spinbox.pack(anchor=NW)

root.mainloop()
