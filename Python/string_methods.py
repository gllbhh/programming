students_count = 1000
rating = 4.99
is_published = True
course_name = "  python \n\"programming\""  # \ - exacape caracter
#\"     - allows to have " in the string
#\'     - allows to have ' in the string
#\\     - allows to have \ in the string
#\n     -    new line
print(course_name)
print(len(course_name))

first = "Gll"
last = "Bhh"
full = first + last
print(full)

full = f"{first} {last}"
print(full)

print(course_name.upper())  # - all CASPS
print(course_name.lower())  # - all low
print(course_name.title())  # - Cap every first letter of the word
print(course_name.strip())  # - remove spaces in the beginning
print(course_name.find("pro"))  # - returnd index of part of the string in "". -1 meand NOT Found
print(course_name.replace("p", "j"))  # - replace
print("Pro" in course_name)  # - returns True or False
print("swift" not in course_name)