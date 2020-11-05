lxb = (8,8)
grane = 0
counter = 1
for x in range(lxb[0]):
    for y in range(lxb[1]):
        grane+=counter
        counter*=2

print(counter*30, " mg")

