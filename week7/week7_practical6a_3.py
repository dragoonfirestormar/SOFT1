'''
Exercise 3:
Implement the method dim() that returns the dimension of a vector (i.e. the number of
elements in a vector)
'''

#Complete Answer Is Within Vector.py

def dim(self):
        if self._vector == None:
            return 0
        else:
            return len(self._vector)