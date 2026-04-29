from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Python")
root.geometry("250x200")

val = IntVar()


progressbar = ttk.Progressbar(
    orient="horizontal", variable=val).pack(fill=X, padx=6, pady=6)

label = ttk.Label(textvariable=val)
label.pack(anchor=NW, padx=6, pady=6)


def start(): progressbar.start(500)


def stop(): progressbar.stop()


def step(): progressbar.step(2)


startBtn = ttk.Button(text="Start", command=start)
startBtn.pack(anchor=SW, side=LEFT, padx=6, pady=6)
stopBtn = ttk.Button(text="Stop", command=step)
stopBtn.pack(anchor=SE, side=RIGHT, padx=6, pady=6)

stepBtn = ttk.Button(text="Step", command=step)
stepBtn.pack(anchor=SE, side=BOTTOM, padx=6, pady=6)


root.mainloop()
