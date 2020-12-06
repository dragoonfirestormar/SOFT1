a = open('week10/Data/precipitations-Europe.txt')
a = a.read()
b = open('week10/Data/precipitations-NAmerica.txt')
b = b.read()
c = open('week10/Data/precipitations-world.txt')
c = c.read()

def getDict(f):
    ignore=False
    container={}
    temp=''
    for x in f.strip()+'\n':
        if(ignore):
            if x == '\n':
                container[temp.split(',')[0]]=temp.split(',')[1]
                temp=''
            else:
                temp+=x
        if x == '\n':
            ignore=True
    return container

a = getDict(a)
b = getDict(b)
c = getDict(c)

toWrite = ''

for x in a.items():
    toWrite = toWrite + x[0] + ': ' + a[x[0]] + ', ' + b[x[0]] + ', ' + c[x[0]] + '\n'

f = open('week10/Data/together2.txt', 'w')
f.write(toWrite)