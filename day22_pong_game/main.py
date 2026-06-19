from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


# Connect keyboard to screen
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
screen.listen()
ball = Ball()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.increase_speed()
    # Detect collision r_paddle
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() <-320:
        ball.bounce_x()
    # Detect ball out of bounds
    if ball.xcor() > 400:
        scoreboard.update_l_score()
        ball.respawn()
    if ball.xcor() < -400:
        scoreboard.update_r_score()
        ball.respawn()












screen.exitonclick()