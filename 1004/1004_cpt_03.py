import numpy as np

import random

# Es1: lindspace, random, sum

# Crea un array di 12 numeri equidistanti tra 0 e 1 usando lispace.

arr = np.linspace(0, 1, 12)

print(arr)


# Cambia la forma dell'array a una matrice 3 * 4

reshaped_arr = arr.reshape((3, 4))

print(reshaped_arr)

print("Forma dell'array:", reshaped_arr)

# Genera una matrice 3,4 di numeri casuali tra 0 e 1.

random_arr = np.random.rand(3, 4)

print(random_arr)

# Extra: provare a farlo girare tramite classi e funzioni

class Data:
    
    def __init__(self, arr=None):
        self.arr = np.random.rand(3, 4)
               
    def analise_info(self):
        self.sum_value = np.sum(arr)
        self.mean_value = np.mean(arr)
        self.std_value = np.std(arr)   
            
    def stampa_info(self):  # metodo di istanza
        print("Matrice:", self.arr)
        print("Somma:", self.sum_value)
        print("Media:", self.mean_value)
        print("Deviazione standard:", self.std_value)
        
d = Data()
d.analise_info()
d.stampa_info()