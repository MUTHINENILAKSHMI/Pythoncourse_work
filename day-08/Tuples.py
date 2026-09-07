Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Tuple
t=()
t=tuple()
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1)
t
1
t=(1,)
t
(1,)
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,2,3.4, "lakshmi", [1,2,3],(1,2,3,4),True)
t
(1, 2, 3.4, 'lakshmi', [1, 2, 3], (1, 2, 3, 4), True)
# tuple is collection of elements enclosed with paranethsis
# it is orderded
# allows duplicates
# fixed size data set
# it is hetrogenous
# it  is immutable.

# we can't store single value beacuse it takes as intger
# if you want to store single value and comma should mentioned
#ex:1,

#operations
#------------
""" 1. concatnation
2. reptation
3.membership
4. indexing
5. slicing"""
' 1. concatnation\n2. reptation\n3.membership\n4. indexing\n5. slicing'
# concatnation:
t=(1,2,3)+(4,5,6)
t
(1, 2, 3, 4, 5, 6)
# repatition
t=(1,2,3)*10
t
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t=(1,2,3.4, "lakshmi", [1,2,3],(1,2,3,4),True)
"lakshmi" in t
True
True  in t
True
False in t
False
# indexing
t=[-1]
t
[-1]
t[0]
-1
t=(1,2,3.4, "lakshmi", [1,2,3],(1,2,3,4),True)
t[5]
(1, 2, 3, 4)
t[-1]
True
t[3]
'lakshmi'
# Slicing:
>>> t[::-1]
(True, (1, 2, 3, 4), [1, 2, 3], 'lakshmi', 3.4, 2, 1)
>>> t[-1:-3:-1]
(True, (1, 2, 3, 4))
>>> 
>>> # methods
>>> t=(12,56,45,3,4,22,3,5,66,777,89)
>>> sorted(t)
[3, 3, 4, 5, 12, 22, 45, 56, 66, 89, 777]
>>> max(t)
777
>>> min(t)
3
>>> len(t)
11
>>> t.index(3)
3
>>> t.count(3)
2
>>> sum(t)
1082
>>> all(t)
True
>>> any(t)
True
>>> clear(t)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    clear(t)
NameError: name 'clear' is not defined
>>> t=(1,2,3.4, "lakshmi", [1,2,3],(1,2,3,4),True)
>>> t[4]
[1, 2, 3]
>>> t[4].append(4)
>>> t
(1, 2, 3.4, 'lakshmi', [1, 2, 3, 4], (1, 2, 3, 4), True)
>>> t=(1,2,3)
>>> t
(1, 2, 3)
