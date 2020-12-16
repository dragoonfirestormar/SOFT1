'''
Exercise 1:
Given list A of 𝑛 numbers, find the largest possible sum of a contiguous sub-list.
-2 1 -3 4 -1 2 1 -5 4
For example, for the list given above, the contiguous sub-list with the largest sum is [4, -1, 2,
1], with sum 6 (in red).
Brute force approach
One obvious solution is to calculate the sum of every possible sub-list and the maximum of
those would be the solution. We can start from index 0 and calculate the sum of every possible
sub-list starting with the element A[0]. Then, we would calculate the sum of every possible
sub-list starting with A[1], A[2] and so on up to A[n-1], where 𝑛 denotes the size of the list.
Note that every single element is a sub-list itself.
Using the pseudo code notation shown in Seminar 1, write the brute force algorithm to solve
the problem. Given a list of size 𝑛, how many comparisons are done?
Could you think of a better approach?
This is quite difficult, and a better approach will be explained during the seminar session. But
it does not hurt to have a thought about it beforehand.
'''

#brute force with O(n^3)
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

# Proper Kadane's Algorithm with sub-array
def lis(lis):
    Max = Lmax = lis[0]
    L = M = [lis[0]]
    for x in range(1,len(lis)):
        if lis[x]>Lmax+lis[x]:
            Lmax=lis[x]
            L=[lis[x]]
        else:
            Lmax=lis[x]+Lmax
            L.append(lis[x])
        if Lmax > Max:
            Max = Lmax
            M=L
    return (Max,M)

# Life hack Kadane's Algorithm with sub-array
def lis2(lis):
    Max = Lmax = lis[0]
    L = M = [lis[0]]
    for x in range(1,len(lis)):
        if Lmax<0:
            Lmax=lis[x]
            L=[lis[x]]
        else:
            Lmax=lis[x]+Lmax
            L.append(lis[x])
        if Lmax > Max:
            Max = Lmax
            M=L
    return (Max,M)

# Proper Kadane's Algorithm
def num(lis):
    Max = Lmax = lis[0]
    for x in range(1,len(lis)):
        Lmax = lis[x] if lis[x]>Lmax+lis[x] else lis[x]+Lmax
        if Lmax > Max: Max = Lmax
    return Max

# Life hack Kadane's Algorithm
def num2(lis):
    Max = Lmax = lis[0]
    for x in range(1,len(lis)):
        Lmax = lis[x] if Lmax<0 else lis[x]+Lmax
        if Lmax > Max: Max = Lmax
    return Max


# Proper Kadane's Algorithm, returns the max sum and the index of last and first element included
def index(lis):
    Max = Lmax = lis[0]
    L = M = (0,1)
    for x in range(1,len(lis)):
        if lis[x]>Lmax+lis[x]:
            Lmax=lis[x]
            L=(x,x+1)
        else:
            Lmax=lis[x]+Lmax
            L=(L[0],L[1]+1)
        if Lmax > Max:
            Max = Lmax
            M=L
    return (Max,M)

print(index([-10,-5,-24,-5,-1,-6,-2]))