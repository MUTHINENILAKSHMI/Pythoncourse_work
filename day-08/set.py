Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#set
#it is collection of elements enclosed with '{}'
# it is muttable
# it is unordered
# it is hetrogenous
# it is dynamically size
#doesn,t allows dupliactes
s={} # can't diclear like this beacuse it is dict
type(s)
<class 'dict'>
s=set()
type(s)
<class 'set'>
s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}

s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}
s={1,1,1,1}
s
{1}
s=set()
s.add(1)
s.add(12.3)
s.add[(1,2,3)]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.add[(1,2,3)]
TypeError: 'builtin_function_or_method' object is not subscriptable

# doesn't allows muttable only allow immutable elements into set
s=set()
s.add(1)
s.add(12.3)
s.add(True)
s.add((1,2,3))
s
{1, (1, 2, 3), 12.3}
s.add(False)
s
{False, 1, (1, 2, 3), 12.3}
a={1,2,3,4}
b={5,6,7,8,9}
2 in a
True
10 not in a
True
# intersection ="|"
# union is "&"
# difference "-"
#  symmetric difference "^"
# subset <=
#super set >=
# disjoint
a={1,2,3,4,5}
b={6,7,8,9}
 a|b
 
SyntaxError: unexpected indent
a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a&b
set()
a-b
{1, 2, 3, 4, 5}
b-a
{8, 9, 6, 7}
a<=b
False
a>=b
False
{1}<=a
True
{1,2,3,4}<=a
True
a>={1,2,3}
True
m={1,2,3}
n={4,5,6}
n.isdisjoint(m)
True
a.isdigoint(b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.isdigoint(b)
AttributeError: 'set' object has no attribute 'isdigoint'. Did you mean: 'isdisjoint'?
a.isdijoint(b)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.isdijoint(b)
AttributeError: 'set' object has no attribute 'isdijoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
True
a={12,43,1,7,5,6}
sorted(a)
[1, 5, 6, 7, 12, 43]
a.index()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
all({1,2,3})
True
any({0,''})
False
max(a)
43
min(a)
1
len(a)
6
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> sum(a)
74
>>> a={1,2,3}
>>> b=a
>>> c=a.copy()
>>> c
{1, 2, 3}
>>> a.append(4)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.append(4)
AttributeError: 'set' object has no attribute 'append'
>>> c.append(4)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    c.append(4)
AttributeError: 'set' object has no attribute 'append'
>>> c.add(5)
>>> c
{1, 2, 3, 5}
>>> c.add(8)
>>> c
{1, 2, 3, 5, 8}
>>> c.update({10,20,30})
>>> c
{1, 2, 3, 5, 8, 10, 20, 30}
>>> c.clear()
>>> c
set()
>>> c={1, 2, 3, 5, 8, 10, 20, 30}
>>> c.pop()
1
>>> c.pop()
2
>>> c.remove(10)
>>> c
{3, 5, 8, 20, 30}
>>> c.discard(10)
>>> c.discard(8)
>>> c
{3, 5, 20, 30}
>>> a=frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})
