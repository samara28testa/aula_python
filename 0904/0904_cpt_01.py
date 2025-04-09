# creazione di una classe

class Automobile: # dichiaro la classe
    numero_di_ruote = 4 # attributo di classe
    def __init__(self, marca, modello): # metodo construttore
        self.marca = marca # attributo di instanza
        self.modello = modello # attributo di instanza
        
    def stampa_info(self): # metodo di instanza
        print("L'automobile è una", self.marca, self.modello)
    
print("L'automobile è una", "Fiat", "Topolino")
