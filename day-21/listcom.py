'''# list of numbers
l=[i for i in range(1,11)]
print(l)
# even number
m=[i for i in range(2,11,2)]
print(m)
# factors
n=16
f=[i  for i in range(1,n+1) if n%i==0]
print(f)
# even or odd
x=[1,2,3,4,5,6,7,8,9]
e=[i  if i%2==0 else 0 for i in x]
print(e)'''
#list 
'''l=[]
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)'''
#dict
s={i:i*i for i in range(1,11)}
print(s)
#set
s={i for i in range(1,11)}
print(s)
#list
l=[[j for j in range(1,4)] for i in range(3)]
print(l)
