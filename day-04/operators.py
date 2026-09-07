Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Python Operators

"1. Arithmetic operators"
'1. Arithmetic operators'
a=10
b=20
a+b
30
a-b
-10
a//b
0
a/b
0.5
a%b
10

#2. Comparison Operators
a=10
b=5
a>b
True
a<b
False
a>=b
True
a<=b
False
a!=b
True
a==b
False

#Assignment Operators
a=10
a=a+10
a
20
a=a+20 # genral assignment
a
40
a+=10
a
50
a-=10
a
40
a/=10
a
4.0
a//=10
a
0.0
a=50
a//=10
a
5
a%=10
a
5
a*=10
a
50
#Relational Operators

a=10
b=20
a%2==0  and b%2==0
True
a%3==0 and b%3==0
False
a%2==0 and b%3==0
False

# or condtion
a%2==0 or a%3==0
True
#not condition
not a%2==0
False
# if the condtion true it gives false ,if the condtion false it gives true

#Membership Operators

's' in 'aeiou'
False
s="python Programming"
s="python Programming"

'p' in s
True
'c' in s
False
'java' in s
False
'ing' not in s
False
'ing' in s
True
# list
l=[1,2,3,5,4,'lakshmi']
25 in l
False

'java' not in l
True
'lak' in l
False
'lakshmi' in l
True

# tuple
t=(12,4,3,6,7.8)
5 in t
False

45 not in t
True

#set
s={1,2,3,5,6}
'lak' in s
False
5  in s
True
10 not in s
True
6 not in s
False

#dict
d={'name' : 'lakshmi', 'branch': 'ece', 'subject':'python' }
# in dict membership opertaors not work for values


'name' in d
True
True
True
'batch' in d
False

#identity Operators
n=[1,2,3,4]
l=[1,2,3,4]
id(n)
2047850137472
id(l)
2047895032256
n is m
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    n is m
NameError: name 'm' is not defined
>>> n s l
SyntaxError: invalid syntax
>>> n is l
False
>>> n=m
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    n=m
NameError: name 'm' is not defined
>>> m=n
>>> m
[1, 2, 3, 4]
>>> id(m)
2047850137472
>>> n is m
True
>>> n is not l
True
>>> True
True
>>> 
>>> 
>>> #bit wise operators
>>> 8&2
0
>>> 3|1  #3--->0011, #1--->0001
3
>>> ~4
-5
>>> #~  -->4+1=5 and gives - symbol
>>> 14>>2
3
>>> 15<<8
3840
>>> 3840
3840
>>> 15^2
13
