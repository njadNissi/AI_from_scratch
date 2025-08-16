from tkinter import *

languages = ["Python", "JS", "C#", "Java", "F#",
             "Rugby", "Go", "R", "T-SQL", "Cobol", "Fortran", "Assembly"]

root = Tk()
root.title("Gui for scrollbar")


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)

for language in languages:
    languages_listbox.insert(END, language)


languages_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=languages_listbox.yview)

root.mainloop()
