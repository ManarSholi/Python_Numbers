## NumPy
## Uses python by bringing super fast multi dimentional arrays that take
## less memory that built in lists in python. So any time you want to work
## with large, multi dimentional arrays, NumPy is the best choice.

import numpy as np

array = np.array([1, 2, 3])
print(array)
print(type(array))

two_dimentional_array = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dimentional_array)
print(type(two_dimentional_array))
print(two_dimentional_array.shape) ## Return tuple of the number of rows and columns

zero_init_array = np.zeros((3, 4), dtype=int)
print(zero_init_array)
ones_init_array = np.ones((3, 4), dtype=int)
print(ones_init_array)
number_init_array = np.full((3, 4), fill_value=5, dtype=int)
print(number_init_array)
random_init_array = np.random.random((3, 4))
print(random_init_array)
print(random_init_array[0, 0]) ## Element in first row and first column
print(random_init_array > 0.2)
print(random_init_array[random_init_array > 0.2]) ## Return the numbers that are greater than 0.2
print(np.sum(random_init_array))
print(np.floor(random_init_array))
print(np.ceil(random_init_array))
print(np.round(random_init_array))

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)
print(first + 2)

dimentions_inch = np.array([1, 2, 3])
dimentions_cm = dimentions_inch *  2.54
print(dimentions_cm)
