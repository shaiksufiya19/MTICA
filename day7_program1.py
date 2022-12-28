#Use a dctionary comprehension to count the length of each word in a sentence


string='''Practice problems for List Com pre hension in Python.'''

wordsLst=string.split(' ')
print(wordsLst)
wordsLst=[i.strip("\n") for i in wordsLst ]
print(wordsLst)
ans={i:len(i) for i in wordsLst }
print(ans)
