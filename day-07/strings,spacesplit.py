Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#trimming or space methods
""" 1.strip
2. rstrip
3.lstrip"""
' 1.strip\n2. rstrip\n3.lstrip'
s="    hello    World              "
s.strip()
'hello    World'
# remove space from start and ending
# lstrip: leftside removing spaces
# rstrip : right sides removing spaces
s="    hello    World              "
s.lstrip()
'hello    World              '

s.rstrip()
'    hello    World'
s.replace('  ',' ')
'  hello  World       '
s=" java-python-sql-django"
s.split('-')
[' java', 'python', 'sql', 'django']
s.split('-',2)
[' java', 'python', 'sql-django']
s.split(' ',-2)
['', 'java-python-sql-django']
s.rsplit('-',2)
[' java-python', 'sql', 'django']
s.lsplit('-',2)
s.rsplit('-')
[' java', 'python', 'sql', 'django']
c= [' java', 'python', 'sql', 'django']
c
[' java', 'python', 'sql', 'django']
''.join(c)
' javapythonsqldjango'
', '.join(c)
' java, python, sql, django'
'@'.join(c)
' java@python@sql@django'
a="string.py"
a
'string.py'
a.partition('.')
('string', '.', 'py')
>>> a='string.py.java.png.txt'
>>> s
' java-python-sql-django'
>>> '-'.join(('1','2','3'))
'1-2-3'
>>> '-'.join({'1','2','3'})
'1-3-2'
>>> a.rpartition('.')
('string.py.java.png', '.', 'txt')
>>> # Testing Methods

>>> a="lakshmi.python"
>>> a.startswith("lak")
True
>>> a.endswith("thon")
True
>>> a.endswith("java")
False
>>> 'python'.islower()
True
>>> 'Python'.islower()
False
>>> 'Python'.isupper()
False
>>> 'PYTHON'.isupper()
True
>>> 'python'.isalpha()
True
>>> 'python1235456'.isalnum()
True
>>> 'Python'.istitle()
True
>>> 'python'.istitle()
False
>>> "Python Hello".isspace()
False
>>> "        ".isspace()
True
>>> "My_var".isidentifier()
True
>>> "1My_var".isidentifier()
False
>>> '213'.isdecimal()
True
>>> 'V|||'.isnumeric()
False
>>> "e43w1".isdigit()
False
