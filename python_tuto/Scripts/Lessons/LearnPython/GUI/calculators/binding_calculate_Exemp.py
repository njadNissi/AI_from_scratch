from tkinter import *

root = Tk()
root.title("GUI via Python")


def click_button():
    res.set(a.get() + b.get())


# these binding could be defined before the click function
a = IntVar()
b = IntVar()
res = IntVar()
res.set(0)  # inialize to zero

a_label = Label(text="Operand 1").grid(row=0, column=0)
a_entry = Entry(textvariable=a).grid(row=0, column=1)

b_label = Label(text="Operand 2").grid(row=1, column=0)
b_entry = Entry(textvariable=b).grid(row=1, column=1)

btn = Button(text="calculate", command=click_button).grid(
    row=2, column=0, columnspan=2)

res_label = Label(text="result").grid(row=3, column=0)
res_entry = Entry(textvariable=res).grid(row=3, column=1)

root.mainloop()
