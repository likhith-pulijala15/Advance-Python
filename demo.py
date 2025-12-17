import numpy as np
import random

# creating array
a = np.array([1,2,3])
print(a)

# 2D array
b = np.array([[1,2,3],[4,5,6]])
print(b)

# 3D Array
c = np.array([
    [[1,2,3],[4,5,6]], 
    [[7,8,9],[10,11,12]]
])
print(c)
print(c.ndim)

# Array properties
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Dimensions: {arr.ndim} \nShape: {arr.shape} \nSize: {arr.size} \nType: {arr.dtype}")

# Special Arrays
print(np.zeros((3,2)))
print(np.ones((2,3)))
print(np.eye((3)))
print(np.arange(1,10,2))
print(np.linspace(1,10,5))

# Indexing and Slicing
arr  = np.array([10,20,30,40,50])
print(arr[2])
print(arr[3,:])
print(arr[2:4])

mat = np.array([[1,2,3],[4,5,6]])
print(mat[0,2], mat[1,1])


# Array operations
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
print(a*b)
print(a**2)

# Mathematical operations
a = np.array([1,2,3,4])
b = np.array([[1,2,3,4],[5,6,7,8]])
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print(np.sqrt(a))
print(np.log(a))
print(b.reshape(2,4))
print(b.flatten())

# Broad Casting
# 1D + 1D
a = np.array([1,2,3])
print(a+10) # [1,2,3] + [10,10,10]

# 2D + 1D
a = np.array([[1,2,3],
              [4,5,6]])
b = np.array([10, 20, 30])
print(a + b)
"""
[1,2,3] + [10,20,30]
[4,5,6] + [10,20,30]
"""

# Boolean Indexing
arr = np.array([11,3,55,67,3,6])
print(arr[arr>10])

# Random Module
print(np.random.rand(3))
print(np.random.randint(1,20,5))
print(np.random.randn(5))

# # Copy (Deep copy) and View (Shallow Copy)
a = np.array([1,2,3])
b = a.copy()
b[0] = 999
print(a)
print(b)

# c = np.array([1, 2, 3])
d = c.view()
d[0] = 100
print(c)
print(d)


# Stacking and Splitting
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.hstack((a,b)))
print(np.vstack((a,b)))
print(np.stack((a,b)))
# [[1 2 3]
#  [4 5 6]]

print(np.stack((a,b), axis=1))
# [[1 4]
#  [2 5]
#  [3 6]]


# Linear Algebra
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
print(np.linalg.det(A))
print(np.linalg.inv(B))