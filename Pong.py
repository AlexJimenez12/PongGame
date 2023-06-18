import turtle
import random

# Setup the screen and the paddle shape
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.register_shape("paddle", ((0, 0), (10, 0), (10, 100), (0, 100)))

# Draw boundary
boundary_turtle = turtle.Turtle()
boundary_turtle.color("white")
boundary_turtle.speed(0)
boundary_turtle.penup()
boundary_turtle.goto(-300, 300)
boundary_turtle.pensize(2)
boundary_turtle.pendown()
for _ in range(4):
    boundary_turtle.forward(600)
    boundary_turtle.right(90)

# Player 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("paddle")
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-290, 0)
paddle_1.setheading(90)

# Player 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("paddle")
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(300, 0)
paddle_2.setheading(90)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.right(random.randint(-30, 30))  # Start off in a random direction

# Score
player_1_score = 0
player_2_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center",
          font=("Courier", 24, "normal"))

# Movement functions


def paddle_1_up():
    paddle_1.forward(30)


def paddle_1_down():
    paddle_1.backward(30)


def paddle_2_up():
    paddle_2.forward(30)


def paddle_2_down():
    paddle_2.backward(30)


# Key binds
screen.onkey(paddle_1_up, "w")
screen.onkey(paddle_1_down, "s")
screen.onkey(paddle_2_up, "Up")
screen.onkey(paddle_2_down, "Down")
screen.listen()


def change_ball_direction(context):
    # Find offset to any plane
    ball_heading = ball.heading()

    if context == "topBound" or context == "bottomBound":
        ball.setheading(360 - ball_heading)
    elif 0 <= ball_heading < 180:
        ball.setheading(180 - ball_heading)
    elif 180 <= ball_heading < 360:
        ball.setheading(540 - ball_heading)


# Main game loop
while True:
    ball.forward(2)

    # If the ball is within the coordinates of paddle 1 (left side)
    if abs(paddle_1.xcor() - ball.xcor()) < 10 and paddle_1.ycor() <= ball.ycor() <= paddle_1.ycor() + 100:
        change_ball_direction("paddle_1")

    # If the ball is within the coordinates of paddle 2 (right side)
    elif abs(ball.xcor() - paddle_2.xcor()) <= 10 and paddle_2.ycor() <= ball.ycor() <= paddle_2.ycor() + 100:
        change_ball_direction("paddle_2")

    # Ball exceeded boundaries on the left; paddle 1 missed the ball
    elif ball.xcor() <= -300:
        # Set heading to face left again so that we do not start off in the wrong angle
        ball.setheading(180)
        ball.right(random.randint(-30, 30))
        ball.goto(0, 0)
        paddle_1.clear()
        paddle_2.clear()
        paddle_2.write("     I Win!")
        player_2_score += 1
        pen.clear()
        pen.write("Player 1: " + str(player_1_score) + " Player 2: " + str(player_2_score), align="center",
                  font=("Courier", 24, "normal"))

    # Ball exceeded boundaries on the right; paddle 2 missed the ball
    elif ball.xcor() >= 300:
        # Set heading to face right again so that we do not start off in the wrong angle
        ball.setheading(0)
        ball.right(random.randint(-30, 30))
        ball.goto(0, 0)
        paddle_1.clear()
        paddle_2.clear()
        paddle_1.write("     I Win!")
        player_1_score += 1
        pen.clear()
        pen.write("Player 1: " + str(player_1_score) + " Player 2: " + str(player_2_score), align="center",
                  font=("Courier", 24, "normal"))

    # Top boundary
    elif ball.ycor() >= 290:
        change_ball_direction("topBound")

    # Bottom boundary
    elif ball.ycor() <= -290:
        change_ball_direction("bottomBound")

    # Update the screen with changes
    screen.update()
