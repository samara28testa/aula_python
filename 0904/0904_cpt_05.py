# Creare una classe biblioteca che permeta di creare un libro e stamparlo

class Libro:
  
    def __init__(self, titolo, autore, pagine):
           self.titolo = titolo
           self.autore = autore
           self.pagine = pagine
           
    def stampa_info(self):
        print(f"TITOLO: {self.titolo}, AUTORE: {self.autore}, PAGINE: {self.pagine}")

class Biblioteca:
        def __init__(self):
            self.libri = []
            
        def aggiungi_libro(self, libro):
            self.libri.append(libro)

        def stampa_libri(self):
            print("Libri presenti in biblioteca:")
            for libro in self.libri:
                libro.stampa_info()
            
biblioteca = Biblioteca()
    
for i in range(1):
    titolo = input("Dimmi un titolo di un libro")
    autore = input("Dimmi il autore")
    pagine = input("Dimmi i numeri di pagini")

    nuovo_libro = Libro(titolo, autore, pagine)
    biblioteca.aggiungi_libro(nuovo_libro)
    

          
biblioteca.stampa_libri()