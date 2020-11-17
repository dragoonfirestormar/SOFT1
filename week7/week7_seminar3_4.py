    # ABCDE
B = [[0,1,1,1,0],
     [0,0,1,0,1],
     [0,0,0,0,0],
     [0,0,1,0,0],
     [0,1,1,0,0]]

ElementsName = ['A','B','C','D','E']

#Brute Force
influencer=[]
# row should have 0's        
def rowCheck(List):
    factor = True
    for row in range(len(List)):
        for column in range(len(List[0])):
            if List[row][column] !=0:
                factor = False
                break
        if factor:
            columnCheck(List,row)
        factor = True
    return influencer

# column should have 1's    
def columnCheck(List, ColumnID):
    for row in range(len(List)):
        if row == ColumnID:
            pass
        else:
            if List[row][ColumnID]==1:
                pass
            else:
                return False
    influencer.append(ElementsName[ColumnID])


print(rowCheck(B))

#God Like Move
influencer=[]
#One Extra Loop for More Efficiency 
def godsPlan(List):
    l = len(List)
    for diagnol in range(l):
        if List[diagnol][diagnol] == 0:
            NewtonPlan(List,diagnol,l)
            pass
    return influencer

#Cross Check with O(n) efficiency
def NewtonPlan(List, Index, Len):
    #factor = True
    for x in range(Len):
        if List[x][Index]==1 and List[Index][x]==0:
            pass
        else:
            if x == Index:
                pass
            else:
                return False
    influencer.append(ElementsName[Index])

print(godsPlan(B))