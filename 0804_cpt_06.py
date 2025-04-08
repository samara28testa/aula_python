# Esercizio di cicli, numero 4

# Utilizzo di if, while e for insieme.

# Scrivi un sistema che prende in input una lista di numeri interi che precedentemente è stata valorizzata dall'utente.

# il sietma deve:

# Utilizzare un ciclo for per trovare il numero massimo nella lista.
# Utilizzare un ciclo while per contare quanti numeri sono presente nella lista.
# Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.



lista = []

for i in range(5):
    numero = int(input("Dimmi un numero"))
    lista.append(numero)

while True:
    conteggio = len(lista)
    
    print(conteggio)
    
    for m in (lista):
        m = max(lista)
    
    if lista == 0:
        print("Lista Vuota.")
        
    else:
        print("Numero massimo della lista è", m)
    break