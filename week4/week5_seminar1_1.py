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
toFind = [-1, 1, 2, 4, 8]
target = 7

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
for x in range(0, len(toFind)):
    ind = int(len(toFind)/2)
    y=x
    while x<ind and y<len(toFind):
        if toFind[y] + toFind[ind] > target:
            ind = ind - int(ind/2)
        elif toFind[y] + toFind[ind] < target:
            ind = ind + int(ind/2)
        else:
            if not( (toFind[y],toFind[y]) in output or (toFind[y],toFind[y]) in output ):
                output.append((toFind[y],toFind[ind]))
                break
        y+=1

print(output)
'''