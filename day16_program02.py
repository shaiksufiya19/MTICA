'''
WAP to remove special characters from a string.
Any character excluding alphabets and digits are special character.

INPUT:
fun_Add(_
OUTPUT:
funAdd
'''
def removeSpecialChar(s):
    ans=''
    for i in s:
        if (ord(i) in range(65,91) or ord(i) in range(97,123)
        or ord(i) in range(48,58)):
            ans +=i
    return ans

inp=input()
print(removeSpecialChar(inp))
