from tkinter import *

root = Tk()
root.title("Gui for listbox")
root.geometry("300x280")

languages = ["Python", "JS", "C#", "Java"]
languages_var = StringVar(value=languages)

languages_listbox = Listbox(listvariable=languages_var, selectmode=EXTENDED)
languages_listbox.pack(expand=1, fill=BOTH)
languages_listbox.select_set(first=1, last=2)

root.mainloop()
