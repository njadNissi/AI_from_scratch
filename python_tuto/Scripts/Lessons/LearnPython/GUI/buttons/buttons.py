from tkinter import *
from tkinter import messagebox

root = Tk()

clicks = 0


def myClick():
    global clicks
    clicks += 1
    messagebox.showinfo("Gui Python", "Clicked the Button")
    root.title('Clicks{}'.format(clicks))
    # the root arg is optional
    myLabel = Label(root, text="Look! I clicked a button!")
    myLabel.pack()


# creating a button widget; state=DISABLED, for resize : padx=x; pady=y; fg="blue"; bg="red"
# you add root as 1st arg or just pack it later.
myButton = Button(text="Click me!",
                  background="#555",
                  foreground="#ccc",
                  padx="20", pady="8",
                  font="16",
                  command=myClick,
                  fg="blue", bg="red")
myButton.pack()

root.mainloop()
