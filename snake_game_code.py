from tkinter import *
import random

#Constants
GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 60
SPACE_SIZE = 40
BODY_PARTS = 2
SNAKE_COLOR = "#ffffff"
FOOD_COLOR = "#00d600"
BACKGROUND_COLOR = "#000000"

class snake:
    def _init_(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y +SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class food:
    def _init_(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)- 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHTH/SPACE_SIZE)- 1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

#Defining the game functionality and score when snake eats food
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE

    snake.coordinates.insert(0, (x,y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global Score

        score += 1

        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.square[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

#Defining the change in direction when key is pressed
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

#Defining the collisions for the game
def game_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_WIDTH:
        return True

    for body_part in snake.coordinates[1:]:
        if x ==  body_part[0] and y == body_part[1]:
            return True

    return False

#Defining game over
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('Arial', 70), text="GAME OVER!", fill="red", tag="gameover")

#Window Creation
window = Tk()
window.title("Snake Game Project")
window.resizable(False, False)

score = 0
direction = 'right'

label = label(window, text="Score:{}".format(score), font=('Arial', 40)
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack
window.update()

#Keybind
window.bind('<Left>', lambda even: change_direction('left'))
window.bind('<Right>', lambda even: change_direction('right'))
window.bind('<Up>', lambda even: change_direction('up'))
window.bind('<Down>', lambda even: change_direction('down'))

snake = snake()
food = food()

next_turn(snake, food)

window.mainloop()
