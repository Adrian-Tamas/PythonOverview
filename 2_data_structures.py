from collections import namedtuple

# Dictionaries
print("\n Dictionaries \n")
user = {
    "name": "Adrian",
    "id": 3,
    "location": "Cluj"
}

print(user["name"], "\n")

for value in user.values():
    print(value)

for key, value in user.items():
    print(f"value for key {key} is {value}")

# Named Tuples
print("\n Named Tuples \n")
Coordinates = namedtuple("Coordinates", ["x", "y"])
location = Coordinates(46.7712,23.6236)
print(location)
print(location._asdict())
print(location.x)

# Sets
print("\n Sets \n")
my_set = {1, 2, 3, "four", "five"}
print(my_set)
my_set.add(6)
print(my_set.pop())
print(my_set.pop())
print(my_set)

# tuples
print("\n Tuples \n")
my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[2])

# lists
print("\n Lists \n")
my_list = [1,2,3,4]
print(my_list)
print(my_list[2])

# Comprehensions
print("\n Comprehension \n")
comprehension_list = [x for x in range(1, 20) if x % 2 == 0]
print(comprehension_list)

comprehension_dict = {chr(index + ord('a')): index + 1 for index in range(26)}
print(comprehension_dict)


