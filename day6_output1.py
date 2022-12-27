Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.sqrt(2)
1.4142135623730951
math.gcd(24,40)
8
from math import *
sqrt(2)
1.4142135623730951
gcd(24,40)
8
from math import sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(24,40)
8

================================ RESTART: Shell ================================
from math import *
sqrt(2)
1.4142135623730951
gcd(24,40)
8


================================ RESTART: Shell ================================
from math import sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(24,40)
8

============================================ RESTART: Shell ============================================
import math as M
M.sqrt(3)
1.7320508075688772
M.gcd(24,40)
8

============================================ RESTART: Shell ============================================
import math as m
m.sqrt(3)
1.7320508075688772
m.gcd(24,40)
8
m.sqrt(5)
2.23606797749979
m.trunc(4.5)
4
m.floor(9.8)
9
m.ceil(9.1)
10
m.log(1024,2)
10.0
m.ceil(8.9)
9
