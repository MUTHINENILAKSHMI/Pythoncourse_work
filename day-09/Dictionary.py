Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
... Enter "help" below or click "Help" above for more information.
... >>> # Dictionary
... >>> # mutable ord het dyn unique/duplicates
... >>> d={}
... >>> type(d)
... <class 'dict'>
... >>> d={1:2, 2:8, 3:13}
... >>> d
... {1: 2, 2: 8, 3: 13}
... >>> d={}
... >>> d[1]=1
... >>> d[12.3]=1
... >>> d['str']=1
... >>> d[(1,2,3)]=1
... >>> d[(2+3j)]=1
... >>> d[True]=1
... >>> d[[1,2,3]]=1
... Traceback (most recent call last):
...   File "<pyshell#13>", line 1, in <module>
...     d[[1,2,3]]=1
... TypeError: unhashable type: 'list'
... >>> d[{1,2,3}]=1
... Traceback (most recent call last):
...   File "<pyshell#14>", line 1, in <module>
...     d[{1,2,3}]=1
...     
... TypeError: unhashable type: 'set'
... >>> d[{1:1,2:2,3:3}]=1
... Traceback (most recent call last):
...   File "<pyshell#15>", line 1, in <module>
...     d[{1:1,2:2,3:3}]=1
... TypeError: unhashable type: 'dict'
... >>> d
... {1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
... >>> d[False]=1
... >>> d
... {1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1}
... >>> d[1]=1
... >>> d[2]=12.3
... >>> d[3]='str'
... >>> d[4]=2+3j
... >>> d[5]=True
... >>> d[6]=[1,2,3]
... >>> d[7]=(1,2,3)
... >>> d[8]={1,2,3}
... >>> d[9]={1:1,2:2,3:3}
... >>> d[10]=frozenset({1,2,3})
d[11]=None
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: {1: 1, 2: 2, 3: 3}, 10: frozenset({1, 2, 3}), 11: None}

# Keys should be unique which means it allows immutable where as values should be anything
d={}
d[1]=2
d
{1: 2}
d[1]=3
d
{1: 3}
# only one time key value it does not allow repeated keys
data={'name':"lakshmi",'course':'pfs','batch':65}
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65}
data[name]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    data[name]
NameError: name 'name' is not defined
data['name']
'lakshmi'
data['pfs']
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    data['pfs']
KeyError: 'pfs'
data['age']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('name')
'lakshmi'
data.get('age')
data.get('age','key is not present')
'key is not present'
data.get('batch','key is present')
65
# membership
'lakshmi' in data
False
'name' in data
True
# It only check keys not values
'batch' in data
True
'age' not in data
True
# For accessing any value we use key with "get" method   ---->data.get('name')
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65}
data['age']=21
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21}
data['phone no']=9876543210
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 9876543210}
data.update({'email':'lakshmi@gmail.com','py':2026})
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 9876543210, 'email': 'lakshmi@gmail.com', 'py': 2026}
id(data)
2516673979072
data['py']
2026
data['py']=2027
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 9876543210, 'email': 'lakshmi@gmail.com', 'py': 2027}
data['age']=22
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 9876543210, 'email': 'lakshmi@gmail.com', 'py': 2027}
id(data)
2516673979072
data.popitem()
('py', 2027)
data.pop('email')
'lakshmi@gmail.com'
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 22, 'phone no': 9876543210}
data.pop('course')
'pfs'
data
{'name': 'lakshmi, 'batch': 65, 'age': 22, 'phone no': 9876543210}
del data['batch']
data
{'name': 'lakshmi', 'age': 22, 'phone no': 9876543210}
data.clear()
data
{}
data={'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 9876543210, 'email': 'lakshmi@gmail.com', 'py': 2027}
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 9876543210, 'email': 'lakshmi@gmail.com', 'py': 2027}
len(data)
7
data.keys()
dict_keys(['name', 'course', 'batch', 'age', 'phone no', 'email', 'py'])
data.values()
dict_values(['lakshmi', 'pfs', 65, 21, 9876543210, 'vishnu@gmail.com', 2027])
data.items()
dict_items([('name', 'lakshmi'), ('course', 'pfs'), ('batch', 65), ('age', 21), ('phone no', 9876543210), ('email', 'lakshmi@gmail.com'), ('py', 2027)])
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phone no', 'py']

max(data)
'py'
min(data)
'age'
d={1:1,2:2}
m=d
m
{1: 1, 2: 2}
m[5]=5
m
{1: 1, 2: 2, 5: 5}
d
{1: 1, 2: 2, 5: 5}
n=d.copy()
n[3]=3
n
{1: 1, 2: 2, 5: 5, 3: 3}
d
{1: 1, 2: 2, 5: 5}
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 9876543210, 'email': 'lakshmi@gmail.com', 'py': 2027}
data.get('key')
data.setdefault('name',2026)
'vishnu'
data.setdefault('key',2026)
2026
data
{'name': 'lakshmi', 'course': 'pfs', 'batch': 65, 'age': 21, 'phone no': 9876543210, 'email': 'lakshmi@gmail.com', 'py': 2027, 'key': 2026}

dict.fromkeys(["python","java",'Mysql'],0)
{'python': 0, 'java': 0, 'Mysql': 0}
 
SyntaxError: invalid decimal literal
""" Dictionary Introduction: A collection of key-value pairs used to store data.

Properties:  Mutable, ordered, dynamic, heterogeneous, and contains unique keys.

Keys: Keys must be unique and hashable.

Values: Values can be of any data type and can contain duplicates.

Accessing Values: Values can be accessed using their corresponding keys.

get() Method: Safely retrieves a value using a key.

Membership: in and not in check whether a key exists.

Adding & Updating: New elements can be added and existing values can be updated
.
Dictionary Methods: update(), pop(), popitem(), clear(), keys(), values(), and items().

Copying: Learned the difference between dictionary reference and copy().

setdefault(): Returns an existing value or adds a key with a default value.

