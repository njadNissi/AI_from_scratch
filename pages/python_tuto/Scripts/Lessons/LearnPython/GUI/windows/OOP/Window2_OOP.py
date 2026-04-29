from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Main Window, ID: " + root. winfo_id().__str__())
root.geometry("350x200")


def click():
    window = Tk()
    window.title("Window ID: " + window.winfo_id().__str__())
    window.geometry("350x200")
    label = ttk.Label(window, text="Completely new window")
    label.pack(anchor=CENTER, expand=1)

    close_button = ttk.Button(
        window, text="Close window", command=lambda: window.destroy())
    close_button.pack(anchor=CENTER, expand=1)


button = ttk.Button(text="Create window", command=click)
button.pack(anchor=CENTER, expand=1)


def all_children():
    # list root.children
    for child in root.winfo_children():
        if type(child) is ttk.Button:
            print(str(child.info))


button = ttk.Button(text="all children", command=all_children)
button.pack(anchor=CENTER, expand=1)

root.mainloop()
