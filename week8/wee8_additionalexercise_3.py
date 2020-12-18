V = [20, 5, 5, 10, 40, 15, 25]
W = [1, 2, 2, 3, 8, 7, 4]
Mw = 10

def val(value, weight, max_weight):
    if value == []:
        return 0
    if len(value) == 1:
        if weight[0] <= max_weight:
            return value[0]
        return 0
    else:
        temp, tv, tw = 0, 0, 0
        for x in range(1,len(value)):
            print('\n###################################')
            if x == len(value)-1:
                t = val(value[x:], weight[x:], max_weight)
                v,w = value[x:][0], weight[x:][0]
            else:
                t = val(value[x:-len(value)+1+x], weight[x:-len(value)+1+x], max_weight)
                v,w = value[x:-len(value)+1+x][0], weight[x:-len(value)+1+x][0]
            tw+=w
            tv+=t
            if tw >= max_weight:
                tv=0
            else:
                if tv>temp:
                    temp=tv
            print(t)
            print(v,w)
        return temp


print('\n',val([1,6,7],[1,4,7],10))
x=1
#print(V[x:-len(V)+x+1])
#print(val(V[x:-len(V)+1+x], W[x:-len(V)+1+x], Mw))

#print([1,6][:])
#print([1,6][1:-1+1+1])