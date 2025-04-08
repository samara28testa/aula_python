# compiti con cicli

# Utilizzo di range( ), secondo compiti con numeri pari.

pari = []

while len(pari) < 5:

    numero = int(input("Dimmi un numero."))

    if numero % 2 == 0:
        print("Il numero è pari.")
        pari.append(numero)
    else:
        print("Il numero non è par. Prove un'altra volta")

    
print("Hai messo 5 numero par.", pari)