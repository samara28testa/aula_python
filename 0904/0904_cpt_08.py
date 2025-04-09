import pip

import numpy as np

# Es1: ndarray, dtype, shape, arrange

# Crea un array Numpy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.

# Verifica il tipo di dato dell'array e stampa il risultado.

# Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo dato.

# Stampa la forma dell'array.



arr = np.arange(10, 50)

print("Tipo di dati:", arr.dtype)
print("Forma dell'array:", arr.shape)


arr_float = arr.astype(float)

print("Nuovo tipo di dati:", arr_float.dtype)