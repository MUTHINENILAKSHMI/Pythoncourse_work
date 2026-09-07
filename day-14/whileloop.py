# print 1 to 10 numbers
"""i=1
while i<=10:
    print(i)
    i+=1

"""
"""i=10
while i>=0:
    print(i)
    i+=1"""
# 5 multiply
"""i=5
while i<=50:
    print(i)
    i+=5
"""
#string:
"""s="while loop"
i=0
while i<len(s):
    print(s[i])
    i+=1"""
#rverse a string
"""s="while loop"
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1
"""
#list
"""l=[5467,5578,6789,987]
i=0
while i<len(l):
    print(l[i])
    i+=1"""
#digits print line by line
""""n=int(input())
while n>0:
     x = n%10
    print(x)
     n=n//10
  """
#sum of digits
"""n=int(input())
s=0
while n>0:
     x = n%10
     s+=x
     n=n//10
print(s)""" 

#product of digits
"""
n=int(input())
s=1
while n>0:
     x = n%10
     s*=x
     n=n//10
print(s)"""

#reverse a digit
"""n=int(input())
res=0
while n>0:
     x = n%10
     res=res*10+x
     n=n//10
print(res)
"""
#even digit sum
"""n=int(input())
s=0
while n>0:
    x=n%10
    if x%2==0:
        s+=x
    n=n//10
print(s)"""
# In the list remove zero:
"""n=list(map(int,input().split()))
while 0 in n:
    n.remove(0)
print(n)"""

#In the list first and last elemnt should be add
"""l=list(map(int,input().split()))
s=0
end=len(l)-1
while s<=end:
    if s==end:
        print(l(s))
    else:
        print(l[s]+l[end])
    s+=1
    end-=1"""


    

    
    
