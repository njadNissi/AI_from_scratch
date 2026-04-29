from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Anjie-Plots')
root.geometry("600x100")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
   # plt.pie(house_prices)
   #plt.polar(house_prices)
    plt.show()

my_button = Button(root, text="Graph It!", command=graph).pack()

root.mainloop()
