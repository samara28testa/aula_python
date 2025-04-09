# Esercizio di ciclo, utilizzo di while e range

# Scrivi un sistema che prende in input in numero intero positivo n e stapa tutti i numeri da n a 0 (compresso), decrementando di 1. Deve potersi ripetere all'infinito.


while True:
    numero = int(input("Inserisci un numero intero positivo"))

    if numero < 0:
        print("Il numero deve essere positivo. Riprova.")
        continue

    for i in range(numero, -1, -1):
        print(i)

    risposta = input("Vuoi ripetere? (si/no): ").lower()

    if risposta != "si":
        print("Ciao! Programma terminato.")
        break
