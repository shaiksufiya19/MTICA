#Use a dctionary comprehension to reverse string.


string='''Practice problems for List Com pre hension in Python.'''

wordsLst=string.split(' ')
#print(wordsLst)
wordsLst=[i.strip("\n") for i in wordsLst ]
#print(wordsLst)
ans={i:i[::-1] for i in wordsLst }
print(ans)
