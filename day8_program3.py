def Factorial(num):
    assert(num>=0),"Factorial of negative number is not defined!"
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-45))
except Exception as obj:
    print(obj)
try:
    print(Factorial(45))
except Exception as obj:
    print(obj)

#output

Factorial of negative number is not defined!
119622220865480194561963161495657715064383733760000000000
