'''
Exercise 1: Class’ constructor
First of all, create a module called vector.py, then define the class Vector. The next step is to
define what will be the internal representation of a vector and then write the constructor
__init__. The design decision is to store the element of the vector[
𝑎
𝑏
𝑐
] in a list [a,b,c].
The constructor will take only one parameter, a list of float. The instance attribute _vector.
should have a copy of the list passed in the parameters.
def __init__(self, data = None):
 “”” some doc-string “””
 Pass
'''

#Complete Answer Is Within Vector.py

class Vector():
    def __init__(self, data=None):
        self._vector = data
        pass
