def to_upper_case(input_file, output_file):
    with open(input_file) as x:
        with open(output_file, 'w') as y:
            print(x.read().upper(), file=y)

to_upper_case('ayy','exo1.txt')