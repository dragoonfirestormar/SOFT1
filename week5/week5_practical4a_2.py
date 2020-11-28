'''
Exercise 2 :
Write a function concat_dico(dico1, dico2) that takes two dictionaries as parameters
and returns a single dictionary containing the pairs from both dictionaries. An important
requirement is that both dictionaries are NOT modified by the function.
For example:
>>> concat_dico ({“one”:1, “two”:2, “three”:3},
 {“four”:4, “five”:5})
{“one”:1, “two”:2, “three”:3, “four”:4, “five”:5}
The Advanced bit:
An issue may arise when both dictionaries share a least one common key. Rewrite the function
so that the method store the values in a list if dico1 and dico2 share a common key. In the
example below both dictionaries share the keys “two” and “five”.
>>> concatDico ({“one”:1, “two”:2, “five”:5},
 {“two”: ”10”, “five”:”101”})
{“one”:1, “two”:[2, ”10”], “five”:[5,”101”]}
'''
def concatDico(dico1, dico2):
    ayy = {}
    for k,v in dico1.items():
        ayy[k]=v
    for k,v in dico2.items():
        ayy[k]=v

    return (ayy)

print('For Starters ',concatDico({'“one”':1, '“two”':2, '“three”':3}, {'“four”':4, '“five”':5}))


def concatDico2(dico1, dico2):
    ayy = {}
    for k,v in dico1.items():
        if k in dico2:
            ayy[k]=[v,dico2[k]]
            del dico2[k]
        else:
            ayy[k]=v
    for k,v in dico2.items():
        ayy[k]=v

    return (ayy)

print('For Advance Bit ',concatDico2({'“one”':1, '“two”':2, '“five”':5},{'“two”': '”10”', '“five”':'”101”'}))
