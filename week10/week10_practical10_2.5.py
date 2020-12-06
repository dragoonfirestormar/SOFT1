def collate_precipitation(filenames, outputfile):
    container={}
    for x in filenames:
        f = open(x)
        f = f.read()
        ignore=False
        temp=''
        for x in f.strip()+'\n':
            if(ignore):
                if x == '\n':
                    if temp.split(',')[0] not in container:
                        container[temp.split(',')[0]]=temp.split(',')[1]
                    else:
                        container[temp.split(',')[0]]=container[temp.split(',')[0]]+ ', '+temp.split(',')[1]
                    temp=''
                else:
                    temp+=x
            if x == '\n':
                ignore=True
    
    toWrite = ''
    for x in container.items():
        toWrite += x[0]+': '+x[1]+'\n'
    f = open(outputfile, 'w')
    f.write(toWrite)

collate_precipitation(['week10/Data/precipitations-Europe.txt','week10/Data/precipitations-NAmerica.txt','week10/Data/precipitations-world.txt'],'week10/Data/together2.5.txt')