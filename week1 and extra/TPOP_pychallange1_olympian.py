import math
input = int(input("Enter Your Number: "))

factors = []

x=1
while (input > 2):
    x=x+1
    if(input%x==0):
        factors.append(x)
        input=input/x
        x=1
        pass

factor = list(dict.fromkeys(factors))
multiple=1

for x in factor:
    multiple=multiple*x
    pass

print (multiple)