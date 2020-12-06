f = open('week10/Data/aberporth_meteorological_data.txt')
f = f.read()

container={}
ignore=False
temp=''
for x in f.strip()+'\n':
    if(ignore):
        if x == '\n':
            if temp.split(',')[0] not in container:
                container[temp.split(',')[0]]=[ float(temp.split(',')[4]), float(temp.split(',')[5]), float(temp.split(',')[6]) ]
            else:
                geez = container[temp.split(',')[0]]
                container[temp.split(',')[0]]=[ geez[0]+ float(temp.split(',')[4]), geez[1]+float(temp.split(',')[5]), geez[2]+float(temp.split(',')[6]) ]
            temp=''
        else:
            temp+=x
    if x == '\n':
            ignore=True

toWrite = 'Year, Air Frost, Rain, Sunshine\n'
for x in container.items():
    toWrite += x[0]+', '+str(x[1][0])+', '+str(x[1][1])+', '+str(x[1][2])+'\n'
f = open('week10/Data/together.csv', 'w')
f.write(toWrite)