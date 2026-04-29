from cgitb import text
from tkinter import *
from tkinter import messagebox
from tokenize import Double
from unittest import result

root = Tk()
# entry widget
# for bordering: borderwidth=2
entry1 = Entry(root, width=50)
entry2 = Entry(root, width=50)
entry3 = Entry(root, width=50)
entry1.pack()
entry2.pack()
entry3.pack()

myLabel = Label(text="result")
myLabel.pack()

# e.insert(0, "enter a book you read") # set text in an entr


def myClick():
    result = int(entry1.get()) + int(entry2.get())
    entry3.insert(END, str(result))  # result in an entry
    myLabel.config(text="result {}".format(result))  # result on a label
    messagebox.showinfo("result", str(result))  # result in a message box


# creating a button widget; state=DISABLED, for resize : padx=x; pady=y; fg="blue"; bg="red"
myButton = Button(root, text="calculate",
                  command=myClick, fg="blue", bg="red")
myButton.pack()

root.mainloop()
