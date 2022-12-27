Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
apple,banana,carrot
print('{0},{1}{0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,bananaappleapplepen carrot
print('{0},{1} {0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana appleapplepen carrot
print('{0},{1},{0},{0},{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana,apple,apple,pen carrot
print('{},{},{}'.format('apple','banana','carrot'))
apple,banana,carrot
print('Shilpa purchased a kg of {},a dozen of {} and half kg of {}'.format('apple','banana','carrot'))
Shilpa purchased a kg of apple,a dozen of banana and half kg of carrot
print('Ganguly purchased a kg of {0} and {2},Manohar purchased a dozen of {1} and Arun purchased half kg of {2}'.format('apple','banana','carrot'))
Ganguly purchased a kg of apple and carrot,Manohar purchased a dozen of banana and Arun purchased half kg of carrot

================================ RESTART: Shell ================================
print('{2},{1},{0}'.format('apple','banana','carrot'))
carrot,banana,apple
print('{2},{1},{1},{0}'.format('apple','banana','carrot'))
carrot,banana,banana,apple
print('{2},{1},{0}'.format('*abcd'))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print('{2},{1},{0}'.format('*abcd'))
IndexError: Replacement index 2 out of range for positional args tuple
print('{2},{1},{0}'.format(*'abcd'))
c,b,a
x,*y,z='computer'
x
'c'
z
'r'
y
['o', 'm', 'p', 'u', 't', 'e']
*x,y='abcd'
x
['a', 'b', 'c']
y
'd'

============================================ RESTART: Shell ============================================
print('Coordinates: {latitude},{longitude}'.format(latitude='37.24N',longitude='-115.81W'))
Coordinates: 37.24N,-115.81W
print('Welcome: {name}, your college is: {college}'.format(name='Sufiya',college='MTICA.'))
Welcome: Sufiya, your college is: MTICA.

============================================ RESTART: Shell ============================================
coord={'latitude': '37.24N','longitude': '-115.81W'}
print('Coordinates: {latitude},{longitude}'.format(**coord))
Coordinates: 37.24N,-115.81W
student={48:'Abhi',43:'Sufiya'}
type(student)
<class 'dict'>
student
{48: 'Abhi', 43: 'Sufiya'}
student.keys()
dict_keys([48, 43])
student.values()
dict_values(['Abhi', 'Sufiya'])
type(coord)
<class 'dict'>
coord.keys()
dict_keys(['latitude', 'longitude'])

============================================ RESTART: Shell ============================================
coord=(3,5)
abc=(2,9)
type(coord)
<class 'tuple'>
type(abc)
<class 'tuple'>
abc[0]
2
print('x: {0[0]}; y:{0[1]};abc : {1[0]},{1[1]}'.format(coord,abc))
x: 3; y:5;abc : 2,9
