from cgitb import text
from struct import pack
from tkinter import *

from numpy import place

root = Tk()
root.title("GUI in Python")
root.geometry("300x250")

ismarried = IntVar()

ismarried_chkbtn = Checkbutton(
    text="Single/Married", variable=ismarried).pack()

ismarried_lbl = Label(textvariable=ismarried)
ismarried_lbl.place(relx=.5, rely=.5, anchor="c")  # c:center, n:north etc...

root.mainloop()
