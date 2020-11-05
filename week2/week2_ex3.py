'''
Exercise 3:
A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage and
packaging. If an order is over £50.00, the P&P is reduced by £1.50. Write a script that will take
the number of kilo of bananas as a user input and print the cost of that order.
'''

print('Welcome to the Banana Shopping.\nToday\'s Price Is £3.00/kg\n(For all the orders below £50 we cost £4.99 delivery charges, and if above that, then we charges £3.49)')

amount = float(input("Please enter the Kg(s) of Banana you want to buy : "))

print( 'Total Cost Is: £', amount*3+4.99 if amount>50 else amount*3+3.49 )
