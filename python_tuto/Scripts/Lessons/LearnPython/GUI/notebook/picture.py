from cgitb import text
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Menu")
root.geometry("250x200")

notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)


frame1 = ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
notebook.add(frame1, text="Python")

frame2 = ttk.Frame(notebook)
frame2.pack(fill=BOTH, expand=True)
notebook.add(frame2, text="Java")

btn = Button(frame1, text="mybt").place(relx=0.3, rely=0.3)
entry = Entry(frame2, text="mybt").place(relx=0.5, rely=0.5)

java_logo = PhotoImage(file="./java.png")
py_logo = PhotoImage(file="./python.png")

notebook.add(frame1, text="Java", image=java_logo)
notebook.add(frame2, text="Python", image=py_logo)

root.mainloop()
