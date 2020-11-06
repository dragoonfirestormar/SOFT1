def rasterise(list_1D, width):
    if len(list_1D)%width !=0:
        return None
    store=[]
    temp=[]
    count=0
    for _ in range(int(len(list_1D)/width)):
        for _ in range(width):
            temp.append(list_1D[count])
            count+=1
        store.append(temp)
        temp=[]
    return store

    
print(rasterise([1,2,3,4,5,6,7,8],2))