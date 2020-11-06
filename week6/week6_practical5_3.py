def flatten(list_2D):
    temp=[]
    for x in list_2D:
        for y in x:
            temp.append(y)
    return temp

print(flatten([[1,2],[],[7],[]]))