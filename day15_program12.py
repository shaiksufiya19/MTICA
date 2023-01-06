def outer():
    print('outer function')
    def inner():
        print('inner function')
    inner()
outer()

'''
OUTPUT:
outer function
inner function
'''


