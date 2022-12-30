#Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

#For example, given s = "abcba" and k = 2 , the longest substring with k distinct characters is "bcb".

s = input()
k = int(input())
a = ""
list = []
for i in s:
    a += i
    if len(set(a)) < k:
        continue
    if len(set(a)) > k:
        m = a[0]
        a = a.replace(m, '')
        continue
    if len(set(a)) == k:
        list.append(a)
print(max(list, key = len))