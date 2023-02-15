""""Test cose with numbers"""

import math

# x = 1       # integer
# x = 1.1     # float
# x = 1 + 2j # a + bi - complex number

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

print(round(2.9))
# print(abs(-2.9)
print(math.ceil(2.9))


# x = input("x: ")
# y = int(x) + 11
# print(y)


#Falsy values
#   "" - empty string
#   0 - zero
#   None - None 
#   False
temperature = 29
if temperature > 30:
    print("apple"[:3])
elif temperature > 20:
    print("go out!"[3:])