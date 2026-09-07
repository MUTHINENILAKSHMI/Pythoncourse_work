Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#integer
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable

# Float
f=10
int(f)
10
str(f)
'10'
complex(f)
(10+0j)
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(f)
TypeError: 'int' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(f)
TypeError: 'int' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    set(f)
TypeError: 'int' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(f)
TypeError: 'int' object is not iterable

# string

s='codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
bool(s)
True
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'o', 'c', 'n', 'e', 'd', 'g', 'a'}
dict(S)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(S)
NameError: name 'S' is not defined. Did you mean: 's'?

#bool

b=True
int(b)
1
float(b)
1.0
str(b)
'True'
complex(b)
(1+0j)
list(b)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
sett(b)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    sett(b)
NameError: name 'sett' is not defined. Did you mean: 'set'?
set(b)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
TypeError: 'bool' object is not iterable
SyntaxError: invalid syntax

#complex
\
c=10+5j
int(c)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+5j)'
bool(c)
True
list(c)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable

#list
l=[10,20,'lakshmi',30.5]
int(l)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
"[10, 20, 'lakshmi', 30.5]"
complex(l)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
tuple(l)
(10, 20, 'lakshmi', 30.5)
set(l)
{10, 'lakshmi', 20, 30.5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence

#tuple
t=(10,20,30,'lak')
int(t)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
bool(t)
True
list(t)
[10, 20, 30, 'lak']
set(t)
{10, 'lak', 20, 30}
dic(t)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    dic(t)
NameError: name 'dic' is not defined. Did you mean: 'dir'?

#set
s={1,2,3,4,5,6}
int(s)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
bool(s)
True
list(s)
[1, 2, 3, 4, 5, 6]
tuple(s)
(1, 2, 3, 4, 5, 6)
>>> str(s)
'{1, 2, 3, 4, 5, 6}'
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> TypeError: cannot convert dictionary update sequence element #0 to a sequence
SyntaxError: invalid syntax
>>> 
>>> #frozen set
>>> fs={12,3,4,5}
>>> #dict
>>> 
>>> d={1:2,3:4,5:6}
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> bool(d)
True
>>> list(d)
[1, 3, 5]
>>> tuple(d)
(1, 3, 5)
>>> set(d)
{1, 3, 5}
