Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2+3
5
2-9
-7
2*9
18
2/8
0.25
2//8
0
2>=4
False
2<6
True
9<0
False
2**8*9
2304
2*3**5
486
2!=8
True
2==2
True

============== RESTART: D:/Pythonpractice57/Day9/day9_program10.py =============
False
False
Traceback (most recent call last):
  File "D:/Pythonpractice57/Day9/day9_program10.py", line 9, in <module>
    print(x3 is y3)
NameError: name 'y3' is not defined. Did you mean: 'y1'?

============== RESTART: D:/Pythonpractice57/Day9/day9_program10.py =============
False
True
False
id(x1)
140715529520040
id(y1)
140715529520040
print(id(x3),id(y3))
2459828824320 2459788195584
print(id(x2),id(y2))
2459828928752 2459828928752

========================== RESTART: D:/Pythonpractice57/Day9/day9_program11.py =========================
True
True
True
False
True
False
True

========================== RESTART: D:/Pythonpractice57/Day9/day9_program12.py =========================
True
False
True
False

========================== RESTART: D:/Pythonpractice57/Day9/day9_program10.py =========================
False
True
False

========================== RESTART: D:/Pythonpractice57/Day9/day9_program12.py =========================
False

========================== RESTART: D:/Pythonpractice57/Day9/day9_program13.py =========================
x= 10 y= 4 x&y= 0
x= 10 y= 4 x|y= 14
x= 10 ~x= -11
x= 10 y= 4 x^y= 14
x= 10 x>>2= 2
x= 10 x<<2= 40
a=10
b=2
a<<b
40
a>>b
2
