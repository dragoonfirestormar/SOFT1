import turtle

bob = turtle.Turtle()

bob.color("red", "cyan")

bob.begin_fill()
for x in range(0,4):
    bob.forward(100)
    bob.right(90)
    pass
bob.end_fill()

bob.penup()

turtle.done()