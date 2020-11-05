def sum_from_file(filename):
    with open('exo1.txt') as x:
        temp=''
        su=0
        for y in x.read()+' ':
            if(y==' ' or y=='\n'):
                su+=int(temp)
                temp=''
                pass
            else:
                temp+=y
        return su

print(sum_from_file('exo1.txt'))