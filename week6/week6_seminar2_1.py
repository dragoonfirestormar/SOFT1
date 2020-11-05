def lar(lis):
    max=0
    temp=0
    moretemp=[]
    lismax=[]
    for num in range(len(lis)):
        for x in range(num,len(lis)):
            for y in range(num,x):
                temp+=lis[y]
                moretemp.append(y)
            if(max<temp):
                max=temp
                lismax=lis[num:x]
            temp=0
            moretemp.clear()
    return max,lismax


print(lar([-2,1,-3,4,-1,2,1,-5,4]))