class TagCloud:
    def __init__(self) -> None:
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
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("Java")
cloud.add("C++")
cloud["java"] = 10
for tag in cloud:
    print(f"{tag} mentioned {cloud[tag]} times")

print(cloud._TagCloud__tags)
print(f"Total number of different tags: {len(cloud)}")
