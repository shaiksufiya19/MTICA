def add(n1,n2):
    temp=n1+n2
    #global variables:a,b,c,add
    #local variables:n1,n2,temp
    global a,b
    a+=10
    b+=5
    print("Output of globals:",globals())
    print("Output of locals:",locals())
    return temp
a=int(input())
b=int(input())
c=add(a,b)
print(a,'+',b,'=',c)
