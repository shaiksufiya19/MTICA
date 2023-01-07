##def reverseString(s):
##    ans=[i[::-1] for i in s]
##    return ans
##inp=input().split()
###print(inp)
##print(*reverseString(inp))


#2nd approach

def printResult(n):
    return [i[::-1] for i in n]
a=input().strip().split()
print(*printResult(a))
