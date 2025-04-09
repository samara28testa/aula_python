import pip

import numpy as np

# Slicing

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base
print(arr[2:7])

# Slicing con passo
print(arr[1:8:2])

# Omettere start e stop
print(arr[:5])
print(arr[5:])

# Utilizzare indici negativi
print(arr[-5:])
print(arr[:-5])