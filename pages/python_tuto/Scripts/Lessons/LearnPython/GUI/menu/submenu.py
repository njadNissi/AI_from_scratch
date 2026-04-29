from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Menu")
root.geometry("250x200")

main_menu = Menu()

#file_menu = Menu(font=("Verdana", 13, "bold"), tearoff=0)
file_menu = Menu()
file_menu.add_cascade(label='New')
file_menu.add_cascade(label='Save')
file_menu.add_cascade(label='Open')
file_menu.add_separator()
file_menu.add_cascade(label='Exit')

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit')
main_menu.add_cascade(label='View')

root.config(menu=main_menu)


root.mainloop()
