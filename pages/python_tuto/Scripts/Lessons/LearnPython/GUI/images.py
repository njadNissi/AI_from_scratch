from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Anjie_njad')
#root.iconbitmap('c:/')

#button_quit = Button(root, text="Quit", command=root.quit).pack()

my_img = ImageTk.PhotoImage(Image.open("gui/image.png"))
my_label = Label(image=my_img).pack()

root.mainloop()