def checkEven(num1):
    str=''
    if num1%2==0:
       str1=str(num1)+"is even"
       return "Even"
    return None

def checkOdd(num1):
    if num1%2==1:
       return "Odd"
    return None

x=checkEven(num1)
y=checkOdd(num1)

print("x=",x)
print("y=",y)
