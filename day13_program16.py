a=10
b=9
try:
    #condition for checking for negative values
    if a<0 or b<0:
        #raising exception using raise keyword
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("please enter valid integer value")


'''
INPUT;
10
9
OUTPUT:
1.1111111111111112
input:
-5
9
OUTPUT:
please enter valid integer value
'''
