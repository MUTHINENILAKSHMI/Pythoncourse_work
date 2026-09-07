#print 10 t0 1
'''def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)'''
#sum of n  numbers
'''
def display(n,i):
    if i==len(n):
          return 0
    return n[i] + display(n,i+1) 
n=[10,20,30,40]
print(display(n,0))'''
# 
'''def display(s,i):
    if i==len(s):
        return 
    display(s,i+1)
    print(s[i] ,end=" ")
display("Codegnan",0)'''
#sliding window
'''def display(s,i,w):
    if len(s)-w+1==i:
        return 
    print(s[i:i+w])
    display(s,i+1,w)
s=input("enter a string")
w=int(input("enter the widith"))
display(s,0,w)'''
#sum of digits
'''def display(l):
    if l==0:
        return 0
    return l%10 + display(l=l//10)
l=1234
print(display(l))'''
'''def display(fact):
    if fact==1:
        return 1
    return fact * display( fact-1)
fact=5
print(display(fact))'''

# fiboncoi
def display(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return display(n-1)+display(n-2)
for i in range(20):
    print(display(i))
    

    




