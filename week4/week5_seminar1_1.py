'''
Exercise 1:
You have given a sorted list of numbers with no duplicates, and you need to find the pairs of
numbers in that list whose sum is equal to the given target value.
Numbers can be either positive, negative, or both.
a) Test Case 1:
Input: [-1, 1, 2, 4, 8], target = 7
Output: [(-1, 8)]
b) Test Case 2:
Input: [2, 4, 5, 7], target = 9
Output: [(2,7), (5, 4)]
c) Test Case 3:
Input: [2, 4, 5, 7], target = 8
Output: []
Write an algorithm to find all such pairs given a list and a target. Note there are two approaches
to the problem, one called brute force where we try all possible combination of pairs and keep
the correct one (computationally expensive), one cleverer that is far more efficient.
'''
if(input('Enter anything if you want to insert custom input else hit enter: ')!=''):
    toFind = list(map(int,input('Enter Numbers in List Seperated by Space: ').split()))
    target = int(input('Enter Number to Find: '))
else:
    toFind = [2, 4, 5, 7]
    target = 9
'''
#brute force
output = set()
for x in range(len(toFind)):
    for y in range(len(toFind)):
        if toFind[x]+toFind[y] == target:
            if output.issubset((toFind[x],toFind[y])):
                output.add((toFind[x],toFind[y]))
print(output)
'''

#better way to do so
output = []
for x in range(0, int(len(toFind)/2)):
    if toFind[x]>=target:
        break
    #print('x :',x,toFind[x])
    T = (x,len(toFind))
    while T[1]-T[0]>1:
        ind = int((T[0]+T[1])/2)
        #print('T: ',T)
        #print('ind: ',ind)
        #print()
        if toFind[x] + toFind[ind] > target:
            T = (T[0], ind)
        elif toFind[x] + toFind[ind] < target:
            T = (ind, T[1])
        else:
            output.append((toFind[x],toFind[ind]))
            break

print(output)