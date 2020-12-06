f = open('week10/Data/precipitations-Europe.txt')
f = f.read()
ignore=False
container=[]
temp=''
for x in f.strip()+'\n':
    if(ignore):
        if x == '\n':
            container.append(temp.split(','))
            temp=''
        else:
            temp+=x
    if x == '\n':
        ignore=True

def min_Precipitation(data):
    minm=data[0][1]
    for x in data:
        if x[1]<minm:
            minm = x[1]
            miny = x
    return miny

def max_Precipitation(data):
    maxm=data[0][1]
    for x in data:
        if x[1]>maxm:
            maxm = x[1]
            maxy = x
    return maxy

def average_Precipitation(data):
    total=0
    for x in data:
        total+=float(x[1])
    return total/len(x)
print( min_Precipitation(container) )
print( max_Precipitation(container) )
print( average_Precipitation(container) )