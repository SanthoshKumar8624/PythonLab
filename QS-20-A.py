"""
Question: Implementing Programs using written modulus and python Standerd Libraries (numpy)
"""

import numpy as np

arr = np.array([1, 2, 3])
print("1D Array: \n", arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array: \n", arr)

arr = np.array((1, 2, 3))
print("Array using Tuple: \n", arr)

arr = np.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]])
print("Initial Array: \n", arr)

sliced_arr = arr[:2, ::2]
print("Sliced Array: \n", sliced_arr)

indexed_arr = arr[[1, 2, 0], [0, 2, 1]]
print("Indexed Array: \n", indexed_arr)

print("Adding 1 to Every Elements: \n", arr+1)
print("Subtracting 2 to Every Elements: \n", arr-2)
print("Sum of all Elements: ", arr.sum())


"""
OUTPUT:
-----

1D Array: 
 [1 2 3]

2D Array: 
 [[1 2 3]
 [4 5 6]]

Array using Tuple: 
 [1 2 3]

Initial Array: 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]

Sliced Array: 
 [[1 3]
 [4 6]]

Indexed Array: 
 [4 9 2]

Adding 1 to Every Elements: 
 [[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]

Subtracting 2 to Every Elements: 
 [[-1  0  1]
 [ 2  3  4]
 [ 5  6  7]]

Sum of all Elements:  45

"""