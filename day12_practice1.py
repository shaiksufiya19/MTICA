def printSeries(ch,n):
    assert(n>=0),'INVALID'
    sp='.'
    for i in range(0,n):
        print(sp*(n-i-1) + ch*(2*i+1)+sp*(n-i-1))
    return None
inpCh=input()
inpNum=int(input())
try:
    printSeries(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
