
def sum_all(n):
    if n==0:
        return 0
    elif n<0:
        return -1
    else:
        return n+ sum_all(n-1)

def mul_table(n):
    if n<0:
        return 'error'
    else:
        table = ''
        for x in range(1,11):
            table+= f"{x} x {n} = {x*n}\n"
        return table

def factorial(n):
    if n==0: 
        return 1
    elif n<0:
        return -1
    else:
        return n* factorial(n-1)
    
print(sum_all(10))
print(mul_table(3))
print(factorial(10))