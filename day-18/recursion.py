''''
Recursive Functions

Definition
A recursive function is a function that calls itself.
def function():
if base_condition:
return
function()'''
'''
def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)
def display(s,n):
   if n==len(s):
      return
   print(s[n])
   display(s,n+1)
display("codegnan",0)'''
        
  