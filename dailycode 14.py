#Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).

#Examples:

#vowel_links("a very large appliance")

#vowel_links("go to edabit") → True

#vowel_links("an open fire") → False

#vowel_links("a sudden applause") → False

a = ['a', 'e', 'i', 'o', 'u']
result = []
def vowel_links(text):
    for i in range(len(n) -1):
        if n[i][-1] in a and n[i+1][0] in a:
            result.append(i)
    if result == []:
        return 'False'
    else:
        return 'True'
        
n = input().split(" ")
print(vowel_links(n))