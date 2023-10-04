dict = {"name": "John", "age": 30, "city": "New York"}
print("Original =", str)

dict.update({"country": "USA"})
print(dict)

del dict ["age"]
print(dict)

keys = dict.keys()
print(keys)


values = dict.values()
print(values)

items = dict.items()
print(items)

dict.clear()
print(dict)