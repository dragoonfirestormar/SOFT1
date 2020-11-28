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