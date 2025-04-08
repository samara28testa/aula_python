# Esercizio 3, utilizzo di for

# Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascuno numero nella lista

lista = []

for i in range(5):
    numero = int(input("Dimmi un numero"))
    lista.append(numero)
    
    
for numero in lista:
    quadrato = numero ** 2
    print("l quadrato di questo numero", numero,"è", quadrato)
    

5