'''
Exercise 3:
Write a function map_list(keys, values) that takes two list of the same length as
parameters and returns a dictionary where the keys are the elements from the list keys and the
values are the elements from the list values. The mapping follows the lists indices.
For example:
>>> map_list([‘un’, ‘two’], [1,2])
{‘un’:1, ‘two’:2}
The Advanced bit:
An issue may arise if the list keys as duplicate elements as the keys must be unique. Rewrite
the function so that the method returns None and print an error message if keys has duplicates.
Note that having duplicate values in the values list is fine.
Note: This function could be used to map the list of English alphabet characters with the list of
their frequencies in the English language.
'''
def map_list(keys, values):
    ayy={}
    for x in range(len(keys)):
        if keys[x] in ayy:
            print("Error")
            return None
        ayy[keys[x]]=values[x]
    print (ayy)

map_list(['‘un’', '‘two’'], [1,2])