# Compinti per creare log

nome = ""
password = ""
id = 0
x = True

if x:
    
    nome = input("Inserisci il tua nickname")
    password = input("inserisce il tua password")
    id += 1

if nome == "":
    print("non hai valorizato")
else:
    nome_inserito = input("Inserisci il tua nickname")
    password_inserito = input("inserisce il tua password")
    if nome_inserito == nome and password_inserito == password:
        print("Sei loggato")
