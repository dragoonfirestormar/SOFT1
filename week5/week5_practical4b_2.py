'''
Exercise 2:
Write a function save_list2file(sentences, filename) that takes two
parameters, where sentences is a list of string, and filename is a string representing the
name of the file where the content of sentences must be saved. Each element of the list
sentences should be written on its own line in the file filename.
'''
def save_list2file(sentences, filename):
    with open(filename,'w') as x:
        for y in sentences:
            print(y, file=x)

save_list2file(['yikes','lolxd'],'ayy')