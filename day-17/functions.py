#example:
'''def fun():
    print("welcome to functions")
fun()
#output: welcome to functions'''
#calculate gst:
'''def gst(price):
    print("orignal price",price)
    print("total price",price+price*0.18)
gst(100)
gst(1000)
gst(5000)
gst(100000)
#output:
rignal price 100
total price 118.0
orignal price 1000
total price 1180.0
orignal price 5000
total price 5900.0
orignal price 100000
total price 118000.0'''

#print tables
'''def table(n):
    print(f"{n}-table")
    print("======================")
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
for i in range(1,21):
    table(i)
# output: 1 to 20 tables'''

#leap year
'''def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap year"
    else:
        return "Not leap year"
print(isleap(2004))
print(isleap(2020))
print(isleap(2026))
#output
Leap year
Leap year
Not leap year'''
#prime number
'''def isprime(n):
        for i in range(2,n//2+1):
            if n%i==0:
                return " not a prime number"
            else:
                return " prime number"

print(isprime(5))
print(isprime(8))
#output:
 prime number
 not a prime number'''
#positional arguments:
'''
def display(name,email,pwd):
    print('name:',name)
    print('email:',email)
    print("pwd:",pwd)
display('lakshmi','lakshmi@gmail.com','lakshmi123')
display('lakshmi123','lakshmi','lakshmi@gmail.com')
display('lakshmi@gmail.com','lakshmi123','lakshmi')
#output:
name: lakshmi
email: lakshmi@gmail.com
pwd: lakshmi123
name: lakshmi123
email: lakshmi
pwd: lakshmi@gmail.com
name: lakshmi@gmail.com
email: lakshmi123
pwd: lakshmi'''
#keyarguments:
'''def display(name,email,pwd):
    print('name:',name)
    print('email:',email)
    print("pwd:",pwd)
display(name='lakshmi',email='lakshmi@gmail.com',pwd='lakshmi123')
display(pwd='lakshmi123',name='lakshmi',email='lakshmi@gmail.com')
display(email='lakshmi@gmail.com',pwd='lakshmi123',name='lakshmi')

#ouput:
name: lakshmi
email: lakshmi@gmail.com
pwd: lakshmi123
name: lakshmi
email: lakshmi@gmail.com
pwd: lakshmi123
name: lakshmi
email: lakshmi@gmail.com
pwd: lakshmi123'''
#default arguments:
'''
def display(name,email,pwd=None):
    print('name:',name)
    print('email:',email)
    print("pwd:",pwd)
display('lakshmi','email')
display('lakshmi','email','pwd@123')
#output:
name: lakshmi
email: email
pwd: None
name: lakshmi
email: email
pwd: pwd@123'''
#variable length arguments:
'''def display(*names):
    print(names)
display('lakshmi')
display('vishnu', 'lakshmi')
display('ramadevi','lakshmi','gurujyothi')
('lakshmi',)
('vishnu', 'lakshmi')
('ramadevi', 'lakshmi', 'gurujyothi')'''

'''def display(**names):
    print(names)
display(n1='lakshmi')
display(n1='vishnu', n2='lakshmi')
#output:
{'n1': 'lakshmi'}
{'n1': 'vishnu', 'n2': 'lakshmi'}'''