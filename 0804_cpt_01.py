# compiti con cicli

# Utilizzo di range( )

risposta = True


while risposta:

    numeri = int(input("Dimmi un numero"))

    for i in range(numeri, -1, -1):
    
        print(i)
    
    # controllo della risposta
    risposta = input("Vuoi ripetere?")
    if risposta == "no":
        risposta = False
    


