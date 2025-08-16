from tkinter import *

root = Tk()
root.title("Gui with Python")
root.geometry("300x250")

label1 = Label(text="Hello Python, I am Label", fg="#eee", bg="#333")
label1.pack()

poetry = "Here is the thought to which I am devoted,"

label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.3)

root.mainloop()
