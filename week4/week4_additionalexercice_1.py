'''
Exercise 1: The King and the Wise man
When the creator of the game of chess showed his invention to the ruler of the country, the
ruler was so pleased that he gave the inventor the right to name his prize for the invention. The
man, who was very wise, asked the king this: that for the first square of the chess board, he
would receive one grain of wheat (in some telling, rice), two for the second one, four on the
third one, and so forth, doubling the amount each time. The ruler, arithmetically unaware,
quickly accepted the inventor's offer, even getting offended by his perceived notion that the
inventor was asking for such a low price and ordered the treasurer to count and hand over the
wheat to the inventor. Given that the chessboard is a 8 × 8 board and given the weight of a
single grain of rice is about 30 mg, calculate the total weight of rice the king must give to the
wise man. The program should print the weight of rice for each chessboard square.
'''
lxb = (8,8)
grane = 0
counter = 1
for x in range(lxb[0]):
    for y in range(lxb[1]):
        grane+=counter
        counter*=2

print(counter*30, " mg")

