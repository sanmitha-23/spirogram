import random
import turtle
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255)   # allows to randomly choose different colors


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple

directions = [0, 90, 180, 270]


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("darkblue")

timmy_the_turtle.speed('fastest')


def draw_circle(dist):
    for _ in range(int(360/dist)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + dist)


draw_circle(5)


screen = Screen()
screen.exitonclick()
