'''
Exercise 2:
Write in pseudo code a function merge(listA: List, listB: List) that returns a
sorted list containing the elements of both list where listA and listB are two sorted lists
of integers. If an element exists in both lists, it must appear multiple times in the returned list.
For example:
>>> merge([1,3,4,7],[2,3,5])
[1,2,3,3,4,5,7]
'''
def merge(listA, listB):
    AnB = []
    while listA!=[] and listB!=[]:
        if listA[0]<=listB[0]:
            AnB.append(listA[0])
            listA.pop(0)
        else:
            AnB.append(listB[0])
            listB.pop(0)
    if listA==[]:
        AnB+=listB
    else:
        AnB+=listA
    return AnB

print(merge(list(map(int,input('Enter an Array seperated by space: ').split())),list(map(int,input('Enter an Array seperated by space: ').split()))))