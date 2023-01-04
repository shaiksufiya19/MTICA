def solveProblem(s):
    lst=s.split()
    return [len(i) for i in lst]
inp=input()
print(*solveProblem(inp))


##inp=input()
##temp=inp.split()
##ans=[len(i) for i in temp]
##print(*ans)
'''
OUTPUT:
apple gua mango
5 3 5
'''
