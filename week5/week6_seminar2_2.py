'''
Exercise 2:
Given a matrix (2D list) 𝐴[0. . 𝑛 − 1, 0. . 𝑚 − 1] of numbers, find the largest possible sum of a
rectangle submatrix. The top-left element in the matrix is 𝐴[0][0], and the element 𝐴[𝑟][𝑐] is
the element at row 𝑟, column 𝑐.
6 -5 -7 4 -4
-9 3 -6 5 2
-10 4 7 -6 3
-8 9 -3 3 -7
For example, for the matrix given above, the rectangle with the largest sum is highlighted in
red with sum 17.
Lilian Blot Software 1
P a g e | 2
Brute force approach
The main idea behind the brute force algorithm is to try all possible rectangles within the 2D
array. We can think of two cells to define a rectangle, the top-left corner (in orange) and the
bottom-right corner (in yellow if not the same as top-left corner). Below you can find a subset
of all the possible rectangle, and to understand better how to cover all possible rectangle,
complete the bottom row of the image.
Once you have understood the principle, write the algorithm to find the maximal rectangle sum
'''

# sum of submatrix
def sumMatrix(mat, topRow, topCol, botRow, botCol):
    Sum = 0
    for i in range(topRow, botRow+1):
        for j in range(topCol, botCol+1):
            Sum += mat[i][j]
    return Sum
#brute force with n^4 complexity
def brute(mat):
    R, C = len(mat), len(mat[0])
    Max = mat[0][0]

    for topRow in range(0,R):
        for topCol in range(0,C):
            for botRow in range(R-1, topRow, -1):
                for botCol in range(C-1, topCol, -1):
                    Max = max(Max,sumMatrix(mat, topRow, topCol, botRow, botCol))

    return Max


# Proper Kadane's Algorithm, returns the max sum
def num(lis):
    Max = Lmax = lis[0]
    for x in range(1,len(lis)):
        Lmax = lis[x] if lis[x]>Lmax+lis[x] else lis[x]+Lmax
        if Lmax > Max: Max = Lmax
    return Max
# only gets the max sum using Kadane's Algorithm as space complexity
def lar(mat):
    R, C = len(mat), len(mat[0])
    Max = mat[0][0]
    for r in range(R):
        Arr = [0]*R
        for c in range(r,C):
            Arr = [ mat[x][c]+Arr[x] for x in range(R) ]
            Lmax = num(Arr)
            if Lmax > Max:
                Max = Lmax
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
# returns the max sum and the extreme left, right, top, bottom index of sub matrix with the matrix itself
def larWithIndex(mat):
    R, C = len(mat), len(mat[0])
    Max = mat[0][0]
    for r in range(R):
        Arr = [0]*R
        for c in range(r,C):
            Arr = [ mat[x][c]+Arr[x] for x in range(R) ]
            Re = index(Arr)
            Lmax = Re[0]
            if Lmax > Max:
                Max = Lmax
                Mleft = r
                Mright = c
                Mup = Re[1][0]
                Mdown = Re[1][1]
    return (Max, Mleft, Mright, Mup, Mdown, mat)
# better viwer and showcase the results as the sub matrix as the indexes provided by the the larWithIndex
def printAr(cor):
    yikes=[]
    for r in range(cor[3],cor[4]):
        temp=[]
        for c in range(cor[1],cor[2]+1):
            temp.append(cor[5][r][c])
        yikes.append(temp)
    return (cor[0],yikes)

print((brute([[1,2],
           [3,-4]])))

print( printAr(larWithIndex([[6,-5,-7,4,-4],
           [-9,3,-6,5,2],
           [-10,4,7,-6,3],
           [-8,9,-3,3,-7]] )))
