# Esercizio 1

class Punto:
    
    dx = 0
    dy = 0
    
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy =dy
        print(f"Punto dall'origene{dx} e {dx}")
        
punti= []
  
for i in range(2):
    dx = int(input("Dimmi un valore per x"))
    dy = int(input("Dimmi un valore per y"))
    
    punto = Punto(dx, dy)
    punti.append(punto)
    
def stampa_info(self): # metodo di instanza
    print("Sei arrivato al livello", self.dx, self.dy)
        
for punto in punti:
    punto.stampa_info()
