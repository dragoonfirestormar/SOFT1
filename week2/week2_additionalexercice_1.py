#This is the solution for both Example 1 and 2
'''
Exercise 1:
Imperial to Metric converter
1. Write a series of small script that convert weight, distance, and liquid measurement
from Imperial to Metric system. For example weight:
• the script should ask the user to enter the number of stones
• the script should ask the user to enter the number of pounds
• The script should print the weight in Kilograms
2. Write the reverse conversion, for example
• the script should ask the user to enter the weight in Kg
• The script should print the closest weight in Stones and Pounds

Exercise 2:
We have used input(str) during the lecture. Rewrite the scripts from question 2 in order
to ask the user which conversion he/she want to do. Then the user should enter the measurement
values he/she want to convert.
'''

factor = int(input("Decide Among The Following Choices\n1. Imperial to Metric\n2. Metric to Imperial\nYour Input: "))

#conversion rates
#weight
w_imp = 0.5 #oz
w_met = 14.1748 #g

#distance
d_imp = 1 #inch
d_met = 2.54 #cm

#liquid
l_imp = 250 #ml
l_met = 1.05669 #cup

def moreoptions():
    print('What do you want to be converted?\n1. Weight\n2. Distance\n3. Liquid')

if(factor==1):
    moreoptions()
    moreoptions= int(input('Your Input: '))
    if (moreoptions==1):
        print (w_met/w_imp*float(input("How Much Oz Do You Want To Convert? : ")), "g" )
    elif (moreoptions==2):
        print (d_met/d_imp*float(input("How Much Inch Do You Want To Convert? : ")), "cm")
    elif (moreoptions==3):
        print (l_met/l_imp*float(input("How Much ml Do You Want To Convert? : ")), "Cup")
    else:
        print("Invalid Input!")
elif (factor==2):
    moreoptions()
    moreoptions= int(input('Your Input: '))
    if (moreoptions==1):
        print (w_imp/w_met*float(input("How Much g Do You Want To Convert? : ")), "Oz")
    elif (moreoptions==2):
        print (d_imp/d_met*float(input("How Much cm Do You Want To Convert? : ")), "Inch")
    elif (moreoptions==3):
        print (l_imp/l_met*float(input("How Much Cup Do You Want To Convert? : ")), "ml")
    else:
        pass
else:
    print("Not Valid Input!")