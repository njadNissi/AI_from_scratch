import tkinter as tk
import imageio

class GIFViewer:
    def __init__(self, gif_path):
        self.gif_path = gif_path
        self.gif = imageio.mimread(gif_path)

        self.root = tk.Tk()
        self.root.title("GIF Viewer")

        self.frame_index = 0

        self.label = tk.Label(self.root)
        self.label.pack()

        self.button = tk.Button(self.root, text="Show Frame", 
command=self.show_frame)
        self.button.pack()

        self.update_frame()

    def show_frame(self):
        self.frame_index = (self.frame_index + 1) % len(self.gif)
        self.update_frame()

    def update_frame(self):
        frame = self.gif
        image = tk.PhotoImage(data=frame.tobytes())
        self.label.config(image=image)
        self.label.image = image  # Keep a reference to avoid garbage collection

    def start(self):
        self.root.mainloop()

def start(self):
        self.root.mainloop()

# Example usage
gif_viewer = GIFViewer("path/to/your/gif.gif")  # Replace with the actual path
gif_viewer.start()
