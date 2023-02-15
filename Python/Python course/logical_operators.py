"""Logical Operators"""
high_income = True
good_credit = False
student = True
age = 24

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")


# Chaning comparison operators
if 18 <= age < 65:
    print("Adult")