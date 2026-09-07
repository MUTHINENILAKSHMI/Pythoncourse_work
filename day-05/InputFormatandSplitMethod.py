Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Input fromat
# int float complex str list tuple set dict bool
# default input is string
a=input("enter a name")
enter a name lakshmi
a=input()
lakshmi
a= input()
lakshmi
a
'lakshmi'
'lakshmi'
'lakshmi'
#if you want to convert string into int
b=input("enter a marks")
enter a marks 100
b
' 100'
# marks should be in string but i want in integer
b=int(input("enter a marks"))
enter a marks 100
b
100
# if want calculate cgpa then it is in float . string should be converted into float
cgpa=float(input("enter a cgpa"))
enter a cgpa 8.4
cgpa
8.4
cgpa=float(input("enter a cgpa"))
enter a cgpa 9
cgpa
9.0

#split method
names="vishnu, lakshmi, siva"
names.split()
['vishnu,', 'lakshmi,', 'siva']
names
'vishnu, lakshmi, siva'
list(names)
['v', 'i', 's', 'h', 'n', 'u', ',', ' ', 'l', 'a', 'k', 's', 'h', 'm', 'i', ',', ' ', 's', 'i', 'v', 'a']
#wirhout using split method it can sperated each character
# if use split method it gives names and sperated with space
names.split(',')
['vishnu', ' lakshmi', ' siva']
Courses='python-html-sql-dsa'
names.split('-')
['vishnu, lakshmi, siva']
Course.split()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Course.split()
NameError: name 'Course' is not defined. Did you mean: 'Courses'?
Courses.split()
['python-html-sql-dsa']
Courses.split('-')
['python', 'html', 'sql', 'dsa']
# if you want remove - use split method
names=tuple(input("enter a name"))
enter a name lakshmi vishnu baji siva
names
(' ', 'l', 'a', 'k', 's', 'h', 'm', 'i', ' ', 'v', 'i', 's', 'h', 'n', 'u', ' ', 'b', 'a', 'j', 'i', ' ', 's', 'i', 'v', 'a')
names=tuple(input("enter a name").split())
enter a name lakshmi vishnu siva baji
names
('lakshmi', 'vishnu', 'siva', 'baji')


marks=input().split()
12 34 68 5 75 4
marks
['12', '34', '68', '5', '75', '4']
map(int, marks)
<map object at 0x000001D6F4FEBC10>
marks=list(map(int,input("ente the marks").split()))
ente the marks 10 38 49 59 68 
marks
[10, 38, 49, 59, 68]

marks=tuple(map(int,input("ente the marks").split()))
ente the marks 10 34 59 39 39 28
marks
(10, 34, 59, 39, 39, 28)
marks=set(map(int,input("ente the marks").split()))
ente the marks 10 304 38 49
marks
{304, 49, 10, 38}
marks=tuple(map(float,input("ente the marks").split()))
ente the marks 290343 2256 
marks
(290343.0, 2256.0)
a,b=[1,2]
a
1
b
2
a,b,c=(1,12.3,"str")
a
1
b
12.3
c
'str'
email,password=input("enter mail,password:").split()
enter mail,password:xyz@gmail.com abc123
>>> mail
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    mail
NameError: name 'mail' is not defined. Did you mean: 'email'?
>>> email
'xyz@gmail.com'
>>> password
'abc123'
>>> names,marks=input("enter the name and marks:").split()
enter the name and marks: lakshmi 98
>>> names
'lakshmi'
>>> marks
'98'
>>> int(marks)
98
>>> a,b,c=list(map(int,input().split()))
12 34 45
>>> a
12
>>> b
34
>>> c
45
>>> 
>>> status=eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>
>>> status=eval(input())
2+5j
>>> status
(2+5j)
>>> type(status)
<class 'complex'>
