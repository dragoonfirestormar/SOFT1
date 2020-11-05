import turtle

builder = turtle.Screen()
builder.bgcolor("white")
builder.title("MAZE")
builder.setup(700,700)

'''
tur = turtle.Turtle()
tur.goto(-330,330)
tur.shape("square")
tur.goto(0,0)
'''


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")

pen = Pen()
pen.goto(69,69)
pen.stamp
pen.goto(1,61)
pen.stamp

turtle.done()