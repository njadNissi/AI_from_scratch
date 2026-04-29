from tkinter import *

root = Tk()
root.title("Dictuionary of radioButtons")
root.geometry("300x280")

header = Label(text="Select course", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)


languages = [("Python", 0), ("C#", 1), ("JS", 2), ("Java", 3)]


def select():
    l = language.get()
    selected.config(text="selected " + languages[l][0])


language = IntVar()

row = 1
for txt, val in languages:
    Radiobutton(text=txt, value=val, variable=language,
                padx=15, pady=10, command=select).grid(row=row, sticky=W)
    row += 1


selected = Label(padx=15, pady=10)
selected.grid(row=row, sticky=W)

root.mainloop()
