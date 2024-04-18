from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\Python_color.png")
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #place window on computer screen, listen for events