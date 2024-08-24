# Dictionary: Key-value pairs, unordered, mutable
my_dict = {"name": "Max", "age": 28, "city": "Boston"}
print(my_dict)

value = my_dict["name"]
print(value)

my_dict["email"] = "barra1997@yahoo.com"
print(my_dict)

del my_dict["city"]
print(my_dict)

my_dict2 = dict(name="Mary", age=27, city="New York")
print(my_dict2)

mydict_copy = my_dict
print(mydict_copy)