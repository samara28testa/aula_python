import pip

import numpy as np

# Es1: ndarray, dtype, shape, arrange

# Crea un array Numpy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.



arr = np.arange(10, 50)

print("Tipo di dati:", arr.dtype)
print("Forma dell'array:", arr.shape)


arr_float = arr.astype(float)

print("Nuovo tipo di dati:", arr_float.dtype)