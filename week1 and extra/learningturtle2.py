import turtle

bob = turtle.Turtle()

bob.color("cyan","yellow")

bob.speed(10)
bob.begin_fill()

for x in range(0,50):
    bob.forward(200)
    bob.left(170)
    pass

bob.end_fill()


turtle.done()