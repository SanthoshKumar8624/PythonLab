"""
Question: Write an Program to Create, Append, and remove lists in Python
"""

list = ["A", "B", "C"]
print("List: ", list)

list.append("D")
print("Appended List: ", list)

list.remove("B")
print("Removed List", list)

"""
OUTPUT:
-----

List:  ['A', 'B', 'C']
Appended List:  ['A', 'B', 'C', 'D']
Removed List ['A', 'C', 'D']
"""