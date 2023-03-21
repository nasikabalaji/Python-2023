#printing 1 to 10 number
'''for i in range(11):
    print(i)'''


#printing 1 to 10 number using step count
'''for i in range(1,11,3):
    print(i)'''


#for loop using break statement
'''for i in range(10):
    if i==5:
        break
    else:
        print(i)'''


#for loop using continue statement
'''for i in range(10):
    if i==5:
        continue
    else:
        print(i)'''


#for loop using pass statement
'''for i in range(10):
    if i==5:
        pass
    else:
        print(i)'''


#Using for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a='srisai'
for i in a:
    print(i)'''


#for loop using frozenset
'''a=[10,20,30,40,50,40,40]
b=frozenset(a)
print(b)
for i in b:
    print(i)'''


#converting list into set and using for loop
'''a=[10,20,30,40,50]
b=set(a)
print(b)
for i in b:
    print(i)'''


#printing sum of even number and odd numbers
'''import math
nums = [1,2,3,4,10,22,5,7]
even=[]
odd=[]
for i in nums:
     if i % 2 == 0:
          even.append(i)
     else:
          odd.append(i)
print(math.fsum(even))
print(math.fsum(odd))'''
