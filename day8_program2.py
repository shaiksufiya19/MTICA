def Fact(n):
    assert(n >=0),"Factorial of negative number is not defined"
    if n==0:
        return 1
    else:
        return n*Fact(n-1)
   
try:
    print (Fact(3))
except Exception as ob:
    print(ob)
try:
    print (Fact(-3))
except Exception as ob:
    print(ob)
try:
    print (Fact(0))
except Exception as ob:
    print(ob)
try:
    print (Fact(15))
except Exception as ob:
    print(ob)
print("Thank You")

#output

6
Factorial of negative number is not defined
1
1307674368000
Thank You
