# Task: Find the most repeated character
# My take:
sentense = "This is a common interview question"
letters = [*sentense.lower()]
uniques = set(letters)
uniques.remove(' ')
letter_count = []
for x in uniques:
    letter_count.append(letters.count(x))
pairs = list(zip(uniques, letter_count))
pairs.sort(key=lambda count: count[1], reverse=True)
print(*pairs[0])

# Solution
sentense = "This is a common interview question"
char_frequency = {}  # create an empty dictionary
for char in sentense:  # for every char in sentense
    if char in char_frequency:  # if the char is in the dictionary increment count
        char_frequency[char] += 1
    else:  # if not, add char to the dictionary with count 1
        char_frequency[char] = 1
print(char_frequency)
char_frequency_sorted = sorted(  # sorted applyes only to lists
    char_frequency.items(),  # so we pass items from char_frequency
    # with a lambda function taking second item from a tuple
    key=lambda kv: kv[1],
    reverse=True)  # in reverse order
print(char_frequency_sorted[0])

# feels like my solution is not much worse =)
