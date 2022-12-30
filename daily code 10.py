#There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

#For example, if N is 4, then there are 5 unique ways:

#• 1, 1, 1, 1

#• 2, 1, 1

#• 1, 2, 1

#• 1, 1, 2

#• 2,2

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
    
def count_ways(a):
    return fib(a+1)
a = int(input())
print(count_ways(a))