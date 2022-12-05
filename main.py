# this code is hardly use for good programmers
# from turtle import *

from turtle import Screen, Turtle, colormode
from random import randint

jonny = Turtle()
jonny.shape('turtle')
jonny.color('blue')
colormode(255)


# for _ in range(4):
#     jonny.fd(100)
#     jonny.left(90)

# for _ in range(15):
#     jonny.pendown()
#     jonny.fd(10)
#     jonny.penup()
#     jonny.fd(10)

# for _ in range(3):
#     jonny.fd(50)
#     jonny.right(120)
#
# for _ in range(4):
#     jonny.color('red')
#     jonny.fd(50)
#     jonny.right(90)
#
# for _ in range(5):
#     jonny.color('purple')
#     jonny.fd(50)
#     jonny.right(72)
#
# for _ in range(6):
#     jonny.color('orange')
#     jonny.fd(50)
#     jonny.right(60)
#
# for _ in range(7):
#     jonny.color('yellow')
#     jonny.fd(50)
#     jonny.right(52)
#
# for _ in range(8):
#     jonny.color('brown')
#     jonny.fd(50)
#     jonny.right(45)
#
# for _ in range(9):
#     jonny.color('purple')
#     jonny.fd(50)
#     jonny.right(40)
#
# for _ in range(10):
#     jonny.color('green')
#     jonny.fd(50)
#     jonny.right(36)


# random_walk
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(size):
    for _ in range(int(360/size)):
        jonny.speed('fastest')
        jonny.pensize(2)
        jonny.color(random_color())
        jonny.circle(100)
        # jonny.tiltangle(180)
        jonny.right(size)


draw_spirograph(10)
screen = Screen()
screen.exitonclick()
