#Funzione

def nome_della_funzione():
    pass

def saluta():
    print("Ciao")

saluta()

# funzione con parametri

def somma(x,y):
    risultado = x+y
    print(risultado)
    
somma(1,2)


# funzione di ritorno

def riporta_dato(x):
    risultato = x*x
    return risultato

numero = riporta_dato(3)
print(riporta_dato(3))

somma(riporta_dato(3), riporta_dato(3))


# funzione di ritorno con input interno

def riporta_dato_senza_parametri():
    x = input(("Dimmi un numero"))
    return x*x

# funzione con parametri standart

def funzione_standard(x = 2):
    return x+x

print(funzione_standard(4))


