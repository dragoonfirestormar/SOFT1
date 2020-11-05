def map_list(keys, values):
    ayy={}
    for x in range(len(keys)):
        if keys[x] in ayy:
            print("Error")
            return None
        ayy[keys[x]]=values[x]
    print (ayy)

map_list(['‘un’', '‘two’'], [1,2])