#count the number space in a given string

string='''Practice problems for
List Comprehension in Python.'''

ans=[]
for i in string:
    if i == ' ':
        ans.append(i)
print(len(ans))
