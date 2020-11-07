'''
Exercise 3:
Write a function flatten(list_2D) that transforms a 2D list passed as parameter into a
1D list. For simplicity, the input parameter is assumed to be a valid input. For example:
>>> flatten([[1,2],[3,4,5,6],[7],[8,9]])
[1,2,3,4,5,6,7,8,9]
>>> flatten([[1,2],[],[7],[]])
[1,2,7]
>>> flatten([[1,2,3,4,5]])
[1,2,3,4,5]
'''
def flatten(list_2D):
    temp=[]
    for x in list_2D:
        for y in x:
            temp.append(y)
    return temp

print(flatten([[1,2],[],[7],[]]))