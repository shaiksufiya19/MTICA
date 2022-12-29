num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
try:
    res=num1/num2
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print (num1, '/' ,num2, '=', res)
    
print("Thanks")

#output

 ==========================
Enter a number:5
Enter a number:6
5 / 6 = 0.8333333333333334
Thanks

========================== 
