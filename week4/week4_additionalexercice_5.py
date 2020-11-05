def scalar_product(scalar, vector):
    for x in range(len(vector)):
        vector[x]*=scalar
    return vector

def vector_addition(vector1, vector2):
    if(len(vector2)!=len(vector1)):
        return 'Error'
    for x in range(len(vector1)):
        vector1[x]+=vector2[x]
    return vector1


print(scalar_product(2,[1,2,3]))

print(vector_addition([1,1,1],[2,2,2]))