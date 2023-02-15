successful = False
for number in range(1, 12, 2):
    print("Attempt", number, (number) * ".")
    if successful and number > 6:
        print("Successful")
        break
# for else statment is executed if loop was complete without breaking
else:
    print("Attempted", number, "times and failed")

# nested loop
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")

print(type(range(5)))

for x in "python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)
