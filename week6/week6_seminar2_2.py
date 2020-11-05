def lar(mat):
    temp=0
    bigtemp=0
    max=0
    for row in range(len(mat)):
        for colm in range(len(mat[0])):
            for r in range(row,len(mat)):
                for c in range(colm,len(mat[0])):
                    for sums in range(r):
                        print(mat[sums][c])
                        temp+=mat[sums][c]
                    #print(temp)
                    bigtemp+=temp
                    if(bigtemp>max):
                        max=bigtemp
                    temp=0
                bigtemp=0
    return max

'''
print( lar([[6,-5,-7,4,-4],
           [-9,3,-6,5,2],
           [-10,4,7,-6,3],
           [-8,9,-3,3,-7]] ))
'''

print(lar([[1,2],[3,-4]]))