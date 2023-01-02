Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: D:/Pythonpractice57/Day11/day11_practice1.py ============
5
11
\
Traceback (most recent call last):
  File "D:/Pythonpractice57/Day11/day11_practice1.py", line 31, in <module>
    inpNum=int(input())
ValueError: invalid literal for int() with base 10: '\\'

============= RESTART: D:/Pythonpractice57/Day11/day11_practice1.py ============
5
May
3
March
11
November

============= RESTART: D:/Pythonpractice57/Day11/day11_program1.py =============
5

============= RESTART: D:/Pythonpractice57/Day11/day11_program1.py =============
11
12
December
1
January

================================ RESTART: Shell ================================

============= RESTART: D:/Pythonpractice57/Day11/day11_program1.py =============
5
1
January
16
INVALID
9
September
4
April
-5
INVALID

========================= RESTART: D:/Pythonpractice57/Day11/day11_program2.py =========================
2
Hello world


========================= RESTART: D:/Pythonpractice57/Day11/day11_program2.py =========================
2
'Hello world'


========================= RESTART: D:/Pythonpractice57/Day11/day11_program2.py =========================
4
today is a monday
  3
a 3
d 2
i 1
m 1
n 1
o 2
s 1
t 1
y 2

========================= RESTART: D:/Pythonpractice57/Day11/day11_program2.py =========================
2
Good Morning
  1
G 1
M 1
d 1
g 1
i 1
n 2
o 3
r 1
Hello world
  1
H 1
d 1
e 1
l 3
o 2
r 1
w 1

========================= RESTART: D:/Pythonpractice57/Day11/day11_program2.py =========================
1
hello world
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
d={'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
sorted(d)
[' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w']
d[' ']
1



d['o']
2
sorted(d,reverse=True)
['w', 'r', 'o', 'l', 'h', 'e', 'd', ' ']
sorted(d.items(),key=lambda x:x[1])
[('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1), ('o', 2), ('l', 3)]
sorted(d.values())
[1, 1, 1, 1, 1, 1, 2, 3]
d
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
for i in sorted(d.items(),key=lambda x:x[1]):
    print(i)

    
('h', 1)
('e', 1)
(' ', 1)
('w', 1)
('r', 1)
('d', 1)
('o', 2)
('l', 3)
for i in sorted(d.items(),key=lambda x:x[1]):print(i)

('h', 1)
('e', 1)
(' ', 1)
('w', 1)
('r', 1)
('d', 1)
('o', 2)
('l', 3)
for i in sorted(d.items(),key=lambda x:x[1]):print(i[0],i[1])

h 1
e 1
  1
w 1
r 1
d 1
o 2
l 3
for i in sorted(d.items(),key=lambda x:x[1],reverse=True):print(i[0],i[1])

l 3
o 2
h 1
e 1
  1
w 1
r 1
d 1

========================= RESTART: D:/Pythonpractice57/Day11/day11_program3.py =========================
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program4.py =========================
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program4a.py ========================
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program5.py =========================
{'class': {'student': {'name': 'Abhi', 'marks': {'physics': 70, 'history': 80}}}}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program5.py =========================
{'class': {'student': {'name': 'Abhi', 'marks': {'physics': 70, 'history': 80}}}}
Traceback (most recent call last):
  File "D:/Pythonpractice57/Day11/day11_program5.py", line 15, in <module>
    print(sampleDict["history"])
KeyError: 'history'

========================= RESTART: D:/Pythonpractice57/Day11/day11_program5.py =========================
{'class': {'student': {'name': 'Abhi', 'marks': {'physics': 70, 'history': 80}}}}
Traceback (most recent call last):
  File "D:/Pythonpractice57/Day11/day11_program5.py", line 15, in <module>
    print(sampleDict["marks"]["history"])
KeyError: 'marks'

========================= RESTART: D:/Pythonpractice57/Day11/day11_program5.py =========================
{'class': {'student': {'name': 'Abhi', 'marks': {'physics': 70, 'history': 80}}}}
80

========================= RESTART: D:/Pythonpractice57/Day11/day11_program5.py =========================
80

========================= RESTART: D:/Pythonpractice57/Day11/day11_program6.py =========================
{'Shahrukh': {'designation': 'Developer', 'salary': 80000}, 'khan': {'designation': 'Developer', 'salary': 80000}, 'Salman': {'designation': 'Developer', 'salary': 80000}}
{'designation': 'Developer', 'salary': 80000}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program6.py =========================
{'Shahrukh': {'designation': 'Developer', 'salary': 80000}, 'khan': {'designation': 'Developer', 'salary': 80000}, 'Salman': {'designation': 'Developer', 'salary': 80000}}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program6.py =========================
{'designation': 'Developer', 'salary': 80000}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program6.py =========================
{'Shahrukh': {'designation': 'Developer', 'salary': 80000}, 'khan': {'designation': 'Developer', 'salary': 80000}, 'Salman': {'designation': 'Developer', 'salary': 80000}}
{'designation': 'Developer', 'salary': 80000}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program7.py =========================
{'name': 'Mounika', 'salary': 18000}
{'name': 'Mounika', 'salary': 18000}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program7.py =========================
{'name': 'Mounika', 'salary': 18000}
{'name': 'Mounika', 'salary': 18000}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program8.py =========================
{'age': 22, 'city': 'New york'}

========================= RESTART: D:/Pythonpractice57/Day11/day11_program9.py =========================
{'name': 'Mounika', 'salary': 18000}
