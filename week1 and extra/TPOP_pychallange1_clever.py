import pickle
import math 

inputFile = 'TPOP_pychallange1_clever.data'
fd = open(inputFile, 'rb')
dataset = pickle.load(fd)
print (dataset)

input = int((input("Enter Your Number: ")))

valid = True

for x in dataset:
    if(x==input):
        print("PRIME")
        exit()
        pass
    if(input%x==0):
        print("NON-PRIME")
        exit()
        pass
    pass



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
    dataset.append(input)
    outputFile = 'TPOP_pychallange1_clever.data'
    fw = open(outputFile, 'wb')
    pickle.dump(dataset, fw)
    fw.close()