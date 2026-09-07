'''def display():
    n=10
    print("Inside the function")
display()
print("outside the function")'''
#local variable: A variable declared inside a function is called a local variable.
'''def display():
    n=10
    print("Inside the function",n)
display()
print("Outside the function",n)'''
#global variable: A variable declared outside all functions is called a global variable.
''''
def display():
    print("inside the function",n)
n=10
display()
print("outside the function",n)
nside the function 10
outside the function 10'''
#using non local:Used in nested functions. Allows modification of variables from the outer function.
'''def display():
    course='PFS'
    def update():
        nonlocal course 
        course='JFs'
        print("Inner function",course)
    update()
    print("Outer function",course)

display()
Inner function JFs
Outer function JFs'''

#with out local
'''def display():
    course="PFS"
    def update():
        course="JFS"
        print("Inner function", course)
    update()
    print("outer function",course)
display()
#output
Inner function JFS
outer function PFS'''
'''l=[1,2,3,4]
print(max(l))
print=20
print(max)'''