from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Python")
root.geometry("250x200")


def selected(event):
    selection = combobox.get()
    print(selection)
    label["text"] = f"You selected: {selection}"


languages = ["Python", "C#", "Java", "JS"]
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

combobox = ttk.Combobox(values=languages, state="readonly")
combobox.pack(anchor=NW, fill=X, padx=5, pady=6)
combobox.bind("<<ComboboxSelected>>", selected)


root.mainloop()
