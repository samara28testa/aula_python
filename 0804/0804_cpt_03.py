# Esercizio di cicli, utilizzo di IF

risposta = True

while risposta:

    numero = int(input("Dimmi un numero."))

    if numero % 2 == 0:
        print("Il numero è pari.")
    else:
        print("Il numero è dispari")
        
    risposta = input("Vuoi ripetere?")
    if risposta == "no":
        risposta = False