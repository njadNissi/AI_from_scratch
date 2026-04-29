from tkinter import *

languages = ["Python", "JS", "C#", "Java"]

root = Tk()
root.title("Gui for listbox")
root.geometry("300x280")


languages_listbox = Listbox()

for language in languages:
    languages_listbox.insert(END, language)


languages_listbox.pack()

root.mainloop()
