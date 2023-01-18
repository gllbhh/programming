list = [1, 1.5, 5, 6, 8.4, 12]


def find_last(list, max_val):
    """
    Finds element of the list that is 
    greater than given value
    """
    if max_val > list[-1]:
        return len(list)
    index = 0
    while max_val >= list[index]:
        index += 1
    return index


print(find_last(list, 15))
