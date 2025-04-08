# Esercizio Indovina il numero

# Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è stato generato.

# Dopo ogni tentativo, il programma dovrebbe dire all'utente se il numero da indovinare è più alto o più basso rispetto al numero inserito.

# Il gioco termina quando l'utente indovina il numero o decide di uscire.

import random

def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    
    
    while True:
        tentativo = input("Indovina il numero(o digita 'esci' per terminare):")
        if tentativo.lower() == 'esci':
            print("Hai deciso di uscire. Il numero era:", numero_da_indovinare)
            break
        
        tentativo = int(tentativo)
        
        if tentativo == numero_da_indovinare:
            print("Bravo!, Hai indovinato il numero")
            
        elif tentativo < numero_da_indovinare:
            print("Tropo basso!")
        else:
            print("Troppo alto")

indovina_il_numero()

