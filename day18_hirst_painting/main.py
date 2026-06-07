import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
turtle.colormode(255)

color_array = [
    (234, 232, 227), (230, 233, 239), (239, 231, 235),
    (228, 235, 231), (199, 162, 100), (62, 91, 128),
    (140, 170, 192), (139, 90, 48), (219, 206, 119),
    (135, 27, 52)
]

# Timmy in position and ready
def start():
    timmy.pensize(10)
    timmy.penup()
    timmy.setposition(-250, 250)
    timmy.pendown()

def draw_line():
    for i in range(10):
        timmy.color(random.choice(color_array))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

def get_in_position():
    timmy.penup()
    timmy.setx(-250)
    timmy.right(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.pendown()

def draw_art():
    start()
    for i in range(10):
        draw_line()
        get_in_position()

draw_art()






















screen = Screen()
screen.exitonclick()