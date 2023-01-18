point = {"x": 1, "y": 2}
point = dict(x=1, y=2)  # the same as above: creates a dictionary object
print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)
if "a" in point:
    print(point["a"])
# using "get" method to get value of "a". second argument is default value if pont.get("a") returns "none"
print(point.get("a", 0))
del point["x"]
print(point)

for key in point:
    print(key, point[key])


# list comprehensions
# values = []
# for x in range(5):
#     values.append(x*2)

# does absolutely the same as 3 lines above// list
values = [x*2 for x in range(5)]

values = {x: x*2 for x in range(5)}  # dictionary
print(values)
