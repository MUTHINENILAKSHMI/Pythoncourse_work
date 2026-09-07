#system
'''import sys
print(sys.argv)
 sys.argv is used to take input from the command line when running a Python program.
It comes from the sys module.

print(sys.version) # know the version of vscode or python idle
print(sys.path) know  the path where u save the file
print("Start")
sys.exit() to exit the code or loop
print("end")'''
#platform
'''import platform
print(platform.system()) 
print(platform.version()) 
print(platform.processor())'''
#mathematical function
'''import math
print(math.pi)
print(math.e)
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.sqrt(36))
print(math.gcd(12,18))
print(math.pow(2,3))'''
#round-->round of means nearest value ex:12.999-->13
'''print(round(12.00000001))
print(round(12.999))
print(round(12.3))
print(round(12.7))
print(round(12.4))
import math
#ceil-> we get upper value 12.3-> 13
print(math.ceil(12.3))
print(math.ceil(12.9))
print(math.ceil(12.6))

#floor--> we get lower value 12.3-->12
print(math.floor(12.55))
print(math.floor(12.4))
print(math.floor(12.9))'''
#random
'''import random
random.seed(9) #when we used seed the output doesn't change
print(random.random()) 
print(random.randint(1,6)) #randint in between range 1 t0 6 random number should be output in integer
print(random.uniform(1,6))# uniform means in between range 1 to6 random number should be output in float
l=['r','p','s']
print(random.choice(l))#random choice is the output 
lang=['python','java','sql', 'flask']
print(random.choices(lang,k=2)) #random choices is used for multiplle inputs
random.shuffle(lang)
print(lang)'''

#collections
'''from collections import Counter
s="python programming"
res=Counter(s)
print(res)'''
#defaultdict
'''from collections import Counter,defaultdict
pro=['sugar','salt','butter']
res=defaultdict(list)
for i in pro:
    res[i].append(['des','rev','com'])
print(res)

s='python programming'
d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)'''
#deque
'''from  collections import deque
l=deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(20)
l.append(60)
print(l)'''
'''from  collections import deque
l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(20)
l.appendleft(60)
print(l)'''

