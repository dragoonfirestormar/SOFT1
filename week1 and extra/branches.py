import turtle

s = turtle.Screen() 

t = turtle.Turtle()
i=0

def left(x,y,a,l):
    t.up()
    t.goto(x,y)
    t.down()
    t.rt(a)
    t.fd(l)
    return [t.position(),a,l]


def right(x,y,a,l):
    t.up()
    t.goto(x,y)
    t.down()
    t.rt(-2*a)
    t.fd(l)
    return [t.position(),a,l]

#t.rt(-90)
#t.setheading(90)
#left(0,0,60,60)
#right(0,0,60,60)
#t.setheading(90)

xind=0
yind=0
L=100
def recursive(x,y):
    t.setheading(90)
    global L
    L=0.6*L
    global i
    if i >10:
        #exit()
        return 1
    else:
        i+=1
    Lef=left(x,y,60,30)
    Rig=right(x,y,60,30)
    recursive(Rig[0][0],Rig[0][1])
    recursive(Lef[0][0],Lef[0][1])
    #return recursive(Rig[0][0],Rig[0][1]) + recursive(Lef[0][0],Lef[0][1]) 

recursive(0,0)
#print(t.position())
'''
t.rt(360-90)
t.fd(100)
t.rt(30)
t.fd(50)
'''
#print(t.position())
turtle.done()