# # sets
# numbers = [1, 1, 2, 3, 4]
# uniques = set(numbers)  # set removes duplicates from a list
# second = {1, 4}
# second.add(5)
# second.add(6)
# second.remove(1)
# print(len(second))
# print(second)

# print(type(uniques))


numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second)  # combine two sets
print(first & second)  # intersection of two sets
print(first - second)  # difference of two sets
# symmetric difference of two sets (numbers either only in the first or a second set)
print(first ^ second)

if 1 in first and 1 in second:
    print("Yeeees")
