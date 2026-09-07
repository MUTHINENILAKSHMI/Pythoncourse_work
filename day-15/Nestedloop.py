
#pattern programs:
"""n=int(input("ente the number"))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()
#output
*****
*****
*****
*****
*****"""
#2nd pattern
'''n=int(input())
for i in range(n):
    for j in range(n):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()
    #( or )
n=int(input())
for i in range(n):
    for j in range(n):
        print(j%2,end="")
    print()
01010
01010
01010
01010
01010''' 
# 3rd pattern 
'''n=int(input())
for i in range(n):
    for j in range(n):
        print(i%2,end="")
    print()
#output
00000
11111
00000
11111
00000   '''
#4th pattern
"""n=int(input())
for i in range(n):
    for j in range(n):
        print((i+j)%2,end=" ")
    print()
#output:
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 """
#5th pattern:
"""n=int(input())
for i in range(n):
    for j in range(n):
        print(i+j,end=" ")
    print()
#output:
0 1 2 3 4 
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 """
#6th pattern
"""n=int(input())
c=1
for i in range(n):
    for j in range(n):
        print(c,end="")
        c+=1
    print()
#output
12345
678910
1112131415
1617181920
2122232425"""
#right angle triangle
"""n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
#output:
*
**
***
****
*****"""
#mirror right angle triangle
'''n=int(input())
for i in range(n):
    for j in range(n-i):

        print("*",end="")
    print()
#output:
*****
****
***
**
*'''
"""n=int(input())
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
#output:
          *  
        * * 
      * * * 
    * * * * 
  * * * * * """
#inverse right angle triangle
'''n=int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
* * * * * 
  * * * * 
    * * * 
      * * 
        *  '''
'''n=int(input())
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print("*",end=" ")
    else:
        for k in range(n-i):
            print("*",end=" ")
    print()
# or
n=int(input())
m=n//2
for i in range(n):
    if i<=m:
        print("*"*(i+1),end=" ")
    else:
        print("*"*(n-i),end="")
    print()
#output
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* '''
"""
n=int(input())
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),"*"*(i+1),end=" ",sep=' ')
    else:
        print(' '*(i-m),"*"*(n-i),end=" ",sep=' ')
    print()
     * 
    ** 
   *** 
  **** 
 ***** 
  **** 
   *** 
    ** 
     * """
