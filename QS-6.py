"""
Question: Write a Program to demonstrate working with Tuples in Python
"""

tuple = ("A", "B", "C")
print("Tuple: ", tuple)

print("First Element: ", tuple[0])
print("First Two Elements: ", tuple[0:2])
print("Length of Tuple: ", len(tuple))
print("Tuple Concatenation: ", tuple+tuple)
print("Maximum Value: ", max(tuple))
print("Minimum Value: ", min(tuple))


"""
OUTPUT:
-----

Tuple:  ('A', 'B', 'C')
First Element:  A
First Two Elements:  ('A', 'B')
Length of Tuple:  3
Tuple Concatenation:  ('A', 'B', 'C', 'A', 'B', 'C')
Maximum Value:  C
Minimum Value:  A
"""