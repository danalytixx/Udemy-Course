import numpy as np

# 1D Array to 2D Array
array_1d = np.array([1, 2, 3, 4, 5, 6])
print("Original 1D array:", array_1d)

array_2d = array_1d.reshape((2, 3))
print("Reshaped to 2D array (2x3):\n", array_2d)

# 1D Array to 3D Array
array_3d = array_1d.reshape((2, 1, 3))
print("Reshaped to 3D array (2x1x3):\n", array_3d)

# 2D Array to 1D Array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nOriginal 2D array:\n", array_2d)

array_1d_from_2d = array_2d.reshape(-1)
print("Reshaped to 1D array:", array_1d_from_2d)

# 2D Array to 3D Array
array_3d_from_2d = array_2d.reshape((2, 1, 3))
print("Reshaped to 3D array (2x1x3):\n", array_3d_from_2d)

# 3D Array to 1D Array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nOriginal 3D array:\n", array_3d)

array_1d_from_3d = array_3d.reshape(-1)
print("Reshaped to 1D array:", array_1d_from_3d)

# 3D Array to 2D Array
array_2d_from_3d = array_3d.reshape((4, 3))
print("Reshaped to 2D array (4x3):\n", array_2d_from_3d)
