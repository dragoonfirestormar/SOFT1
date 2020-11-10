import turtle

s = turtle.Screen() 

t = turtle.Turtle()

while(True):
    x = input()
    if x=='w':
        t.fd(100)
        pass
    elif x=='s':
        t.rt(180)
        t.fd(100)
        pass
    elif x=='a': 
        t.rt(270)
        t.fd(100)
        pass
    elif x=='d':
        t.rt(90)
        t.fd(100) 
        pass
    else:
        break
        

turtle.done()