'''
Exercise 5: Where’s that bug!
You have just started your placement, and you are given a piece of code to correct. The aim of
the script is to take a 2D list (that is a list of lists) and print a list containing the sum of each
list. For example, given the list in data, the output should be [6, 2, 10].
Modify the code below such that it gives the right result. In addition, you have been asked to
refactor the script into a function sum_lists(list_2D) that returns the list containing the
sums of each sub-list.
data = [[1,2,3], [2], [1, 2, 3, 4]]
output =[]
total = 0
for row in data:
 for val in row:
 total += val
 output.append(total)
print(output)
'''
data = [[1,2,3], [2], [1, 2, 3, 4]]
output =[]
total = 0
for row in data:
    for val in row:
        total += val
    output.append(total)
    total=0
print(output)