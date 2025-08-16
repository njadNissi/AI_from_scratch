from tkinter import *


def delete():
    selection = languages_listbox.curselection()
    languages_listbox.delete(selection[0])


def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)


root = Tk()
root.title("Gui for listbox")
root.geometry("300x280")

languages_listbox = Listbox()
languages_listbox.grid(row=0, column=1,
                       sticky=W+E, padx=5, pady=5)  # column=0

languages = ["Python", "JS", "C#", "Java"]

language_entry = Entry(width=250)
language_entry.grid(row=1, column=0, columnspan=2, pady=6)


Button(text="Add", command=add).grid(
    row=2, column=0, padx=6, pady=6)
Button(text="Remove", command=delete).grid(
    row=2, column=1, padx=6, pady=6)


root.mainloop()
