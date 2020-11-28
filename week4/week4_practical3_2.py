'''
Exercise 2:
Write a function pairwise_digits(number_a, number_b) that takes two integers
as parameters and returns a binary string where a character 1 is used if the digits at the same
index are the same, a 0 otherwise. Examples are given in the table below.
Input A Input B Output
1213 2113 ‘0011’
1213 10435 ‘10010’
1213 121 ‘1110’
'''
def pairwise_digits(number_a, number_b):
    len_a = len(str(number_a))
    len_b = len(str(number_b))
    smallNbig = [len_a,len_b] if len_a <= len_b else [len_b,len_a]
    tempstr = ''
    for x in range(smallNbig[0]):
        if(str(number_a)[x]==str(number_b)[x]):
            tempstr+='1'
        else:
            tempstr+='0'
    tempstr+=(smallNbig[1]-smallNbig[0])*'0'
    return tempstr

print(pairwise_digits(int(input('Enter First Number: ')),int(input('Enter Second Number: '))))