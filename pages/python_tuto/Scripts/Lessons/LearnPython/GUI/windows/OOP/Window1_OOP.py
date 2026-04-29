import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class Window (tk.Tk):
    def __init__(self, msg):
        super().__init__()
        self.message = msg

# configure the root window
        self.title('My Window in OOP')
        self.geometry('300x250')

    # label
        self.label = ttk.Label(self, text='Hi, OOP!')
        self.label.pack()

    # button
        self.button = ttk.Button(self, text='Press me!')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title='Information', message=self.message)


if __name__ == "__main__":
    window1 = Window('OOP is just nice!')
    window2 = Window('Programming is just fun!')

    window1.mainloop()
    window2.mainloop()
