'''Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [[3, 4, -1, 1]] should give [2]. The input [[1, 2, 0]] should give 3'''


input_list = [int(i) for i in input().split(" ")]
input_list.sort()
sort_list = [j for j in input_list if j>=0]
result = ''
for m in range(sort_list[0],sort_list[-1]+1):
    if m not in sort_list:
        result += str(m)
        break
if result =='':
    print(sort_list[-1]+1)
else:
    print(result)