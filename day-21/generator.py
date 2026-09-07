''' A generator is a special type of function that produces values one at a time
 instead of returning all values at once.
Generators use the yield keyword instead of return.
They are memory efficient because they don't store all values in memory at the same time.
A generator remembers its state between each yield, 
so execution continues from where it stopped.
Generators are useful when working with large data, files, 
or sequences where processing one value at a time is better.'''

#ex:
'''def reels():
    data=['1..100','101..200','201..300','301..400','401..500']
    for i in data:
      yield i 
res=reels()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))'''
# countdown
'''def countdown():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1
res=countdown()
for i in res:
    print(i)'''
#factors
''''def fact(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
res=fact(16)           
for i in res:
    print(i)'''
# prime number range
'''def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            yield i
res=prime(50)
for i in res:
    print(i,end=" ")''' 
            

              
         