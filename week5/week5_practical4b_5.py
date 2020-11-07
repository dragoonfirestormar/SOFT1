'''
Exercise 5:
Write a function to_upper_case(input_file, output_file) that takes two
string parameters containing the name of two text files. The function reads the content of the
input_file and saves it in upper case into the output_file.
'''
def to_upper_case(input_file, output_file):
    with open(input_file) as x:
        with open(output_file, 'w') as y:
            print(x.read().upper(), file=y)

to_upper_case('ayy','exo1.txt')