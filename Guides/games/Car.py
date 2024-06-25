from tkinter import *
import random
from PIL import ImageTk, Image
import threading
import time

check=0
counter = 0
rocks2=[]
GAME_SIZE=400
ROCK_COLOR="orange"
SPACESIZE=32
current="down"
carspace=150
score=0
rocks=[]
class Car():
    global canvas,vehicle,carphoto,window
    def __init__(self):
        self.coordinates = [carspace/2,carspace/2]
        canvas.update()
        self.image=canvas.create_image(carspace/2,carspace/2,image=carphoto,tag="vroom")

    def setimage(self,x2,y2):
        del self.coordinates[-1]
        del self.coordinates[-1]
        self.coordinates.insert(0,x2)
        self.coordinates.insert(1, y2)
        canvas.delete("vroom")
        self.image = canvas.create_image(x2,y2,image=carphoto,tag="vroom")

class Rock():
    global canvas,window,counter
    def __init__(self,x,y,counter):
        if(x==0 and y==0):
            x = window.winfo_screenwidth() - SPACESIZE
            y = random.randint(0, window.winfo_screenheight())
        if(isinstance(counter, str)):
            self.label=counter
        else:
            self.label="rocks"+str(counter)
        self.coordinates=[x,y]
        canvas.create_rectangle(x,y,x+SPACESIZE,y+SPACESIZE,fill=ROCK_COLOR,tag=self.label)

    def decX(self):
        self.coordinates[0]-=SPACESIZE
        x=self.coordinates[0]
        y=self.coordinates[1]
        s=[x,y]
        return s


def run(current):
    global carphoto, begin,window,canvas,c,check,score

    if score==3:
        check=1
        c = threading.Thread(target=victory, args=())
        c.start()

    else:

        x=car.coordinates[0]
        y=car.coordinates[1]

        if current=="up":
            y-=SPACESIZE
        elif current=="down":
            y+=SPACESIZE
        elif current=="left":
            x-=SPACESIZE
        else:
            x+=SPACESIZE

        if x>window.winfo_screenwidth():
            x=carspace/2
            score += 1

        elif x<0:
            x+=SPACESIZE
            print("out of bounds")

        elif y<0:
            y=window.winfo_screenheight()-SPACESIZE

        elif y>window.winfo_screenheight():
            y=carspace/2

        car.setimage(x, y)

        window.update()
        checkcollision(car)
        if check==1:
            c=threading.Thread(target=gameover,args=())
            c.start()

def timer():
    global begin,car,rocks,counter,canvas
    counter=0
    while(check==0):
        time.sleep(0.8)
        rock = Rock(0,0,counter)
        counter+=1
        rocks2.append(rock)
    canvas.delete(ALL)

def movement():
    global canvas
    while (check==0):
        time.sleep(0.5)
        count=0
        for i in rocks:
            if(i.coordinates[0]<=0):
                canvas.delete(i.label)
                rocks.remove(i)
            else:
                s = i.decX()
                temp=i.label
                canvas.delete(i.label)
                rock = Rock(s[0], s[1],temp)
                rocks.remove(i)
                rocks.insert(count,rock)
            checkcollision(car)
            count+=1
        for j in rocks2:
            rocks.append(j)
            rocks2.remove(j)
    canvas.delete(ALL)
def checkcollision(car):
    global rocks,check,canvas,score
    if score!=3:
        for i in rocks:
            x1=car.coordinates[0]
            y1=car.coordinates[1]
            x2=i.coordinates[0]
            y2=i.coordinates[1]
            if x1>x2:
                if x1-x2<SPACESIZE+57:
                    if y1>y2 and y1 - y2 < SPACESIZE+38:
                        check = 1
                    elif y1<y2 and y2-y1 < 11:
                        check = 1

            elif x1 < x2:
                if x2-x1 < 68:
                    if y1>y2 and y1 - y2 < SPACESIZE+38:
                        check = 1
                    elif y1<y2 and y2-y1 < 11:
                        check = 1

def gameover():
    global canvas,a,b
    a.join()
    b.join()
    window.update()
    window.unbind('<Up>')
    window.unbind('<Down>')
    window.unbind('<Left>')
    window.unbind('<Right>')
    canvas.delete(ALL)
    window.update()
    canvas.config(bg="black")
    canvas.create_text(window.winfo_screenwidth()/2,window.winfo_screenheight()/2,text="GAMEOVER",fill="red",font=("Arial",70,"bold"),tag="end")
    time.sleep(2)
    window.destroy()

def restart():
    global window,canvas,start,canvas,background,car,a,b,movement,timer,victoryscreen,road,carphoto

    canvas.destroy()
    window.destroy()
    window = Tk()

    window.geometry("800x800")
    window.config(bg="black")
    window.update()

    victoryscreen = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\Victory Screen.png")

    canvas = Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
    canvas.pack()

    road = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\road.png")
    carphoto = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\car.png")

    background = canvas.create_image(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2, image=road,
                                     tag="road")
    car = Car()

    a = threading.Thread(target=movement, args=())
    a.start()

    b = threading.Thread(target=timer, args=())
    b.start()

    start = threading.Thread(target=start, args=())
    start.start()

def quit():
    window.destroy()
def victory():
    global canvas, a, b,winphoto
    window.update()
    window.unbind('<Up>')
    window.unbind('<Down>')
    window.unbind('<Left>')
    window.unbind('<Right>')
    window.update()
    winphoto = canvas.create_image(window.winfo_screenwidth() / 2, window.winfo_screenheight() / 2, image=victoryscreen,
                                   tag="win")
    window.update()
    frame=Frame(canvas,bd=5,relief=SUNKEN)
    frame.place(x=window.winfo_screenwidth()/2-50,y=0)
    quitbutton=Button(frame,width=10,height=2,text="Quit",fg="black",bg="red",font=("bold"),activebackground="red",command=quit)
    quitbutton.grid(row=0,column=0)

def start():
    global window
    label=Label(canvas,width=10,height=5,text="3",fg="red",bg="black",font=("Arial",15))
    label.place(x=window.winfo_screenwidth()/2,y=4)
    for i in range(2,-1,-1):
        window.update()
        time.sleep(1.5)
        label.config(text=str(i))
    label.config(text="GO!")
    time.sleep(0.5)
    window.bind('<Up>', lambda event: run('up'))
    window.bind('<Down>', lambda event: run('down'))
    window.bind('<Left>', lambda event: run('left'))
    window.bind('<Right>', lambda event: run('right'))
    label.destroy()




window=Tk()

window.geometry("800x800")
window.config(bg="black")
window.update()

victoryscreen = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\Victory Screen.png")


canvas=Canvas(window,width=window.winfo_screenwidth(),height=window.winfo_screenheight())
canvas.pack()

road=PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\road.png")
carphoto=PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\car.png")

background=canvas.create_image(window.winfo_screenwidth()/2,window.winfo_screenheight()/2,image=road,tag="road")

car=Car()

a=threading.Thread(target=movement,args=())
a.start()

b=threading.Thread(target=timer,args=())
b.start()

start=threading.Thread(target=start,args=())
start.start()


window.mainloop()

