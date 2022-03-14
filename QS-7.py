"""
Question: Write a Program to demonstrate working with Dictionaries in Python
"""

dictionary = {1: "A", 2: "B", 3: "C",}
print("Dictionary: ", dictionary)

print("keys: ", dictionary.keys())
print("Values: ", dictionary.values())
print("Length of Dictionary: ", len(dictionary))
print("Value of 1: ", dictionary[3])

# Update an Element
dictionary.update({4: "D"})
print("Dictionary after Updated an Item: ", dictionary)

# Delete an Element
dictionary.pop(2)
print("Dictionary after Deleted an Item: ", dictionary)

# Check Whether an Element is Exist
print("Is B is Exist: ", dictionary.__contains__(2))
print("Is C is Exist: ", dictionary.__contains__(3))

"""
OUTPUT:
-----

Dictionary:  {1: 'A', 2: 'B', 3: 'C'}
keys:  dict_keys([1, 2, 3])
Values:  dict_values(['A', 'B', 'C'])
Length of Dictionary:  3
Value of 1:  C
Dictionary after Updated an Item:  {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
Dictionary after Deleted an Item:  {1: 'A', 3: 'C', 4: 'D'}
Is B is Exist:  False
Is C is Exist:  True
"""