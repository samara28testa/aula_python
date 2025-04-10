import numpy as np

import random


# Es2: linspace, random, sum

# Esercitarsi nell'utulizzo di linscape per generale sequenze di numeri, random per creare array di numeri casuali, e sum per eseguire operazioni di somma sugli array, insluso l'uso di condizioni per la somma parziale.

# Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.

# Utilizza np.random per creare un array di 50 elementi casuali compressi tra 0 e 1.

# Calcola la somma totale degli elementi del nuovo array.

# Calcola la somma degli elementi del nuovo array che sono maggiori di 5.


class Data_1:
    
    def __init__(self):
        self.arr_1 = np.linspace(0, 10, 50)
        
    def stampa_arr_1(self):
        print("Array di Data_1:", self.arr_1)
  

class Data_2:

    def __init__(self):
        self.arr_2 = np.random.rand(50)
        
    def stampa_arr_2(self):
        print("Array di Data_2:", self.arr_2)
        
    def somma(self, data1):
        somma_arr_3 = data1.arr_1 + self.arr_2
        return somma_arr_3
    
    def somma_magg_5(self, somma_arr_3):
        magg_5 = somma_arr_3 > 5
        somma_magg = np.sum(somma_arr_3[magg_5])
        return somma_magg
        
    
d1 = Data_1()
d2 = Data_2()

d1.stampa_arr_1()
d2.stampa_arr_2()

risultato = d2.somma(d1)
risultato_magg = d2.somma_magg_5(risultato)

print("Somma degli array:", risultato)
print("Somma degli elementi > 5:", risultato_magg)