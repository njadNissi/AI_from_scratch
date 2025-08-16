import tkinter as tk


root = tk.Tk()
root.geometry("50x70")


def getTextInput(input_label):
    text_label = tk.Label(text=input_label)
    text_label.pack()

    text = text_input.get("1.0", "end")
    return text


text_input = tk.Text(root, height=1)
text_input.pack()

btnRead = tk.Button(root, height=10, width=5, text="Read",
                    command=getTextInput)
btnRead.pack()

root.mainloop()
