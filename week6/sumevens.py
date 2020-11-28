''''
Sum of even numbers in the list (could not find the real question but was in .rar test files)
'''
def sum_even_numbers(numbers):
    total = 0
    for n in numbers:
        total += n if n%2==0 else 0
    return (total)

print(sum_even_numbers([1,2,3,4]))