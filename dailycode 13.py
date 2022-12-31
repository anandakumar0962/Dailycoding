#Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

#Examples:

#fact_of_fact(4) → 288 # 4! * 3! * 2! * 1! = 288

#fact_of_fact (5) → 34560

#fact_of_fact(6) → 24883200

fact_res= []
def fact(n):
    a = 1
    for i in range(2, n+1):
        a *= i
        if i == n:
            fact_res.append(a)
            return fact(n -1)        
def fact_of_fact(x):
    x = 1
    for i in fact_res:
        x *= i
    return x
n = int(input())
fact(n)
print(fact_of_fact(fact_res))