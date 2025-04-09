# I/O in Python

file = open("esempio_testo.txt", "r")

contenuto = file.read()

riga = file.readline()

print(contenuto)


# Scritura di file, questo modifica il testo, non aggiunge

file.close()

file = open("esempio_testo.txt", "w")

file.write("Sto sostutituendo il testo")

file.close()


# Se vogliamo apprire il file senza dire per chiudere, utilizzo with, perchè cosi se chiuda da solo

with open("esempio_testo_nuovo.txt", "w") as file:
    file.write("Leggemo questo file.")
    

