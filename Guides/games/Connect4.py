from tkinter import *
from PIL import ImageTk, Image

Team1="blue"
Team2="red"

window=Tk()
window.geometry("500x500")
canvas=Canvas(window,width=window.winfo_screenwidth(),height=window.winfo_screenheight())
canvas.pack()
board=[]
for i in range(0,6):
    for j in range(0,7):
        board[i][j]=canvas.create_oval()
print(board)


window.mainloop()