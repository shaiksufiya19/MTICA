
##s1=input().split()
##s2=input().split()
##print(*[(int(i)+int(j)) for i,j in zip(s1,s2)])


#2nd aprroach
def result(s1,s2):
    return [int(i)+int(j) for i,j in zip(s1,s2)]
inp1=input().strip().split()
inp2=input().strip().split()
print(*result(inp1,inp2))

'''
OUTPUT:
11 22 33 44 55 66
1 2 3 4 5 6
12 24 36 48 60 72
'''
