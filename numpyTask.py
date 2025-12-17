import numpy as np

# Studnet Marks Analyser
marks = np.array([95,90,85,70,55])
print(f"Total: {np.sum(marks)}")
print(f"Average: {np.mean(marks)}")
print(f"Max: {np.max(marks)} Min: {np.min(marks)}")
print(f"Standard deviation: {np.std(marks)}")

# Matrix Creation and properties
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(f"Dimensions: {matrix.ndim} \nShape: {matrix.shape} \nSize: {matrix.size} \nType: {matrix.dtype}")
print(matrix[1,2])

# Special Arrays
zeros = np.zeros((4,4))
print(zeros)

ones = np.ones((2,5))
print(ones)

identity = np.eye((3))
print(identity)

even = np.arange(10,50,2)
print(even)

linsp = np.linspace(0,1,5)
print(linsp)


# Salary Increment Calculator
salaries = np.array([25000,30000,40000,50000])
increased = salaries * 1.10
print(f"10% Increase: {increased}")
print(f"Yearly: {salaries*12}")
print(f"Salaries greater than 35k: {salaries[salaries>35000]}")

# Random data
arr = np.random.randint(1,100,12)
print(arr)

new = arr.reshape(3,4)
print(new)

for row in arr:
    print(row)

print(arr.flatten())

for row in arr:
    print(np.sum(row))