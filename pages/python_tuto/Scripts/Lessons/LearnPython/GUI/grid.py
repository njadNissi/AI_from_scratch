from tkinter import *

root = Tk()

#creating a label widget
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Joao Andre!")
myLabel3 = Label(root, text="                      ")

#shoving it onto the screen
myLabel3.grid(row=1, column=1)
myLabel2.grid(row=1, column=2)

root.mainloop()
