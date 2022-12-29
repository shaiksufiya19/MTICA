num1=input("Enter a number:")
num2=input("Enter a number:")
try:
    res=int(num1)/int(num2)# execute with num2=non zero and zero
except (ZeroDivisionError,ValueError):
    print("Exception handled by Manohar")
except Exception as ob:
    print (ob)
else:
    print (num1, '/' ,num2, '=', res)
finally:
    print("Thanks")
print("Visit again at python class at MTICA")

#output
Enter a number:5
Enter a number:8
5 / 8 = 0.625
Thanks
Visit again at python class at MTICA

