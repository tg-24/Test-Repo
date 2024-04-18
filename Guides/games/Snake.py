# ************************************
# Python Snake
# ************************************
from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 500
SPEED = 50
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "lime green"
FOOD_COLOR = "turquoise"
BACKGROUND_COLOR = "#000000"



class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE))-1) * SPACE_SIZE
        y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE
        t=0
        while(t!=1):
            t=1
            for x2,y2 in snake.coordinates:
                if(x==x2 and y==y2):
                    x = random.randint(0, int((GAME_WIDTH / SPACE_SIZE)) - 1) * SPACE_SIZE
                    y = random.randint(0, int((GAME_HEIGHT / SPACE_SIZE)) - 1) * SPACE_SIZE
                    t=0

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global BODY_PARTS
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)


    if x == food.coordinates[0] and y == food.coordinates[1]:
        BODY_PARTS += 1
        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):
    global BODY_PARTS
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1] and BODY_PARTS>6:
            return True

    return False


def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="new_game")
    restart_button.config(state=ACTIVE)

def new_game():
    global score,food,snake,direction, BODY_PARTS
    restart_button.config(state=DISABLED)
    canvas.delete(ALL)
    score=0
    direction="down"
    label.config(text="Score:{}".format(score))
    food = Food()
    BODY_PARTS = 3
    snake = Snake()
    window.update()
    next_turn(snake, food)

def end_game():
    window.destroy()

window = Tk()
window.title("Snake game")
window.resizable(False,False)

score = 0
direction = 'down'

frame=Frame(window)
frame.pack()

label = Label(frame, text="Score:{}".format(score), font=('consolas', 40))
label.grid(row=0,column=1)

end_button=Button(frame,text="Quit",font=("Arial",10),width=10,height=5,command=end_game)
end_button.grid(row=0,column=2)

restart_button=Button(frame,text="restart game",font=("Arial",10),width=10,height=5,command=new_game,state=DISABLED)
restart_button.grid(row=0,column=0)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/1.8))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

image=PhotoImage(file="C:\\Users\\tmghi\\Test-Repo\\Extra Images\\Python_color.png")
window.iconphoto(True,image)

window.mainloop()