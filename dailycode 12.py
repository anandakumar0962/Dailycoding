input_list = list(map(int, input().split(" ")))
result = []
for i in range(len(input_list)-2):
    a = max(input_list[i], input_list[i+1], input_list[i+2])
    result.append(a)
print(result)