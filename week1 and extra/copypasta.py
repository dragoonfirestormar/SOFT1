import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Maze")
wn.setup(500,500)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        pass
    pass

levels = [""]

level_1 = [
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

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            chachrecter = level[y][x]
            screen_x = -233 + (x*24)
            screen_y = 233 - (y*24) 

            if(chachrecter=="X"):
                pen.goto(screen_x,screen_y)
                pen.stamp()
                pass
            pass
        pass
    pass

pen = Pen()

setup_maze(levels[1])

turtle.done()