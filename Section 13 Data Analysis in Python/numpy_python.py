import numpy as np

# Create 1d array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))
print(arr1.shape)

# Reshape
arr2 = np.array([1, 2, 3, 4, 5])
print(arr2.reshape(1, 5))

arr3 = np.array([[1, 2, 3, 4, 5]])
print(arr3)
print(arr3.shape)

arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr4)
print(arr4.shape)

# range in numpy
print(np.arange(0, 8, 2))
print(np.arange(0, 8, 2).reshape(2, 2))

# predefined array
print(np.ones((3, 4)))

# identity matrix
print(np.eye(3))

# array attributes
arr5 = np.array([[1, 2, 3], [4, 5, 6]])

print("Array: \n", arr5)
print("Shape: ", arr5.shape)
print("Number of dimensions: ", arr5.ndim)
print("Number of elements: ", arr5.size)
print("Data types: ", arr5.dtype)
print("Items size (in bytes)", arr5.itemsize)

# Numpy Vectorized operations
arr6 = np.array([1, 2, 3, 4, 5])
arr7 = np.array([10, 20, 30, 40, 50])

print("Addition: ", arr6 + arr7)
print("Substraction: ", arr6 - arr7)
print("Multiplication: ", arr6 * arr7)
print("Division: ", arr6 / arr7)

# Universal Function
arr8 = np.array([2, 3, 4, 5, 6])
print("np sqrt", np.sqrt(arr8))
print("np exp", np.exp(arr8))
print("np sin", np.sin(arr8))
print("np log", np.log(arr8))

# Array slicing and indexing
arr9 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("Array:\n ", arr9)

## array[nd_index] , array[nd, nd-1, ..., nd-n + 1], array[array_index1][array_index2][array_index3]
print(arr9[0])
print(arr9[0][0], arr9[0, 0])
print(arr9[1:])
print(arr9[1:, 2:], end="\n")
print(arr9[1:][:, 2:])

# Modify array elements
arr9[0, 0] = 100
print(arr9)

arr9[1:] = 101
print(arr9)

# Statistical concepts ~ Normalization
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
std_dev = np.std(data)

normalized_data = (data - mean) / std_dev
print("Normalized Data: ", normalized_data)

# Calculate mean median mode
data2 = np.arange(1, 11)
mean = np.mean(data2)
print("Mean: ", mean)
median = np.median(data2)
print("Median: ", median)
std_dev = np.std(data2)
print("Standard deviation: ", std_dev)
variance = np.var(data2)
print("Variance: ", variance)

data3 = np.arange(1, 11)
print(data3 > 5)
print((data3 >= 5) & (data3 <= 8))

print(data3[data3 > 5])
print(data3[(data3 > 5) & (data3 <= 8)])
