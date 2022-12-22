#Create a function that determines whether a number is a Disarium or not.

#Examples

#is_disarium (75) → False # 7^1 + 5^2 = 7+ 25 = 32

#is_disarium (135) → True # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

n = int(input())
a = 1
result = 0
for i in map(int, str(n)):
    result += i**a
    a += 1
if result == n:
    print("Disarium Number")
else:
    print("Not a Disarium Number")