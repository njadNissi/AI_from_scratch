from tkinter import *
from tkinter import messagebox

clicks = 0


def myClick():
    global clicks
    clicks += 1
    buttonText.set("clicks {}".format(clicks))


root = Tk()
root.title("Gui the Python")
root.geometry("300x250")

buttonText = StringVar()
buttonText.set("clicks {}".format(clicks))  # set initial button text

# creating a button widget; state=DISABLED, for resize : padx=x; pady=y; fg="blue"; bg="red"
# you add root as 1st arg or just pack it later.
myButton = Button(textvariable=buttonText,
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
