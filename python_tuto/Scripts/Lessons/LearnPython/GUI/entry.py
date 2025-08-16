from cgitb import text
from tkinter import *

root = Tk()

# title and instruction labels
myLabelTitle = Label(root, text="READ BOOK STACK")
myLabelTitle.pack()
myLabelTask = Label(root, text="Enter a book you read:")
myLabelTask.pack()

# entry widget
# for bordering: borderwidth=2
entry = Entry(root, width=50)
#e.insert(0, "enter a book you read")
entry.pack()

bookno = 0


def myClick():
    global bookno
    bookno += 1
    myLabel = Label(text=str(bookno) + ". " + entry.get())
    myLabel.pack()


# creating a button widget; state=DISABLED, for resize : padx=x; pady=y; fg="blue"; bg="red"
myButton = Button(text="Add your book!",
                  command=myClick, fg="blue", bg="red")
myButton.pack()

myLabelList = Label(text="This is your Library:")
myLabelLine = Label(text="----------------------------------")
root.mainloop()
