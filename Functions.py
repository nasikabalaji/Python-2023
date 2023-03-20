'''def sum(a,b):
    c = a + b
    return c
c = sum(2,3)
print(c)'''


# Return value and with Arguments
# checking the given number is even or odd
'''def even_or_odd(n):
    if n % 2 == 0:
        return ('it is an even number')
    else:
        return ('it is an odd number')
n = int(input('enter a number: '))
result = even_or_odd(n)
print(result)'''


# No return value and without Argument
# checking the given number is even or odd
'''def even_or_odd():
    n = int(input('enter a number: '))
    if n % 2 == 0:
        print('{} is an even number'.format(n))
    else:
        print('{} is an odd number'.format(n))
even_or_odd()'''


# Return value and without Argument
# checking the given number is even or odd
'''def even_or_odd():
    n = int(input('enter a number: '))
    if n % 2 == 0:
        return ('{} is an even number'.format(n))
    else:
        return ('{} is an odd number'.format(n))
result=even_or_odd()
print(result)'''


# No return value and with Arguments
# checking the given number is even or odd
'''def even_or_odd(n):
    n = int(input('enter a number: '))
    if n % 2 == 0:
        print('{} is an even number'.format(n))
    else:
        print('{} is an odd number'.format(n))
even_or_odd(30)'''


'''def fun(address) :
    for i in address:
        if i%2==0 :
           continue
           print(i)
        else:
            print("not divisble by 2: ",i)
add=[1,2,3,4]
fun(add)'''


#A function that adds two numbers:
'''def add_numbers(a, b):
    return a + b
result = add_numbers(5, 7)
print(result)'''


#  A function that calculates the area of a rectangle:
'''def rectangle_area(width, height):
    return width * height

result = rectangle_area(3, 4)
print(result) 
'''

#A function that checks if a number is even or odd:
'''def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(5)
print(result) 
'''
# A function that prints a message a given number of times:
'''
def print_message(message, times):
    for i in range(times):
        print(message)

print_message("Hello", 3)'''

#A function that returns the maximum value from a list of numbers:


'''def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

result = find_max([2, 6, 3, 8])
print(result) '''



#to print unique values from a list
'''
def number():
    nums = [1, 2, 2, 3, 4, 5, 4, 4, 5, 5, 6, 7]
    nums1 = list()
    nums1.append(nums[0])
    for item in nums:
        if item != nums1[-1]:
            nums1.append(item)
            #return nums1
    print(nums1)
number()'''
#A function that calculates the factorial of a number:

'''def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

result = factorial(5)
print(result)'''

# A function that calculates the area and perimeter of a rectangle:

'''def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

result = rectangle_properties(4, 6)
print(result)'''