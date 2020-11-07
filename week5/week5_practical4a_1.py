'''
Exercise 1:
Write a Python function display_dico(dico) that takes a dictionary as parameter and print the
content of the dictionary, one paired element per line as follow:
Key --> Value
For example:
>>> display_dico({“un”:1, “deux”:2, “trois”:3})
un --> 1
deux --> 2
trois --> 3
Note: if the order in which the mapped pairs of a dictionary appear differs from the one shown
in the example, your solution is still valid.
'''
def display_dico(dico):
    for x in dico:
        print(f"{x} --> {dico[x]}")

x = {'un':1, 'deux':2, 'trois':3}
display_dico(x)