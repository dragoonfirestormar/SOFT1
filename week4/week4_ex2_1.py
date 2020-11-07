'''
design a function draw_triangle to draw a triangle. Using this function and a for loop, draw the following image:
'''
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

n = 10

l=0
'''
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
for x in range (n):
    l=l+10
    my_turtle.penup()
    my_turtle.goto(-2*l,-l*math.sqrt(3)/2)
    triangle(l*4)

'''
my_turtle.penup()
my_turtle.goto(-50,0)
triangle(100)

my_turtle.penup()
my_turtle.goto(-100,-86.6/2+10)
triangle(200)
'''
'''
for x in range(1,n+1):
    my_turtle.penup()
    print(my_turtle.pos()+(10.0,10.0))
    my_turtle.goto(my_turtle.pos()+(10.0,10.0))
    triangle(x*10)
'''




#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
