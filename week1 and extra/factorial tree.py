import turtle

s = turtle.Screen() 

t = turtle.Turtle()


#s.setup(500,500)
s.setworldcoordinates(-200,0,200,400)
t.setheading(90)
i=0

x=y=0
L=1
angle=75

t.speed(0)

def draw(len):
    if(len>5):
        t.fd(len)
        t.rt(angle)
        draw(len*0.67)

        t.rt(-2*angle)
        draw(len*0.67)

        t.rt(angle)
        t.backward(len)

    

draw(100)
turtle.done()