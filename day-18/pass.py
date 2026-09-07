#Pass by Value → ,When immutable objects are passed to a function, changes inside the function do not affect
#the original value.
# Pass by Reference → When immutable objects are passed to a function, changes inside the function  affect
#the original value.
#int
'''def display(n):
    n+=10
    print("inside funtion",n)
n=10
display(n)
print("outside function",n)
inside funtion 20
outside function 10
#float
def display(n):
    n+=10.3
    print("inside funtion",n)
n=10.3
display(n)
print("outside function",n)
inside funtion 20.6
outside function 10.3

#string
def display(n):
    n+="lang"
    print("inside funtion",n)
n="python"
display(n)
print("outside function",n)
inside funtion pythonlang
outside function python
#complex
def display(n):
    n+=4
    print("inside funtion",n)
n=2+5j
display(n)
print("outside function",n)
inside funtion (6+5j)
outside function (2+5j)
#boolean
def display(n):
    n="True"
    print("inside funtion",n)
n='False'
display(n)
print("outside function",n)
inside funtion True
outside function False

#tuple
def display(n):
    n+=(1,2,3)
    print("inside funtion",n)
n=(4,5,6,7)
display(n)
print("outside function",n)
inside funtion (4, 5, 6, 7, 1, 2, 3)
outside function (4, 5, 6, 7)

#list:
def display(n):
    n+=[1,2,3]
    print("inside funtion",n)
n=[4,5,6,7]
display(n)
print("outside function",n)
inside funtion [4, 5, 6, 7, 1, 2, 3]
outside function [4, 5, 6, 7, 1, 2, 3]

#set
def display(n):
    n.add(1)
    print("inside funtion",n)
n={4,5,6}
display(n)
print("outside function",n)
inside funtion {1, 4, 5, 6}
outside function {1, 4, 5, 6}

#dict
def display(n):
    n[5]=6
    print("inside funtion",n)
n={1:2,3:4}
display(n)
print("outside function",n)
inside funtion {1: 2, 3: 4, 5: 6}
outside function {1: 2, 3: 4, 5: 6}'''
