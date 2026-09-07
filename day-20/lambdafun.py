"""lambda function is a anynomous function:Lambda is an anonymous function 
>>> it does not have a function name.
It is created using the lambda keyword.
A lambda function can take any number of arguments, but it can have only one expression.
It is mainly used for short and simple operations.
Lambda functions are commonly used with map(), filter(), and sorted().
synatx for lambda function:
=============================
varname= lambda arg:exp

wish=lambda name: f"welcome to the course{name}"
print(wish("lakshmi"))
print(wish("pfs"))

avg=lambda a,b,c:(a+b+c)/3
print(avg)

iseven=lambda a:"even" if a%2==0 else "odd"
print(iseven(10))
print(iseven(9))

largest= lambda a,b,c : a if a>b and b>c else (b if b>c else c)
print(largest(10,20,30))
print(largest(20,30,5))

gst=lambda price: price+price*0.18
print(gst(1000))

isvowel=lambda a: "vowel" if a in "AEIOUaeiou" else "cons"
print(isvowel('u'))

#map method:
l=[1,2,3,4,5,6,7]
temp=list(map(lambda i: i+10,l))
print(temp)

t=[789,567,9023,4567]
discount=list(map(lambda i: i-i*0.3,t))
print(discount)
#filter

l=[1,2,3,4,5,6,7]
temp=list(filter(lambda i: i%2!=0 ,l))
print(temp)

t=[789,567,9023,4567]
great=list(filter(lambda i: i>1000,t))
print(great)"""

'''email=['lak@gmail.com', 'vishnu@123.com', 'sowmya@codegnan.com']
domain=list(map(lambda i: i.split('@')[-1], email))
print(domain)

from functools import reduce
l=[1,2,3,4,5,6]
res=reduce(lambda sum,i:sum+i,l)
print(res)
seats={'s1':True,
       's2':False,
       's3':True,
       's4':False,
       's5':True}
avali=list(filter(lambda i:seats[i]!=True,seats))
print(avali)

pro={
    'egg':80,
    'sugar':98,
    'milk':33,
    'butter':90}
res=list(filter(lambda i:pro[i]>50,pro))
print(res)

pro={
    'egg':80,
    'sugar':98,
    'milk':33,
    'butter':90}
print(dict(sorted(pro.items(),key=lambda i:i[1])))
print(dict(sorted(pro.items(),key=lambda i:i[1],reverse=True)))'''
