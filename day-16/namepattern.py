'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#A 
"""
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if  (j==0 and i>=m)or (j==n-1 and i>=m) or i+j==m or (j==m+1 and j<=m) or (j-i==m and i<=m)  or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
   *     
  *   *   
* * * * * 
*       * 
*       * """ 
#B
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1 or i==m):
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
5
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * '''
#C
'''n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
5
* * * * * 
*         
*         
*         
* * * * * '''
#D
'''n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
#output:
5
* * * * * 
*       * 
*       * 
*       * 
* * * * * '''
#E
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==m:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
5 
* * * * * 
*         
* * * * * 
*         
* * * * * '''
#F
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or i==m:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
* * * * * 
*         
* * * * * 
*         
*   '''

#G
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
5
* * * * * 
*         
* * * * * 
*       * 
* * * * * '''
#H
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*       * 
*       * 
* * * * * 
*       *
*       * '''

#I
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * 
    *     
    *     
    *     
* * * * * '''

#J
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m or  i==n-1 and j<=m  or j==0 and i>m :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * 
    *     
    *     
*   *     
* * * 
'''
#k
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m or  i==n-1 and j<=m  or j==0 and i>m :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*     * 
*     *   
* * *     
*     *   
*       *'''
#L
''' n=int(input())
for i in  range(n):
    for j in range(n):
        if j==0  or i==n-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
5
*         
*         
*         
*         
* * * * * '''


#M
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m)or (i+j==n-1 and i<=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*       * 
* *   * * 
*   *   * 
*       * 
*       * '''
#N
'''n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1  or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
5
*       * 
* *     * 
*   *   * 
*     * * 
*       * '''
#O
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or  i==n-1   or j==0 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * * 
*         * 
*         * 
*         * 
*         * 
* * * * * * 

'''
#p
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (j==n-1 and i<=m) or i==m or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
5
* * * * * 
*       * 
* * * * * 
*         
*   '''
#Q
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or  i==n-1   or j==0 or (i==j and j>=m) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * 
*       * 
*   *   * 
*     * * 
* * * * *'''
#R
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or (i+j==n-1 and i<=m) or (i==m and j<=m) or  (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * 
*     *   
* * *     
*     *   
*       * '''

#s
'''n=int(input())
m=n//2
for i in  range(n):
    for j in range(n):
        if i==0   or i==n-1 or (j==0 and m>=i) or m==i or(j==n-1 and m<=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
5
* * * * * 
*         
* * * * * 
        * 
* * * * * '''
#T
'''n=int(input())
m=n//2
for i in  range(n):
    for j in range(n):
        if i==0 or j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
5
* * * * * 
    *     
    *     
    *     
    *     '''
#U
''''n=int(input())
for i in  range(n):
    for j in range(n):
        if j==0  or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*       * 
*       * 
*       * 
*       * 
* * * * * '''
#v
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if  (j==0 and i<=m)or (j==n-1 and i<=m)or i-j==m or i+j==m+n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*       * 
*       * 
*       * 
  *   *   
    *  '''


#W
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i>=m)or (i+j==n-1 and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*       * 
*       * 
*   *   * 
* *   * * 
*       *'''


#X
'''n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
*       * 
  *   *   
    *     
  *   *   
*       * '''
#Y
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if  (i==j and i<=m) or (i+j==n-1 and i<=m) or i>=m and j==m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
5
*       * 
  *   *   
    *     
    *     
    *   '''
#z
'''n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()
* * * * * 
      *   
    *     
  *       
* * * * * '''