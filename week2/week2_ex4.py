'''
Exercise 4:
Write a script that take the age and rate (the heart rate) that print a description of a person's
training zone based on his or her age and training heart rate, rate. The zone is determined
by comparing rate with the person's maximum heart rate m:
Interval range Training Zone
rate ≥ 0.9 m Interval training
0.7 m ≤ rate < 0.9 m Threshold training
0.5 m ≤ rate < 0.7 m Aerobic training
rate < 0.5 m Couch potato
The maximum heart rate in beats per minute is given by the formula:
𝑚𝑚 = 208 − 0.7 age.
'''
age = int(input('Your age: '))
rate = float(input('Your rate: '))

m=208-0.7*age

if (rate<0.5*m):
    print('Couch potato')
    pass
elif (rate<0.7*m):
    print('Aerobic training')
    pass
elif (rate<0.9*m):
    print('Threshold training')
    pass
else: 
    print('Interval training')
    pass