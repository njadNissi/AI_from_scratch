from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Old/Main window')
root.geometry("300x250")

windows = []


def click():
    window = Tk()
    windows.append(window)
    window.title('Main Window ' + str(len(windows)))
    window.geometry("250x250")
    label = ttk.Label(window, text="window " + str(len(windows)))
    label.pack(anchor=CENTER, expand=1)


button = ttk.Button(text="create Window", command=click)
button.pack(anchor=CENTER, expand=1)


root.mainloop()
