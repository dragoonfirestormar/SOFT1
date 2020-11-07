'''
Exercise 4:
Write a function reverse_dictionary(dico) that reverse the mapping between keys
and values. The parameter dico is a dictionary where the keys and values are all immutable.
The function should return a dictionary where the pair key1:value1 in dico becomes the
pair value1:key1. For example
>>> reverse_dictionary({“one”:1, “two”:2})
{1:“one”, 2:“two”}
The Advanced bit:
An issue may arise again if the dictionary dico as duplicate elements in its values. Rewrite
the function so that the method returns None and print an error message if that is the case.
'''
def reverse_dictionary(dico):
    ayy={}
    for k in dico:
        if dico[k] in  ayy:
            print("Error")
            return None
        ayy[dico[k]]=k
    print(ayy)

reverse_dictionary({'“one”':1, '“two”':2})