N=int(input("Enter The Number: "))
firstnsum=0
table="\n"
factorial=1
for x in range(1,N+1,1):
    firstnsum+=x
    table+=str(N)+"x"+str(x)+"="+str(N*x)+"\n"
    factorial*=x
    pass

print("Sum of first N digits: ",firstnsum)
print("Table: ",table)
print("Factorial: ",factorial)