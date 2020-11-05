import math

input = int((input("Enter Your Number: ")))

valid = True

lowerlimit = 2
upperlimit = math.ceil(pow(input,1/2))

print(upperlimit)

for x in range(2,upperlimit+1):
    if(input%x==0):
        valid=False
        print('non-prime')
        exit()
        pass
    pass
if(valid):
    print( 'prime' )