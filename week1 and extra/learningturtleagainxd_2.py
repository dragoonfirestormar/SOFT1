import turtle
import random

s = turtle.Screen() 
t = turtle.Turtle()
s.setup(500,500)
s.setworldcoordinates(0, 17*4+2, 17*4+2, 0)
s.bgcolor('black')
s.title("Maze")

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

#s.tracer(1, -250)
s.delay(0.001)

for y in maze:
    for x in y:
        if x==' ':
            #sq(xind*Edge, yind*Edge, L, 'black')
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



'''
sq(0, 4, L, 'red')
sq(0, 8, L, 'red')
sq(0, 4, L, 'black')
xind=int(60/4)
yind=int(64/4)
'''
xind=int(0)
yind=int(1)

sq(xind*Edge, yind*Edge, L, 'red')
s.update()

targetX = 15
targetY = 16

def f(var=None):
    global xind
    global yind
    if yind == 0:
        return None
    else:
        if maze[yind-1][xind+0] == 'X':
            print('X')
            return None
        else:
            if var == None:
                sq(xind*Edge, yind*Edge, L, 'black')
            elif var == 'line':
                pass
                #sq(xind*Edge, yind*Edge, L, 'black')
            else:
                sq(xind*Edge, yind*Edge, L, 'blue')
            xind+=0
            yind-=1
            sq(xind*Edge, yind*Edge, L, 'red')
    print('Up')
    

def d(var=None):
    global xind
    global yind
    if yind == len(maze)-1:
        return None
    else:
        if maze[yind+1][xind+0] == 'X':
            print('X')
            return None
        else:
            if var == None:
                sq(xind*Edge, yind*Edge, L, 'black')
            elif var == 'line':
                pass
                #sq(xind*Edge, yind*Edge, L, 'black')
            else:
                sq(xind*Edge, yind*Edge, L, 'blue')
            xind+=0
            yind+=1
            sq(xind*Edge, yind*Edge, L, 'red')
    print('Down')

def l(var=None):
    global xind
    global yind
    if xind == 0:
        return None
    else:
        if maze[yind+0][xind-1] == 'X':
            print('X')
            return None
        else:
            if var == None:
                sq(xind*Edge, yind*Edge, L, 'black')
            elif var == 'line':
                pass
                #sq(xind*Edge, yind*Edge, L, 'black')
            else:
                sq(xind*Edge, yind*Edge, L, 'blue')
            xind-=1
            yind+=0
            sq(xind*Edge, yind*Edge, L, 'red')
    print('Left')

def r(var=None):
    global xind
    global yind
    if xind == len(maze[0])-1:
        print('len')
        return None
    else:
        if maze[yind+0][xind+1] == 'X':
            print('X')
            return None
        else:
            if var == None:
                sq(xind*Edge, yind*Edge, L, 'black')
            elif var == 'line':
                pass
                #sq(xind*Edge, yind*Edge, L, 'black')
            else:
                sq(xind*Edge, yind*Edge, L, 'blue')
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

def autoMazer(x,y):
    global lastStep
    steps=[str(xind)+','+str(yind)]
    for _ in range(190):
        if xind == x and yind == y:
            print('You Won!')
            break
        if lastStep == 'f':
            if maze[yind][xind-1] != 'X':
                lastStep= 'l'
                l('duo')
            elif maze[yind-1][xind] == 'X':
                lastStep= 'r'
            else:
                f('duo')
        elif lastStep == 'r':
            if maze[yind-1][xind] != 'X':
                lastStep= 'f'
                f('duo')
            elif maze[yind][xind+1] == 'X':
                lastStep = 'd'
            else:
                r('duo')
        elif lastStep == 'd':
            if maze[yind][xind+1] != 'X':
                lastStep= 'r'
                r('duo')
            elif maze[yind+1][xind] == 'X':
                lastStep= 'l'
            else:
                d('duo')
        elif lastStep == 'l':
            if maze[yind+1][xind] != 'X':
                lastStep= 'd'
                d('duo')
            elif maze[yind][xind-1] == 'X':
                lastStep= 'f'
            else:
                l('duo')
        steps.append(str(xind)+','+str(yind))
        s.update()
        pass
    return steps



def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

#path = common_elements(autoMazer(targetX,targetY),autoMazer(0,1))

firstRoute = autoMazer(targetX,targetY)
lastStep = firstStep()
lastRoute = autoMazer(0,1)

finalRoute = common_elements(firstRoute,lastRoute)

print(finalRoute)

#wew = ['0,1', '1,1', '3,1', '3,2', '3,3', '3,4', '3,5', '4,5', '5,5', '5,4', '5,3', '5,2', '5,1', '6,1', '7,1', '8,1', '9,1', '10,1', '11,1', '13,1', '13,2', '13,3', '13,4', '13,5', '13,6', '13,7', '13,7', '11,7', '10,7', '9,7', '8,7', '7,7', '7,8', '7,9', '7,10', '7,11', '7,12', '7,13', '8,13', '9,13', '10,13', '11,13', '12,13', '13,13', '15,13', '15,14', '15,15', '15,16'] 

for x in finalRoute:
    y = x.split(',')
    #print(y)
    sq(int(y[0])*Edge, int(y[1])*Edge, L, 'cyan')
    pass



#sq(int(wew[0][0])*Edge, int(wew[0][2])*Edge, L, 'cyan')

s.onkey(f, "Up")
s.onkey(d, "Down")
s.onkey(l, "Left")
s.onkey(r, "Right")
s.listen()

print(t.position())

#s.mainloop()
turtle.done()