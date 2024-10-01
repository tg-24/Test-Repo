from tkinter import *
from PIL import (ImageTk, Image)
window=Tk();
def setscale():
    scale.set(int(entry.get()))
scalebutton=Button(window,text="submit",bg="black",fg="blue",font=("Arial",10,"underline"),command=setscale)
scalebutton.place(x=100,y=40)
scale=Scale(window,from_=1000,to=0,tickinterval=10,font=(20),length=600,resolution=5)
scale.pack()
window.mainloop()