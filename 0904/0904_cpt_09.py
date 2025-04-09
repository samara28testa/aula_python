# Indexing e Slicing:

import pip

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0])

#Slicing
print(arr[1:3])

# Boolean Indexing

print(arr[arr > 2])

# esempio

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# Slicing sulle righe

print(arr_2d[1:3])

# Slicing sulle colonne
print(arr_2d[:, 1:3])

# Slicing misto

print(arr_2d[1:, 1:3])
