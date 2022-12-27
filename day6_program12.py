#Remove all vowels in a given string

string='''Practice problems for
List Comprehension in python.'''
##ans=[]
##for i in string:
##    if i not in 'AEIOUaeiou':
##        ans.append(i)
##print(*ans)

ans=[i for i in string if i not in 'AEIOUaeiou']
print(*ans)
