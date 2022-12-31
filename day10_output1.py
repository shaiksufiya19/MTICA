Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict={'Name':'Zara','Age':7,'Class':'First'}
dict1={'Name':'Zara','Age':7,'Class':'First'}
print(dict1)
{'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict1['Name'])
Zara
print(dict1['Class'])
First
dict1['Age']=8
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Class': 'First'}
dict1['Course']='MCA'
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Class': 'First', 'Course': 'MCA'}
del dict1['Class']
print(dict1)
{'Name': 'Zara', 'Age': 8, 'Course': 'MCA'}
dict1.clear()
print(dict1)
{}
dict1={'Name':'Zara','Age':7,'Class':'First'}
print(dict1)
{'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict1.keys()
dict_keys(['Name', 'Age', 'Class'])
dict1.values()
dict_values(['Zara', 7, 'First'])
dict1.items()
dict_items([('Name', 'Zara'), ('Age', 7), ('Class', 'First')])
for i in dict1.keys():print(i)

Name
Age
Class
for i in dict1:print(i)

Name
Age
Class
for i,j in dict1.items():print(i)

Name
Age
Class
for i,j in dict1.items():print(i,j)

Name Zara
Age 7
Class First
