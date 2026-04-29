from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Menu")
root.geometry("250x200")

main_menu = Menu()
main_menu.add_cascade(label='File')
main_menu.add_cascade(label='Edit')
main_menu.add_cascade(label='View')

root.config(menu=main_menu)


root.mainloop()
