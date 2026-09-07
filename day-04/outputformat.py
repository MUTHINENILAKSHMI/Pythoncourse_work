Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=85.4
>>> c="Python"
>>> print(a,b,c)
10 85.4 Python
>>> # output Fromat
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 85.4 c= Python
>>> print("a=",a,"b=",b,"c=",c, sep='') #sep: use for remove spaces
a=10b=85.4c=Python
>>> print("a=",a,"b=",b,"c=",c, sep='/t') #/t : use for tab space
a=/t10/tb=/t85.4/tc=/tPython
>>> print("a=",a,"b=",b,"c=",c, sep='\t') #\t : blackslash t use for tab space
a=	10	b=	85.4	c=	Python
>>> print("a=",a,"b=",b,"c=",c, sep='/n') #\n : use for next line
a=/n10/nb=/n85.4/nc=/nPython
>>> print("a=",a,"b=",b,"c=",c, sep='\n') #\n " Blackslash n use for next line
a=
10
b=
85.4
c=
Python
>>> print("a=",a,"b=",b,"c=",c, sep='\t', end= '\n\n')
a=	10	b=	85.4	c=	Python

>>> print("a=",a,"b=",b,"c=",c, sep='\t', end='@')
a=	10	b=	85.4	c=	Python@
>>> #end: adding @ in end we use end
>>> 
>>> #fstrip:
>>> print(f'={a} b={b} c={c}')
=10 b=85.4 c=Python
>>> print(f'a={a} b={b} c={c}')
a=10 b=85.4 c=Python
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=85.400000 c=Python
>>> print('a={] b={] c={}'.format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('a={] b={] c={}'.format(a,b,c))
ValueError: unexpected '{' in field name
>>> print('a={] b={} c={}'.format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print('a={] b={} c={}'.format(a,b,c))
ValueError: unexpected '{' in field name
>>> print('a={} b={} c={}'.format(a,b,c))
a=10 b=85.4 c=Python
>>> print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=85.4 c=Python
