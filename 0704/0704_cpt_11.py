# compiti con IF e elif

lista = ["Brasile", "Italia", "Germania", "Francia", "Spagna"]

scelta = input("Cosa vuoi fare")

if scelta.lower() == "eliminare":
    print(lista)
    scelta = input("Sclegli un paese per eliminare")
    lista.remove(scelta)
    print(lista)
elif scelta.lower() == "aggiungere":
    scelta = input("Sclegli un paese da aggiungere")
    lista.append(scelta)
    print(lista)
elif scelta.lower() == "modificare":    
    scelta = int(input("Dimmi quale posizione vuoi modificare da 0 a 4"))
    scelta2 = input("Sclegli un paese da aggiungere")
    lista[scelta] = scelta2
    print(lista)
else:
    print("comando sbagliato")
    


