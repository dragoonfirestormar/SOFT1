factor = True
sum=0
total=0
evens=0

def printEXIT(a,b,c):
    print("Sum of all the number entered:",a)
    print("Average of all the number entered:",b)
    print("Number of even number entered:",c)
    exit()
    pass

while factor:
    x=input("Enter A Number: ")
    total+=1
    sum+=float(x)
    evens+=1 if float(x)%2==0 else 0
    print("You have entered:", x if float(x)>=0 else printEXIT(sum,sum/total,evens))
    pass