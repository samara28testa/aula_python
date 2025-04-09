# Creazione di un array

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

