from tkinter import *
from PIL import ImageTk, Image
def click():
    print("Successful!")

def submit():
    print(entry.get())
    #entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window=Tk();
x=IntVar()
def check():
    if(x.get()==1):
        print("click!")
window.geometry("100000x100000")
icon=ImageTk.PhotoImage(Image.open("C:\\Users\\tmghi\\Test-Repo\\Extra Images\\Lion.png"))
window.title("Whats up?")
window.iconphoto(True,icon)
#window.config(background="black")
"""label=Label(window,text="Thomas is a train",font=("Impact",50,"bold"),fg="green",bg="red")
label.pack()
#button=Button(window,command=click,text="Click me!",font=("Comic Sans",20,"bold"),fg="blue",bg="white")
#button.place(x=550,y=100)
entry=Entry(window,font=("Impact",30,"bold"),fg="white",bg="blue")
entry.pack()
submit_button=Button(window,command=submit,text="submit",font=("Arial",20,"bold"),fg="blue",bg="white")
submit_button.pack(side=RIGHT)
delete_button=Button(window,command=delete,text="delete",font=("Arial",20,"bold"),fg="blue",bg="white")
delete_button.pack(side=RIGHT)
backspace_button=Button(window,command=backspace,text="backspace",font=("Arial",20,"bold"),fg="blue",bg="white")
backspace_button.pack(side=RIGHT)
photo=ImageTk.PhotoImage(Image.open("Python_color.png"))
check_button=Checkbutton(window,text="If Mogos is dumb!",variable=x,onvalue=1,offvalue=0,font=("Arial",10),fg="black",bg="blue",activeforeground="black",activebackground="blue",command=check,image=photo,compound="left")
check_button.pack()"""
anime=["one piece","dragon ball","naruto"]
label=Label(window,text="Best Anime?",font=("Arial",20,"bold"),fg="white",bg="yellow")
label.pack()
op=PhotoImage(file="op.png")
dragonb=PhotoImage(file="dragonb.png")
naruto=ImageTk.PhotoImage(Image.open("naruto.jpg"))
images=[op,dragonb,naruto]
z=IntVar()
def choice2():
    if (z.get() == 0):
        print("Gum Gum Pistol!")
    elif (z.get() == 1):
        print("Kamehameha!")
    else:
        print("Rasengan!")

opbutton=Radiobutton(window,text=anime[0],variable=z,value=0,font=("Impact",20,"bold"),command=choice2,image=images[0],compound="right")
opbutton.pack(anchor=W)
dbbutton=Radiobutton(window,text=anime[1],variable=z,value=1,font=("Impact",20,"bold"),command=choice2,image=images[1],compound="right")
dbbutton.place(x=700,y=40)
narbutton=Radiobutton(window,text=anime[2],variable=z,value=2,font=("Impact",20,"bold"),command=choice2,image=images[2],compound="right")
narbutton.place(x=350,y=350)
window.mainloop()