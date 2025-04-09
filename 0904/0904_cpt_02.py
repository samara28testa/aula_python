# Esempio di metodo decorato

class Contatore:
    numero_istanze = 0 # attributo di classe
    
    def __init__(self):
        Contatore.numero_istanze += 1
        
    @classmethod
    def mostra_numero_istanze(cls):
            print(f"Sono state create {cls.numero_istanze} istanze.")
            
# creazione di alcune istanze
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()