def save_to_log(entry, logfile):
    with open(logfile,'a') as x:
        print(entry, file=x)

save_to_log('more','ayy')