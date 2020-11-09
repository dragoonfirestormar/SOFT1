'''
Exercise 5:
Implement the method add(other_vector) that emulate the vector addition operator. The
method should return a new vector.
• You will have to check that other_vector is a Vector instance, and raise a
TypeError if it is not the case.
• You must check that both vector have the same dimension, raise a ValueError if it
is not the case.
• You must return a new Vector instance like we have done in
scalar_product(scalar).
Once implemented we should be able to do the following:
>>> vector1 = Vector([1, 2, 3])
>>> vector2 = Vector([0, 1, 3])
>>> added = vector1.add(vector2)
>>> print(added)
<1, 3, 6>
'''

#Complete Answer Is Within Vector.py

def addition(self, matrix):
        if not(isinstance(matrix,Vector)):
            return 'TypeError'
        elif len(self._vector) != len(matrix._vector):
            if self._vector == None:
                return 'Matrixes is Empty'
            else: 
                return 'Both Matrix should be of same dimention'
        else:
            newMat=[]
            for x in range(len(matrix._vector)):
                newMat.append(self._vector[x]+matrix._vector[x])
            return newMat