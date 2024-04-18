import os
import random
import shutil
from tkinter import *
import time
from PIL import ImageTk, Image

window=Tk()
score = 0
buttonwidth=9
operator = ["/","*","+","-"]
one = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\BASE.png")
two = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\super saiyan.png")
three = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\super saiyan 3.png")
four = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\SSG.png")
five = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\SSB.png")
six = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\ui.png")
list = [one,two,three,four,five,six]
image = list[0]
def button_press(num):

    global equationtext,textLabel

    if(equationtext[:-2]=="= "):
        equationtext=""

    equationtext  = equationtext + str(num)

    textLabel.set(equationtext)
    window.update()

def clear():

    global equationtext,textLabel

    textLabel.set("")

    equationtext = ""

def delete():

    global equationtext,textLabel

    equationtext=equationtext[:-1]

    textLabel.set(equationtext)

def ask():
    global textLabel,guess,score,equationtext,answer
    print(score)
    if(score==5):
        powerup(score)
        victory()
    else:
        pick1=str(random.randint(0, 20))
        operation = random.choice(operator)
        pick2=str(random.randint(0,10))
        while(operation=="/" and pick2=="0"):
            pick1 = str(random.randint(0, 20))
            operation = random.choice(operator)
            pick2 = str(random.randint(0, 10))
        op = pick1 + operation + pick2 + " = "
        textLabel.set(op)
        op=op[:-2]
        answer=str(int(eval(op)))
        window.update()


def victory():
    #maybe play a video
   global canvas,frame,label,goku
   frame.destroy()
   label.destroy()
   canvas.destroy()
   window.config(bg="yellow")
   window.update()
   label2=Label(window,text="Victory!!!",width=window.winfo_width(),height=window.winfo_height(),bg="yellow",fg="blue",font=("Arial",50))
   label2.pack()
   window.update()
   time.sleep(2)
   window.destroy()

def powerup(score):
    global list,image,canvas,goku
    image=list[score]
    canvas.delete("goku")
    window.update()
    goku = canvas.create_image(canvas.winfo_width()/6, 0, image=image, anchor=NW,tag="goku")
    window.update()



def gameover():
    global equationtext,label,restart_button,window,frame
    equationtext = ""
    canvas.destroy()
    frame.destroy()
    label.destroy()
    window.config(bg="black")
    canvas2=Canvas(window,highlightthickness=0,bg="black",width=window.winfo_width(),height=window.winfo_height())
    canvas2.pack()
    canvas2.create_text(window.winfo_width()/2, window.winfo_height()/2+50,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="new_game")
    window.update()
    time.sleep(2)
    window.destroy()


def submit():
    global equationtext,answer,op,score,label,textLabel
    window.update()
    if equationtext != answer:
        gameover()

        # else if answer is correct increment score and change label color to green "correct"
    else:
        equationtext=""
        textLabel.set("")
        score += 1
        textLabel.set("correct")
        label.config(bg="green")
        powerup(score)
        time.sleep(2)
        label.config(bg="white")
        ask()

def quit():
    window.destroy()

def escape():
    window.attributes("-fullscreen", False)

window.geometry("500x500")
image2=PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\Dragon Balls.png")
window.iconphoto(True,image2)

window.title("Goku game")

textLabel=StringVar()

equationtext=""

label=Label(window, textvariable=textLabel, font=("Arial",20), bg="white", width=20, height=2)
label.place(x=0,y=0)

window.update()

labelheight=label.winfo_height()

labelwidth=label.winfo_width()

canvas=Canvas(window,width=window.winfo_screenwidth(),height=window.winfo_screenheight())
canvas.place(x=labelwidth,y=0)

window.update()
canvas.update()

background_photo=PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\dbz.png")
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

goku=canvas.create_image(labelwidth,0,image=image,anchor=NW,tag="goku")

frame=Frame(window)
frame.place(x=0,y=labelheight)

button1 = Button(frame, text=1, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

buttonbuttonwidth = Button(frame, text=buttonwidth, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(buttonwidth))
buttonbuttonwidth.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=buttonwidth, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

decimal = Button(frame, text='.', height=4, width=buttonwidth, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

button_neg = Button(frame, text='-', height=4, width=buttonwidth, font=35,
                 command=lambda: button_press('-'))

button_neg.grid(row=3,column=2)

clear_button = Button(frame, text='clear', height=4, width=buttonwidth, font=35,
                 command=clear)

clear_button.grid(row=4,column=0)


backspace_button = Button(frame, text='delete', height=4, width=buttonwidth, font=35,
                 command=delete)

backspace_button.grid(row=4,column=1)

submit_button = Button(frame, text='submit', height=4, width=buttonwidth, font=35,
                 command=submit)

submit_button.grid(row=4,column=2)


quit_button = Button(frame, text='quit', height=4, width=buttonwidth, font=35,
                 command=quit)

quit_button.grid(row=5,column=0)

escapebutton = Button(frame, text="Escape", command=escape, height=4, width=buttonwidth,font=35)
escapebutton.grid(row=5,column=1)


window.update()



window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/1.8))

window.attributes("-fullscreen", True)

ask()

window.mainloop()