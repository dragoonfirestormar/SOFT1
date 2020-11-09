'''
Exercise 4:
Implement the following accessor and mutator:
• get(index) which returns the value of the element at position index in the vector
• set(index, value) which set the element at position index to the new value
value. The method does not return any value.
Let’s implement the scalar product method scalar_product(scalar) as an example.
The method needs only one parameter, the scalar. In addition, the method should return a new
Vector containing the result of the operation, but MUST NOT modify the calling instance,
e.g. my_vector.scalar_product(3) must not modify the instance my_vector.
 def scalar_product(self, scalar):
 '' add some doc-string''
 pass
'''

#Complete Answer Is Within Vector.py

def getValue(self, position):
        if self._vector == None:
            return 'Matrix is Empty'
        else:
            try:
                return self._vector[position]
            except:
                return 'Out of Index!'

def setValue(self, position, value):
        if self._vector == None:
            return 'Matrix is Empty'
        else:
            try:
                self._vector[position] = value
                return None
            except:
                return 'Out of Index!'