"""
    A HMI for IoT devices an AC and a lamp
    Author: Ndombasi Diakusala Joao Andre
    Date: October 3rd, 2024
"""
from tkinter import *
from tkinter import ttk
import tkinter as tk
import queue
from PIL import Image, ImageTk
import time
import serial
import random as rd
from threading import Thread


class Window():

    def __init__(self, title:str, size:str) -> None:
        self.title = title
        self.size = size
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root, column=("c0", "c1", "c2"), height=40)
        self.title_label = tk.Label(self.root, text="Smart IoT-Devices HMI")
        self.ac_image_paths = ["img/ac-off.png", "img/ac-on.png"]
        self.led_image_paths = ["img/led-off.png", "img/led-on.png"]
        
        self.speech_no = 0
        self.queue = queue.Queue()
        
        # initializations
        self.__customize_window()


    def __customize_window(self) -> None:
        self.root.title(self.title)
        # self.root.geometry(self.size)
        self.title_label.grid(row=0, column=0)

        self.ac_label = tk.Label(self.root)
        self.temp_label = tk.Label(self.root, text="28 ºC", 
                                   font=("Arial", 18), bg="white")
        self.led_label = tk.Label(self.root)
        self.show_images(states=(0, 0, 0))

        
        # Create button
        self.change_button = tk.Button(self.root, text="Light Switch", command=self.change_image)
        self.change_button.grid(row=0, column=1)

        # style
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TreeView", background="lightblue", fieldbackground="grey", foreground="yellow")
        style.configure("TreeView.heading", background="lightgray", foreground="black")

        # treeview
        col_names = ("Timestamp", "occupancy", "room temp", "out temp")
        for i in range(len(col_names)):
            self.tree.column("#" + str(i), anchor=CENTER)
            self.tree.heading("#" + str(i), text=col_names[i])
        self.tree.grid(row=2, column=0, columnspan=2, sticky="nsew")

        
    def showGUI(self) -> None:
        self.root.mainloop()


    def close(self):
        self.root.destroy()
        print('Window Closed!')


    def update_cmds(self, input_buffer:queue.Queue) -> None:
        """
            input_buffer: data from UDP
                user: sensor name
                values: [ac_state, ac_value, led_state]
        """
        while True:
            try:
                values = input_buffer.get(timeout=1) # day_hour, occupancy, ac_temp, light_on
                
                print(values)
                try:
                    self.show_images(states=values[1:4]) # 1, 2, 3
                    self.tree.insert("", 0, values=values[1:2]+values[-2:], text=values[0])
                except IndexError:
                    print('Index Error')
                
                self.root.update()
            
            except queue.Empty:
                print('Waiting...', end='\r')
            time.sleep(.1)

    
    def show_images(self, states:tuple) -> None:
        """
            states = [ac_state, ac_value, led_state]
        """
        ac_state, ac_value, led_state = states 
        # AC
        self.ac_image = Image.open(self.ac_image_paths[ac_state])
        self.ac_image = self.ac_image.resize((600, 250)) # if need
        self.ac_photo = ImageTk.PhotoImage(self.ac_image)  # Keep reference to avoid garbage collection
       
        self.ac_label.config(image=self.ac_photo) # reset image
        self.ac_label.grid(row=1, column=0)
        self.temp_label.config(text=f"{ac_value} ºC" if ac_state else "")
        self.temp_label.place(x=500, y=180, anchor="center")  # Place text label on top

        # LED
        self.led_image = Image.open(self.led_image_paths[led_state])
        self.led_image = self.led_image.resize((160, 250)) # if need
        self.led_photo = ImageTk.PhotoImage(self.led_image)  # Keep reference to avoid garbage collection
         
        self.led_label.config(image=self.led_photo) # reset image
        self.led_label.grid(row=1, column=1)

 
    def change_image(self):
        self.show_images(states=(1, 25, 1))



def get_data(out_buffer:queue.Queue): 
    for i in range(1_000):
        QUEUE.put(("Andre", (rd.randint(0,1), rd.randint(-50, 50), rd.randint(0,1))))
        time.sleep(1)


def AI(out_buffer:queue.Queue): 
    import pickle
    import numpy as np
    import pandas as pd
    from datetime import datetime

    regressor = None
    classifier = None
    # Load the models from the pickle files
    with open('artifacts/ac_temperature_model.pkl', 'rb') as ac_model_file:
        regressor = pickle.load(ac_model_file)

    with open('artifacts/light_on_off_model.pkl', 'rb') as light_model_file:
        classifier = pickle.load(light_model_file)

    # Define the feature names for the input data
    feature_names = ['outside_temperature', 'room_temperature', 'occupancy', 'hour', 'day_of_week']
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    while True:
        # Input collection
        out_temp       = rd.randint(-50, 50)
        room_temp      = rd.randint(-50, 50)
        occupancy      = rd.randint(0, 1)
        hour           = rd.randint(0, 23)
        day_of_week    = np.random.choice([day for day in range(7)])
        features       = pd.DataFrame([[out_temp, room_temp, occupancy, hour, day_of_week]], columns=feature_names)
        # Predictions
        ac_temp        = int(regressor.predict(features)[0])
        light_on       = classifier.predict(features)[0]
        # QUEUE.put(("Andre", (rd.randint(0,1), rd.randint(-50, 50), rd.randint(0,1)))) # MANUAL DATA
        QUEUE.put((f"{days[day_of_week]} {hour}h", bool(occupancy), f"{ac_temp} °C", light_on, f"{room_temp} °C", f"{out_temp} °C")) # MANUAL DATA
        time.sleep(1)
            

def udp_data(out_buffer:queue.Queue):
    """
        udp data => (input, output)
        input  = [SENSOR, outside_temp, room_temp, occupancy@hour]
        output = (ac_state, ac_value, led_state) 
    """
    port = '/dev/ttyUSB0'
    br =  9600

    print(f"Reading FROM : port={port}, Baud-Rate={br}")

    ser = serial.Serial(port, br)

    while True:
        data = str(ser.readline(), 'utf-8').strip('/n/r')
        data = data.split(',')
        states = [data[0]] + [int(v) for v in data[1:]]
        out_buffer.put(states)
  
            
if __name__=="__main__":
    
    app = Window(size="1000x700", title="Smart-IoT-Home")
   
    QUEUE = queue.Queue() 
        
    Thread(target=AI, args=(QUEUE,), daemon=True).start()
    Thread(target=app.update_cmds, args=(QUEUE,), daemon=True).start()
    app.showGUI()
