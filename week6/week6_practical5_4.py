'''
Exercise 4:
Write a function rasterise(list_1D, width) that transforms a 1D list passed as
parameter into a 2D list, where each sub-list have width elements. If the length of the 1D list
is not a multiple of width, the function returns None. If width is less than 1, the function
returns None.
For example:
>>> rasterise([1,2,3,4,5,6,7,8],4)
[[1,2,3,4],[5,6,7,8]]
>>> rasterise([1,2,3,4,5,6,7,8],2)
[[1,2],[3,4],[5,6],[7,8]]
>>> rasterise([1,2,3,4,5,6,7,8],1)
[[1],[2],[3],[4],[5],[6],[7],[8]]
>>> rasterise([1,2,3,4,5,6,7,8],0)
None
>>> rasterise([1,2,3,4,5,6,7,8],3)
None
'''
def rasterise(list_1D, width):
    if len(list_1D)%width !=0:
        return None
    store=[]
    temp=[]
    count=0
    for _ in range(int(len(list_1D)/width)):
        for _ in range(width):
            temp.append(list_1D[count])
            count+=1
        store.append(temp)
        temp=[]
    return store

    
print(rasterise([1,2,3,4,5,6,7,8],2))