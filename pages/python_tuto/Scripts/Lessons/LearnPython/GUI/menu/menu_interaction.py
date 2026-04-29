from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def edit_click():
    messagebox.showinfo("GUI Python", "Clicked option Edit")


root = Tk()
root.title("Menu")
root.geometry("250x200")

main_menu = Menu()
main_menu.add_cascade(label='File')
main_menu.add_cascade(label='Edit', command=edit_click)
main_menu.add_cascade(label='View')

root.config(menu=main_menu)


root.mainloop()
