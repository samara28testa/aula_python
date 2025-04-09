import pip

import numpy as np

# Fancy Indexing in NumPy

arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indice = np.array([1, 3])
print(arr[indice])

# Utilizzo di una lista di indici
indice = [0, 2, 4]
print(arr[indice])