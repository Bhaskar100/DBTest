import numpy as np

# Creating array object
arr = np.array([1, 2, 3])
arr2 = np.array([4,5,6])

print('substracting arrays')
print(arr- arr2)

# Printing type of arr object
print("Array is of type: ", type(arr))


# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Slicing array
temp = arr[:2, :2]
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp)

# maximum element of array
print("Largest element is:", arr.max())
print("Row-wise maximum elements:",
      arr.max())



# minimum element of array
print("Column-wise minimum elements:",
      arr.min())

# sum of array elements
print("Sum of all array elements:",
      arr.sum())

# Printing shape of array
print("Shape of array: ", arr.shape)


# Printing size (total number of elements) of array
print("Size of array: ", arr.size)



# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

# add 1 to every element
print("Adding 1 to every element:", arr + 1)

# subtract 3 from each element
print("Subtracting 3 from each element:", arr - 3)

# multiply each element by 10
print("Multiplying each element by 10:", arr * 10)

# square each element
print("Squaring each element:", arr ** 2)

# modify existing array
arr *= 2
print("Doubled each element of original array:", arr)

