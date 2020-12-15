import random
Column = []
for x in range(ord('A'),ord('I')+1):
    Column.append(chr(x))
print(Column)

Rows = [None]*9


Game = [[0 for i in range(len(Column))] for j in range(len(Rows))]


print(Game)

mX = len(Game[0])
mY = len(Game)

print(mX)
print(mY)

Bombs = []

mB = 10

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
    temp = ''
    for x in game:
        temp+=str(x)+'\n'
    return temp

print(game(Game))

for x in Bombs:
    Game[x[1]][x[0]]='X'

print(game(Game))

showcase = [[0 for i in range(len(Column))] for j in range(len(Rows))]

print(game(showcase))

def yikes(inp):
    #inp = (0,0)
    # inp[0]=_ inp[1]=|
    sR = inp[0]
    while sR>=0:
        sC = inp[1]
        while sC>=0:
            if Game[sC][sR] !=0:
                break
            else:
                showcase[sC][sR] = 'xo'
                sC-=1
        sC = inp[1]
        while sC<mX:
            if Game[sC][sR] !=0:
                break
            else:
                showcase[sC][sR] = 'xo'
                sC+=1
        sR-=1
    sR = inp[0]
    while sR<mX:
        sC = inp[1]
        while sC>=0:
            if Game[sC][sR] !=0:
                break
            else:
                showcase[sC][sR] = 'xo'
                sC-=1
        sC = inp[1]
        while sC<mX:
            if Game[sC][sR] !=0:
                break
            else:
                showcase[sC][sR] = 'xo'
                sC+=1
        sR+ =1
    '''
    if inp[1]>=0 and inp[0]>=0 and inp[1]<9 and inp[0]<9:
        if Game[inp[1]][inp[0]] !=0:
            print('oof')
            return
        else:
            showcase[inp[1]][inp[0]]='XO'
            yikes((sA-1,sB))
            yikes((sA+1,sB))


    else:
        return
    '''
yikes((1,1))
print(game(showcase))