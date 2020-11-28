'''
Exercise 3:
Suppose you have a rod of length 𝑛, and you want to cut up the rod and sell the pieces in a way
that maximizes the total amount of money you get. A piece of length 𝑖 is worth £ 𝑝_𝑖.
Table 1: An example of a price list.
Length 1 2 3 4 5 6
Price 𝒑𝒊
(£) 1 5 8 9 10 17
For example, if you have a rod of length 4, there are eight different ways to cut it, and given
the price list in Table 1, the best strategy is cutting it into two pieces of length 2, which gives
you £ 10.00 (see Figure 1).
Figure 1: The 8 possible ways of cutting up a rod of length 4. Given the price list in Table 1,
the optimal strategy is (c) cutting the rod into two pieces of length 2, which as a total value
of £10.00.
Lilian Blot Software 1
P a g e | 3
We can view the problem recursively as follows:
• First, cut a piece off the left end of the rod, and sell it.
• Then, find the optimal way to cut the remainder of the rod.
Part A: Naïve approach
Now we don't know how large a piece we should cut off. So, we try all possible cases. First,
we try cutting a piece of length 1, and combining it with the optimal way to cut a rod of length
𝑛 − 1. Then we try cutting a piece of length 2 and combining it with the optimal way to cut a
rod of length 𝑛 − 2. We try all the possible lengths and then pick the best one.
This is summarised by the equation
𝑟𝑛 = 𝒎𝒂𝒙1≤ 𝑖≤ 𝑛 (𝑝𝑖 + 𝑟𝑛−𝑖)
Write in pseudo-code rod_cutting(prices:list, length:int):int a recursive
algorithm that returns the optimal way to cut a rod of size length given a price list prices.
The parameter length is a positive integer. The parameter prices is a list of strictly positive
integers, where the first element is the price of a piece of length 1, the second element is the
price of a piece of length 2, and so on.
Part B: A better approach using memoization
You have seen during the lecture that we can improve the recursive implementation of the
Fibonacci function using memoization. We can also use this technique for this problem. Write
the algorithm using memoization. What should we “remember” between each recursive call?
'''
def road(prices,length,counter=None):
    if length <= 1:
        return length
    else:
        if counter is None:
            counter = 'R?'*(length-1) + 'R1'
        if not '?' in counter:
            Rcount=0
            Tsum=0
            for x in counter:
                if x == '1':
                    Tsum+=prices[Rcount-1]
                    Rcount=0
                    pass
                if x == 'R':
                    Rcount+=1
            return [str(Tsum)+','+counter[:-1].replace('0','').replace('1','|')]
        else:
            return road(prices,length,counter.replace('?','1',1))  + road(prices,length,counter.replace('?','0',1))

print(road([1,5,8,9,10,17],4))
