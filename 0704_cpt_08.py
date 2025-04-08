# Competi con IF in tre livello di profundimento

lista = [0, 5, 10, 58, 100.55]


if 12 not in lista:
    lista.append(12)
    
    if 58 in lista:
        lista.remove(58)
        
        if lista[3]:
            lista[3] = 100
else:
    print(lista)
    
print(lista)