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
        print("done!")
    else:
        print("undone!")
window.geometry("50x50")
icon=ImageTk.PhotoImage(Image.open("Lion.jpg"))
window.title("Whats up?")
window.iconphoto(True,icon)
window.config(background="black")
label=Label(window,text="Thomas is a train",font=("Impact",50,"bold"),fg="green",bg="red")
label.pack()
#button=Button(window,command=click,text="Click me!",font=("Comic Sans",20,"bold"),fg="blue",bg="white")
#button.place(x=550,y=100)
entry=Entry(window,font=("Impact",30,"bold"),fg="yellow",bg="green")
entry.pack()
submit_button=Button(window,command=submit,text="submit",font=("Arial",20,"bold"),fg="blue",bg="white")
submit_button.pack(side=RIGHT)
delete_button=Button(window,command=delete,text="delete",font=("Arial",20,"bold"),fg="blue",bg="white")
delete_button.pack(side=RIGHT)
backspace_button=Button(window,command=backspace,text="backspace",font=("Arial",20,"bold"),fg="blue",bg="white")
backspace_button.pack(side=RIGHT)
photo=ImageTk.PhotoImage(Image.open("Python_color.png"))
check_button=Checkbutton(window,text="If Mogos is dumb!",variable=x,onvalue=1,offvalue=0,font=("Arial",20),fg="green",bg="red",activeforeground="green",activebackground="red",command=check,image=photo,compound="left")
check_button.pack()
window.mainloop()
