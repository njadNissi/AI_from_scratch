from tkinter import *

root = Tk()
root.title("Radio button")
root.geometry("300x250")

header = Label(text="Select course", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

lang = IntVar()

python_radiobtn = Radiobutton(
    text="Python", value=1, variable=lang, padx=15, pady=10)
python_radiobtn.grid(row=1, column=0, sticky=W)

java_radiobtn = Radiobutton(
    text="Java", value=2, variable=lang, padx=15, pady=10)
java_radiobtn.grid(row=2, column=0, sticky=W)

selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=3, column=0, sticky=W)

root.mainloop()
