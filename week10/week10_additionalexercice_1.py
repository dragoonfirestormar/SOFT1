import random

Column = []
for x in range(ord('A'),ord('I')+1):
    Column.append(chr(x))
print(Column)

Rows = [None]*9


Game = [[0 for i in range(len(Column))] for j in range(len(Rows))]


print(Game,'\n')

mX = len(Game[0])
mY = len(Game)

print(mX)
print(mY,'\n')

Bombs = []

mB = _mB = 1

while mB>0:
    ran = (random.randint(0,mX-1),random.randint(0,mY-1))
    if not ran in Bombs:
        Bombs.append(ran)
        mB-=1

for x in Bombs:
    cI = x[0]
    rI = x[1]

    for r in range(3):
        if r+rI-1>=0 and r+rI-1<mY:
            T = Game[r+rI-1]
            for c in range(3):
                if c+cI-1>=0 and c+cI-1<mY:
                    if T[c+cI-1] == 0:
                        T[c+cI-1] = 1
                    else:
                        T[c+cI-1] += 1
            Game[r+rI-1] = T

def game(game):
    temp = ' '*5
    t=0
    for x in range(0, len(game)):
        temp+=str(x)+' '*2
    temp+='\n\n'
    for x in game:
        temp+=str(t)+' '*4
        t+=1
        for y in x:
            temp+=str(y)+' '*2
        temp+='\n'
    return temp

print(game(Game))

for x in Bombs:
    Game[x[1]][x[0]]='X'

print(game(Game))

showcase = [[0 for i in range(len(Column))] for j in range(len(Rows))]

print(game(showcase))

gg=0

def check(arr, ind):
    for x in arr:
        count = x.count(0)
        ind-=count
    if ind==0: return True
    else: False

var = ' '

def yikes(inp):
    #print(game(showcase))
    global gg
    gg+=1
    print(gg)
    if gg>100:
        exit()
    I = inp[0]
    J = inp[1]
    print(inp)
    if I>=0 and J>=0 and I<mX and J<mY:
        if str(Game[I][J]) == str(0):
            showcase[I][J] = var
            if J+1<mY:
                if str(showcase[I][J+1]) != str(var):
                    yikes((I,J+1))
            if J-1>=0:
                if str(showcase[I][J-1]) != str(var):
                    yikes((I,J-1))
            if I+1<mX:
                if str(showcase[I+1][J]) != str(var):
                    yikes((I+1,J))
            if I-1>=0:
                if str(showcase[I-1][J]) != str(var):
                    yikes((I-1,J))
        else:
            temp = Game[I][J]
            if temp != 'X':
                showcase[I][J] = Game[I][J]
            else:
                exit("You Lost")
    else:
        return False

while(True):
    yikes((int(input("A: ")), int(input("B: "))))
    if(check(showcase, _mB)):
        exit('Won!')
    print(game(Game))
    print(game(showcase))


