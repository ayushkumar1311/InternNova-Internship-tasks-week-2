import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Element at index 2:", arr[2])
print("Element at index 5:", arr[5])

print("Sliced array:", arr[2:6])

two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nTwo-Dimensional Array:")
print(two_d)

print("\nFirst Row:", two_d[0])
print("Second Row:", two_d[1])

print("First Column:", two_d[:, 0])
print("Second Column:", two_d[:, 1])

print("\nOriginal Array:")
print(arr)

reshaped = arr.reshape(2, 4)

print("\nReshaped Array (2 x 4):")
print(reshaped)

reshaped_2 = arr.reshape(4, 2)

print("\nReshaped Array (4 x 2):")
print(reshaped_2)
