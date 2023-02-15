# use array ONLY for large amount of data when expecting peformance problems
from array import array

# first argument is array type. google dif types
numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.insert(-2, 5)
numbers[0] = 6
print(numbers[:])
