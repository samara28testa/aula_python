# Classi

# Le classi consentono di definire strutture he ragruppano dati (attributi) e comportamenti (metodi) correlati in un unico oggetto di un determinato tipo.

# Sono modeli logici di oggeti.

# esempio oggeto basilare

class Esempio():
    x = 10
    
oggetto_1 = Esempio()
oggetto_2 = Esempio()
oggetto_1.x = 20
oggetto_2.x = 50

print(oggetto_1.x)
print(oggetto_2.x)


# Metodo speciale: Construtore

class Penna():
    altezza = 0
    larghezza = 0
    
    def __init__(self, h, l):
        self.altezza = h
        self.larghezza = l
        
oggetto_penna = Penna(10,1)

print(oggetto_penna.altezza)
print(oggetto_penna.larghezza)

penna2 = Penna(2, 0.8)

print(penna2.altezza)
print(penna2.larghezza)

# classe teste

class Casa():
    altezza = 0
    larghezza_1 = 0
    larghezza_2 = 0
    
    def __init__(self, h, l1, l2):
        self.altezza = h
        self.larghezza_1 = l1
        self.larghezza_2 = l2

casa_1 = Casa(5, 10, 8)

print(casa_1.altezza)
print(casa_1.larghezza_1)
print(casa_1.larghezza_2)



    