
>>> #Data Types: 

>>> #Numeric datatypes:
they are 3 types
>>> #int
>>> # float complex
>>> # these are numeric
>>> a=12
>>> type(a)
<class 'int'>
>>> b=13.4
>>> type(b)
<class 'float'>
>>> c=12+4j
>>> type(c)
<class 'complex'>
>>> # sequence data type
>>> # string list tuple
>>> 
>>> #string is a collection of characters it enclose single quotes or double quotes
>>>
    
>>> # it is immuatable
>>> #immutable we can't change within its obj refernces
>>> s='codegnan'
>>> id(s)
1340729612336
>>> s+="python"
>>> s
'codegnanpython'
>>> #list : list is a collection elements which are enclosed within square braces
>>> l=[1,2,3,4]
>>> type(l)
<class 'list'>


>>> # list is muttable ,list is ordered, list is hetrogenous element, it is dynamically sized , we can modfiy it
>>> #allow duplicates
>>> #ex:instagram post
>>> # Tuple : Tuple is collection of elements enclosed with parenthese
>>> # it is immuatble, orderded, duplicates allow, hetrogenous, fixed size
>>> # ex:
>>> # mapping data types
# set is collection of elements enclosed within flower braces
s={1, 20, 30, 40, 50, 505 ,4}
type(S)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    type(S)
type(s)
<class 'set'>
# set is immuatble , set is hetrogenous, set doesnot allow duplicates, set is unordered, set is dynamically
a={1,'lak', 22.5}
type(a)
<class 'set'>
#dictionary
# it contains collection of key values pairs enclosed with in folwer braces
# it is mutable,dynamically,hetrogenous,duplicates,ordered
d={'productname':'xyz','price':876,'stock': True}
d
{'productname': 'xyz', 'price': 876, 'stock': True}
type(d)
<class 'dict'>
s=frozenset({1,1,1,116,18})
s
frozenset({1, 18, 116})
#boolean
a=True
b=False
type(a)
<class 'bool'>
#empty list,dict,tuple
a=[]
a={}
t=()
s=' '
s=None
s
type(s)
<class 'NoneType'>
