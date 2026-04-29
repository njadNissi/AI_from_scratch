from tkinter import *

root = Tk()

# creating a label widget
myLabel = Label(root, text="Je t'aime!")

# shoving it onto the screen just as big is it is
# # and the resize of window afects the location
myLabel.pack()

root.mainloop()
