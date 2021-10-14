#Write a function called square that takes a parameter named t, which is a turtle.
#It should use the turtle to draw a square. Write a function call that passes bob as an argument to square, and then run the program again.
from turtle import Turtle
import math
bob = Turtle()


def draw_square(length):
    for i in range(4):
        bob.forward(length);
        bob.right(90)

draw_square(100);


def draw_polygon(sides, length):
    for i in range(sides):
        bob.forward(length);
        bob.right(360/sides)

draw_polygon(9, 100);

#Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle
#by calling draw_polygon with an appropriate length and number of sides. Test your function with a range of values of r.
#Hint: figure out the circumference of the circle and make sure that length * n = circumference.
def draw_circle(r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    draw_polygon(n,r);

def draw_arc(r,a):
    arc_length = 2 * math.pi * r * a / 360
    n = int(arc_length / 3) + 1
    length = arc_length / n
    angle = a / n
    for i in range(n):
        bob.fd(length);
        bob.lt(angle);

draw_circle(20);
draw_arc(100,90);
