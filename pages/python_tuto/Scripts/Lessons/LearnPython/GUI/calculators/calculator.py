from cgitb import text
from ctypes.wintypes import SIZE
from tkinter import *
from turtle import width

win = Tk()
win.configure(background="light gray")
win.title("Anjie Calculator")

# entry widget
screen = Entry(win, width=50, borderwidth=1)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

result = 0
num1 = 0
num2 = 0
operation = ""
# operations


def press(num):
    current = screen.get()
    screen.delete(0, END)  # delete all
    screen.insert(0, current + num)


def add():
    global num1
    num1 = float(screen.get())
    screen.delete(0, END)
    global operation
    operation = "add"


def subtract():
    global num1
    num1 = float(screen.get())
    screen.delete(0, END)
    global operation
    operation = "subtract"


def multiply():
    global num1
    num1 = float(screen.get())
    screen.delete(0, END)
    global operation
    operation = "multiply"


def divide():
    global num1
    num1 = float(screen.get())
    screen.delete(0, END)
    global operation
    operation = "divide"


def calculate():
    global num2
    num2 = float(screen.get())
    screen.delete(0, END)
    global operation

    if operation == "add":
        screen.insert(0, num1+num2)
    elif operation == "subtract":
        screen.insert(0, num1-num2)
    elif operation == "multiply":
        screen.insert(0, num1*num2)
    elif operation == "divide":
        screen.insert(0, num1/num2)


def clrAll():
    screen.delete(0, END)


# define buttons for chars
pad_x = 40
pad_y = 20
# functions buttons
button_clr = Button(win, text="clr", padx=132, pady=pad_y,
                    command=clrAll).grid(row=1, column=0, columnspan=3)

# operations buttons
button_div = Button(win, text="/", padx=pad_x-1, pady=pad_y, bg='gray', fg='white',
                    command=divide).grid(row=1, column=3)
button_prod = Button(win, text="*", padx=pad_x-1, pady=pad_y, bg='green', fg='white',
                     command=multiply).grid(row=2, column=3)
button_sub = Button(win, text="-", padx=pad_x, pady=pad_y, bg='yellow',
                    command=subtract).grid(row=3, column=3)
button_add = Button(win, text="+", padx=pad_x-1, pady=pad_y, bg='blue', fg='white',
                    command=add).grid(row=4, column=3)
button_dot = Button(win, text=".", padx=pad_x+1, pady=pad_y,
                    comman=lambda: press(".")).grid(row=5, column=1)
button_eq = Button(win, text="=", padx=89, pady=pad_y-2, bg='red', fg='white',
                   command=calculate).grid(row=5, column=2, columnspan=2)

# digit buttons
button9 = Button(win, text="9", padx=pad_x, pady=pad_y,
                 command=lambda: press("9")).grid(row=2, column=2)
button8 = Button(win, text="8", padx=pad_x, pady=pad_y,
                 command=lambda: press("8")).grid(row=2, column=1)
button7 = Button(win, text="7", padx=pad_x, pady=pad_y,
                 command=lambda: press("7")).grid(row=2, column=0)
button6 = Button(win, text="6", padx=pad_x, pady=pad_y,
                 command=lambda: press("6")).grid(row=3, column=2)
button5 = Button(win, text="5", padx=pad_x, pady=pad_y,
                 command=lambda: press("5")).grid(row=3, column=1)
button4 = Button(win, text="4", padx=pad_x, pady=pad_y,
                 command=lambda: press("4")).grid(row=3, column=0)
button3 = Button(win, text="3", padx=pad_x, pady=pad_y,
                 command=lambda: press("3")).grid(row=4, column=2)
button2 = Button(win, text="2", padx=pad_x, pady=pad_y,
                 command=lambda: press("2")).grid(row=4, column=1)
button1 = Button(win, text="1", padx=pad_x, pady=pad_y,
                 command=lambda: press("1")).grid(row=4, column=0)
button0 = Button(win, text="0", padx=pad_x, pady=pad_y,
                 command=lambda: press("0")).grid(row=5, column=0)

win.mainloop()
