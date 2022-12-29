num1=input("Enter a number:")
num2=input("Enter a number:")
try:
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print("Exception handled by Manohar")
except ValueError:
    print("Exception handled by Ganguly")
except Exception as ob:
    print (ob)
else:
    print (num1, '/' ,num2, '=', res)
finally:
    print("Thanks")
print("Visit again at python class at MTICA")


#output

Enter a number:5
Enter a number:0
Exception handled by Manohar
Thanks
Visit again at python class at MTICA
