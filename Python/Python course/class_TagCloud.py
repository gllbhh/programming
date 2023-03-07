class TagCloud:
    # __tags - private class member
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("Python")
cloud.add("Python")
cloud["Java"] = 10
cloud["C++"] = 4
print(cloud["Java"])
print(cloud["c++"])
print(cloud.__len__())
for tag in cloud:
    print(tag)

# __dict__ prints all atributes of a class
print(cloud.__dict__)
print(cloud._TagCloud__tags)
