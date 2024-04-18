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
SPACESIZE=35
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
    global carphoto, begin,window,canvas,c,check

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
        time.sleep(0.5)
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
            print(i.label)
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
    global rocks,check,canvas

    for i in rocks:
        if(abs(car.coordinates[0]-i.coordinates[0])<=carspace and abs(car.coordinates[1]-i.coordinates[1])<=carspace):
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
    window.update()
    canvas.config(bg="black")
    canvas.create_text(window.winfo_screenwidth()/2,window.winfo_screenheight()/2,text="GAMEOVER",fill="red",font=("Arial",70,"bold"),tag="end")
    time.sleep(2)
    window.destroy()

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

canvas=Canvas(window,width=window.winfo_screenwidth(),height=window.winfo_screenheight())
canvas.pack()

road=PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\road.png")
carphoto=PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\car.png")

background=canvas.create_image(window.winfo_screenwidth()/2,window.winfo_screenheight()/2,image=road,tag="road")

car=Car()

print(threading.active_count())
a=threading.Thread(target=movement,args=())
a.start()

b=threading.Thread(target=timer,args=())
b.start()

start=threading.Thread(target=start,args=())
start.start()


window.mainloop()
