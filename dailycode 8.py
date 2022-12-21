'''Implement an autocomplete system. That is, given a query string [s] and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string | de | and the set of strings [[dog], [deer], [deal]], return

[[ deer deal]].'''

input_string = input()
list_of_strings = input().split(' ')
result = []
for i in list_of_strings:
    if i.startswith(input_string):
        result.append(i)
print(result)   