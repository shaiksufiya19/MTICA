import sys
print(sys.argv)
for i in range(len(sys.argv)):
    if i==0:
        print("Function name: {0}".format(sys.argv[0]))
        #print("Function name: %s" % sys.argv[0])
    else:
        print("{0}. argument: {1}".format(i,sys.argv[i]))
        #print("%d. argument: %s" % (i,sys.argv[i]))

'''
OUTPUT
D:\Pythonpractice57\Day17>python day17_program03.py shaik sufiya mca mtica
['day17_program03.py', 'shaik', 'sufiya', 'mca', 'mtica']
Function name: day17_program03.py
1. argument: shaik
2. argument: sufiya
3. argument: mca
4. argument: mtica
'''
