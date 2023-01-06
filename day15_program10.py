#nonlocal
x=7
print('id(x)in outside function:',id(x))
#First function
def f():
    global x
    x=10
    print('id(x)in outer:',id(x))
    #Nested function
    def g():
        global x
        x=15
        print('id(x)in inner:',id(x))
    g()
    print(x)
f()
        

#nonlocal scope

def outer():
    message='Outer function'
    print(message)
    def inner():
        print(message)
    inner()
outer()
'''
OUTPUT:
id(x)in outside function: 140718403273704
id(x)in outer: 140718403273800
id(x)in inner: 140718403273960
15
Outer function
Outer function
'''
