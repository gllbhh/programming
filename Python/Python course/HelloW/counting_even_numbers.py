# Counting_even_numbers.py
count = 0
number_range = int(input("In range from 1 to: "))
for number in range(1, number_range + 1):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")
