Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import *
random()
0.9389188809344603
random()
0.3234725164918073
randint(10,20)
16
random()
0.20571444927615068
randint(10,20)
14
help(randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

import random
random.random()
0.3651193285314299
import random as r
r.random()
0.5801960286980168
for i in range(100):
    print(randint(10,20),end=',')

    
19,10,16,11,20,11,18,14,10,19,14,15,18,15,11,16,18,10,19,18,13,19,11,14,10,11,13,11,13,13,10,17,11,18,19,17,11,11,17,10,18,12,13,10,19,20,15,12,10,20,15,13,18,20,14,14,14,17,20,16,14,12,19,12,10,15,17,16,19,12,16,14,16,15,14,19,11,17,12,20,16,14,13,13,11,17,11,10,12,11,17,16,15,19,20,10,14,15,17,16,

============================================ RESTART: Shell ============================================
import random
random.random()
0.12308992521077289

============================================ RESTART: Shell ============================================
import random as r
r.random()
0.18438357123786264
help(r.random)
Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).

r.randint(10,99)
66
help(r.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help(r.uniform)
Help on method uniform in module random:

uniform(a, b) method of random.Random instance
    Get a random number in the range [a, b) or [a, b] depending on rounding.

r.uniform(10,100)
15.14992941765158
items=[1,2,3,4,5,6,7,8,9,10]
r.shuffle(items)
items
[4, 8, 9, 7, 2, 3, 10, 6, 1, 5]
a=[12,'papaya',45,7.8,'mango']
r.shuffle(a)
a
[12, 'papaya', 45, 'mango', 7.8]
r.shuffle(a)
a
[7.8, 12, 'mango', 'papaya', 45]
import random as r
items=[1,2,3,4,5,6,7,8,9,10]
x=sample(items, 3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x=sample(items, 3)
NameError: name 'sample' is not defined
x=r.sample(items, 3)
x
[9, 6, 3]
x=r.sample(items, 3)
x
[2, 10, 9]
x=r.sample(items, 2)
x
[1, 6]

========================= RESTART: D:/Pythonpractice57/Day17/day17_program01.py ========================
0.6942063806801504
1
7.094141065901772
[8, 10, 1, 3, 9, 6, 5, 2, 7, 4]
x= [1, 10, 2]
1
[1, 5, 7, 9]

========================= RESTART: D:/Pythonpractice57/Day17/day17_program01.py ========================
0.9641994286490573
37
1.8831899623645498
[9, 6, 7, 4, 8, 10, 2, 1, 5, 3]
x= [3, 4, 2]
3
[4, 2, 1, 10]
Sandra

========================= RESTART: D:/Pythonpractice57/Day17/day17_program02.py ========================
3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)]
sys.version_info(major=3, minor=11, micro=0, releaselevel='alpha', serial=5)
import sys
print(sys.version);
3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)]
print(sys.version_info)
sys.version_info(major=3, minor=11, micro=0, releaselevel='alpha', serial=5)

========================= RESTART: D:/Pythonpractice57/Day17/day17_program03.py ========================
['D:/Pythonpractice57/Day17/day17_program03.py']
Function name: D:/Pythonpractice57/Day17/day17_program03.py
shaik sufiya mca mtica
SyntaxError: invalid syntax

========================= RESTART: D:/Pythonpractice57/Day17/day17_program04.py ========================
Coming through stdout
Today is last day of python training in jan 8th.