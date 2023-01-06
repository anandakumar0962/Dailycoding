#Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.

alphabet = [chr(x) for x in range(97, 123)]
def alphabet_index(n):  
    x = 0
    for i in input_str:
        if alphabet.index(i) > x:
            x = alphabet.index(i) + 1
    result = str(x) + alphabet[x-1]
    return result

input_str = input().lower()
print(alphabet_index(input_str))