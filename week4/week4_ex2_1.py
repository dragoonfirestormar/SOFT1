'''
design a function draw_triangle to draw a triangle. Using this function and a for loop, draw the following image:
'''
import turtle
import math
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################

my_turtle.speed(0)

def triangle(x):
    my_turtle.pendown()
    my_turtle.forward(x)
    my_turtle.left(180-60)
    my_turtle.forward(x)
    my_turtle.left(180-60)
    my_turtle.forward(x)
    my_turtle.left(180-60)

n = 10

l=0

for x in range (n):
    l=l+10
    my_turtle.penup()
    my_turtle.goto(-2*l,-l*math.sqrt(3)/2)
    triangle(l*4)


#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
