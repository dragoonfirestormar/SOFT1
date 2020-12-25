def rec (value, weight, max_weight):
    if len(value) == 0:
        return 0
    else:
        return max( value[0] + rec(value[1:], weight[1:], max_weight-weight[0]), rec(value[1:], weight[1:], max_weight) ) if max_weight-weight[0]>0 else 0


print( rec([20, 5, 5, 10, 40, 15, 25], [1, 2, 2, 3, 8, 7, 4], 10) )