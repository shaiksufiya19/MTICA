'''
Write a program that accepts two inputs an integer and a string,
first is the number of test cases and
second is string iput and
prints frequency of alphabets in an input string.
INPUT
2
Hello World
OUTPUT
H 1
d 1
e 1
l 3
o 2
r 1
w 1
'''

def findFrequency(s):
    frequencyDict=dict()
    for i in s:
        if i in frequencyDict:
            frequencyDict[i]+=1
        else:
            frequencyDict[i]=1
    return frequencyDict
##def formatOutput(d):
##    for i in sorted(d):
##        print(i,d[i])
##    return None
##    

n=int(input())
for i in range(n):
    inpStr=input()
    print(findFrequency(inpStr))
    #formatOutput(findFrequency(inpStr))
