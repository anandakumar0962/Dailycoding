#Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

#For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8].

input_list = list(map(int, input().split(" ")))
result = []
for i in range(len(input_list)-2):
    a = max(input_list[i], input_list[i+1], input_list[i+2])
    result.append(a)
print(result)