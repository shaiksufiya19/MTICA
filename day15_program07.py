#WAP to find list of factors of a numbers.
#Factor is the integer that can exactly divide
#a given number without leaving a remainder

def findFactor(n):
    temp=list()
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp

        
a=int(input())
print(*findFactor(a))


'''
OUTPUT:
60
1 2 3 4 5 6 10 12 15 20 30 60
'''
