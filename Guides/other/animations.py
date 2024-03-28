from tkinter import *
import time
import math

window = Tk()

WIDTH = 10000
HEIGHT = 10000

window.geometry(str(WIDTH)+"x"+str(HEIGHT))



xVelocity = 3
yVelocity = 3

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\space.png")
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\ufo.png")
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

width2=background_photo.width()
height2=background_photo.height()
print(width2)
print(height2)
image_width = photo_image.width()
image_height = photo_image.height()
def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window.bind("<Button-1>",doSomething) #left mouse click

w=0
h=0
if(WIDTH<width2):
    w=WIDTH
else:
    w=width2
w=w-image_width
if(HEIGHT<height2):
    h=HEIGHT
else:
    h=height2
h=h-image_height
while True:
    coordinates = canvas.coords(my_image)
    if(coordinates[0]>=(w) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(h) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()