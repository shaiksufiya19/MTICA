def printSeries(n):
    
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(i,end=' ')
            
    return None
inpNum=int(input())
printSeries(inpNum)
'''
INPUT
5
OUTPUT
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
