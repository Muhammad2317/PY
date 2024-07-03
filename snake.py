import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0) 

# snake body
segments = []

# creating the snake head
for i in range(1):
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("green")
    segment.penup()
    segment.goto(-20 * i, 0)
    segments.append(segment)

# Create the apple
apple = turtle.Turtle()
apple.shape("square")
apple.color("red")
apple.penup()
apple.goto(0, 100)

# Define movement step size
step_size = 20

# Initialize direction
direction = "stop"

def go_up():
    global direction
    if direction != "down":  
        direction = "up"

def go_down():
    global direction
    if direction != "up":  
        direction = "down"

def go_left():
    global direction
    if direction != "right":  
        direction = "left"

def go_right():
    global direction
    if direction != "left":  
        direction = "right"

# Move the snake
def travel():
    
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the head
    if direction == "up":
        y = segments[0].ycor()
        segments[0].sety(y + step_size)
    if direction == "down":
        y = segments[0].ycor()
        segments[0].sety(y - step_size)
    if direction == "left":
        x = segments[0].xcor()
        segments[0].setx(x - step_size)
    if direction == "right":
        x = segments[0].xcor()
        segments[0].setx(x + step_size)

# Handle apple collision and growth
def handle_apple_position():
    apple_x = random.randint(-14, 14) * step_size
    apple_y = random.randint(-14, 14) * step_size
    apple.goto(apple_x, apple_y)

    # Add a new segment to the snake
    new_segment = turtle.Turtle()
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    segments.append(new_segment)

# Check for collision with the screen boundaries
def check_boundaries():
    head_x = segments[0].xcor()
    head_y = segments[0].ycor()
    if head_x > 290 or head_x < -290 or head_y > 290 or head_y < -290:
        return True
    return False

# Check for collision with the snake's own body
def check_self_collision():
    for segment in segments[1:]:
        if segments[0].distance(segment) < step_size:
            return True
    return False

# Keyboard controls
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# game loop
game_on = True
while game_on:
    screen.update()
    travel()

    # if snake eats apple
    if segments[0].distance(apple) < step_size:
        handle_apple_position()

    # Check collisions
    if check_boundaries() or check_self_collision():
        game_on = False
        screen.clear()
        screen.bgcolor("black")
        screen.title("Game Over")
        print("Game Over")
        break

    # Delay
    time.sleep(0.2)

screen.mainloop()
