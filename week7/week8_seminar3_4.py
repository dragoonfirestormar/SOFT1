
'''
Exercise 4:
An influencer is a person who doesn’t follow anybody but is followed by everybody. Given N
peoples and an adjacency matrix for the graph “following”, where the edge (A,B) means A
follows B, find the influencer among the group of N peoples if it exists.
Figure 1: Example of 2 social networks. On the left-hand side, the network does not have an
influencer, however on the right-hand side, C is an influencer.
Lilian Blot Software 1
P a g e | 2
In this exercise, you must use the adjacency matrix representation. Given a matrix following
that represents users following other users within a community of N users (with ids from 0 to
N-1):
• 𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔[𝑖][𝑗] = 1 if and only if user 𝑖 is following user 𝑗. However, it doesn’t
imply 𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔[𝑗][𝑖] = 1.
• Let’s also agree that 𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔𝑀𝑎𝑡𝑟𝑖𝑥[𝑖][𝑖] = 0.
Find an Influencer find the influencer in this community network (that is its index), or return -
1 if there is no Influencer in this group.
Brute force
For each user 𝑈, you can check that the two properties below hold:
1. Everybody follows 𝑈,
2. 𝑈 doesn’t follow anybody.
A better approach
We can find the influencer in O(n) time by testing each person for the above properties. We
can select a person 𝑈 as a candidate influencer and then test if 𝑈 is indeed a influencer by
testing with next person. If the next person 𝑈𝑘 doesn’t follow the current candidate or the
candidate follows 𝑈𝑘 then 𝑈𝑘 may be the influencer. We can choose such a candidate and then
test if all other person followsthe candidate 𝑈𝑘 and the candidate 𝑈𝑘 doesn’t follow anybody.
If any of these properties fail, we say there is no such influencer.
Write the pseudo-code to implement this approach.

'''
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


#print(rowCheck(B))

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

#print(godsPlan(B))
influencer=[]
def xd(List):
    Elm = []
    NotInf = {}
    MayInf = {}
    l = len(List)
    for row in range(l):
        for column in range(l):
            if len(Elm) == len(ElementsName):
                return influencer
            if List[row][column] == 1:
                NotInf.add(1)
                if ElementsName[row] in MayInf:
                    MayInf.remove(ElementsName[row])
                    pass
            else:
                pass
