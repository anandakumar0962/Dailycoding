'''Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [[2, 4, 6, 2, 5]] should return

[13], since we pick 2, 6, and 5

[5, 1, 1, 5] should return | 10 |, since we

pick 5 and 5'''

input = [int(i) for i in input().split(" ")]
sum_input = input[:]
if len(input) == 0:
    print(0)
elif len(input) == 1:
    print(input[0])
else:
	sum_input[1] = max(sum_input[0], sum_input[1])
for i in range(2,len(input)):
	sum_input[i] = max(sum_input[i-1], sum_input[i-2] + input[i])
print(max(sum_input))