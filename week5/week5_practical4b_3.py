'''
Exercise 3:
Write a function save_to_log(entry, logfile) that takes two parameters, a string
entry to be written at the end of the text file named logfile (also a string). The previous
content of the logfile MUST NOT be erased
'''
def save_to_log(entry, logfile):
    with open(logfile,'a') as x:
        print(entry, file=x)

save_to_log('more','ayy')