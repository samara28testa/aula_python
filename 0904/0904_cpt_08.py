import pip

import numpy as np

# Es1: ndarray, dtype, shape, arrange

arr = np.arange(10, 50)

print("Tipo di dati:", arr.dtype)

arr_float = arr.astype(float)

print("Nuovo tipo di dati:", arr_float)