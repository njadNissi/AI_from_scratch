from pydoc import cli
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Gui the Python")
root.geometry("300x250")


clicks = 0


def myClick():
    global clicks
    clicks += 1
    myButton.config(text="Clicks {}".format(clicks))


# creating a button widget; state=DISABLED, for resize : padx=x; pady=y; fg="blue"; bg="red"
# you add root as 1st arg or just pack it later.
myButton = Button(text="Clicks 0",  # initial text
                  background="#555",
                  foreground="#ccc",
                  padx="20",
                  pady="8",
                  font="16",
                  command=myClick,
                  fg="blue",
                  bg="red")
myButton.pack()

root.mainloop()
