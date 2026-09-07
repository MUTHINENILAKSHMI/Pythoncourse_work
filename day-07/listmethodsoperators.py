Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list
#list is a mutable,ordered,hetrogenoous
l=[]
l=list()
type(l)
<class 'list'>
l=[(1,2,3,5,6,True,"lakshmi"]
   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
l=[1,2,3,5,6,True,"lakshmi"]
   
l
   
[1, 2, 3, 5, 6, True, 'lakshmi']
1=[1,1,1,1]
   
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[1,1,1,1]
   
l
   
[1, 1, 1, 1]
#concentation
   
a=[1,2,3]
   
b=[1,2,3]
   
a+b
   
[1, 2, 3, 1, 2, 3]
#reptition
   
a=[1,1,1,1]
   
a*5
   
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#indexing
   
a=[1,2,3,4,5,5,6,7]
   
a[0]
   
1
 
a[4]
   
5
a[-1]
   
7
a[-5]
   
4
#slicing
   
a=[496,462,480,481,472,466]
   
a[:]
   
[496, 462, 480, 481, 472, 466]
a[1::2]
   
[462, 481, 466]
a[::2]
   
[496, 480, 472]
a[:4]
   
[496, 462, 480, 481]
a[::-1]
   
[466, 472, 481, 480, 462, 496]
a[-4]
   
480
a[-1:-5:-2]
   
[466, 481]
#membership
   
496 in a
   
True
454 not in a
   
True
419 in a
   
False
max(a)
   
496
min(a)
   
462
sorted(a)
   
[462, 466, 472, 480, 481, 496]
len(a)
   
6
a.append(4)
   
a
   
[496, 462, 480, 481, 472, 466, 4]
a.append(7)
   
4
   
4
a
   
[496, 462, 480, 481, 472, 466, 4, 7]
#append is used for single value add
   
   
[496, 462, 480, 481, 472, 466, 4, 7]
a.extend([1,2,3])
   
a
   
[496, 462, 480, 481, 472, 466, 4, 7, 1, 2, 3]
#extend is used for multiple values
   
a.insert(2,47)
   
a
   
[496, 462, 47, 480, 481, 472, 466, 4, 7, 1, 2, 3]
a.pop()
   
3
a.insert(-1,100)
   
a
   
[496, 462, 47, 480, 481, 472, 466, 4, 7, 1, 100, 2]
a.pop(3)
   
480


a.remove(496)
   
a
   
[462, 47, 481, 472, 466, 4, 7, 1, 100, 2]
del a[1]
   
a
   
[462, 481, 472, 466, 4, 7, 1, 100, 2]
a.clear()
   
a
   
[]
a=[462, 481, 472, 466, 4, 7, 1, 100, 2]
   
del a[1:3]
   
a
   
[462, 466, 4, 7, 1, 100, 2]
a.index(466)
   
1
a.count(462)
   
1
a=[1,2,3,4]
   
b=a
   
b
   
[1, 2, 3, 4]
b.append(5)
   
b
   
[1, 2, 3, 4, 5]
a
   
[1, 2, 3, 4, 5]

c=a.copy()
   
c
   
[1, 2, 3, 4, 5]
>>> a
...    
[1, 2, 3, 4, 5]
>>> c.append(6)
...    
>>> c
...    
[1, 2, 3, 4, 5, 6]
>>> a
...    
[1, 2, 3, 4, 5]
>>> a.reverse()
...    
>>> a
...    
[5, 4, 3, 2, 1]
>>> a.sorted()
...    
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> a.sort()
...    
>>> a
...    
[1, 2, 3, 4, 5]
>>> a.any(1,[],{},()'')
...    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a.any(1,[],{},(),'')
...    
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.any(1,[],{},(),'')
AttributeError: 'list' object has no attribute 'any'
>>> any([1,[],{},(),''])
...    
True
>>> all(1[,[],{},(),''])
...    
SyntaxError: invalid syntax
>>> all([1,[],{},(),''])
...    
False
>>> sum(a)
...    
15
