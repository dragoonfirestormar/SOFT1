import turtle
import random

s = turtle.Screen() 
t = turtle.Turtle()

s.setworldcoordinates(0, 100, 100, 0)
s.bgcolor('black')
t.hideturtle()

def sq(x,y,l,c):
    t.penup()
    l=l*0.9
    t.goto(x,y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    t.fd(l)
    t.rt(360-90)
    t.fd(l)
    t.rt(360-90)
    t.fd(l)
    t.rt(360-90)
    t.fd(l)
    t.rt(360-90)
    t.end_fill()
    pass

print(s.screensize())

#sq(0,0,10)

maze = [
    "XXXXXXXXXXXXXXXXX",
    "    X         X X",
    "XXX X XXXXXXX X X",
    "X X X X     X X X",
    "X X X X XXX X X X",
    "X X   X   X X X X",
    "X XXXXXXXXX X X X",
    "X             X X",
    "XXX XXX XXXXX X X",
    "X     X X   X   X",
    "X XXX X X X X XXX",
    "X   X X X X     X",
    "X X X X XXXXXXXXX",
    "X X X X         X",
    "XXX X XXXXXXXXX X",
    "X   X         X X",
    "XXXXXXXXXXXXXXX X"
]

xind=0
yind=0
t.speed(0)
L = 4
Edge = 4
i=0

#s.tracer(0, 0)
for y in maze:
    for x in y:
        if x==' ':
            sq(xind*Edge, yind*Edge, L, 'black')
            pass
        else:
            sq(xind*Edge, yind*Edge, L, 'white')
            pass
        xind+=1
        if i <1:
            print(t.position())
            i+=1
    xind=0
    yind+=1

sq(0*Edge, 1*Edge, L, 'red')
s.update()

'''
sq(0, 4, L, 'red')
sq(0, 8, L, 'red')
sq(0, 4, L, 'black')
'''
xind=0
yind=1


def f():
    global xind
    global yind
    if yind == 0:
        return None
    else:
        if maze[yind-1][xind+0] == 'X':
            print('X')
            return None
        else:
            sq(xind*Edge, yind*Edge, L, 'black')
            xind+=0
            yind-=1
            sq(xind*Edge, yind*Edge, L, 'red')
    print('Up')
    

def d():
    global xind
    global yind
    if yind == len(maze):
        return None
    else:
        if maze[yind+1][xind+0] == 'X':
            print('X')
            return None
        else:
            sq(xind*Edge, yind*Edge, L, 'black')
            xind+=0
            yind+=1
            sq(xind*Edge, yind*Edge, L, 'red')
    print('Down')

def l():
    global xind
    global yind
    if xind == 0:
        return None
    else:
        if maze[yind+0][xind-1] == 'X':
            print('X')
            return None
        else:
            sq(xind*Edge, yind*Edge, L, 'black')
            xind-=1
            yind+=0
            sq(xind*Edge, yind*Edge, L, 'red')
    print('Left')

def r():
    global xind
    global yind
    if xind == len(maze[0]):
        print('len')
        return None
    else:
        if maze[yind+0][xind+1] == 'X':
            print('X')
            return None
        else:
            sq(xind*Edge, yind*Edge, L, 'black')
            xind+=1
            yind+=0
            sq(xind*Edge, yind*Edge, L, 'red')
    print('Right')


while(False):
    n = random.randint(0,3)
    if n==0:
        f()
    elif n==1:
        d()
    elif n==2:
        l()
    elif n==3:
        r()
    else:
        exit()

def multicheck(x,y):
    top=True
    bottom=True
    left=True
    right=True
    if y == len(maze):
        bottom=False
        pass
    if y == 0:
        top=False
        pass
    if x == len(maze[0]):
        right=False
        pass
    if x == 0:
        left=False
        pass
    if(top):
        if maze[y-1][x] == 'X':
            top=False
    if(bottom):
        if maze[y+1][x] == 'X':
            bottom=False
    if(left):
        if maze[y][x-1] == 'X':
            left=False
    if(right):
        if maze[y][x+1] == 'X':
            right=False
    return [top, bottom, left, right]

def firstStep():
    if xind == 0:
        return 'r'
    if xind == len(maze[0]):
        return 'l'
    if y==0:
        return 'd'
    else:
        return 'f'
    


lastStep = firstStep()
for x in range(100):
    try:
        if lastStep == 'f':
            if maze[yind][xind-1] != 'X':
                lastStep= 'l'
                l()
            elif maze[yind-1][xind] == 'X':
                lastStep= 'r'
            else:
                f()
        if lastStep == 'r':
            if maze[yind-1][xind] != 'X':
                lastStep= 'f'
                f()
            elif maze[yind][xind+1] == 'X':
                lastStep = 'd'
            else:
                r()
        if lastStep == 'd':
            if maze[yind][xind+1] != 'X':
                lastStep= 'r'
                r()
            elif maze[yind+1][xind] == 'X':
                lastStep= 'l'
            else:
                d()
        if lastStep == 'l':
            if maze[yind+1][xind] != 'X':
                lastStep= 'd'
                d()
            elif maze[yind][xind-1] == 'X':
                lastStep= 'f'
            else:
                l()
    except:
        print('You Won')
        break
    s.update()
    pass

s.onkey(f, "Up")
s.onkey(d, "Down")
s.onkey(l, "Left")
s.onkey(r, "Right")
s.listen()

print(t.position())

turtle.done()