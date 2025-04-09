import pip

import numpy as np

# Esercizio Slicing e F. Indexing

arr = np.array([10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 30, 35, 40, 45, 46, 47, 48, 50])

#L'array originale
print(arr)

# Slicing 10 primi
print(arr[:10])

# Slicing ultimi 5
print(arr[-5:])

# Slicing dall'indice 5 all 15 escluso
print(arr[5:15])

# Slicing per ogni terzo elemento
print(arr[::3])

# Modifica tramite slicing, gli elementi dall'indice 5 all,indice 10 (escluso)
arr[5:10] = 99
print(arr) 
