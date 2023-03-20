'''a = 10 * 2 + 3 % 4
print(a)'''
# first is modulus (3 % 4 is 0)
# next is multiplication (10 * 2 is 20)
# last is addition (20 + 3 is 23)

'''b = 3 + (5 - 3) /10
print(b)'''
# first comes brackets (5 - 3 is 2)
# next is division (2 / 10 is 0.2)
# last is addition (3 + 0.2 is 3.2)

'''c = 54 // 9 - 20 + 10
print(c)'''
# first comes floor division (54 // 9 is 6)
# next is addition (-20 + 10 is -10)
# last is subtraction (6 - 10 is -4)

'''d = 4 ** 2 & 7 | 3
print(d)'''
# first is exponential (4 ** 2 is 16)
# next is (16 & 7 is 0)
# last is (0 | 3 is 3)

'''e = 30 % 4 <= 10
print(e)'''
# first is modulus (30 % 4 is 2)
# next is comparision (2 <= 10 is True)

'''f = ((2 - 3 + 5) // 10) & 4 + 20
print(f)'''
# first addition (- 3 + 5 is 2) and (4 + 20 is 24)
# next is subtraction (2 - 2 is 0)
# next is floor division (0 // 10 is 0)
# last is bitwise AND (0 & 24 is 0)

'''g = 2 ** 3 | 5 ^ 10 + (20 - 11 * 2)
print(g)'''
# first is bracket (11 * 2 is 22) and (20 - 22 is -2)
# next is exponential (2 ** 3 is 8)
# next is subtraction(addition) (10 - 2 is 8)
# next is XOR (5 ^ 8 is 13)
# last is OR (8 | 13 is 13)

'''h = (4 // 2 + 13) ^ 7
print(h)'''
# first is floor division (4 //2 is 2)
# next is addition (2 + 13 is 15)
# last is XOR (15 ^ 7 is 8)