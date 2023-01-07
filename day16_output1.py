Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst=[1,2,3,4,5]
it=iter(lst)
type(it)
<class 'list_iterator'>
print(next(it))
1
print(next(it))
2
print(next(it))
3
print(next(it))
4
print(next(it))
5
print(next(it))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(next(it))
StopIteration

============= RESTART: D:/Pythonpractice57/Day16/day16_program01.py ============
1 2 3 4 Traceback (most recent call last):
  File "D:/Pythonpractice57/Day16/day16_program01.py", line 7, in <module>
    print(next(it))
StopIteration

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:/Pythonpractice57/Day16/day16_program01.py", line 9, in <module>
    sys.exit()
NameError: name 'sys' is not defined

============= RESTART: D:/Pythonpractice57/Day16/day16_program01.py ============
1 2 3 4 

========================= RESTART: D:/Pythonpractice57/Day16/day16_program01.py ========================
1 2 3 4 

========================= RESTART: D:/Pythonpractice57/Day16/day16_program01.py ========================
1 2 3 4 

========================= RESTART: D:/Pythonpractice57/Day16/day16_program01.py ========================
1 2 3 4 

========================= RESTART: D:/Pythonpractice57/Day16/day16_program01.py ========================
1 2 3 4 
a="Without revision you have forgotten"
a[::-1]
'nettogrof evah uoy noisiver tuohtiW'
a[::2]
'Wtotrvso o aefrotn'
a[::3]
'Whtesnoheooe'
a[::-3]
'ntr au iv oi'
a[::1]
'Without revision you have forgotten'
