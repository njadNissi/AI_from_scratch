from tkinter import *

root = Tk()
root.title("Check button")
root.geometry("300x250")

python_lang = IntVar()
python_chkbtn = Checkbutton(
    text="Python", variable=python_lang, onvalue=1, offvalue=0, padx=15, pady=10)
python_chkbtn.grid(row=0, column=0)

java_lang = IntVar()
java_chkbtn = Checkbutton(
    text="Java", variable=python_lang, onvalue=1, offvalue=0, padx=15, pady=10)
java_chkbtn.grid(row=1, column=0, sticky=W)


root.mainloop()
