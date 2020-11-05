import turtle
import math
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################


def triangle(x):
    my_turtle.pendown()
    my_turtle.forward(x)
    my_turtle.left(180-60)
    my_turtle.forward(x)
    my_turtle.left(180-60)
    my_turtle.forward(x)
    my_turtle.left(180-60)

#triangle(100)

def square(x):
    my_turtle.pendown()
    my_turtle.forward(x)
    my_turtle.left(180-90)
    my_turtle.forward(x)
    my_turtle.left(180-90)
    my_turtle.forward(x)
    my_turtle.left(180-90)
    my_turtle.forward(x)
    my_turtle.left(180-90)

#square(100)

def pentagan(x):
    my_turtle.pendown()
    my_turtle.forward(x)
    my_turtle.left(180-108)
    my_turtle.forward(x)
    my_turtle.left(180-108)
    my_turtle.forward(x)
    my_turtle.left(180-108)
    my_turtle.forward(x)
    my_turtle.left(180-108)
    my_turtle.forward(x)
    my_turtle.left(180-108)

#pentagan(100)

def hexagan(x):
    my_turtle.pendown()
    my_turtle.forward(x)
    my_turtle.left(180-120)
    my_turtle.forward(x)
    my_turtle.left(180-120)
    my_turtle.forward(x)
    my_turtle.left(180-120)
    my_turtle.forward(x)
    my_turtle.left(180-120)
    my_turtle.forward(x)
    my_turtle.left(180-120)
    my_turtle.forward(x)
    my_turtle.left(180-120)

#hexagan(100)



def polygon(n,x):
    angle = (n-2)*180/n
    print(angle)
    my_turtle.pendown()
    for dummy in range(n):
        my_turtle.forward(x)
        my_turtle.left(180-angle)

polygon(3,100)
    
#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
