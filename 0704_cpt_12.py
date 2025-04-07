numero = int(input("dammi un numero superiore a 5"))
if numero > 5:
    
    numero = int(input("dammi un numero superiore a 10"))
    if numero > 10:
        
        numero = int(input("dammi un numero superiore a 20"))
        if numero > 20:
            
            print("Sei arrivato al terzo livello")
            
            
        else: 
            print("numero inferiore a 20")
    else:
        print("numero inferiore a 10")
else:
    print("numero inferiore a 5")