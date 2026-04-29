from tkinter import *
from tkinter import ttk
import tkinter as tk
import queue
from PIL import Image, ImageTk
import time

class Window():

    def __init__(self, title:str, size:str, image_path:str) -> None:
        self.title = title
        self.size = size
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root, column=("c0", "c1", "c2"), height=40)
        self.label = tk.Label(self.root, text="Smart voice Control")
        self.ac_label = tk.Label(self.root)
        self.ac_canvas = Canvas(self.root, width=200, height=160)#int(size.split('x')[0])
        self.gif_image = Image.open(image_path)
        self.gif_frames = []
        self.speech_no = 0
        # initializations
        self.__path_to_frames()
        self.__customize_window()


    def __customize_window(self) -> None:
        self.root.title(self.title)
        self.root.geometry(self.size)
        

        # style
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TreeView", background="lightblue", fieldbackground="grey", foreground="yellow")
        style.configure("TreeView.heading", background="lightgray", foreground="black")

        # treeview
        col_names = ("ID", "Speech Command", "Devices involved", "Actions")
        for i in range(len(col_names)):
            self.tree.column("#" + str(i), anchor=CENTER)
            self.tree.heading("#" + str(i), text=col_names[i])

        # packing
        self.label.pack()
        self.ac_label.pack()
        self.ac_canvas.pack()
        self.tree.pack(fill=tk.BOTH, expand=True)


    def __path_to_frames(self):
        for i in range(self.gif_image.n_frames):
            self.gif_image.seek(i)
            self.gif_frames.append(ImageTk.PhotoImage(self.gif_image.resize((200, 180))))


    def showGUI(self) -> None:
        self.__animate_gif(frame_number=0)
        self.root.mainloop()

    def close(self):
        self.root.destroy()
        print('Window Closed!')


    def update_cmds(self, input_buffer:queue.Queue) -> None:

        while True:
            try:
                speech, commands, actions = input_buffer.get(timeout=1)
                self.speech_no += 1
                self.tree.insert('', 0, values=(speech, '', ''),
                                    text='S' + str(self.speech_no))
            
                for i in range(len(commands)):
                    try:
                        self.tree.insert('', 0, values=(commands[i], actions[i][0], actions[i][1]),
                                        text='A' + str(len(self.tree.get_children("")) +1 - self.speech_no))
                    except IndexError:
                        print('Index Error')
                
                self.root.update()
            
            except queue.Empty:
                print('Waiting...', end='\r')
            time.sleep(.1)

    
    def __animate_gif(self, frame_number:int) -> None:

        self.ac_canvas.delete(ALL)
        self.ac_canvas.create_image(0, 0, anchor=NW, image=self.gif_frames[frame_number])
        time_delay = self.gif_image.info['duration']
        self.ac_label.after(time_delay,
                            lambda: self.__animate_gif((frame_number + 1)%len(self.gif_frames)))
                    
                    

if __name__=="__main__":
    
    Window(size="400x300", title="Smart-IoT-Home", image_path="img/ac.gif").showGUI()