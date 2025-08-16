from tkinter import *
import tkinter

root = tkinter.Tk()
root.title('Human Machine Interface')
root.geometry('400x300+300+250')  # width x height + X + Y

btn = Button(text="Hello")
btn.pack()

photo = PhotoImage(file=r"image.png")
btn1 = Button(text="Hello",
              background="#555",
              foreground="#ccc",
              padx="20",
              pady="8",
              font="16",
              image=photo,
              compound=LEFT
              )
btn1.pack()

btn2 = Button(text="Hello")
btn2.place(x="150", y="150")  # with this no need of packing

root.mainloop()
