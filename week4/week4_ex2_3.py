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


'''
l=0
l=l+10
my_turtle.penup()
my_turtle.goto(-2*l,-l*math.sqrt(3)/2)
triangle(l*4)
my_turtle.penup()
my_turtle.goto(+2*l,+l*math.sqrt(3)/1.4)
my_turtle.left(180)
triangle(l*4)

l=l+20
my_turtle.left(180)
my_turtle.penup()
my_turtle.goto(-2*l,-l*math.sqrt(3)/2)
triangle(l*4)
my_turtle.penup()
my_turtle.goto(+2*l,+l*math.sqrt(3)/1.7)
my_turtle.left(180)
triangle(l*4)
'''
n = 4
l=5
my_turtle.left(180)
for x in range (1,n+1):
    l=l*2.2
    my_turtle.left(180)
    my_turtle.penup()
    my_turtle.goto(-2*l,-l*math.sqrt(3)/1.5)
    triangle(l*4)
    my_turtle.penup()
    my_turtle.goto(+2*l,+l*math.sqrt(3)/1.5)
    my_turtle.left(180)
    triangle(l*4)
'''
for x in range (n):
    l=l+10
    my_turtle.penup()
    my_turtle.goto(-2*l,-l*math.sqrt(3)/2)
    triangle(l*4)
    my_turtle.penup()
    my_turtle.goto(+2*l,+l*math.sqrt(3)/1.25)
    my_turtle.left(180)
    triangle(l*4)

my_turtle.penup()
my_turtle.goto(-l/2,0)
triangle(l*4)

my_turtle.penup()
my_turtle.goto(-2*l,-l*math.sqrt(3)/2)
triangle(l*4)

l=10*2
my_turtle.penup()
my_turtle.goto(-2*l,-l*math.sqrt(3)/2)
triangle(l*4)
'''




#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
