#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

def numDecodings(s):
    if len(s) == 0 or (len(s) == 1 and s[0] == '0'):
        return 0
    return numDecodingsHelper(s, len(s))
 
 
def numDecodingsHelper(s, n):
    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n-1] > "0":
        count = numDecodingsHelper(s, n-1)
    if (s[n - 2] == '1'
        or (s[n - 2] == '2'
            and s[n - 1] < '7')):
        count += numDecodingsHelper(s, n - 2)
    return count
 
input_string= input()
print(numDecodings(input_string))