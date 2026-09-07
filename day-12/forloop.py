#str list, tuple,set,dict,range
# syntax:
#for var in seq:
    #stmnts

#string
"""s="python programming"
for i in s:
    print(i)"""
#list
"""list=[10,20,30,40,50,60]
for lists in list:
    print(lists)"""
#tuple:
"""Tuple=(9998,87665,7877,1235)
for price in Tuple:    print(price)"""
#set
"""set={"lakshmi", "Python", "Codegnan"}
for name in set:
    print(name)"""
#dictionary
"""dictionary={1:2,3:6,2:4,4:8,5:10}
for num in dictionary:
    print(num,dictionary[num]) #num for keys, dictionary[num]=to get values"""

#range: it is used for genarating ranging values
# range(start,end+1,step): by default(start=0,end,step=1)
#printing 1 to 10 numbers
"""for i in range(1,11):
    print(i)"""
#printing even number:
"""for i in range(2,21,2):
    print(i)"""
#printing multiple 5 upto 100
"""for  i in range(5,101,5):
    print(i)"""
#reverse printing number
"""for  i in range(5,0,-1):
    print(i)"""
# odd number printing
"""for  i in range(19,0,-2):
    print(i)"""

#range and indexing of elements
"""s="python programming"
for i in range(len(s)):
    print(i,s[i])"""
#range  used for list and indexing
"""s=["lakshmi",23,23.5,"True"]
for i in range(len(s)):
    print(i,s[i])"""
#range used for tuple and indexing
"""s=(10,20,50,80)
for i in range(len(s)):
    print(i,s[i])
"""
#enumerate:the olp should be in tuple with sequence and value.
#string
s="Python Programming"
"""for i in enumerate(s):
    #print(i)
    print(i[0],i[1])"""
#list
"""l=[10,20,30,40,50]
for i in enumerate(l):
    print(i[0],i[1])"""
#tuple
"""t=(100,200,300,400,500)
for i in enumerate(t):
    print(i[0],i[1])"""
#set
"""s={1000,2000,3000,4000,5000}
for i in enumerate(s):
    print(i[0],i[1])"""
#dict
"""d={1:2,2:4,5:6}
for i in enumerate(d):
    print(i[0],i[1])"""

#break and continue
#break: it is used for termating the sequence
#continue : it is used for skip the sequence

#break
"""for i in range(1,11):
    if i==5:
        break
    print(i)"""
#continue
"""for i in range(1,11):
    if i==5:
       continue
    print(i)"""
# the number is avilable 
"""l=[12,67,45,96,78,54]
n=26
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")"""
#unlock phone:
"""pin=2580
for i in range(5):
    epin=int(input("enter your pin"))
    if epin==pin:
        print("unlock phone")
        break
    else:
        print("invaild phone")
else:
    print("try again after 30 seconds")"""
#prime number
#prime number :  It is divisibel 1 and itself
n=int(input("enter a number")) 
for i in range(2,n//2+1):
    if n%i==0:
        print("not a prime number")
        break
else:
    print("Prime number")