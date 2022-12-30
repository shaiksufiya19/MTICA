def printDecreasingSeries(ch,n):
    assert isinstance(ch,str),'First argument should be string'
    assert isinstance(n,int),'Second argument should be int'
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpCh=input("Enter a character:")
inpNum=int(input("Enter a number:"))
print('-'*40)
try:
    printDecreasingSeries(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
