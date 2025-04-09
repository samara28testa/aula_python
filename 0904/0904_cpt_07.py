# Creazione di un array
import pip

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi

print("Forma dell'array:", arr.shape)
print("Dimensione dell'array:", arr.ndim)
print("Tipo di dati:", arr.dtype)
print("Numero di elemento:", arr.size)
print("Somma degli elementi:", arr.sum())
print("Media degli elementi:", arr.mean())
print("Valore massimo:", arr.max())
print("Indice del valore massimo:", arr.argmax())

# utilizzo di arange

arr = np.arange(10)

print(arr)

# utilizzo di reshape

arr = np.arange(6)

reshaped_arr = arr.reshape((2, 3))

print(reshaped_arr)