'''
Week 7 – Practical 6 Part A
You may remember the exercise you have done in week 4 (additional exercise 5) regarding
vectors. For your convenience I have rewritten the definition here.
A vector of dimension 𝑛 can be represented by a list of n elements in Python. We would like
to create a class Vector with two basic operations on vectors:
Scalar product: 𝜆 ∙ [
𝑎
𝑏
𝑐
] = [
𝜆 ∙ 𝑎
𝜆 ∙ 𝑏
𝜆 ∙ 𝑐
]
Addition: [
𝑎
𝑏
𝑐
] + [
𝑑
𝑒
𝑓
] = [
𝑎 + 𝑑
𝑏 + 𝑒
𝑐 + 𝑓
]
Implementing a Vector Class
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
Exercise 2:
Another very useful method to write is __str__. This will enable us to print the content of
the instance using the print function. For the purpose of this exercise we have decided to
represent the vector [
𝑎
𝑏
𝑐
] with the string '<a, b, c>' to differentiate it from a list.
Implement __str__.
 def __str__(self):
 pass
Lilian Blot Software 1
P a g e | 2
Now let see how we can instantiate (create) some vectors.
>>> my_vector = Vector([1, 2, 3])
>>> print(my_vector)
<1, 2, 3>
>>> empty_vector = Vector()
>>> print(empty_vector)
<>
Adding behaviours to the class Vector
We now need to think about the definition of a vector, what operation could be done? We know
that we can add two vectors of same dimension, we can do the scalar product with a number
(called a scalar), what else?
• Get the dimension of a vector (e.g. the number of elements in the vector)
• Get the value at a defined position in the vector
• Set a value at a defined position in the vector
• Check if they are equals, not equals
• Do the scalar product
• Do an addition between two vectors of equal size.
Exercise 3:
Implement the method dim() that returns the dimension of a vector (i.e. the number of
elements in a vector)
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
 'add some doc-string'
 pass
Lilian Blot Software 1
P a g e | 3
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
Exercise 6:
In Programming, being able to compare objects is important, in particular determining if two
objects are equal or not. Let’s try a comparison of two vectors:
>>> vector1 = Vector([1, 2, 3])
>>> vector2 = Vector([1, 2, 3])
>>> vector1 == vector2
False
>>> vector1 != vector2
True
>>> vector3 = vector1
>>> vector3 == vector1
True
As you can see, in the current state of implementation of our class Vector does not produce the
expected result when comparing two vectors. In the example above the == operator return
True if the two vectors are physically stored at the same memory address, it does not compare
the content of the two vectors.
Therefore, you need to implement a method equals(other_vector) that returns True
if the vectors are equals (i.e. have the same value at the same position), False otherwise.
Hint: to check if an object is of a certain type you can use isinstance(var, Type). For
example isinstance(other_vector, Vector).
Lilian Blot Software 1
P a g e | 4
Once implemented we should have the following results
>>> vector1 = Vector([1, 2, 3])
>>> vector2 = Vector([1, 2, 3])
>>> vector1.equals(vector2)
True
>>> vector3 = Vector([0, 2, 0])
>>> vector3.equals(vector1)
False
>>> vector1 == vector2
False
'''


'''
Week 7 – Practical 6 part B
Before attempting this practical, you should complete part A. The aim of this practical is to
improve the functionality of the class Vector you implemented earlier this week. You will do
so by refactoring your code and overloading existing operators. All tests from previous
practical should still work. You should try to ensure backward compatibility.
Exercise 1:
We are now able to compare two vectors, however it would be nice if we could use the operator
== instead of .equals(…). Fortunately Python allows to overload operators such as +, *,
== and !=. To overload the operator ==, we must override the method __eq__. (for the
operator !=, override the method __ne__).
Implement the two methods:
def __eq__(self, other_vector):
 <body>
def __ne__(self, other_vector):
 <body>
Exercise 2:
Instead of using the method add(…) and scalar_product(…) we would like to overload
the operators + and *. The vector addition operator is commutative, i.e. v1+v2 == v2+v1
and we can override the method __add__ to overload the + operator. When considering the
multiplication, it is a little bit more complicated, 3 * v1 is allowed, but v1 * 3 is not.
Investigate the methods __mul__ and __rmul__. One other programming shortcut we
could find useful is v1 += v2 for v1 = v1+v2. It can be implemented by overloading
__iadd__. Similarly, the shortcut v1 *= 3 for v1 = 3 * v1 can be implemented by
overloading __imul__. Implement all these operators overloading.
Exercise 3:
There is a way to add the following functionality to our class Vector.
>>> vector1 = Vector(1, 2, 3, 5, 6, 1)
>>> vector1[2] += 5
>>> print(vector1)
<1.0, 2.0, 8.0, 5.0, 6.0, 1.0>
Search the web to find out how it can be done (I will NOT provide the answer). For method
with undefined number of parameters search *args. Note, the tests provided in previous
practical should still be working, including the test for the __init__ method
'''
class Vector():
    def __init__(self, data=None):
        self._vector = data
        pass

    def __str__(self):
        add=''
        if self._vector == None:
            add=''
            pass
        else:
            for x in range(len(self._vector)):
                add +=  (str(self._vector[x]) + ', ')
                pass
        return '<'+add[:-2]+'>'

    def dimension(self):
        if self._vector == None:
            return 0
        else:
            return len(self._vector)

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

    def equal(self, matrix):
        if not(isinstance(matrix,Vector)):
            return 'TypeError'
        if self._vector==matrix._vector:
            return True
        else:
            return False

    def scalar(self, intValue):
        if self._vector == None:
            return 'Matrix is Empty'
        else:
            vector = self._vector
            for x in range(len(vector)):
                vector[x] = int(vector[x]*intValue)
            return vector
    
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

    def __eq__(self, matrix):
        return self.equal(matrix)
    
    def __ne__(self, matrix):
        return not(self.equal(matrix))

    def __add__(self, matrix):
        return self.addition(matrix)

    def __mul__(self, intValue):
        return self.scalar(intValue)
 
    def __rmul__(self, intValue):
        return self.scalar(intValue)

    def __iadd__(self, matrix):
        return self.addition(matrix)
    
    def __imul__(self, intValue):
        return self.scalar(intValue)

    def __getitem__(self, position):
        return self.getValue(position)

    def __setitem__(self, position, value):
        return self.setValue(position, value)

    pass

my_vector = Vector([1,2,3])
print(my_vector+(Vector([1,2,3])))
my_vector[0] *= 2
print(my_vector)